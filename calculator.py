class Calculator(object):
    """A calculator that performs operations (multiply, divide, modulo, add, subtract)
       using the correct order of operations."""
    def __init__(self):
        self.operator_dictionary = {
        '*': self.multiply,
        '/': self.divide,
        '+': self.add,
        '-': self.subtract,
        '%': self.modulo
        }

    def evaluate(self, equation):
        """Evalutes an equation using the correct order of operations
           and returns the answer as a float."""
        equation = self.process_operations(equation.split(' '), ['*', '/', '%']) # process multiplication, division, and modulo first
        equation = self.process_operations(equation, ['+', '-']) # then process addition and subtraction
        return(float(equation[0])) # return final answer as a float, not a string

    def process_operations(self, equation, operator_list):
        """Takes as arguments an equation as a string and a list of operations
           and returns the equation with only those operations performed."""
        # throws a descriptive keyerror if operator is not in the dictionary
        for operator in operator_list:
            if operator not in self.operator_dictionary:
                raise KeyError("The operator %s is not currently supported by the calculator." % operator)
        index = 1
        while index != len(equation):
            if equation[index] in operator_list:
                answer = self.operator_dictionary[(equation[index])](float(equation[index-1]), float(equation[index+1]))
                equation[index-1:index+2] = [str(answer)]
            else:
                index += 2
        return(equation)
    
    def multiply(self, num1, num2):
        """Takes as arguments two numbers and returns the product."""
        return(num1 * num2)
    
    def divide(self, num1, num2):
        """Takes as arguments two numbers and returns the quotient."""
        return(num1 / num2)
    
    def add(self, num1, num2):
        """Takes as arguments two numbers and returns the sum."""
        return(num1 + num2)
    
    def subtract(self, num1, num2):
        """Takes as arguments two numbers and returns the difference."""
        return(num1 - num2)
    
    def modulo(self, num1, num2):
        """Takes as arguments two numbers and returns the modulo."""
        return(num1 % num2)
