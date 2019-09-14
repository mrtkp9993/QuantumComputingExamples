'''
    Grover's algorithm

    For given an oracle function f : {0, 1}^n -> {0, 1}^n, ∃! ω : f(ω) = a, 
    find ω.

    Although the purpose of Grover's algorithm is usually described as "searching a database", 
    it may be more accurate to describe it as "inverting a function". Roughly speaking, if we 
    have a function y=f(x) that can be evaluated on a quantum computer, Grover's algorithm 
    allows us to calculate x when given y. Inverting a function is related to the searching of 
    a database because we could come up with a function that produces a particular value of y 
    if x matches a desired entry in a database, and another value of y for other values of x.

    Source: https://www.quantiki.org/wiki/grovers-search-algorithm

'''
from qiskit import IBMQ, BasicAer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

qr = QuantumRegister(3)  # Initialize qubits
cr = ClassicalRegister(3)  # Initialize bits for record measurements
circuit = QuantumCircuit(qr, cr)

# We want to search two marked states
# |101> and |110>

# Apply Hadamard to all qubits
circuit.h(qr)
circuit.barrier()

# Phase oracle (Marks states |101> and |110> as results)
circuit.cz(qr[2], qr[0])
circuit.cz(qr[2], qr[1])

# Inversion around the average
circuit.h(qr)
circuit.x(qr)
circuit.barrier()
circuit.h(qr[2])
circuit.ccx(qr[0], qr[1], qr[2])
circuit.h(qr[2])
circuit.barrier()
circuit.x(qr)
circuit.h(qr)

# Measure
circuit.measure(qr, cr)

# Run our circuit with local simulator
backend = BasicAer.get_backend('qasm_simulator')
shots = 1024
results = execute(circuit, backend=backend, shots=shots).result()
answer = results.get_counts()
print(answer)
