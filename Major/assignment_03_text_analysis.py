"""
Assignment 3: Generate a text file of 250 words. Given a large text file, count word frequencies
and output the top 20 most common words, ignoring stop words.
"""

import re
import string
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
import seaborn as sns
import random

# ==================== TEXT GENERATION ====================


class TextGenerator:
    """Generate sample text for analysis"""

    # Sample sentences for text generation
    SAMPLE_SENTENCES = [
        "The artificial intelligence revolution is transforming how we work and live.",
        "Machine learning algorithms can process vast amounts of data efficiently.",
        "Natural language processing enables computers to understand human language.",
        "Deep learning networks mimic the structure of the human brain.",
        "Data science combines statistics, programming, and domain expertise.",
        "Computer vision allows machines to interpret and analyze visual information.",
        "Robotics engineering integrates mechanical, electrical, and software systems.",
        "Cybersecurity protects digital systems from malicious attacks and threats.",
        "Cloud computing provides scalable and flexible computing resources.",
        "Big data analytics reveals patterns and insights from large datasets.",
        "Software development requires careful planning and systematic implementation.",
        "User experience design focuses on creating intuitive and accessible interfaces.",
        "Database management systems organize and store information efficiently.",
        "Network protocols enable communication between different computer systems.",
        "Algorithm optimization improves performance and reduces computational complexity.",
        "Information technology continues to evolve at an unprecedented pace.",
        "Digital transformation reshapes traditional business models and processes.",
        "Programming languages provide tools for expressing computational solutions.",
        "System architecture determines how software components interact and communicate.",
        "Technology innovation drives economic growth and social progress.",
        "Research and development fuel advances in scientific and technological fields.",
        "Human-computer interaction studies how people use and interact with technology.",
        "Distributed systems handle computation across multiple connected computers.",
        "Mobile applications have revolutionized how we access and share information.",
        "Internet connectivity has created a global network of communication.",
        "Virtual reality creates immersive digital environments for various applications.",
        "Augmented reality overlays digital information onto the physical world.",
        "Blockchain technology enables secure and decentralized digital transactions.",
        "Quantum computing promises to solve complex problems beyond classical capabilities.",
        "Biotechnology applies engineering principles to biological systems and processes.",
    ]

    @classmethod
    def generate_text(cls, target_words=250):
        """Generate text with approximately target_words words"""
        text_parts = []
        word_count = 0

        while word_count < target_words:
            # Randomly select a sentence
            sentence = random.choice(cls.SAMPLE_SENTENCES)
            text_parts.append(sentence)

            # Count words in the sentence
            words_in_sentence = len(sentence.split())
            word_count += words_in_sentence

        # Join sentences with spaces
        generated_text = " ".join(text_parts)

        # Trim to approximately target words
        words = generated_text.split()
        if len(words) > target_words:
            words = words[:target_words]
            generated_text = " ".join(words)

        return generated_text


# ==================== STOP WORDS ====================


class StopWords:
    """Handle stop words for text analysis"""

    # Common English stop words
    ENGLISH_STOP_WORDS = {
        "a",
        "an",
        "and",
        "are",
        "as",
        "at",
        "be",
        "been",
        "by",
        "for",
        "from",
        "has",
        "he",
        "in",
        "is",
        "it",
        "its",
        "of",
        "on",
        "that",
        "the",
        "to",
        "was",
        "will",
        "with",
        "would",
        "have",
        "had",
        "his",
        "her",
        "she",
        "they",
        "their",
        "them",
        "we",
        "us",
        "our",
        "you",
        "your",
        "i",
        "me",
        "my",
        "this",
        "these",
        "those",
        "but",
        "or",
        "can",
        "could",
        "should",
        "would",
        "do",
        "does",
        "did",
        "dont",
        "don't",
        "wont",
        "won't",
        "cant",
        "can't",
        "not",
        "no",
        "nor",
        "only",
        "own",
        "same",
        "so",
        "than",
        "too",
        "very",
        "s",
        "t",
        "all",
        "any",
        "both",
        "each",
        "few",
        "more",
        "most",
        "other",
        "some",
        "such",
        "up",
        "out",
        "just",
        "now",
        "then",
        "when",
        "where",
        "why",
        "how",
        "what",
        "which",
        "who",
        "whom",
        "whose",
        "if",
        "because",
        "while",
        "during",
        "before",
        "after",
        "above",
        "below",
        "between",
        "through",
        "into",
        "over",
        "under",
        "again",
        "further",
        "once",
        "here",
        "there",
        "everywhere",
        "anywhere",
        "somewhere",
    }

    @classmethod
    def is_stop_word(cls, word):
        """Check if a word is a stop word"""
        return word.lower().strip() in cls.ENGLISH_STOP_WORDS

    @classmethod
    def add_stop_words(cls, words):
        """Add custom stop words"""
        if isinstance(words, str):
            words = [words]
        cls.ENGLISH_STOP_WORDS.update(word.lower().strip() for word in words)


# ==================== TEXT ANALYZER ====================


class TextAnalyzer:
    """Comprehensive text analysis tools"""

    def __init__(self, custom_stop_words=None):
        self.stop_words = StopWords()
        if custom_stop_words:
            self.stop_words.add_stop_words(custom_stop_words)

        self.word_frequencies = Counter()
        self.processed_text = ""
        self.total_words = 0
        self.unique_words = 0

    def preprocess_text(self, text):
        """Clean and preprocess text"""
        # Convert to lowercase
        text = text.lower()

        # Remove punctuation and special characters
        text = re.sub(r"[^\w\s]", " ", text)

        # Remove extra whitespace
        text = re.sub(r"\s+", " ", text).strip()

        self.processed_text = text
        return text

    def extract_words(self, text):
        """Extract words from text, filtering stop words"""
        preprocessed = self.preprocess_text(text)
        words = preprocessed.split()

        # Filter out stop words and very short words
        filtered_words = []
        for word in words:
            if (
                len(word) >= 2
                and not self.stop_words.is_stop_word(word)
                and word.isalpha()
            ):  # Only alphabetic words
                filtered_words.append(word)

        return filtered_words

    def analyze_text(self, text):
        """Perform comprehensive text analysis"""
        # Extract and count words
        words = self.extract_words(text)
        self.word_frequencies = Counter(words)

        # Calculate statistics
        self.total_words = len(words)
        self.unique_words = len(self.word_frequencies)

        # Analysis results
        results = {
            "total_words": self.total_words,
            "unique_words": self.unique_words,
            "word_frequencies": self.word_frequencies,
            "vocabulary_richness": (
                self.unique_words / self.total_words if self.total_words > 0 else 0
            ),
            "most_common": self.word_frequencies.most_common(20),
            "longest_words": self.get_longest_words(),
            "word_length_distribution": self.get_word_length_distribution(words),
        }

        return results

    def get_longest_words(self, top_n=10):
        """Get the longest words in the text"""
        if not self.word_frequencies:
            return []

        # Sort words by length (descending) and frequency (descending)
        sorted_words = sorted(
            self.word_frequencies.items(), key=lambda x: (len(x[0]), x[1]), reverse=True
        )

        return sorted_words[:top_n]

    def get_word_length_distribution(self, words):
        """Get distribution of word lengths"""
        lengths = [len(word) for word in words]
        length_counter = Counter(lengths)
        return dict(sorted(length_counter.items()))

    def get_top_words(self, n=20):
        """Get top N most frequent words"""
        return self.word_frequencies.most_common(n)

    def search_words(self, pattern):
        """Search for words matching a pattern"""
        matching_words = []
        for word, freq in self.word_frequencies.items():
            if re.search(pattern, word, re.IGNORECASE):
                matching_words.append((word, freq))

        return sorted(matching_words, key=lambda x: x[1], reverse=True)


# ==================== VISUALIZATION ====================


class TextVisualizer:
    """Create visualizations for text analysis"""

    @staticmethod
    def plot_word_frequencies(word_freq_list, title="Top 20 Most Common Words"):
        """Plot word frequency bar chart"""
        if len(word_freq_list) == 0:
            print("No words to plot")
            return

        words, frequencies = zip(*word_freq_list)

        plt.figure(figsize=(12, 8))
        bars = plt.bar(
            range(len(words)), frequencies, color="skyblue", edgecolor="navy", alpha=0.7
        )

        plt.title(title, fontsize=16, fontweight="bold")
        plt.xlabel("Words", fontsize=12)
        plt.ylabel("Frequency", fontsize=12)
        plt.xticks(range(len(words)), words, rotation=45, ha="right")

        # Add frequency labels on bars
        for i, bar in enumerate(bars):
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2.0,
                height + 0.1,
                str(frequencies[i]),
                ha="center",
                va="bottom",
            )

        plt.tight_layout()
        return plt.gcf()

    @staticmethod
    def plot_word_length_distribution(length_dist):
        """Plot word length distribution"""
        if not length_dist:
            print("No word length data to plot")
            return

        lengths = list(length_dist.keys())
        counts = list(length_dist.values())

        plt.figure(figsize=(10, 6))
        bars = plt.bar(
            lengths, counts, color="lightcoral", edgecolor="darkred", alpha=0.7
        )

        plt.title("Word Length Distribution", fontsize=16, fontweight="bold")
        plt.xlabel("Word Length (characters)", fontsize=12)
        plt.ylabel("Number of Words", fontsize=12)

        # Add count labels on bars
        for bar, count in zip(bars, counts):
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2.0,
                height + 0.1,
                str(count),
                ha="center",
                va="bottom",
            )

        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        return plt.gcf()

    @staticmethod
    def create_word_cloud(word_frequencies, title="Word Cloud"):
        """Create a word cloud visualization"""
        try:
            if not word_frequencies:
                print("No words for word cloud")
                return None

            # Convert Counter to dictionary
            word_dict = dict(word_frequencies)

            # Create word cloud
            wordcloud = WordCloud(
                width=800,
                height=400,
                background_color="white",
                colormap="viridis",
                max_words=100,
                relative_scaling=0.5,
            ).generate_from_frequencies(word_dict)

            plt.figure(figsize=(12, 6))
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.title(title, fontsize=16, fontweight="bold")
            plt.axis("off")
            plt.tight_layout()
            return plt.gcf()

        except ImportError:
            print("WordCloud not available. Install with: pip install wordcloud")
            return None


# ==================== FILE OPERATIONS ====================


class FileManager:
    """Handle file operations for text analysis"""

    @staticmethod
    def save_generated_text(text, filename):
        """Save generated text to file"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Text saved to: {filename}")

    @staticmethod
    def load_text_file(filename):
        """Load text from file"""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"File not found: {filename}")
            return ""
        except Exception as e:
            print(f"Error reading file: {e}")
            return ""

    @staticmethod
    def save_analysis_results(results, filename):
        """Save analysis results to file"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write("TEXT ANALYSIS RESULTS\n")
            f.write("=" * 50 + "\n\n")

            f.write(f"Total Words: {results['total_words']}\n")
            f.write(f"Unique Words: {results['unique_words']}\n")
            f.write(f"Vocabulary Richness: {results['vocabulary_richness']:.4f}\n\n")

            f.write("TOP 20 MOST COMMON WORDS:\n")
            f.write("-" * 30 + "\n")
            for i, (word, freq) in enumerate(results["most_common"], 1):
                f.write(f"{i:2d}. {word:<15} {freq:>3d}\n")

            f.write(f"\nLONGEST WORDS:\n")
            f.write("-" * 30 + "\n")
            for word, freq in results["longest_words"]:
                f.write(f"{word:<20} (length: {len(word)}, freq: {freq})\n")

        print(f"Analysis results saved to: {filename}")


# ==================== MAIN DEMONSTRATION ====================


def demonstrate_text_analysis():
    """Main demonstration of text analysis features"""
    print("Assignment 3: Text Analysis with Word Frequencies")
    print("=" * 60)

    # Step 1: Generate 250-word text
    print("\n1. Generating 250-word text file...")
    generator = TextGenerator()
    generated_text = generator.generate_text(250)

    # Save generated text
    text_filename = "/Users/harshilpatel/CODE/Major/generated_text_250_words.txt"
    FileManager.save_generated_text(generated_text, text_filename)

    print(f"Generated text ({len(generated_text.split())} words):")
    print("-" * 40)
    print(generated_text[:200] + "..." if len(generated_text) > 200 else generated_text)
    print()

    # Step 2: Analyze the text
    print("2. Analyzing text and counting word frequencies...")
    analyzer = TextAnalyzer()
    results = analyzer.analyze_text(generated_text)

    # Display statistics
    print(f"\nTEXT STATISTICS:")
    print(f"Total words (after filtering): {results['total_words']}")
    print(f"Unique words: {results['unique_words']}")
    print(f"Vocabulary richness: {results['vocabulary_richness']:.4f}")

    # Step 3: Display top 20 words
    print(f"\nTOP 20 MOST COMMON WORDS (excluding stop words):")
    print("-" * 50)
    print(f"{'Rank':<5} {'Word':<15} {'Frequency':<10}")
    print("-" * 50)

    for i, (word, freq) in enumerate(results["most_common"], 1):
        print(f"{i:<5} {word:<15} {freq:<10}")

    # Step 4: Additional analysis
    print(f"\nLONGEST WORDS:")
    print("-" * 30)
    for word, freq in results["longest_words"][:10]:
        print(f"{word:<20} (length: {len(word)}, frequency: {freq})")

    # Step 5: Create visualizations
    print(f"\n3. Creating visualizations...")

    # Word frequency plot
    fig1 = TextVisualizer.plot_word_frequencies(
        results["most_common"], "Top 20 Most Common Words (Stop Words Excluded)"
    )
    plt.savefig(
        "/Users/harshilpatel/CODE/Major/assignment_03_word_frequencies.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    # Word length distribution
    fig2 = TextVisualizer.plot_word_length_distribution(
        results["word_length_distribution"]
    )
    plt.savefig(
        "/Users/harshilpatel/CODE/Major/assignment_03_word_lengths.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    # Try to create word cloud
    try:
        fig3 = TextVisualizer.create_word_cloud(
            analyzer.word_frequencies, "Word Cloud of Most Common Terms"
        )
        if fig3:
            plt.savefig(
                "/Users/harshilpatel/CODE/Major/assignment_03_wordcloud.png",
                dpi=300,
                bbox_inches="tight",
            )
            plt.show()
    except Exception as e:
        print(f"Word cloud creation failed: {e}")

    # Step 6: Save analysis results
    results_filename = "/Users/harshilpatel/CODE/Major/text_analysis_results.txt"
    FileManager.save_analysis_results(results, results_filename)

    return results


def demonstrate_large_file_analysis():
    """Demonstrate analysis on larger text"""
    print("\n4. Demonstrating analysis on larger text...")

    # Create a larger sample text by combining multiple texts
    generator = TextGenerator()
    large_text_parts = []

    # Generate multiple sections
    topics = [
        "artificial intelligence and machine learning applications",
        "computer science and software engineering principles",
        "data science and statistical analysis methods",
        "cybersecurity and information protection strategies",
        "cloud computing and distributed systems architecture",
    ]

    for topic in topics:
        section_text = generator.generate_text(100)  # 100 words per section
        large_text_parts.append(f"\n\nSection on {topic}:\n{section_text}")

    large_text = " ".join(large_text_parts)

    # Save large text
    large_filename = "/Users/harshilpatel/CODE/Major/large_text_sample.txt"
    FileManager.save_generated_text(large_text, large_filename)

    # Analyze large text
    analyzer = TextAnalyzer()
    large_results = analyzer.analyze_text(large_text)

    print(f"\nLARGE TEXT ANALYSIS:")
    print(f"Total words: {large_results['total_words']}")
    print(f"Unique words: {large_results['unique_words']}")
    print(f"Vocabulary richness: {large_results['vocabulary_richness']:.4f}")

    print(f"\nTOP 20 WORDS IN LARGE TEXT:")
    print("-" * 40)
    for i, (word, freq) in enumerate(large_results["most_common"], 1):
        print(f"{i:2d}. {word:<15} {freq:>3d}")

    return large_results


def test_custom_stop_words():
    """Test custom stop words functionality"""
    print("\n5. Testing custom stop words...")

    # Sample technical text
    tech_text = """
    The algorithm processes data structures efficiently. The data structure 
    implementation uses advanced algorithms for optimization. Machine learning 
    algorithms analyze data patterns in the dataset. The dataset contains 
    various data points for analysis.
    """

    print("Original analysis:")
    analyzer1 = TextAnalyzer()
    results1 = analyzer1.analyze_text(tech_text)
    print("Top words:", [word for word, freq in results1["most_common"][:10]])

    print("\nWith custom stop words (algorithm, data, analysis):")
    analyzer2 = TextAnalyzer(custom_stop_words=["algorithm", "data", "analysis"])
    results2 = analyzer2.analyze_text(tech_text)
    print("Top words:", [word for word, freq in results2["most_common"][:10]])


def main():
    """Main function to run all demonstrations"""
    # Main text analysis demonstration
    results = demonstrate_text_analysis()

    # Large file analysis
    large_results = demonstrate_large_file_analysis()

    # Custom stop words test
    test_custom_stop_words()

    # Summary
    print("\n" + "=" * 60)
    print("ASSIGNMENT 3 SUMMARY")
    print("=" * 60)
    print("\nFeatures Implemented:")
    print("✓ Text generation (250 words)")
    print("✓ Word frequency analysis")
    print("✓ Stop words filtering")
    print("✓ Top 20 most common words extraction")
    print("✓ Text preprocessing and cleaning")
    print("✓ Statistical analysis (vocabulary richness)")
    print("✓ Word length distribution analysis")
    print("✓ Visualization (bar charts, word cloud)")
    print("✓ File I/O operations")
    print("✓ Custom stop words support")
    print("✓ Large text file processing")

    print(f"\nGenerated Files:")
    print("• generated_text_250_words.txt")
    print("• large_text_sample.txt")
    print("• text_analysis_results.txt")
    print("• assignment_03_word_frequencies.png")
    print("• assignment_03_word_lengths.png")
    print("• assignment_03_wordcloud.png (if wordcloud available)")

    print(f"\nKey Results:")
    print(
        f"• Small text: {results['total_words']} words, {results['unique_words']} unique"
    )
    print(
        f"• Large text: {large_results['total_words']} words, {large_results['unique_words']} unique"
    )
    print(
        f"• Most common word: '{results['most_common'][0][0]}' ({results['most_common'][0][1]} times)"
    )


if __name__ == "__main__":
    main()
