import hashlib
from datetime import datetime, timezone


class Block:
    def __init__(
        self,
        index: int,
        version: str,
        data: str,
        previous_hash: str,
        timestamp: str | None = None,
    ) -> None:
        self.index = index
        self.version = version
        self.timestamp = timestamp or datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        value = f"{self.index}{self.version}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(value.encode("utf-8")).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        target_prefix = "0" * difficulty
        while not self.hash.startswith(target_prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self, difficulty: int = 3) -> None:
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        genesis = Block(index=0, version="1.0", data="Genesis Block", previous_hash="0")
        genesis.mine_block(self.difficulty)
        return genesis

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, data: str, version: str = "1.0") -> None:
        latest = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            version=version,
            data=data,
            previous_hash=latest.hash,
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        target_prefix = "0" * self.difficulty

        for i in range(len(self.chain)):
            current = self.chain[i]

            if current.hash != current.calculate_hash():
                return False

            if not current.hash.startswith(target_prefix):
                return False

            if i > 0:
                previous = self.chain[i - 1]
                if current.previous_hash != previous.hash:
                    return False

        return True

    def get_all_transactions(self) -> list[str]:
        return [block.data for block in self.chain[1:]]

    def modify_block_data(self, index: int, new_data: str) -> None:
        if index <= 0 or index >= len(self.chain):
            raise ValueError("Modify only non-genesis blocks with valid index.")

        block = self.chain[index]
        block.data = new_data
        block.hash = block.calculate_hash()

    def re_mine_from_block(self, start_index: int) -> None:
        if start_index <= 0 or start_index >= len(self.chain):
            raise ValueError("Re-mine only non-genesis blocks with valid index.")

        for i in range(start_index, len(self.chain)):
            block = self.chain[i]
            block.previous_hash = self.chain[i - 1].hash
            block.nonce = 0
            block.hash = block.calculate_hash()
            block.mine_block(self.difficulty)

    def print_chain(self) -> None:
        for block in self.chain:
            print(f"\nBlock #{block.index}")
            print(f"Version      : {block.version}")
            print(f"Timestamp    : {block.timestamp}")
            print(f"Data         : {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Nonce        : {block.nonce}")
            print(f"Hash         : {block.hash}")


def main() -> None:
    print("Simple Blockchain Demo (5 Blocks)")

    blockchain = Blockchain(difficulty=3)

    blockchain.add_block("Tx1: Alice pays Bob 10")
    blockchain.add_block("Tx2: Bob pays Charlie 4")
    blockchain.add_block("Tx3: Charlie pays David 2")
    blockchain.add_block("Tx4: David pays Eve 1")

    print(f"\nDifficulty set to: {blockchain.difficulty}")
    print(f"Total blocks     : {len(blockchain.chain)}")

    print("\n--- Full Chain ---")
    blockchain.print_chain()

    print("\n--- Verification ---")
    print(f"Chain valid before tampering? {blockchain.is_chain_valid()}")

    print("\n--- All Transactions ---")
    for i, tx in enumerate(blockchain.get_all_transactions(), start=1):
        print(f"{i}. {tx}")

    print("\n--- Modify Block Data ---")
    blockchain.modify_block_data(2, "Tx2: Bob pays Charlie 4000 (TAMPERED)")
    print("Block #2 data changed.")
    print(f"Chain valid after tampering?  {blockchain.is_chain_valid()}")

    print("\n--- Re-mine to Restore Validity ---")
    blockchain.re_mine_from_block(2)
    print(f"Chain valid after re-mining?  {blockchain.is_chain_valid()}")


if __name__ == "__main__":
    main()
