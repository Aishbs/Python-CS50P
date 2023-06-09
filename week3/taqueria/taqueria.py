menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():

  bill = 0.0
  while True:
    # Fetch order from user
    try:
      item = input('Item: ').title()

      #check if item is present in menu
      if item in menu:
        bill += menu[item]
      else:
        continue
      print('Total: $',end = '')
      print('{:.2f}'.format(bill))
    except EOFError:
      print()
      break

main()