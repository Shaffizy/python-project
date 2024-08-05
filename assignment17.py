enter = ""
car_start = False
while enter != "quit":
    enter = input("> ").lower()
    if enter == "start":
        if car_start:
           print("Car already started")
        else:
            car_start = True
            print("Car started...")
    elif enter == "stop":
        if not car_start:
           print("Car already stopped...")
        else:
            car_start = False
            print("Car stopped...")
    elif enter == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit 
 """ )
    elif enter == "quit":
        break
    else:
        print("Sorry i don't understand")

