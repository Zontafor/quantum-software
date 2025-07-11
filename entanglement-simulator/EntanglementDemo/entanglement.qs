// QSD Entanglement Tests
// Copyright 2025 Michelle L. Wu & The MITRE Corporation.
//
// DO NOT MODIFY THIS FILE.

// entanglement.qs
// Q# operations for Bell state entanglement demo

namespace EntanglementDemo {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Canon;

    operation MeasureBellPair() : (Result, Result) {
        use qs = Qubit[2];
        H(qs[0]);
        CNOT(qs[0], qs[1]);

        let r0 = M(qs[0]);
        let r1 = M(qs[1]);

        ResetAll(qs);
        return (r0, r1);
    }

    operation BreakEntanglement() : (Result, Result) {
        use qs = Qubit[2];
        H(qs[0]);
        CNOT(qs[0], qs[1]);

        X(qs[1]); // Break entanglement

        let r0 = M(qs[0]);
        let r1 = M(qs[1]);

        ResetAll(qs);
        return (r0, r1);
    }
}