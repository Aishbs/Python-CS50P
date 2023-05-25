import random


def main():
    #Calls get_level() function
    level = get_level()
    score = 0

    # Generates 10 math problems
    for i in range(10):
      #Calls generate_integer() function
      num1, num2 = generate_integer(level)
      value = num1 + num2
      res = prompt_user(value, num1, num2)
      score += res

    print('Score:', score)

def get_level():
    #Input level from user
    while True:
        try:
          l = int(input('Level: '))
          # Check if level is 1, 2 or 3
          if l == 1 or l == 2 or l == 3:
              # Returns level
              return l
        except:
            #Re-prompt the user for level input
            pass

def generate_integer(level):
    # Throws error is level is not 1, 2 or 3
    if level < 0 or level > 3:
        raise ValueError
    # If level is 1
    elif level == 1:
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
    # If level is 1
    elif level == 2:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
    # If level is 1
    else:
        num1 = random.randint(100,999)
        num2 = random.randint(100,999)

    return num1, num2

def prompt_user(val, x, y):

    tries = 0
    while tries < 3:
        #Ask user for answer
        ans = int(input(f'{x} + {y} = '))
        score = 0

        try:
            # Compares input with actual value
            # print('wrong')
            if ans == val:
                score = 1
                break
            elif ans != val:
                # Display error message
                print('EEE')
                #Display actual result after 3 tries
                if tries == 2:
                    print(f'{x} + {y} = ', val)
        except:
            #Re-prompts for answer
            pass
        # Increment tries
        tries += 1
    return score

if __name__ == "__main__":
    main()