import sys, time, os

message = "Computer: Hello, i'm a David's python program \(^-^)/.\n\
And now i'm going to identify some numbers,\n\
that you will enter and tell if it's less or greater than another. \n\
"

def typewriter(message):
    for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()

            if char != "\n":
                time.sleep(0.1)
            else:
                time.sleep(1)


os.system("cls")

typewriter(message)


a = int(input("First enter a number please( ͡° ͜ʖ ͡°): "))

b = int(input("Now enter another number ༼ つ ◕_◕ ༽つ: "))

c = int(input("Finally enter another number (ﾉ◕ヮ◕)ﾉ: "))




message2 = "Well, after some thought i have come \n\
to the conclusion that: "
for char in message2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

if a < b and b < c:
    print("Your first number " + str(a) + " is less than your second number " + str(b) + "and less than \n\
your third number" + str(c))
if a < b and b > c:
    print("Your first number " + str(a) + " is less than your second number " + str(b) + "but no less than \n\
your third number" + str(c))
if a > b and b < c:
    print("Your first number " + str(a) + " is greater than your second number " + str(b) + "and less than \n\
your third number" + str(c))
else:
    print("Your first number " + str(a) + " is greater than your second number " + str(b) + "and greater than \n\
             your third number" + str(c))

message3 = "Thank you for your time:3"
for char in message3:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
