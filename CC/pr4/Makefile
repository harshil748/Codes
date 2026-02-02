# Makefile for Expression & Conditional Parser

# Compiler and tools
CC = gcc
LEX = flex
YACC = bison
CFLAGS = -Wall -Wno-unused-function
LDFLAGS = -lfl

# File names
LEXER = lexer.l
PARSER = parser.y
TARGET = parser
LEX_OUT = lex.yy.c
YACC_OUT = parser.tab.c
YACC_HDR = parser.tab.h

# Test files
TEST_VALID = test.txt
TEST_INVALID = test_invalid.txt
TEST_EXTENDED = test_extended.txt

# Default target
all: $(TARGET)

# Generate lexer
$(LEX_OUT): $(LEXER)
	$(LEX) $(LEXER)

# Generate parser
$(YACC_OUT) $(YACC_HDR): $(PARSER)
	$(YACC) -d $(PARSER)

# Compile parser
$(TARGET): $(LEX_OUT) $(YACC_OUT)
	$(CC) $(CFLAGS) $(LEX_OUT) $(YACC_OUT) -o $(TARGET) || \
	$(CC) $(CFLAGS) $(LEX_OUT) $(YACC_OUT) -o $(TARGET) $(LDFLAGS)

# Run with default test file
run: $(TARGET)
	@echo "========================================="
	@echo "Running parser with valid test cases..."
	@echo "========================================="
	./$(TARGET) $(TEST_VALID)

# Test with valid cases
test-valid: $(TARGET)
	@echo "========================================="
	@echo "Testing with VALID cases..."
	@echo "========================================="
	./$(TARGET) $(TEST_VALID)

# Test with invalid cases
test-invalid: $(TARGET)
	@echo "========================================="
	@echo "Testing with INVALID cases..."
	@echo "========================================="
	./$(TARGET) $(TEST_INVALID) || true

# Test with extended features
test-extended: $(TARGET)
	@echo "========================================="
	@echo "Testing with EXTENDED features..."
	@echo "========================================="
	./$(TARGET) $(TEST_EXTENDED)

# Interactive mode
interactive: $(TARGET)
	@echo "========================================="
	@echo "Interactive mode (Ctrl+D to finish)..."
	@echo "========================================="
	./$(TARGET)

# Clean build artifacts
clean:
	rm -f $(TARGET) $(LEX_OUT) $(YACC_OUT) $(YACC_HDR)
	rm -f parser.output y.output
	@echo "Cleaned all build artifacts"

# Verbose yacc output (for debugging conflicts)
verbose: clean
	$(YACC) -d -v $(PARSER)
	@echo "Created parser.output with detailed information"
	@echo "Check for shift-reduce or reduce-reduce conflicts"

# Full rebuild
rebuild: clean all

# Show parser statistics
stats: $(TARGET)
	@echo "Parser Statistics:"
	@wc -l $(LEXER) $(PARSER)
	@echo "\nTokens defined:"
	@grep "^%token" $(PARSER) || true
	@echo "\nGrammar rules:"
	@grep -E "^[a-z_]+:" $(PARSER) | wc -l

# Help message
help:
	@echo "Available targets:"
	@echo "  all           - Build the parser (default)"
	@echo "  run           - Run with default test file"
	@echo "  test-valid    - Test with valid cases"
	@echo "  test-invalid  - Test with invalid cases"
	@echo "  test-extended - Test with extended features"
	@echo "  interactive   - Run in interactive mode"
	@echo "  clean         - Remove build artifacts"
	@echo "  rebuild       - Clean and rebuild"
	@echo "  verbose       - Generate verbose parser output"
	@echo "  stats         - Show parser statistics"
	@echo "  help          - Show this help message"

# Phony targets
.PHONY: all run test-valid test-invalid test-extended interactive clean rebuild verbose stats help
