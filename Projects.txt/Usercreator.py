aleria i don't know why you want this code, it's so basic ._.

class ACC:

    def __init__(self, first, last, number):
        self.first = first
        self.last = last
        self.number = number
        self.email = f"{first}.{last}@company.com"

    def full(self):
        return f"{self.first} {self.last}"


home = "Hi, this is the user create bot ^^ \n"
# Here i just made a basic writing effect nvm
for i in home:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.1)

while True:
    a = input("Please enter your name: ")

    if not a.isalpha():
        print("Only letters are allowed!")
        continue
    elif len(a) < 3:
        print("Name is too short. Please try again.")

    else:
        break


while True:
    b = input("Enter your last name: ")

    if not b.isalpha():
        print("Only letters are allowed!")
        continue
    elif len(b) < 3:
        print("Name is too short. Please try again.")
    else:
        break

while True:
    try:
        c = int(input("Enter your number: "))

    except ValueError:
        print("Enter a correct number")
        continue
    if len(str(c)) < 6:
        print("Number is too short")
        continue
    else:
        break

Code = "Now we will send a verification code to your number. \n\
...\nwait\n"
for char in Code:
    sys.stdout.write(char)
    sys.stdout.flush()
    if char != "\n":
        time.sleep(0.1)
    else:
        time.sleep(1)

while True:
    try:
        d = int(input("Enter the verification code: "))
    except ValueError:
        print("Invalid code, try again")
        continue
    if len(str(d)) < 6:
        print("Number is too short")
    else:
        break

user = ACC(a, b, c)
z = f"Ok, now we are processing your data \n\
    Congratulations! Your user has been created successfully :D \n\
    Here are your new credentials: \n\
    Your fullname is {user.full()} \n\
    Your new brand email is {user.email}"

for x in z:
    sys.stdout.write(x)
    sys.stdout.flush()
    if x != "\n":
        time.sleep(0.1)
    else:
        time.sleep(1)

# That was it, i think it's pretty easy to understand

# print(f"Your fullname is {user.full()}")
# print(f"Your fullname is {user.email}")
