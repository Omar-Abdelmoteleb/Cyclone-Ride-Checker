height = int(input("how tall are you: "))
credit = int(input("how much credit do you have: "))
if height >= 137 and  credit >= 10:
  print("enjoy the ride")
elif height < 137:
  print("You are not tall enough to ride.")
elif credit  < 10:
  print( "You don't have enough credits.")
else:
  print("You don't have enough credits.")