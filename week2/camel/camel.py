# Input from user
case = input('camelCase:')
s = ''

for c in case:
  if(c.isupper()):
    s = s + '_' + c.lower()
  else:
    s = s + c

print('snake_case:' + s)