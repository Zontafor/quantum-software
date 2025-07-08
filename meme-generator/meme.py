#	Add more qubits to increase meme possibilities
#	Use different quantum gates (e.g., X, T, Z) before measuring
#	Compare repeated runs to see measurement randomness in action

# !pip install qiskit matplotlib
from qiskit import QuantumCircuit, Aer, execute
import matplotlib.pyplot as plt

# Define meme options (up to 2^n options)
meme_options = ["cat", "dog", "alien", "robot"]

# Create 2-qubit circuit for 4 outcomes
qc = QuantumCircuit(2, 2)
qc.h([0, 1])                     # Apply Hadamard gates for superposition
qc.measure([0, 1], [0, 1])       # Measure into classical bits

# Run simulation
sim = Aer.get_backend('qasm_simulator')
job = execute(qc, sim, shots=1)
counts = job.result().get_counts()

# Get result
bitstring = list(counts.keys())[0]
index = int(bitstring, 2)
selected = meme_options[index]

# Output
print(f"Quantum says... your meme is: {selected.upper()}!")
qc.draw("mpl")