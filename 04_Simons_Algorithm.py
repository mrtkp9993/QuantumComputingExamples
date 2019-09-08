'''
    Simon's algorithm

    We know that an oracle function f which has period a:

    f : {0, 1}^n -> {0, 1}^n

    ∃!a != 0: ∀x f(x) = f(y) => y = x ⊕ a

    Task: Find a.

'''
from qiskit import IBMQ, BasicAer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

qr = QuantumRegister(4)  # Initialize qubits
cr = ClassicalRegister(4)  # Initialize bits for record measurements
circuit = QuantumCircuit(qr, cr)

# First two qubits form a register to store x, last two qubits from a register to store f(x)
# Apply Hadamard to first two
circuit.h(qr[0])
circuit.h(qr[1])

circuit.barrier()

# Oracle function, a = 11
circuit.cx(qr[0], qr[2])
circuit.cx(qr[1], qr[2])
circuit.cx(qr[0], qr[3])
circuit.cx(qr[1], qr[3])

circuit.barrier()

# Measure last two qubits
circuit.measure(qr[2], cr[2])
circuit.measure(qr[3], cr[3])

circuit.barrier()

# Apply Hadamard to first two qubits
circuit.h(qr[0])
circuit.h(qr[1])

circuit.barrier()

circuit.measure(qr[0], cr[0])
circuit.measure(qr[1], cr[1])

# Run our circuit with local simulator
backend = BasicAer.get_backend('qasm_simulator')
shots = 1024
results = execute(circuit, backend=backend, shots=shots).result()
answer = results.get_counts()

# Categorize measurements by input register values
answer_plot = {}
for measresult in answer.keys():
    measresult_input = measresult[2:]
    if measresult_input in answer_plot:
        answer_plot[measresult_input] += answer[measresult]
    else:
        answer_plot[measresult_input] = answer[measresult]

print(answer_plot)


def sdotz(a, b):  # Calculate the dot product of the results
    accum = 0
    for i in range(len(a)):
        accum += int(a[i]) * int(b[i])
    return (accum % 2)


print('s, z, s.z (mod 2)')
for z_rev in answer_plot:
    z = z_rev[::-1]
    print(f'{11}, {z}, {11}.{z}={sdotz("11",z)}')
# We can recover the value of a = 11.
