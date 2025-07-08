#   Measure qubit 0 alone and show how qubit 1 “knows” the result
#   Switch order of measurement or apply additional gates to break entanglement
#   Extend to CHSH game or Bell inequality experiment for advanced groups

# !pip install qiskit matplotlib

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create Bell state circuit
bell = QuantumCircuit(2, 2)

# Step 1: Apply Hadamard to qubit 0 (superposition)
bell.h(0)

# Step 2: Apply CNOT (entanglement)
bell.cx(0, 1)

# Step 3: Measure both
bell.measure([0, 1], [0, 1])

# Simulate
sim = Aer.get_backend("qasm_simulator")
job = execute(bell, sim, shots=1024)
counts = job.result().get_counts()

# Output results
print("Bell State Measurement Outcomes:")
print(counts)

# Plot
plot_histogram(counts)
plt.title("Bell State Entanglement Outcome (|00⟩ or |11⟩)")
plt.show()