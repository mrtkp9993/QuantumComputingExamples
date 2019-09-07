# Quantum Computing Examples
Quantum computing examples with Qiskit.

## Examples

**Deutsch's Algorithm**

> Problem. For given an oracle function f : {0, 1} -> {0, 1}, determine f is balanced or constant. 

![Deutsch's Algorithm](./circuit_diagrams/01_deutsch.png)

**Deutsch-Jozsa Algorithm**

> Problem. For given an oracle function f : {0, 1}^n -> {0, 1}, determine f is balanced or constant.

![Deutsch-Jozsa Algorithm](./circuit_diagrams/02_deutsch_jozsa.png)

**Bernstein-Vazirani Algorithm**

> Problem. For given an oracle function f : {0, 1}^n -> {0, 1}, f(x) = a x, determine a.

![Bernstein-Vazirani Algorithm](./circuit_diagrams/03_bernstein_vazirani.png)

**Simon's Algorithm**

> Problem. For given an oracle function f : {0, 1}^n -> {0, 1}^n which has period `a`: ∃!a != 0: ∀x f(x) = f(y) => y = x ⊕ a. Determine a.

![Simon's Algorithm](./circuit_diagrams/04_simon.png)
