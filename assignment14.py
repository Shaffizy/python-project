enter = ""
started = False

while True:
    enter = input("> ").lower()

    if enter == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started ... Ready to go!")

    elif enter == "stop":
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car stopped.")

    elif enter == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif enter == "quit":
        break
else:
    print("I dont understand that...")
