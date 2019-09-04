'''
    Deutsch-Jozsa Algorithm

    Consider a function f(x) that takes as input n-bit strings x and returns 0 or 1. Suppose we are
    promised that f(x) is either a constant function that takes the same value c in {0,1} on all
    inputs x, or a balanced function that takes each value 0 and 1 on exactly half of the inputs. 
    The goal is to decide whether f is constant or balanced by making as few function evaluations 
    as possible. Classically, it requires 2^{n-1}+1 function evaluations in the worst case. Using 
    the Deutsch-Jozsa algorithm, the question can be answered with just one function evaluation.
    
    Deutsch's algorithm is the simpler case of Deutsch-Jozsa Algorithm which has a function f(x) 
    which takes 1-bit as input.

    Source: https://github.com/Qiskit/ibmqx-user-guides/blob/master/rst/full-user-guide/004-Quantum_Algorithms/080-Deutsch-Jozsa_Algorithm.rst

'''
from qiskit import IBMQ, BasicAer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.tools.monitor import job_monitor

qr = QuantumRegister(2)  # Initialize two qubits
cr = ClassicalRegister(2)  # Initialize two bits for record measurements
circuit = QuantumCircuit(qr, cr)

circuit.x(qr[1])  # initialize the ancilla qubit in the |1> state

# First step of quantum algorithms - Prepare the superposition
# For superposition, we apply the Hadamard gate on both qubits
circuit.h(qr[0])
circuit.h(qr[1])

# Oracle function
circuit.cx(qr[0], qr[1])

# Apply Hadamard gates after querying oracle function
circuit.h(qr[0])
circuit.h(qr[1])

# Measure qubit
circuit.measure(qr[0], cr[0])

# Run our circuit with local simulator
backend = BasicAer.get_backend('qasm_simulator')
shots = 1024
results = execute(circuit, backend=backend, shots=shots).result()
answer = results.get_counts()
print("Simulator result")
for c1c0 in answer:
    print(f'c0 = {c1c0[1]} ({answer[c1c0]} shots)')
# C0 observed as 1 in 1024 shots
# It indicates f(0) != f(1)

# Run our circuit with real devices
IBMQ.load_account()
IBMQ.backends()
backend_lb = least_busy(IBMQ.backends(simulator=False))
backend = backend_lb
shots = 1024
job_exp = execute(circuit, backend=backend, shots=shots)
job_monitor(job_exp, interval=2)
results = job_exp.result()
answer = results.get_counts(circuit)
print("Real Device Result")
for c1c0 in answer:
    print(f'c0 = {c1c0[1]} ({answer[c1c0]} shots)')
# As we can see in results, most of the results for C0 is 1
# It indicates f(0) != f(1)
# The results with C0 = 0 occur due to errors in the quantum computation.
