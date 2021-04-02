# def calculator(result):
#     return result


# operation=input("Select the operation=> addition,substraction,multiply,divide ")
# number1=int(input("Enter the 1st number"))
# number2=int(input("Enter the 2nd number"))
# result=0
# if operation == "addition" :
#     result = number1+number2
# elif operation == "substraction" :
#     result = number1-number2
# elif operation == "multiply" :
#     result == number1*number2
# elif operation == "divide" :
#     result = number1/number2
# else:
#     print("Invalid Output")


# calculator(result)
# print(result)



def calculator(number_x,number_y,operation):
    if operation== "add":
        add = number_x  + number_y
        return add
    elif operation == "subtract" :
        subtract = number_x - number_y
        return subtract
    elif operation == "multiply" :
        multiply = number_x * number_y
        return multiply
    elif operation == "divide":
        divide = number_x / number_y
        return divide
    


number_1 = calculator(20, 25, "add")
print("Additon is ",number_1)
number_2 = calculator(40, 3, "subtract")
print("Subtract is", number_2)
number_3 = calculator(10, 4, "multiply")
print("Multiply is", number_3)
number_4 = calculator(40, 4, "divide")
print("Divide is",number_4)



