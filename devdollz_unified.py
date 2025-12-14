#!/usr/bin/env python3
"""
DevDollz Unified Engine Interface
Commercial dual-engine system supporting both Void-Proof and Resonant Amplification approaches.
"""

import sys
import os
from enum import Enum

class OptimizationMode(Enum):
    VOID_PROOF = "void_proof"
    RESONANT_AMPLIFICATION = "resonant_amplification"

class DevDollzUnified:
    """
    Unified interface for DevDollz Axiom-Zero Engine variants.
    Commercial system supporting multiple optimization paradigms.
    """

    def __init__(self):
        self.modes = {
            OptimizationMode.VOID_PROOF: self._void_proof_optimize,
            OptimizationMode.RESONANT_AMPLIFICATION: self._resonant_optimize
        }

    def optimize(self, source_file: str, mode: OptimizationMode = OptimizationMode.VOID_PROOF):
        """
        Optimize a Python file using the specified DevDollz approach.

        Args:
            source_file: Path to Python file to optimize
            mode: Optimization mode (VOID_PROOF or RESONANT_AMPLIFICATION)

        Returns:
            Tuple of (output_file, proof_echo)
        """
        if not os.path.exists(source_file):
            raise FileNotFoundError(f"Source file not found: {source_file}")

        if mode not in self.modes:
            raise ValueError(f"Unknown optimization mode: {mode}")

        optimizer = self.modes[mode]
        return optimizer(source_file)

    def _void_proof_optimize(self, source_file: str):
        """Apply Void-Proof Descent optimization."""
        # Import the void-proof agent
        sys.path.append(os.path.dirname(__file__))
        from void_proof_agent import VoidProofAgent
        from void_spec import VoidSpec

        with open(source_file, 'r') as f:
            source_code = f.read()

        # Create void specification
        spec = VoidSpec("UnifiedVoid", source_code)

        # Apply void-proof agent
        agent = VoidProofAgent()
        optimized_spec = agent.analyze_and_void(spec)

        # Generate manifest and output
        manifest = optimized_spec.get_manifest_header()
        final_code = manifest + "\n" + optimized_spec.source_code

        output_file = source_file.replace('.py', '_void_devdollz.py')
        with open(output_file, 'w') as f:
            f.write(final_code)

        return output_file, optimized_spec.proof_echo

    def _resonant_optimize(self, source_file: str):
        """Apply Resonant Amplification Descent optimization."""
        # Import the resonance agent
        sys.path.append(os.path.dirname(__file__))
        from resonance_descent import ResonanceAgent

        with open(source_file, 'r') as f:
            source_code = f.read()

        # Apply resonance agent
        agent = ResonanceAgent()
        optimized_code, proof = agent.analyze_and_resonate(source_code)

        # Generate resonance manifest
        manifest = f'''"""
# --- DEV DOLLZ :: AXIOM-ZERO RESONANCE ENGINE ---
# Perfection through resonant voids.
# {proof}
"""
'''
        final_code = manifest + "\n" + optimized_code

        output_file = source_file.replace('.py', '_resonance_devdollz.py')
        with open(output_file, 'w') as f:
            f.write(final_code)

        return output_file, proof

def main():
    """Unified command-line interface."""
    print("="*60)
    print("DEVDOLLZ UNIFIED ENGINE :: AXIOM-ZERO")
    print("="*60)

    if len(sys.argv) < 2:
        print("Usage: python3 devdollz_unified.py <source_file> [mode]")
        print("Modes:")
        print("  void      - Void-Proof Descent (default)")
        print("  resonance - Resonant Amplification Descent")
        print("\nExample:")
        print("  python3 devdollz_unified.py my_code.py void")
        print("  python3 devdollz_unified.py my_code.py resonance")
        return

    source_file = sys.argv[1]
    mode_str = sys.argv[2] if len(sys.argv) > 2 else "void"

    # Map string to enum
    mode_map = {
        "void": OptimizationMode.VOID_PROOF,
        "resonance": OptimizationMode.RESONANT_AMPLIFICATION
    }

    if mode_str not in mode_map:
        print(f"❌ Unknown mode: {mode_str}")
        print("Use: python3 devdollz_unified.py <file> void|resonance")
        return

    mode = mode_map[mode_str]

    try:
        engine = DevDollzUnified()
        output_file, proof = engine.optimize(source_file, mode)

        print("✅ OPTIMIZATION COMPLETE")
        print(f"📁 Output: {output_file}")
        print(f"🔬 Proof: {proof}")
        print("\n" + "="*60)
        print("DevDollz Axiom-Zero Engine")
        print("Perfection through resonant absence.")
        print("="*60)

    except Exception as e:
        print(f"❌ Optimization failed: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
