grocery = {}

while True:

    try:
      # Fetch input from user
      i = input()

      #Check if item is already present in dict
      if i in grocery:
        grocery[i] += 1
      else:
        grocery[i] = 1

    # On clicking Ctrl + D :
    except EOFError:
      for key in sorted(grocery.keys()):
        print(grocery[key], key.upper())
      break