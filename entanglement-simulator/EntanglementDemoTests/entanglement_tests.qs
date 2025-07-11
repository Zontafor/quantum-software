// QSD Entanglement Tests
// Copyright 2025 Michelle L. Wu & The MITRE Corporation.
//
// DO NOT MODIFY THIS FILE.

namespace EntanglementDemoTests {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Diagnostics;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Canon;
    open EntanglementDemo;

    @Test()
    operation TestMeasureBellPair() : Unit {
        mutable matchCount = 0;
        let trials = 100;

        for _ in 1..trials {
            let (r0, r1) : (Result, Result) = MeasureBellPair();
            if (r0 == r1) {
                set matchCount += 1;
            }
        }

        Message($"Matching outcomes in {matchCount} of {trials} trials.");

        let ratio = IntAsDouble(matchCount) / IntAsDouble(trials);
        Fact(ratio > 0.9, "Qubits are not sufficiently correlated (Bell pair entanglement test).");
    }

    @Test()
    operation TestBreakEntanglement() : Unit {
        mutable matchCount = 0;
        let trials = 100;

        for _ in 1..trials {
            let (r0, r1) : (Result, Result) = BreakEntanglement();
            if (r0 == r1) {
                set matchCount += 1;
            }
        }

        Message($"Matching outcomes after break: {matchCount} of {trials}");

        let ratio = IntAsDouble(matchCount) / IntAsDouble(trials);
        Fact(ratio < 0.7 and ratio > 0.3, "Qubits are still too correlated — entanglement break may have failed.");
    }
}