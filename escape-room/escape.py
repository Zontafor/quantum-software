#	Hadamard Puzzle: Set goal to achieve a 50/50 mix of 0 and 1
#	Multi-Gate Puzzle: Use 2+ qubits, unlock only if the student applies a proper sequence (e.g., H, CX)
#	Teleportation Challenge: Send a state across qubits using entanglement

# !pip install qiskit matplotlib
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create the puzzle circuit (initially locked)
qc = QuantumCircuit(1, 1)

# === Student adds operations here ===
# To unlock, apply an X gate to flip |0⟩ → |1⟩
qc.x(0)

# ======================
qc.measure(0, 0)

# Simulate the circuit
sim = Aer.get_backend('qasm_simulator')
job = execute(qc, sim, shots=1024)
counts = job.result().get_counts()

# Output
print("🔐 Quantum Lock Result:")
print(counts)

# Plot
plot_histogram(counts)
plt.title("Quantum Escape Room Outcome")
plt.show()