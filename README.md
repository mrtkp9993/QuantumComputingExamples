# Quantum Computing Examples

Quantum computing examples with QISKit.

## Examples

### Deutsch's Algorithm

> Problem. For given an oracle function f : {0, 1} -> {0, 1}, determine f is balanced or constant.

![Deutsch's Algorithm](./circuit_diagrams/01_deutsch.png)

### Deutsch-Jozsa Algorithm

> Problem. For given an oracle function f : {0, 1}^n -> {0, 1}, determine f is balanced or constant.

Scheme for `n=2`:

![Deutsch-Jozsa Algorithm](./circuit_diagrams/02_deutsch_jozsa.png)

### Bernstein-Vazirani Algorithm

> Problem. For given an oracle function f : {0, 1}^n -> {0, 1}, f(x) = a x, determine a.

Scheme for `n=3`:

![Bernstein-Vazirani Algorithm](./circuit_diagrams/03_bernstein_vazirani.png)

### Simon's Algorithm

> Problem. For given an oracle function f : {0, 1}^n -> {0, 1}^n which has period `a`: ∃!a != 0: ∀x f(x) = f(y) => y = x ⊕ a. Determine a.

Scheme for `n=2`:

![Simon's Algorithm](./circuit_diagrams/04_simon.png)

### Quantum Fourier Transform (QFT)

Scheme for `n=3`:

![Quantum Fourier Transform](./circuit_diagrams/05_qft.png)

### Superdense Coding

> Task. Transmit two bits of classical information between Alice and Bob using only one qubit.

![Superdense Coding](./circuit_diagrams/e1_superdense_coding.png)

### Quantum Teleportation

> Task. Alice would like to send Bob a qubit that is in some unknown state.

![Quantum Teleportation](./circuit_diagrams/e2_quantum_teleportation.png)

### Quantum Phase Estimation

> Problem. Given an unitary operator U, estimate θ in U|ψ>=exp(2πiθ)|ψ>.

![Quantum Phase Estimation](./circuit_diagrams/e3_quantum_phase_estimation.png)

## References

* [Jonahtan Hui, Quantum Computing Series, Medium](https://medium.com/@jonathan_hui/qc-quantum-computing-series-10ddd7977abd)

* [Qiskit, Medium](https://medium.com/qiskit)

* [Qiskit, GitHub](https://github.com/Qiskit/qiskit-terra)

* [An Introduction to Quantum Computing, Kaye, ‎Laflamme, Mosca](https://books.google.com.tr/books/about/An_Introduction_to_Quantum_Computing.html?id=8jwVDAAAQBAJ&source=kp_book_description&redir_esc=y)

* [Learn Quantum Computation using Qiskit](https://community.qiskit.org/textbook/)
