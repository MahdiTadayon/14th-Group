
# multiples of 3 --> Hop
# multiples of 7 --> Wiz
# multiples of 3 and 7 --> HopWiz

# solution 1 
for number  in range(1, 100):print("HopViz") if not number % 21  else print("Hop") if not number % 3  else print("Viz") if not number % 7  else print(number)
# solution 2 ---> pythonic 
for number  in range(1, 100):print("HopViz") if number in range(0, 100, 21) else print("Hop") if number in range(0, 100, 3) else print("Viz") if number in range(0, 100, 7) else print(number)

