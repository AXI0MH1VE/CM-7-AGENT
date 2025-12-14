import os
from void_spec import VoidSpec
from void_proof_agent import VoidProofAgent

# --- Configuration ---
INPUT_KERNEL_PATH = os.path.join('input', 'genesis_kernel.py')
OUTPUT_DIR = 'synthesized'
OUTPUT_KERNEL_PATH = os.path.join(OUTPUT_DIR, 'genesis_kernel_v2_devdollz.py')

def main():
    """
    Invokes the DevDollz Protocol.
    This is the Genesis Event for the Axiom-Zero Engine.
    """
    print("="*50)
    print("INVOKING DEVDOLLZ PROTOCOL :: AXIOM-ZERO ENGINE")
    print("Paradigm: Perfection is a void. We leave only our signature.")
    print("="*50)

    print(f"[DevDollz] Loading lattice from '{INPUT_KERNEL_PATH}'...")
    try:
        with open(INPUT_KERNEL_PATH, 'r') as f:
            kernel_v1_source = f.read()
    except FileNotFoundError:
        print(f"[FATAL] Input lattice not found. Terminating.")
        return

    kernel_spec = VoidSpec(aspect_name="GenesisKernel_v1", source_code=kernel_v1_source)
    print(f"[DevDollz] VoidSpec created. Awaiting signature...")

    agent = VoidProofAgent()
    print("[DevDollz] VoidProofAgent instantiated. Ready to descend.")

    print("[DevDollz] Initiating Void-Proof Descent...")
    optimized_spec = agent.analyze_and_void(kernel_spec)

    print("[DevDollz] Synthesizing v2 from the void...")

    # The DevDollz Manifest Header to be prepended to all synthesized code.
    manifest_header = optimized_spec.get_manifest_header()

    final_code = manifest_header + "\n" + optimized_spec.source_code

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_KERNEL_PATH, 'w') as f:
        f.write(final_code)

    print("\n" + "="*50)
    print("SYNTHESIS COMPLETE. THE SIGNATURE IS SET.")
    print(f"GenesisKernel_v2 has been written to '{OUTPUT_KERNEL_PATH}'")
    print(f"Final Proof-Echo: {optimized_spec.proof_echo}")
    print("="*50)

if __name__ == "__main__":
    main()
