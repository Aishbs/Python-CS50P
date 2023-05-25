def main():
  # machine sells bottles of Coca-Cola (Coke) for 50 cents
  amt = 50;

  while amt > 0:
    print('Amount Due:', amt)
    amt = coke_machine(amt)

  print('Change Owed:', abs(amt))

def coke_machine(amt):

  coin = int(input('Insert coin: '))

  # only accepts coins: 25 cents, 10 cents, and 5 cents
  if coin == 25 or coin == 10 or coin == 5:
    amt = amt - coin

  return amt



main()