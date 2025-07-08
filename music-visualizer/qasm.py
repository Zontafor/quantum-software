#   Create rhythmic/tempo rules for multi-qubit gates vs single-qubit gates
#   Use Python packages like midiutil, scamp, or music21 to convert notes to MIDI output 

# QASM Music Visualizer – Gate-to-Note Mapping (Text Version)

# This demo parses a simple QASM circuit and maps quantum gates to musical notes or symbols.
# Students can see how different gates "compose" a melody or rhythm based on quantum logic.

import re
from typing import List

# def qasm_to_notes(qasm_str: str) -> List[str]:
#     gate_to_note = {
#             "h": "C",
#             "x": "D",
#             "z": "E",
#             "cx": "G",
#             "cz": "A",
#             "t": "B",
#             "tdg": "C#",
#             "s": "D#",
#             "sdg": "E#",
#             "y": "F",
#             "ccx": "Rest",
#         }

# # Match only valid gate names in sequence
# pattern = re.compile(r"\b(" + "|".join(gate_to_note.keys()) + r")\b")
# gates = pattern.findall(qasm_str.lower())

# return [gate_to_note[g] for g in gates]

# Example mini QASM string (can also load from file)
qasm_str = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
h q[0];
cx q[0],q[1];
x q[1];
z q[0];
"""

# Define gate-to-note map (C major scale + rhythm marks)
gate_to_note = {
    "h": "C",
    "x": "D",
    "z": "E",
    "cx": "G",
    "cz": "A",
    "t": "B",
    "tdg": "C#",
    "s": "D#",
    "sdg": "E#",
    "y": "F",
    "ccx": "Rest",
}

# Parse the QASM for known gates
pattern = re.compile(r"\b(" + "|".join(gate_to_note.keys()) + r")\b")
gates = pattern.findall(qasm_str)

# Map gates to notes
notes_sequence = [gate_to_note[g] for g in gates]

# Print the musical sequence
notes_sequence