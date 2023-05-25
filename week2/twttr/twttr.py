def main():
    # Input text from user
    word = input('Input: ')
    print(shorten(word))

def shorten(word):

  new = ''
  for c in word:
    # Create new word without vowels
    match c:
      case 'a' | 'A' | 'e' | 'E' | 'i' | 'I' | 'o' | 'O' | 'u' | 'U':
        new += ''
      case _:
        new += c
  return new

if __name__ == "__main__":
    main()