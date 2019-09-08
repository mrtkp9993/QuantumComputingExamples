'''
    Quantum Fourier Transform (QFT)

    The Fourier transform occurs in many different versions throughout classical computing, 
    in areas ranging from signal processing to data compression to complexity theory. 
    The quantum Fourier transform (QFT) is the quantum implementation of the discrete Fourier 
    transform over the amplitudes of a wave function. It is part of many quantum algorithms, 
    most notably Shor's factoring algorithm and quantum phase estimation.

'''
import math


def qft(circuit, qr, n):
    for j in range(n):
        circuit.h(qr[j])
        for k in range(j+1, n):
            circuit.cu1(math.pi / float(2**(k-j)), qr[k], qr[j])
        circuit.barrier()
