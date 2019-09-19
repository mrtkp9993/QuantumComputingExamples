'''
    Quantum Teleportation

    Task. Alice would like to send Bob a qubit that is in some unknown state.

'''
from qiskit import IBMQ, BasicAer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

qr = QuantumRegister(3)  # Initialize qubits
cr0 = ClassicalRegister(1)
cr1 = ClassicalRegister(1)
cr2 = ClassicalRegister(1)
circuit = QuantumCircuit(qr, cr0, cr1, cr2)

# Prepare the initial state which we want to transfer
circuit.x(qr[0])

# Prepare the Bell pair
circuit.h(qr[1])
circuit.cx(qr[1], qr[2])

circuit.barrier()

# Measure in the Bell basis
circuit.cx(qr[0], qr[1])
circuit.h(qr[0])
circuit.measure(qr[0], cr0[0])
circuit.measure(qr[1], cr1[0])

circuit.barrier()

# Apply a correction
circuit.z(qr[2]).c_if(cr0, 1)
circuit.x(qr[2]).c_if(cr1, 1)
circuit.measure(qr[2], cr2[0])

# Run our circuit with local simulator
backend = BasicAer.get_backend('qasm_simulator')
shots = 1024
results = execute(circuit, backend=backend, shots=shots).result()
answer = results.get_counts()
print(answer)
