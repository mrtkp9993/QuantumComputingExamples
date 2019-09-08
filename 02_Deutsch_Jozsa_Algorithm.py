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

qr = QuantumRegister(3)  # Initialize qubits
cr = ClassicalRegister(3)  # Initialize bits for record measurements
circuit = QuantumCircuit(qr, cr)

circuit.x(qr[2])  # initialize the ancilla qubit in the |1> state

circuit.barrier()

# First step of quantum algorithms - Prepare the superposition
# For superposition, we apply the Hadamard gate on all qubits
circuit.h(qr[0])
circuit.h(qr[1])
circuit.h(qr[2])

circuit.barrier()

# Oracle function
circuit.h(qr[0])
circuit.cx(qr[1], qr[0])
circuit.z(qr[2])
circuit.h(qr[0])

circuit.barrier()

# Apply Hadamard gates after querying oracle function
circuit.h(qr[0])
circuit.h(qr[1])
circuit.h(qr[2])

circuit.barrier()

# Measure qubit
circuit.measure(qr[0], cr[0])
circuit.measure(qr[1], cr[1])

circuit.barrier()

# Run our circuit with local simulator
backend = BasicAer.get_backend('qasm_simulator')
shots = 1024
results = execute(circuit, backend=backend, shots=shots).result()
answer = results.get_counts()
print("Simulator result")
for c2c1c0 in answer:
    print(f"{c2c1c0} is observed in {answer[c2c1c0]} times")
# If we measure |0>^n, then f is constant, other results tell us that f is balanced
