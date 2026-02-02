# Makefile for Email Validator and Lexer

CC = gcc
CFLAGS = -Wall -Wextra -std=c11
FLEX = flex

# Targets
all: email_validator lexer

# Email validator compilation
email_validator: email_validator.c
	$(CC) $(CFLAGS) email_validator.c -o email_validator
	@echo "Email validator compiled successfully!"

# Lexer compilation
lexer: lex.yy.c main.c
	$(CC) $(CFLAGS) lex.yy.c main.c -o lexer
	@echo "Lexer compiled successfully!"

lex.yy.c: lexer.l
	$(FLEX) lexer.l

# Run email validator
run-email: email_validator
	./email_validator

# Run lexer with test file
run-lexer: lexer
	./lexer < test.c

# Clean build artifacts
clean:
	rm -f email_validator lexer lex.yy.c
	@echo "Cleaned build artifacts!"

# Clean and rebuild
rebuild: clean all

# Help
help:
	@echo "Available targets:"
	@echo "  all          - Build both email validator and lexer"
	@echo "  email_validator - Build email validator only"
	@echo "  lexer        - Build lexer only"
	@echo "  run-email    - Run email validator"
	@echo "  run-lexer    - Run lexer with test.c"
	@echo "  clean        - Remove build artifacts"
	@echo "  rebuild      - Clean and rebuild all"
	@echo "  help         - Show this help message"

.PHONY: all clean rebuild run-email run-lexer help
