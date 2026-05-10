import ast

class QuadGen(ast.NodeVisitor):
    def __init__(self):
        self.quads = []
        self.temp = 0

    def new_temp(self):
        self.temp += 1
        return f"t{self.temp}"

    def visit_Assign(self, node):
        target = node.targets[0].id
        res = self.visit(node.value)
        self.quads.append(("=", res, "-", target))

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op = {ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/"}[type(node.op)]
        t = self.new_temp()
        self.quads.append((op, left, right, t))
        return t

    def visit_Name(self, node):
        return node.id

    def visit_Constant(self, node):
        return str(node.value)


def gen_quads(expr):
    tree = ast.parse(expr, mode="exec")
    g = QuadGen()
    for node in tree.body:
        g.visit(node)
    return g.quads


# Example
print("('op', 'arg1', 'arg2', 'result')")
for q in gen_quads("x = (a + b) * (c - d) + e * f / g"):
    print(q)
