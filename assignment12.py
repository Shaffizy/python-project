weight = input("what is your weight: ")
conversion = input("(L)Ibs or (K)kg: ")
if conversion.upper() == "K":
    solve = float(weight)/0.45
    print(solve)
elif conversion.upper() == "L":
    solve = float(weight)*0.45
    print(solve)
else:
    print("invalid input")

