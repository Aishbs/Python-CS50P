def main():
    while True:
      # Prompt user for fraction
      fraction = input('Fraction: ')
      percentage = convert(fraction)
      if percentage < 100.0:
          print(gauge(percentage))
          break
      else:
          continue

def convert(fraction):
    #spliting the fraction
    x, y = fraction.split('/')

    try:
      # Convert fraction to percent
      percentage = int(x) * 100 / int(y)
      return int(percentage)
    # Handles error
    except (ValueError, ZeroDivisionError):
      raise
      

def gauge(percentage):
    # Check fuel tank
    if percentage <= 1.0:
      return 'E'
    elif percentage >= 99.0:
      return 'F'
    else:
      return f'{int(round(percentage))}%'

if __name__ == "__main__":
    main()