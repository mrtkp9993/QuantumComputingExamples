'''
    Swap Test

    Task. For given two unknown quantum states, determine how much them differs.

'''
from qiskit import IBMQ, BasicAer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

qr = QuantumRegister(3)  # Initialize qubits
cr = ClassicalRegister(1)  # Initialize bits for record measurements
circuit = QuantumCircuit(qr, cr)

# Our 'unknown' states
circuit.x(qr[1])

circuit.barrier()

# Swap test
circuit.h(qr[2])
circuit.cswap(qr[2], qr[0], qr[1])
circuit.h(qr[2])

circuit.barrier()

# Measure
circuit.measure(qr[2], cr[0])
''' If unknown states are: 
    * Orthogonal, then 0 is measured with probability 50%;
    * Equal, then 0 is measured with probability 100%.
'''

# Run our circuit with local simulator
backend = BasicAer.get_backend('qasm_simulator')
shots = 1024
results = execute(circuit, backend=backend, shots=shots).result()
answer = results.get_counts()
print(answer)
# Since our states are orthogonal (qr[0] = |0>, qr[1] = |1>)
# 0 is observed with probability approx. 50%  and
# 1 is observed with probability approx. 50%.
