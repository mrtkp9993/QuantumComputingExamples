'''
    Deutsch-Jozsa Algorithm

    Consider a function f(x) that takes as input n-bit strings x and returns 0 or 1. Suppose we are
    promised that f(x) is either a constant function that takes the same value c in {0,1} on all
    inputs x, or a balanced function that takes each value 0 and 1 on exactly half of the inputs. 
    The goal is to decide whether f is constant or balanced by making as few function evaluations 
    as possible. Classically, it requires 2^{n-1}+1 function evaluations in the worst case. Using 
    the Deutsch-Jozsa algorithm, the question can be answered with just one function evaluation.

    Source: https://github.com/Qiskit/ibmqx-user-guides/blob/master/rst/full-user-guide/004-Quantum_Algorithms/080-Deutsch-Jozsa_Algorithm.rst

'''
from qiskit import IBMQ, BasicAer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

n = 3
oracle = "b"  # b for balanced, c for constant

if oracle == "b":
    b = 5

if oracle == "c":
    c = 0  # or 1

qr = QuantumRegister(n+1)  # Initialize qubits
cr = ClassicalRegister(n)  # Initialize bits for record measurements
circuit = QuantumCircuit(qr, cr)

circuit.x(qr[n])  # initialize the ancilla qubit in the |1> state

circuit.barrier()

# First step of quantum algorithms - Prepare the superposition
# For superposition, we apply the Hadamard gate on all qubits
circuit.h(qr)

circuit.barrier()

# Oracle function
if oracle == "c":  # constant, return c
    if c == 1:
        circuit.x(qr[n])
    else:
        circuit.iden(qr[n])
else:  # balanced, return inner product of input with b
    for i in range(n):
        if (b & (1 << i)):
            circuit.cx(qr[i], qr[n])

circuit.barrier()

# Apply Hadamard gates after querying oracle function
circuit.h(qr)

circuit.barrier()

# Measure qubits
for i in range(n):
    circuit.measure(qr[i], cr[i])

circuit.barrier()

# Run our circuit with local simulator
backend = BasicAer.get_backend('qasm_simulator')
shots = 1024
results = execute(circuit, backend=backend, shots=shots).result()
answer = results.get_counts()
print("Simulator result")
print(answer)
