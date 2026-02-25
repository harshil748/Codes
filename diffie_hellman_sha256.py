import hashlib
import random
from typing import Tuple


class DiffieHellmanKeyExchange:

    def __init__(self, p: int = None, g: int = None):
        
        if p is None:
            self.p = 23  
        else:
            self.p = p

        if g is None:
            self.g = 5  
        else:
            self.g = g

    def generate_private_key(self) -> int:
        return random.randint(2, self.p - 2)

    def generate_public_key(self, private_key: int) -> int:
        """
        Generate public key from private key

        Formula: A = g^a mod p (for Alice) or B = g^b mod p (for Bob)

        Args:
            private_key (int): Private key (a or b)

        Returns:
            int: Public key to be shared over the channel
        """
        return pow(self.g, private_key, self.p)

    def generate_shared_secret(self, private_key: int, other_public_key: int) -> int:
        """
        Generate the shared secret using the other party's public key and own private key

        Formula: s = B^a mod p (Alice's computation) or s = A^b mod p (Bob's computation)

        Both parties compute the same secret without transmitting it.

        Args:
            private_key (int): Own private key
            other_public_key (int): Received public key from other party

        Returns:
            int: Shared secret (same at both ends)
        """
        return pow(other_public_key, private_key, self.p)


class SecureMessageHandler:
    """
    Handles secure message hashing and verification using SHA256
    """

    @staticmethod
    def compute_hash(message: str, secret: int) -> str:
        """
        Compute SHA256 hash of message concatenated with secret

        Formula: H(M||s) where || denotes concatenation

        Args:
            message (str): Original message M
            secret (int): Shared secret s

        Returns:
            str: Hexadecimal representation of the hash
        """
        # Concatenate message with secret (convert secret to string)
        combined = message + str(secret)

        # Compute SHA256 hash
        hash_obj = hashlib.sha256(combined.encode("utf-8"))
        return hash_obj.hexdigest()

    @staticmethod
    def verify_hash(message: str, secret: int, received_hash: str) -> bool:
        """
        Verify that received message has not been altered

        Args:
            message (str): Received message M
            secret (int): Shared secret s
            received_hash (str): Received hash H(M||s) to verify against

        Returns:
            bool: True if hash matches (message not altered), False otherwise
        """
        computed_hash = SecureMessageHandler.compute_hash(message, secret)
        return computed_hash == received_hash


def demonstrate_protocol():
    """
    Demonstrate the complete Diffie-Hellman key exchange and message verification protocol
    """

    print("=" * 80)
    print("SECURE MESSAGE EXCHANGE PROTOCOL DEMONSTRATION")
    print("Using Diffie-Hellman Key Exchange and SHA256 Hashing")
    print("=" * 80)

    # ============================================================================
    # STEP 1: SETUP - Public parameters (known to both parties and attackers)
    # ============================================================================
    print("\n[STEP 1] PUBLIC PARAMETERS (Known to everyone)")
    print("-" * 80)

    dh = DiffieHellmanKeyExchange(p=23, g=5)
    print(f"Prime modulus (p) = {dh.p}")
    print(f"Generator (g) = {dh.g}")
    print("\nThese values are public and can be transmitted over insecure channels.")

    # ============================================================================
    # STEP 2: BOB's Key Generation
    # ============================================================================
    print("\n[STEP 2] BOB'S KEY GENERATION")
    print("-" * 80)

    bob_private_key = dh.generate_private_key()
    bob_public_key = dh.generate_public_key(bob_private_key)

    print(f"Bob's private key (a) = {bob_private_key} [KEPT SECRET - Not transmitted]")
    print(
        f"Bob's public key (A) = g^a mod p = {dh.g}^{bob_private_key} mod {dh.p} = {bob_public_key}"
    )
    print(
        f"\nBob sends his public key {bob_public_key} over the insecure channel to Alice."
    )

    # ============================================================================
    # STEP 3: ALICE's Key Generation
    # ============================================================================
    print("\n[STEP 3] ALICE'S KEY GENERATION")
    print("-" * 80)

    alice_private_key = dh.generate_private_key()
    alice_public_key = dh.generate_public_key(alice_private_key)

    print(
        f"Alice's private key (b) = {alice_private_key} [KEPT SECRET - Not transmitted]"
    )
    print(
        f"Alice's public key (B) = g^b mod p = {dh.g}^{alice_private_key} mod {dh.p} = {alice_public_key}"
    )
    print(
        f"\nAlice sends her public key {alice_public_key} over the insecure channel to Bob."
    )

    # ============================================================================
    # STEP 4: SHARED SECRET COMPUTATION
    # ============================================================================
    print("\n[STEP 4] SHARED SECRET COMPUTATION")
    print("-" * 80)

    # Bob computes shared secret using Alice's public key and his private key
    bob_shared_secret = dh.generate_shared_secret(bob_private_key, alice_public_key)
    print(
        f"Bob computes: s = B^a mod p = {alice_public_key}^{bob_private_key} mod {dh.p} = {bob_shared_secret}"
    )

    # Alice computes shared secret using Bob's public key and her private key
    alice_shared_secret = dh.generate_shared_secret(alice_private_key, bob_public_key)
    print(
        f"Alice computes: s = A^b mod p = {bob_public_key}^{alice_private_key} mod {dh.p} = {alice_shared_secret}"
    )

    # Verify that both computed the same secret
    print(
        f"\n✓ Both parties have computed the SAME secret: {bob_shared_secret == alice_shared_secret}"
    )
    print(f"\nShared Secret (s) = {bob_shared_secret}")
    print("This secret was NEVER transmitted over the channel! 🔐")

    # ============================================================================
    # STEP 5: BOB SENDS MESSAGE WITH HASH
    # ============================================================================
    print("\n[STEP 5] BOB SENDS MESSAGE TO ALICE")
    print("-" * 80)

    message = "Hello Alice! This is a secure message."
    print(f"Original Message (M) = '{message}'")

    # Bob computes hash of message concatenated with secret
    hash_value = SecureMessageHandler.compute_hash(message, bob_shared_secret)
    print(f"\nBob computes: H(M||s) = SHA256('{message}' || {bob_shared_secret})")
    print(f"Hash H(M||s) = {hash_value}")

    print(f"\nBob sends over the channel:")
    print(f"  - Message (M): '{message}'")
    print(f"  - Hash (H): {hash_value}")
    print("\nAttackers can see both M and H(M||s), but they cannot modify M")
    print("because they don't know the secret s!")

    # ============================================================================
    # STEP 6: ALICE RECEIVES AND VERIFIES
    # ============================================================================
    print("\n[STEP 6] ALICE RECEIVES AND VERIFIES MESSAGE")
    print("-" * 80)

    print(f"Alice receives:")
    print(f"  - Message (M): '{message}'")
    print(f"  - Hash (H): {hash_value}")

    # Alice computes hash using her secret and received message
    alice_computed_hash = SecureMessageHandler.compute_hash(
        message, alice_shared_secret
    )
    print(f"\nAlice computes: H(M||s) = SHA256('{message}' || {alice_shared_secret})")
    print(f"Hash computed by Alice: {alice_computed_hash}")

    # Verify hash
    is_verified = SecureMessageHandler.verify_hash(
        message, alice_shared_secret, hash_value
    )
    print(f"\nVerification: Received Hash == Computed Hash?")
    print(f"{hash_value}")
    print(f"==")
    print(f"{alice_computed_hash}")
    print(f"\n✓ MESSAGE VERIFIED: {is_verified}")
    if is_verified:
        print("The message has NOT been altered by attackers!")

    # ============================================================================
    # STEP 7: DEMONSTRATE TAMPERING DETECTION
    # ============================================================================
    print("\n[STEP 7] TAMPERING DETECTION DEMONSTRATION")
    print("-" * 80)

    tampered_message = "Hello Alice! This is a malicious message."
    print(f"If an attacker tampers with the message to: '{tampered_message}'")

    tampered_hash = SecureMessageHandler.compute_hash(
        tampered_message, alice_shared_secret
    )
    is_tampered_verified = SecureMessageHandler.verify_hash(
        tampered_message, alice_shared_secret, hash_value
    )

    print(f"The hash of tampered message would be: {tampered_hash}")
    print(f"\nVerification result: {is_tampered_verified}")
    print("✗ MESSAGE AUTHENTICITY FAILED: Tampering detected!")
    print("\nAlice would reject this message as it's not authentic.")

    # ============================================================================
    # MATHEMATICAL EXPLANATION
    # ============================================================================
    print("\n" + "=" * 80)
    print("WHY DIFFIE-HELLMAN WORKS - MATHEMATICAL FOUNDATION")
    print("=" * 80)

    print(
        """
The security relies on the following mathematical property:

    Bob computes: s = B^a mod p = (g^b mod p)^a mod p = g^(b*a) mod p
    Alice computes: s = A^b mod p = (g^a mod p)^b mod p = g^(a*b) mod p
    
Since multiplication is commutative: b*a = a*b
Therefore: g^(b*a) mod p = g^(a*b) mod p

Both parties arrive at the SAME secret!

An attacker who intercepts A and B cannot compute the secret because:
- They would need to solve: g^x ≡ A (mod p), which is the DISCRETE LOGARITHM PROBLEM
- This is computationally infeasible for large primes
    """
    )

    # ============================================================================
    # SUMMARY TABLE
    # ============================================================================
    print("\n" + "=" * 80)
    print("SUMMARY TABLE")
    print("=" * 80)

    print(f"\n{'Parameter':<30} {'Value':<20} {'Status'}")
    print("-" * 70)
    print(f"{'Prime (p)':<30} {dh.p:<20} Public")
    print(f"{'Generator (g)':<30} {dh.g:<20} Public")
    print(f"{'Bob Private Key (a)':<30} {bob_private_key:<20} Secret ✓")
    print(f"{'Bob Public Key (A)':<30} {bob_public_key:<20} Public")
    print(f"{'Alice Private Key (b)':<30} {alice_private_key:<20} Secret ✓")
    print(f"{'Alice Public Key (B)':<30} {alice_public_key:<20} Public")
    print(f"{'Shared Secret (s)':<30} {bob_shared_secret:<20} Secret ✓")
    print(f"{'Message':<30} {'(shown above)':<20} Public")
    print(f"{'Hash H(M||s)':<30} {'(first 16 chars)':<20} Public")
    print(f"  {hash_value[:16]}...")

    print("\n" + "=" * 80)


def demonstrate_with_larger_primes():
    """
    Demonstrate with larger prime values and compare computation time
    """
    import time

    print("\n\n" + "=" * 80)
    print("SUPPLEMENTARY: DIFFIE-HELLMAN WITH LARGER PRIMES")
    print("=" * 80)

    # Small primes (original demonstration)
    print("\n[TEST 1] Small Primes (p=23)")
    print("-" * 80)
    dh_small = DiffieHellmanKeyExchange(p=23, g=5)

    start = time.time()
    for _ in range(1000):
        private = dh_small.generate_private_key()
        public = dh_small.generate_public_key(private)
    small_time = time.time() - start

    print(f"Time for 1000 iterations: {small_time:.6f} seconds")

    # Larger primes
    print("\n[TEST 2] Larger Prime (p=104729, g=2)")
    print("-" * 80)
    dh_large = DiffieHellmanKeyExchange(p=104729, g=2)

    start = time.time()
    for _ in range(1000):
        private = dh_large.generate_private_key()
        public = dh_large.generate_public_key(private)
    large_time = time.time() - start

    print(f"Time for 1000 iterations: {large_time:.6f} seconds")

    # Even larger primes
    print("\n[TEST 3] Very Large Prime (2^16 - 15 = 65521, g=2)")
    print("-" * 80)
    dh_very_large = DiffieHellmanKeyExchange(p=65521, g=2)

    start = time.time()
    for _ in range(1000):
        private = dh_very_large.generate_private_key()
        public = dh_very_large.generate_public_key(private)
    very_large_time = time.time() - start

    print(f"Time for 1000 iterations: {very_large_time:.6f} seconds")

    print("\n[COMPARISON]")
    print("-" * 80)
    print(f"Small primes (p=23): {small_time:.6f}s")
    print(
        f"Larger primes (p=104729): {large_time:.6f}s (≈{large_time/small_time:.1f}x slower)"
    )
    print(
        f"Very large primes (p=65521): {very_large_time:.6f}s (≈{very_large_time/small_time:.1f}x slower)"
    )

    print("\nNote: Modern implementations use much larger primes (2048-4096 bits)")
    print("to prevent discrete logarithm attacks. The computation time increases")
    print("logarithmically with the bit size of the prime.")


def answer_key_questions():
    """
    Answer the key questions posed in the assignment
    """
    print("\n\n" + "=" * 80)
    print("ANSWERS TO KEY QUESTIONS")
    print("=" * 80)

    print(
        """
QUESTION 1: Why is key exchange necessary when Bob and Alice do not want 
             to send the actual secret key on the communication channel?

ANSWER:
--------
Key exchange is necessary for several critical reasons:

1. SECURE COMMUNICATION OVER PUBLIC CHANNELS
   - In many scenarios, Bob and Alice cannot physically meet to share a secret
   - They must establish shared secrets over potentially insecure networks
   - Directly sending the secret key would expose it to interception

2. PREVENTING EAVESDROPPING
   - If they send the secret key directly, attackers can intercept it
   - The entire communication then becomes compromised
   - Key exchange allows them to establish secrets without exposing them

3. FORWARD SECRECY
   - Different communication sessions can use different secrets
   - Even if one session is compromised, others remain protected
   - This is impossible if they use a pre-shared key for all sessions

4. SCALABILITY
   - In a network with many parties, key exchange allows pairwise secrets
   - Without it, maintaining many different pre-shared keys becomes impractical
   - Key exchange enables secure communication between any pair of parties

5. MAN-IN-THE-MIDDLE ATTACK PREVENTION
   - Key exchange, when properly authenticated, prevents attackers from 
     inserting themselves between the communicating parties

REAL-WORLD ANALOGY:
Alice and Bob are in different rooms. They want to create a "code" together.
- If Alice shouts the code, everyone in the building hears it (insecure)
- Using key exchange, they can each compute the code using public information
  in a way that only they can derive the same private code (secure)


QUESTION 2: How does the Diffie–Hellman key exchange generate the same 
             secret at both ends without transmitting it?

ANSWER:
--------
Diffie-Hellman leverages the mathematical property of modular exponentiation:

MATHEMATICAL BASIS:
-------------------
Given a prime p, generator g, and the discrete logarithm problem hardness:

Bob's computation:      Alice's computation:
A = g^a mod p          B = g^b mod p
s = B^a mod p          s = A^b mod p

Due to the property: (g^b)^a ≡ g^(ba) ≡ g^(ab) ≡ (g^a)^b (mod p)

Both compute: s = g^(ab) mod p = SAME SECRET

WHY IT WORKS:
-------------
1. SECRECY OF PRIVATE KEYS
   - Bob keeps 'a' secret; Alice keeps 'b' secret
   - These are NEVER transmitted over the network
   
2. PUBLIC EXCHANGE
   - Only A = g^a mod p and B = g^b mod p are transmitted
   - These are public, but knowing A and B alone doesn't reveal a or b
   
3. DISCRETE LOGARITHM PROBLEM
   - An attacker intercepting A and B cannot easily find 'a' or 'b'
   - They would need to solve: g^x ≡ A (mod p)
   - This is computationally infeasible for large primes
   
4. SYMMETRIC COMPUTATION
   - The mathematical properties ensure both parties compute g^(ab) mod p
   - Different private values (a, b) combine to create identical secrets

CONCRETE EXAMPLE:
-----------------
p = 23, g = 5 (public)
Bob: a = 6 (secret)    → A = 5^6 mod 23 = 8 (public)
Alice: b = 15 (secret) → B = 5^15 mod 23 = 19 (public)

Bob computes: s = 19^6 mod 23 = 2
Alice computes: s = 8^15 mod 23 = 2

They both get 2, though through different paths!
An attacker seeing only 8 and 19 cannot determine 2.

LIMITATIONS AND SOLUTIONS:
--------------------------
- Basic DH is vulnerable to man-in-the-middle attacks
- Solution: Authenticate the public keys using digital signatures
- Modern protocols (ECDHE, TLS) use authenticated variants
    """
    )


if __name__ == "__main__":
    # Run the main demonstration
    demonstrate_protocol()

    # Demonstrate with larger primes
    demonstrate_with_larger_primes()

    # Answer key questions
    answer_key_questions()

    print("\n" + "=" * 80)
    print("DEMONSTRATION COMPLETE")
    print("=" * 80)
