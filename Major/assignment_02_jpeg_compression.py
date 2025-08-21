"""
Assignment 2: Implement JPEG standards for image compression with DCT / Huffman coding/decoding
of image files. Repeat the process for text files.
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import heapq
from collections import defaultdict, Counter
import pickle
import os
from typing import Dict, List, Tuple, Any
import json

# ==================== DCT (Discrete Cosine Transform) IMPLEMENTATION ====================


class DCT:
    """Discrete Cosine Transform implementation for JPEG compression"""

    @staticmethod
    def dct_2d(block):
        """2D DCT transform"""
        N = block.shape[0]
        dct_matrix = DCT._create_dct_matrix(N)
        return dct_matrix @ block @ dct_matrix.T

    @staticmethod
    def idct_2d(block):
        """2D Inverse DCT transform"""
        N = block.shape[0]
        dct_matrix = DCT._create_dct_matrix(N)
        return dct_matrix.T @ block @ dct_matrix

    @staticmethod
    def _create_dct_matrix(N):
        """Create DCT transformation matrix"""
        dct_matrix = np.zeros((N, N))

        # First row (k=0)
        dct_matrix[0, :] = np.sqrt(1 / N)

        # Other rows (k>0)
        for k in range(1, N):
            for n in range(N):
                dct_matrix[k, n] = np.sqrt(2 / N) * np.cos(
                    (2 * n + 1) * k * np.pi / (2 * N)
                )

        return dct_matrix


# ==================== QUANTIZATION IMPLEMENTATION ====================


class Quantization:
    """JPEG quantization implementation"""

    # Standard JPEG quantization table for luminance
    STANDARD_QUANTIZATION_TABLE = np.array(
        [
            [16, 11, 10, 16, 24, 40, 51, 61],
            [12, 12, 14, 19, 26, 58, 60, 55],
            [14, 13, 16, 24, 40, 57, 69, 56],
            [14, 17, 22, 29, 51, 87, 80, 62],
            [18, 22, 37, 56, 68, 109, 103, 77],
            [24, 35, 55, 64, 81, 104, 113, 92],
            [49, 64, 78, 87, 103, 121, 120, 101],
            [72, 92, 95, 98, 112, 100, 103, 99],
        ],
        dtype=np.float32,
    )

    @staticmethod
    def quantize(dct_block, quality_factor=50):
        """Quantize DCT coefficients"""
        # Adjust quantization table based on quality factor
        if quality_factor < 50:
            scale = 5000 / quality_factor
        else:
            scale = 200 - 2 * quality_factor

        q_table = np.clip(
            (Quantization.STANDARD_QUANTIZATION_TABLE * scale + 50) / 100, 1, 255
        )

        return np.round(dct_block / q_table).astype(np.int32), q_table

    @staticmethod
    def dequantize(quantized_block, q_table):
        """Dequantize DCT coefficients"""
        return quantized_block * q_table


# ==================== HUFFMAN CODING IMPLEMENTATION ====================


class HuffmanNode:
    """Node for Huffman tree"""

    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    """Huffman coding implementation"""

    def __init__(self):
        self.codes = {}
        self.reverse_codes = {}
        self.tree = None

    def build_tree(self, data):
        """Build Huffman tree from data"""
        # Count frequencies
        if isinstance(data, str):
            frequency = Counter(data)
        else:
            # For image data (flatten the array)
            flat_data = data.flatten() if hasattr(data, "flatten") else data
            frequency = Counter(flat_data)

        # Create heap of nodes
        heap = []
        for char, freq in frequency.items():
            node = HuffmanNode(char=char, freq=freq)
            heapq.heappush(heap, node)

        # Special case: single character
        if len(heap) == 1:
            single_node = heapq.heappop(heap)
            root = HuffmanNode(freq=single_node.freq, left=single_node)
            self.tree = root
            self.codes[single_node.char] = "0"
            self.reverse_codes["0"] = single_node.char
            return

        # Build tree
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)

            heapq.heappush(heap, merged)

        self.tree = heap[0]
        self._generate_codes(self.tree, "")

    def _generate_codes(self, node, code):
        """Generate Huffman codes recursively"""
        if node is None:
            return

        if node.char is not None:  # Leaf node
            self.codes[node.char] = code if code else "0"
            self.reverse_codes[code if code else "0"] = node.char
            return

        self._generate_codes(node.left, code + "0")
        self._generate_codes(node.right, code + "1")

    def encode(self, data):
        """Encode data using Huffman codes"""
        if isinstance(data, str):
            encoded = "".join(self.codes[char] for char in data)
        else:
            # For image data
            flat_data = data.flatten() if hasattr(data, "flatten") else data
            encoded = "".join(self.codes[val] for val in flat_data)

        return encoded

    def decode(self, encoded_data, original_shape=None):
        """Decode Huffman encoded data"""
        decoded = []
        current_code = ""

        for bit in encoded_data:
            current_code += bit
            if current_code in self.reverse_codes:
                decoded.append(self.reverse_codes[current_code])
                current_code = ""

        if original_shape is not None:
            # Reshape for image data
            decoded_array = np.array(decoded)
            return decoded_array.reshape(original_shape)

        if isinstance(decoded[0], str):
            return "".join(decoded)
        else:
            return decoded


# ==================== JPEG COMPRESSION IMPLEMENTATION ====================


class JPEGCompressor:
    """Complete JPEG compression implementation"""

    def __init__(self, block_size=8, quality=50):
        self.block_size = block_size
        self.quality = quality
        self.huffman = HuffmanCoding()
        self.quantization_table = None
        self.original_shape = None

    def compress_image(self, image_path):
        """Compress an image using JPEG algorithm"""
        # Load image
        if isinstance(image_path, str):
            img = Image.open(image_path).convert("L")  # Convert to grayscale
            image_array = np.array(img, dtype=np.float32)
        else:
            image_array = image_path.astype(np.float32)

        self.original_shape = image_array.shape

        # Pad image to make it divisible by block_size
        padded_image = self._pad_image(image_array)

        # Split into blocks and apply DCT + Quantization
        compressed_blocks = []

        for i in range(0, padded_image.shape[0], self.block_size):
            for j in range(0, padded_image.shape[1], self.block_size):
                block = padded_image[i : i + self.block_size, j : j + self.block_size]

                # Apply DCT
                dct_block = DCT.dct_2d(block - 128)  # Center around 0

                # Quantize
                quantized_block, q_table = Quantization.quantize(
                    dct_block, self.quality
                )
                self.quantization_table = q_table  # Store for decompression

                compressed_blocks.append(quantized_block)

        # Flatten all blocks for Huffman encoding
        all_coefficients = np.concatenate(
            [block.flatten() for block in compressed_blocks]
        )

        # Apply Huffman coding
        self.huffman.build_tree(all_coefficients)
        encoded_data = self.huffman.encode(all_coefficients)

        # Calculate compression statistics
        original_bits = image_array.size * 8  # 8 bits per pixel
        compressed_bits = len(encoded_data)
        compression_ratio = original_bits / compressed_bits

        print(f"Original size: {original_bits} bits")
        print(f"Compressed size: {compressed_bits} bits")
        print(f"Compression ratio: {compression_ratio:.2f}:1")
        print(f"Space saved: {(1 - compressed_bits/original_bits)*100:.2f}%")

        return {
            "encoded_data": encoded_data,
            "huffman_tree": self.huffman,
            "quantization_table": self.quantization_table,
            "original_shape": self.original_shape,
            "padded_shape": padded_image.shape,
            "block_size": self.block_size,
            "compression_ratio": compression_ratio,
        }

    def decompress_image(self, compressed_data):
        """Decompress JPEG compressed image"""
        # Extract compressed data
        encoded_data = compressed_data["encoded_data"]
        huffman_tree = compressed_data["huffman_tree"]
        q_table = compressed_data["quantization_table"]
        original_shape = compressed_data["original_shape"]
        padded_shape = compressed_data["padded_shape"]
        block_size = compressed_data["block_size"]

        # Decode Huffman data
        decoded_coefficients = huffman_tree.decode(encoded_data)

        # Reshape into blocks
        num_blocks = (padded_shape[0] // block_size) * (padded_shape[1] // block_size)
        coefficients_per_block = block_size * block_size

        decoded_blocks = []
        for i in range(num_blocks):
            start_idx = i * coefficients_per_block
            end_idx = start_idx + coefficients_per_block
            block_coeffs = decoded_coefficients[start_idx:end_idx]
            block = np.array(block_coeffs).reshape(block_size, block_size)
            decoded_blocks.append(block)

        # Reconstruct image
        reconstructed_padded = np.zeros(padded_shape)
        block_idx = 0

        for i in range(0, padded_shape[0], block_size):
            for j in range(0, padded_shape[1], block_size):
                # Dequantize
                dequantized_block = Quantization.dequantize(
                    decoded_blocks[block_idx], q_table
                )

                # Apply IDCT
                reconstructed_block = DCT.idct_2d(dequantized_block) + 128

                reconstructed_padded[i : i + block_size, j : j + block_size] = (
                    reconstructed_block
                )
                block_idx += 1

        # Remove padding
        reconstructed_image = reconstructed_padded[
            : original_shape[0], : original_shape[1]
        ]

        # Clip values to valid range
        reconstructed_image = np.clip(reconstructed_image, 0, 255)

        return reconstructed_image.astype(np.uint8)

    def _pad_image(self, image):
        """Pad image to make it divisible by block_size"""
        h, w = image.shape
        new_h = ((h + self.block_size - 1) // self.block_size) * self.block_size
        new_w = ((w + self.block_size - 1) // self.block_size) * self.block_size

        padded = np.zeros((new_h, new_w))
        padded[:h, :w] = image

        return padded


# ==================== TEXT COMPRESSION IMPLEMENTATION ====================


class TextCompressor:
    """Text compression using similar principles to JPEG"""

    def __init__(self):
        self.huffman = HuffmanCoding()

    def compress_text(self, text):
        """Compress text using Huffman coding"""
        # Build Huffman tree
        self.huffman.build_tree(text)

        # Encode text
        encoded_data = self.huffman.encode(text)

        # Calculate compression statistics
        original_bits = len(text) * 8  # 8 bits per character (ASCII)
        compressed_bits = len(encoded_data)
        compression_ratio = (
            original_bits / compressed_bits if compressed_bits > 0 else 1
        )

        print(f"Text compression statistics:")
        print(f"Original size: {original_bits} bits ({len(text)} characters)")
        print(f"Compressed size: {compressed_bits} bits")
        print(f"Compression ratio: {compression_ratio:.2f}:1")
        print(f"Space saved: {(1 - compressed_bits/original_bits)*100:.2f}%")

        return {
            "encoded_data": encoded_data,
            "huffman_tree": self.huffman,
            "original_length": len(text),
            "compression_ratio": compression_ratio,
        }

    def decompress_text(self, compressed_data):
        """Decompress Huffman compressed text"""
        encoded_data = compressed_data["encoded_data"]
        huffman_tree = compressed_data["huffman_tree"]

        # Decode text
        decoded_text = huffman_tree.decode(encoded_data)

        return "".join(decoded_text)


# ==================== DEMONSTRATION AND TESTING ====================


def create_sample_image():
    """Create a sample image for testing"""
    # Create a simple pattern image
    img = np.zeros((64, 64), dtype=np.uint8)

    # Add some patterns
    img[10:30, 10:30] = 255  # White square
    img[35:55, 35:55] = 128  # Gray square

    # Add some gradients
    for i in range(64):
        img[i, :] = i * 4  # Horizontal gradient

    return img


def test_jpeg_compression():
    """Test JPEG compression on sample image"""
    print("=== JPEG Image Compression Test ===")

    # Create sample image
    sample_img = create_sample_image()

    # Test different quality levels
    qualities = [10, 50, 90]

    fig, axes = plt.subplots(2, len(qualities) + 1, figsize=(15, 8))

    # Show original
    axes[0, 0].imshow(sample_img, cmap="gray")
    axes[0, 0].set_title("Original Image")
    axes[0, 0].axis("off")

    axes[1, 0].axis("off")  # Empty space

    results = []

    for i, quality in enumerate(qualities):
        print(f"\nTesting quality level: {quality}")

        # Compress
        compressor = JPEGCompressor(quality=quality)
        compressed = compressor.compress_image(sample_img)

        # Decompress
        decompressed = compressor.decompress_image(compressed)

        # Calculate PSNR
        mse = np.mean((sample_img.astype(float) - decompressed.astype(float)) ** 2)
        psnr = 20 * np.log10(255 / np.sqrt(mse)) if mse > 0 else float("inf")

        print(f"PSNR: {psnr:.2f} dB")

        # Store results
        results.append(
            {
                "quality": quality,
                "compression_ratio": compressed["compression_ratio"],
                "psnr": psnr,
            }
        )

        # Display
        axes[0, i + 1].imshow(decompressed, cmap="gray")
        axes[0, i + 1].set_title(f"Quality {quality}\nPSNR: {psnr:.1f}dB")
        axes[0, i + 1].axis("off")

        # Show difference
        diff = np.abs(sample_img.astype(float) - decompressed.astype(float))
        axes[1, i + 1].imshow(diff, cmap="hot")
        axes[1, i + 1].set_title(
            f'Difference\nRatio: {compressed["compression_ratio"]:.1f}:1'
        )
        axes[1, i + 1].axis("off")

    plt.tight_layout()
    plt.savefig(
        "/Users/harshilpatel/CODE/Major/assignment_02_jpeg_results.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    return results


def test_text_compression():
    """Test text compression"""
    print("\n=== Text Compression Test ===")

    # Sample texts with different characteristics
    texts = {
        "Repetitive": "aaaaaabbbbbbccccccdddddd" * 10,
        "Random": "abcdefghijklmnopqrstuvwxyz" * 10,
        "English": """The quick brown fox jumps over the lazy dog. This sentence contains 
                     every letter of the English alphabet at least once. It is commonly used 
                     for testing fonts and keyboards."""
        * 3,
    }

    compressor = TextCompressor()

    for text_type, text in texts.items():
        print(f"\n--- {text_type} Text ---")
        print(f"Text preview: {text[:50]}...")

        # Compress
        compressed = compressor.compress_text(text)

        # Decompress
        decompressed = compressor.decompress_text(compressed)

        # Verify
        print(f"Decompression successful: {text == decompressed}")


def demonstrate_dct():
    """Demonstrate DCT properties"""
    print("\n=== DCT Demonstration ===")

    # Create a simple 8x8 block
    block = np.array(
        [
            [100, 100, 100, 100, 200, 200, 200, 200],
            [100, 100, 100, 100, 200, 200, 200, 200],
            [100, 100, 100, 100, 200, 200, 200, 200],
            [100, 100, 100, 100, 200, 200, 200, 200],
            [50, 50, 50, 50, 150, 150, 150, 150],
            [50, 50, 50, 50, 150, 150, 150, 150],
            [50, 50, 50, 50, 150, 150, 150, 150],
            [50, 50, 50, 50, 150, 150, 150, 150],
        ],
        dtype=np.float32,
    )

    print("Original block:")
    print(block)

    # Apply DCT
    dct_block = DCT.dct_2d(block - 128)
    print("\nDCT coefficients:")
    print(np.round(dct_block, 2))

    # Apply IDCT
    reconstructed = DCT.idct_2d(dct_block) + 128
    print("\nReconstructed block:")
    print(np.round(reconstructed, 2))

    # Check reconstruction error
    error = np.mean(np.abs(block - reconstructed))
    print(f"\nReconstruction error: {error:.6f}")


def main():
    """Main function to demonstrate all compression techniques"""
    print("Assignment 2: JPEG Compression with DCT and Huffman Coding\n")

    # Demonstrate DCT properties
    demonstrate_dct()

    # Test JPEG compression
    jpeg_results = test_jpeg_compression()

    # Test text compression
    test_text_compression()

    # Summary
    print("\n" + "=" * 50)
    print("COMPRESSION SUMMARY")
    print("=" * 50)

    print("\nJPEG Compression Results:")
    for result in jpeg_results:
        print(
            f"Quality {result['quality']:2d}: Ratio {result['compression_ratio']:5.1f}:1, "
            f"PSNR {result['psnr']:5.1f} dB"
        )

    print("\nKey Features Implemented:")
    print("✓ 2D Discrete Cosine Transform (DCT)")
    print("✓ JPEG quantization with quality control")
    print("✓ Huffman coding for entropy encoding")
    print("✓ Complete JPEG compression/decompression pipeline")
    print("✓ Text compression using Huffman coding")
    print("✓ Performance metrics (PSNR, compression ratio)")

    print("\nApplications:")
    print("• Image compression for web and storage")
    print("• Text compression for data transmission")
    print("• Lossy vs lossless compression trade-offs")
    print("• Frequency domain analysis and compression")


if __name__ == "__main__":
    main()
