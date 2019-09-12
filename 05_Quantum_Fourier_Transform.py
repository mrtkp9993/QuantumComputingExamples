'''
    Quantum Fourier Transform (QFT)

    The Fourier transform occurs in many different versions throughout classical computing, 
    in areas ranging from signal processing to data compression to complexity theory. 
    The quantum Fourier transform (QFT) is the quantum implementation of the discrete Fourier 
    transform over the amplitudes of a wave function. It is part of many quantum algorithms, 
    most notably Shor's factoring algorithm and quantum phase estimation.

    Resource: https://quantum-computing.ibm.com/support/guides/quantum-algorithms-with-qiskit?page=5cbc5e2d74a4010049e1a2b0#qiskit-implementation

'''
import math


def qft(circuit, qr, n):
    for j in range(n):
        circuit.h(qr[j])
        for k in range(j+1, n):
            circuit.cu1(math.pi / float(2**(k-j)), qr[k], qr[j])
        circuit.barrier()


def qft_dagger(circuit, q, n):
    for j in range(n):
        k = (n-1) - j
        for m in range(k):
            circuit.cu1(-math.pi/float(2**(k-m)), q[k], q[m])
        circuit.h(q[k])
