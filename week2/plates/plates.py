def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
  l = len(s)
  #Check for length
  if l <2 or l > 6:
    return False
  elif '0' in s[0: (l-1)]:
    return False
  #Check for alphanumeric
  elif not(s.isalnum()):
    return False
  elif s[0].isalpha == False or s[1].isalpha == False:
    return False
  elif s[0] == 0 or s[-2:l].isdigit or s[0] == 0:
     return False

  for c in s:
     #Check for punctuation
     if c == '.' or c == ',' or c == '!' or c == '?':
        return False

  i = 0
  while i < len(s):
     #Check for position of zero
     if s[i].isalpha() == False:
        if s[i] == '0':
            return False
        else:
            break
     i += 1
  # On passing all tests
  return True

if __name__ == "__main__":
    main()