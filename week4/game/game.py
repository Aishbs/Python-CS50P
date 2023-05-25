import random

while True:

  #Input level from user
  try:
    level = int(input('Level: '))
    #Generate a number
    num = random.randint(1,100)

    # Check if level is positive integer or not
    if level < 1:
      continue

    else:

      while True:

        try:
          # Input guess from user
          guess = int(input('Guess: '))

          #Compare guess with generated number
          if guess < num:
            print('Too small!')
          elif guess > num:
            print('Too large!')
          elif guess == num:
            print('Just right!')
            break
          else:
            continue

        except:
          pass

    break

  except:
    pass
