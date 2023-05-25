import inflect

p = inflect.engine()

# Create an empty list
names = []

while True:
   try:
      #input from user
      names.append(input('Name: '))

   except EOFError:
      print("Adieu, adieu, to ", end ='')
      break

#Print all names if list in not empty
print(p.join(names))