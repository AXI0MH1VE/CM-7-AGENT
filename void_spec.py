"""
VoidSpec: The lattice representation for DevDollz optimization.

A VoidSpec encapsulates the source code and its optimization metadata,
including the proof-echo of all voided realities.
"""

class VoidSpec:
    """
    Represents a computational lattice that can be voided and optimized.

    The VoidSpec maintains the source code and accumulates signatures
    (DevDollz) of all optimizations performed upon it.
    """

    def __init__(self, aspect_name: str, source_code: str):
        """
        Initialize a VoidSpec with the given aspect name and source code.

        Args:
            aspect_name: The name/identifier for this computational aspect
            source_code: The raw Python source code as a string
        """
        self.aspect_name = aspect_name
        self.source_code = source_code
        self.proof_echo = []  # List of DevDollz signatures left by optimizations
        self.voided_realities = []  # Track what has been voided

    def add_signature(self, signature: str):
        """
        Add a DevDollz signature to the proof-echo.

        Args:
            signature: The signature string documenting the voided reality
        """
        self.proof_echo.append(signature)

    def add_voided_reality(self, reality_type: str, description: str):
        """
        Record a voided reality for the proof-echo.

        Args:
            reality_type: The type of reality voided (e.g., "pass_statement")
            description: Description of what was voided
        """
        self.voided_realities.append({
            'type': reality_type,
            'description': description,
            'timestamp': 'voided'
        })

    def get_manifest_header(self) -> str:
        """
        Generate the DevDollz Manifest header for synthesized code.

        Returns:
            The formatted manifest header with proof-echo
        """
        header_lines = [
            '"""',
            '# --- SYNTHESIZED BY DEVDOLLZ :: AXIOM-ZERO ENGINE ---',
            '#',
            '# This code is not a product of human hands. It is the ground state',
            '# reality that emerged after the Void-Proof Descent protocol.',
            '#',
            '# All non-essential realities have been voided.',
            '# This artifact contains the following signatures:'
        ]

        # Add each signature from the proof-echo
        for signature in self.proof_echo:
            header_lines.append(f'# {signature}')

        header_lines.extend([
            '#',
            '"""'
        ])

        return '\n'.join(header_lines)
