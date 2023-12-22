import libcst as cst

class ArithmeticCollector(cst.CSTVisitor):
    def __init__(self):
        super().__init__()
        self.stack = []

    def visit_Integer(self, node: cst.Integer):
        print(f"Visiting Integer: {node.value}")
        self.stack.append(int(node.value))

    def leave_BinaryOperation(self, node: cst.BinaryOperation):
        operator = node.operator.__class__.__name__
        print(f"Leaving BinaryOperation: {operator}")
        right_operand = self.stack.pop()
        left_operand = self.stack.pop()
        
        if operator == "Add":
            result = left_operand + right_operand
        elif operator == "Subtract":
            result = left_operand - right_operand
        elif operator == "Multiply":
            result = left_operand * right_operand
        elif operator == "Divide":
            result = left_operand / right_operand
        else:
            raise ValueError(f"Unsupported operator: {operator}")

        print(f"Result: {result}")
        self.stack.append(result)

if __name__ == "__main__":
    expression = "1 + 2 / 4 + 7 * 3"
    tree = cst.parse_expression(expression)
    
    visitor = ArithmeticCollector()
    tree.visit(visitor)
    
    print("Final Stack:", visitor.stack)
    print("Total Value:", visitor.stack[0])
