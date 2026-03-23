# Makefile for LR(0) Parser - Practical 7

CC = gcc
CFLAGS = -Wall -Wextra -g
TARGET = pr7
SOURCE = pr7.c

# Default target
all: $(TARGET)

# Compile the program
$(TARGET): $(SOURCE)
	@echo "Compiling LR(0) Parser..."
	$(CC) $(CFLAGS) $(SOURCE) -o $(TARGET)
	@echo "✓ Compilation successful!"
	@echo "Run with: ./$(TARGET)"

# Run the program
run: $(TARGET)
	@echo "Running LR(0) Parser..."
	./$(TARGET)

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -f $(TARGET) $(TARGET).exe
	@echo "✓ Clean complete!"

# Rebuild (clean + build)
rebuild: clean all

# Run with test inputs (automated testing)
test: $(TARGET)
	@echo "Running automated tests..."
	@echo "Test 1: aab$"
	@echo -e "1\naab$$\n2" | ./$(TARGET)
	@echo "\nTest 2: bb$"
	@echo -e "1\nbb$$\n2" | ./$(TARGET)

# Help target
help:
	@echo "LR(0) Parser Makefile"
	@echo "────────────────────────────────"
	@echo "Available targets:"
	@echo "  make          - Compile the program"
	@echo "  make run      - Compile and run"
	@echo "  make clean    - Remove build artifacts"
	@echo "  make rebuild  - Clean and rebuild"
	@echo "  make test     - Run automated tests"
	@echo "  make help     - Show this help message"

.PHONY: all run clean rebuild test help
