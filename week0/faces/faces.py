def main():
  str = input()
  newstr = convert(str)
  print(newstr)

def convert(str):
  str = str.replace(':)','🙂')
  str = str.replace(':(','🙁')
  return str

main()