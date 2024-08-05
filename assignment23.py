numbers = input("phone no:")
log ={
    "1":"0ne",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five"
}
output = ""
for number in numbers:
    output += log.get(number,"!") + " "
print(output)