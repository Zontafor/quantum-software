# Quantum Error Correction ExampleFlip qubit 1 or qubit 2 instead of 0 and test recovery
#   Let students build the decoder from scratch
#   Extend to Shor’s 9-qubit code or phase flip correction for advanced sessions

# !pip install qiskit matplotlib

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create circuit with 3 qubits, 1 classical bit
qc = QuantumCircuit(3, 1)

# Step 1: Encode logical |0⟩ → |000⟩ (already default)

# Step 2: Simulate error (flip qubit 0)
qc.x(0)  # Inject bit-flip error

# Step 3: Error correction (majority vote)
qc.cx(1, 0)
qc.cx(2, 0)
qc.ccx(1, 2, 0)

# Step 4: Measure recovered logical qubit
qc.measure(0, 0)

# Simulate
sim = Aer.get_backend("qasm_simulator")
job = execute(qc, sim, shots=1024)
counts = job.result().get_counts()

# Output
print("Error Correction Result:")
print(counts)

# Visualize
plot_histogram(counts)
plt.title("Error Correction: Recovered Logical Bit")
plt.show()