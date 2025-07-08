#   Grover's Algorithm Example in QiskitChange the marked state (e.g., to |11⟩) by tweaking the oracle.
#   Add more qubits to scale the game (requires more Grover iterations)
#   Use random.randint(0, 3) to hide a new target each time

# !pip install qiskit matplotlib
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

n = 2
grover = QuantumCircuit(n, n)

# Step 1: Initialize in uniform superposition
grover.h(range(n))

# === Step 2: Oracle marks state |10⟩ ===
grover.x(0)              # Flip qubit 0 to match |10⟩
grover.cz(0, 1)          # Apply CZ to flip phase of |10⟩
grover.x(0)              # Undo

# === Step 3: Grover Diffusion Operator ===
grover.h(range(n))
grover.x(range(n))
grover.h(1)
grover.cx(0, 1)
grover.h(1)
grover.x(range(n))
grover.h(range(n))

# Step 4: Measure
grover.measure(range(n), range(n))

# Simulate
sim = Aer.get_backend("qasm_simulator")
job = execute(grover, sim, shots=1024)
counts = job.result().get_counts()

# Output
print("Grover Search Result:")
print(counts)

plot_histogram(counts)
plt.title("Grover: Most Likely Position of the Hidden Item")
plt.show()