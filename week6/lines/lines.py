import sys

def main():

    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if '.py' not in sys.argv[1]:
        sys.exit('Not a Python file')

    print(check_code(sys.argv[1]))

def check_code(code):
    num = 0
    try:
        file = open(code)
    except FileNotFoundError:
        sys.exit('File does not exist')

    lines = file.readlines()
    for line in lines:
        if line.lstrip().startswith('#') or line.isspace():
            num += 0
        else:
            num += 1
    return num

main()