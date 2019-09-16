'''
    Shor's Algorithm

    Shor's algorithm is a quantum computer algorithm for integer factorization.
    Informally, it solves the following problem: Given an integer N, find its
    prime factors. It was invented in 1994 by the American mathematician Peter Shor.

    Source: https://www.wikiwand.com/en/Shor%27s_algorithm

    Factorization problem can reduce to period finding problem. Consider the sequence 
    of the powers of two

    1, 2, 4, 8, 16, 32, 64, 128, ...

    Now, let's look at the same sequence 'mod 15':

    1, 2, 4, 8, 1, 2, 4, 8, ...

    This is a modulo sequence that repeats every four numbers, that is, a periodic modulo 
    sequence with a period of four. Reduction of factorization of N to the problem of 
    finding the period of an integer 1 < x < N depends on the following result from number theory:

    The function F(a) = x^a mod N is a periodic function, where x is an integer coprime 
    to N and a >= 0.

    Source: https://github.com/Qiskit/qiskit-community-tutorials/blob/b9266a4f9c1f6b3f4cf5117d9c443f9f1c3518cb/algorithms/shor_algorithm.ipynb

'''
import math

from qiskit import IBMQ, BasicAer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

# We'll build circuit for a^x mod 15 for a = 2
qr = QuantumRegister(5)
cr = ClassicalRegister(5)

circuit = QuantumCircuit(qr, cr)

# Initialize q[0] to |1>
circuit.x(qr[0])

# Apply a**4 mod 15
circuit.h(qr[4])
circuit.h(qr[4])
circuit.measure(qr[4], cr[0])
circuit.reset(qr[4])

# Apply a**2 mod 15
circuit.h(qr[4])
circuit.cx(qr[4], qr[2])
circuit.cx(qr[4], qr[0])
circuit.u1(math.pi/2., qr[4]).c_if(cr, 1)
circuit.u1(math.pi/2., qr[4]).c_if(cr, 1)
circuit.h(qr[4])
circuit.measure(qr[4], cr[1])
circuit.reset(qr[4])

# Apply a mod 15
circuit.h(qr[4])
circuit.cswap(qr[4], qr[3], qr[2])
circuit.cswap(qr[4], qr[2], qr[1])
circuit.cswap(qr[4], qr[1], qr[0])
circuit.u1(3.*math.pi/4., qr[4]).c_if(cr, 3)
circuit.u1(math.pi/2., qr[4]).c_if(cr, 2)
circuit.u1(math.pi/4., qr[4]).c_if(cr, 1)
circuit.h(qr[4])
circuit.measure(qr[4], cr[2])

# Run our circuit with local simulator
backend = BasicAer.get_backend('qasm_simulator')
shots = 1024
results = execute(circuit, backend=backend, shots=shots).result()
answer = results.get_counts()
print(answer)
# We see the measurements yield x = 0, 2, 4 and 6 with equal(ish) probability.
# Using the continued fraction expansion for x/2^3, we note that only x = 2 and
# 6 give the correct period r = 4, and thus the factors p = gcd(a^{r/2}+1,15) = 3
# and q = gcd(a^{r/2}-1,15) = 5.
