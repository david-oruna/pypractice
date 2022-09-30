def imc():
    a = input("Enter your name: ")
    b = float(input("Enter your weight in kg: "))
    c = float(input("Enter your height in meters: "))
    imc = b/(c**2)
    print("Hi," + a)
    if imc < 18:
        print("You are underweight")
    elif imc < 25:
        print("You are ok")
    else:
        print("You are fat wtf")

x = imc()

# RANOM IMC CALCULATOR HAHA
