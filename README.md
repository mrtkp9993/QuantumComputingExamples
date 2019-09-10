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