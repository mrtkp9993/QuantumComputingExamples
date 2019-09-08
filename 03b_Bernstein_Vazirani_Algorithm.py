'''
    Bernstein-Vazirani Algorithm

    We know that an oracle function f is implemented like this

    f : {0, 1}^n -> {0, 1}

    f(x) = a x

    Task: Find a.

'''
from qiskit import IBMQ, BasicAer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

n = 3
a = 7  # integer in the oracle function f

qr = QuantumRegister(n+1)  # Initialize qubits
cr = ClassicalRegister(n+1)  # Initialize bits for record measurements
circuit = QuantumCircuit(qr, cr)

circuit.x(qr[n])  # initialize the ancilla qubit in the |1> state

circuit.barrier()

# First step of quantum algorithms - Prepare the superposition
# For superposition, we apply the Hadamard gate on all qubits
circuit.h(qr)

circuit.barrier()

# Oracle function
for i in range(n + 1):
    if (a & (1 << i)):
        circuit.z(qr[i])
    else:
        circuit.iden(qr[i])

circuit.barrier()

# Apply Hadamard gates after querying oracle function
circuit.h(qr)

circuit.barrier()

# Measure qubits
for i in range(n):
    circuit.measure(qr[i], cr[i])

# Run our circuit with local simulator
backend = BasicAer.get_backend('qasm_simulator')
shots = 1024
results = execute(circuit, backend=backend, shots=shots).result()
answer = results.get_counts()
print("Simulator result")
print(answer)
# 0111 observed in 1024 times
# 0111 in base 2 = 7 in base 10
# hence, a = 7
