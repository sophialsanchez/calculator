class Calculator(object):
    """A calculator that performs operations (multiply, divide, modulo, add, subtract)
       using the correct order of operations.
    """
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
        # throws a keyerror if operators not in the dictionary given as input
        for operator in operator_list:
            if operator not in self.operator_dictionary:
                raise KeyError("The operator %s is not current supported by the calculator." % operator)
        index = 0
        while index != len(equation):
            if equation[index] in operator_list:
                answer = self.operator_dictionary[(equation[index])](float(equation[index-1]), float(equation[index+1]))
                equation[index-1:index+2] = [str(answer)]
            else:
                index += 1
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

myCalculator = Calculator()



# print(myCalculator.multiply(2,3))
# print(myCalculator.divide(2,3))
# print(myCalculator.add(2,3))
# print(myCalculator.subtract(2,3))
# print(myCalculator.modulo(2,3))

print(myCalculator.evaluate("2 + -1 + 1 * 0 % 3 + 2 * 2 - 1")) # answer is 4
print(myCalculator.evaluate("2 * -23423432"))
print(myCalculator.evaluate("2 - -23423432"))
