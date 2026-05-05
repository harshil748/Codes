import re

class QuadrupleGenerator:
    def __init__(self):
        self.quads = []
        self.temp_count = 0

    def new_temp(self):# temp variable gen
        self.temp_count += 1
        return f"t{self.temp_count}"

    def add_quad(self, op, arg1, arg2, result):
        self.quads.append((op, arg1, arg2, result))

    def tokenize(self, expr):
        tokens = re.findall(r"\w+|[+\-*/()=]", expr)
        return tokens

    def precedence(self, op):
        if op in ["+", "-"]:
            return 1
        if op in ["*", "/"]:
            return 2
        return 0

    def infix_to_postfix(self, tokens):
        output = []
        op_stack = []

        for token in tokens:
            if token.isalnum() or token[0].isalpha() or token.isdigit():  # operand
                output.append(token)
            elif token == "(":
                op_stack.append(token)
            elif token == ")":
                while op_stack and op_stack[-1] != "(":
                    output.append(op_stack.pop())
                if op_stack:
                    op_stack.pop()  # Remove '('
            elif token in ["+", "-", "*", "/"]:
                while (
                    op_stack
                    and op_stack[-1] != "("
                    and self.precedence(op_stack[-1]) >= self.precedence(token)
                ):
                    output.append(op_stack.pop())
                op_stack.append(token)

        while op_stack:
            output.append(op_stack.pop())

        return output

    def generate_quads(self, postfix):
        stack = []

        for token in postfix:
            if token.isalnum() or token[0].isalpha() or token.isdigit():  
                stack.append(token)
            elif token in ["+", "-", "*", "/"]:
                if len(stack) < 2:
                    print("Error: Invalid expression")
                    return False

                arg2 = stack.pop()
                arg1 = stack.pop()
                result = self.new_temp()

                self.add_quad(token, arg1, arg2, result)
                stack.append(result)

        return stack[0] if stack else None

    def process_assignment(self, expression):
        parts = expression.split("=")
        if len(parts) != 2:
            print("Error: Must be assignment (lhs = rhs)")
            return False

        lhs = parts[0].strip()
        rhs = parts[1].strip()

        tokens = self.tokenize(rhs)

        postfix = self.infix_to_postfix(tokens)

        expr_result = self.generate_quads(postfix)

        if expr_result is None:
            print("Failed to generate quadruples")
            return False

        self.add_quad("=", expr_result, "-", lhs)

        return True

    def display(self):
        print("\nQuadruples:")
        print(f"{'Op':<6} | {'Arg1':<12} | {'Arg2':<12} | {'Result':<12}")

        for op, arg1, arg2, result in self.quads:
            print(f"{op:<6} | {arg1:<12} | {arg2:<12} | {result:<12}")



def main():
    print("\nEnter expression:")
    expr = input("Input: ").strip()

    if not expr:
        print("No input provided.")
        return

    gen = QuadrupleGenerator()
    if gen.process_assignment(expr):
        gen.display()
    else:
        print("Error processing expression")


if __name__ == "__main__":
    main()
