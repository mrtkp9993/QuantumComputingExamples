'''
    Bernstein-Vazirani Algorithm

    We know that an oracle function f is implemented like this

    f : {0, 1}^n -> {0, 1}

    f(x) = a x

    Task: Find a.

'''
from qiskit import IBMQ, BasicAer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

qr = QuantumRegister(4)  # Initialize qubits
cr = ClassicalRegister(4)  # Initialize bits for record measurements
circuit = QuantumCircuit(qr, cr)

circuit.x(qr[3])  # initialize the ancilla qubit in the |1> state

# First step of quantum algorithms - Prepare the superposition
# For superposition, we apply the Hadamard gate on all qubits
circuit.h(qr[0])
circuit.h(qr[1])
circuit.h(qr[2])
circuit.h(qr[3])

# Oracle function
circuit.cx(qr[0], qr[3])
circuit.cx(qr[1], qr[3])
circuit.cx(qr[2], qr[3])

# Apply Hadamard gates after querying oracle function
circuit.h(qr[0])
circuit.h(qr[1])
circuit.h(qr[2])
circuit.h(qr[3])

# Measure qubit
circuit.measure(qr[0], cr[0])
circuit.measure(qr[1], cr[1])
circuit.measure(qr[2], cr[2])

# Run our circuit with local simulator
backend = BasicAer.get_backend('qasm_simulator')
shots = 1024
results = execute(circuit, backend=backend, shots=shots).result()
answer = results.get_counts()
print("Simulator result")
for c2c1c0 in answer:
    print(f"{c2c1c0} is observed in {answer[c2c1c0]} times")
# 0111 observed in 1024 times
# 0111 in base 2 = 7 in base 10
# hence, a = 7
