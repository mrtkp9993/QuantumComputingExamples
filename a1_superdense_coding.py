'''
    Superdense Coding

    Task. Transmit two bits of classical information between 
    Alice and Bob using only one qubit.

'''
from qiskit import IBMQ, BasicAer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

qr = QuantumRegister(2)  # Initialize qubits
cr = ClassicalRegister(2)  # Initialize bits for record measurements
circuit = QuantumCircuit(qr, cr)

# Create Bell state - Alice and Bob share an entagle qubit pair
circuit.h(qr[0])
circuit.cx(qr[0], qr[1])

circuit.barrier()

# Apply Quantum operations
# I x I -> Alice will get 00
# X x I -> Alice will get 01
# Z x I -> Alice will get 10
# (XZ) x I -> Alice will get 11
circuit.x(qr[0])
circuit.z(qr[0])

circuit.barrier()

# Apply Hadamard to qubit 0 - Take qubit 0 out of superposition
circuit.cx(qr[0], qr[1])
circuit.h(qr[0])

circuit.barrier()

# Measurement
circuit.measure(qr, cr)

# Run our circuit with local simulator
backend = BasicAer.get_backend('qasm_simulator')
shots = 1024
results = execute(circuit, backend=backend, shots=shots).result()
answer = results.get_counts()
print(answer)
# Measurement is 11
