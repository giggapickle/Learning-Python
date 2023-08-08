import math

def quadformula():
    type = input("Do you want to find the Quadratic Formula Answer (QF), or the discriminant (DS): ").upper()
    num1 = 0
    num2 = 0
    num3 = 0
    if type == "DS": 
        num1 = float(input("a: "))
        num2 = float(input("b: "))
        num3 = float(input("c: "))
        answer = num2*num2-(4*num1*num3)
    if type == "QF":
        num1 = float(input("a: "))
        num2 = float(input("b: "))
        num3 = float(input("c: "))
        answer = "Not Finished"
    print(answer)

def repete():
    if_repete = input("Start Program? Y/N")
    if if_repete == "Y":
        quadformula()
    elif if_repete == "N":
        print("Ending")
        exit
    else:
        print("Not Valid Response")
        repete()
repete()
