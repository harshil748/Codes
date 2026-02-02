/*
 * Email Validation using POSIX Regular Expressions
 * Problem: Validate email addresses based on structural and syntactic rules
 * 
 * Email Structure:
 * - Local part (username): alphanumeric, dots, underscores, hyphens
 * - @ symbol (mandatory)
 * - Domain name: alphanumeric, dots, hyphens
 * - Domain extension: at least 2 characters
 */

#include <stdio.h>
#include <regex.h>
#include <string.h>

/**
 * Function: validate_email
 * Purpose: Validates email address using POSIX regex pattern matching
 * 
 * Email Pattern Breakdown:
 * ^                          - Start of string
 * [A-Za-z0-9._%+-]+          - Local part (username): one or more alphanumeric/special chars
 * @                          - Mandatory @ symbol
 * [A-Za-z0-9.-]+             - Domain name: one or more alphanumeric/dots/hyphens
 * \\.                        - Literal dot before extension
 * [A-Za-z]{2,}               - Top-level domain: at least 2 alphabetic characters
 * $                          - End of string
 */
int validate_email(const char *email) {
    regex_t regex;
    int result;
    
    // Regular expression pattern for email validation
    const char *pattern = "^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$";
    
    // Compile the regular expression
    if (regcomp(&regex, pattern, REG_EXTENDED | REG_NOSUB)) {
        fprintf(stderr, "Error: Failed to compile regex pattern\n");
        return -1;
    }
    
    // Execute the pattern matching
    result = regexec(&regex, email, 0, NULL, 0);
    
    // Free the compiled regex memory
    regfree(&regex);
    
    // Return 0 if valid, 1 if invalid
    return result;
}

/**
 * Function: print_validation_result
 * Purpose: Prints validation result in required format
 */
void print_validation_result(const char *email, int is_valid) {
    printf("%-30s : ", email);
    if (is_valid == 0) {
        printf("Valid Email\n");
    } else {
        printf("Invalid Email\n");
    }
}

/**
 * Main function: Demonstrates email validation with multiple test cases
 */
int main() {
    char email[256];
    int choice;
    
    printf("==========================================================\n");
    printf("       EMAIL VALIDATION USING POSIX REGEX ENGINE\n");
    printf("==========================================================\n\n");
    
    printf("Choose mode:\n");
    printf("1. Interactive Mode (Enter email manually)\n");
    printf("2. Test Mode (Run predefined test cases)\n");
    printf("Enter choice: ");
    scanf("%d", &choice);
    
    if (choice == 1) {
        // Interactive Mode
        printf("\nEnter email address (or 'quit' to exit): ");
        while (scanf("%255s", email) == 1 && strcmp(email, "quit") != 0) {
            int result = validate_email(email);
            print_validation_result(email, result);
            printf("\nEnter email address (or 'quit' to exit): ");
        }
    } else if (choice == 2) {
        // Test Mode - Predefined test cases
        printf("\n--- Running Test Cases ---\n\n");
        
        // Valid test cases
        printf("VALID TEST CASES:\n");
        print_validation_result("abc@gmail.com", validate_email("abc@gmail.com"));
        print_validation_result("student123@charusat.edu", validate_email("student123@charusat.edu"));
        print_validation_result("User.name-90@domain.co.in", validate_email("User.name-90@domain.co.in"));
        print_validation_result("test_user@example.org", validate_email("test_user@example.org"));
        print_validation_result("john.doe+tag@company.com", validate_email("john.doe+tag@company.com"));
        
        printf("\nINVALID TEST CASES:\n");
        print_validation_result("123@company.org", validate_email("123@company.org"));
        print_validation_result("abc@@gmail.com", validate_email("abc@@gmail.com"));
        print_validation_result("abc@.com", validate_email("abc@.com"));
        print_validation_result("abc@domain", validate_email("abc@domain"));
        print_validation_result("@domain.com", validate_email("@domain.com"));
        print_validation_result("user@", validate_email("user@"));
        print_validation_result("user name@domain.com", validate_email("user name@domain.com"));
        print_validation_result("user@domain..com", validate_email("user@domain..com"));
        
        printf("\nEDGE CASES:\n");
        print_validation_result("a@b.co", validate_email("a@b.co"));
        print_validation_result("test.email.with.multiple.dots@example.com", 
                              validate_email("test.email.with.multiple.dots@example.com"));
    } else {
        printf("Invalid choice!\n");
        return 1;
    }
    
    printf("\n==========================================================\n");
    printf("Program terminated successfully.\n");
    printf("==========================================================\n");
    
    return 0;
}
