#Perform desired operation based on operand
def opr(x, y, z):
    match y:
      case '+':
        res = float(int(x) + int(z))
      case '-':
        res = float(int(x) - int(z))
      case '*':
        res = float(int(x) * int(z))
      case '/':
        res = float(int(x) / int(z))
      case _:
        res = 0.0
    return(res)

# Fetch an expression from user
expression = input("Expression: ")
# Split expression in operands and operator
x, y, z = expression.split(" ")
# Display output
print(opr(x, y, z))
