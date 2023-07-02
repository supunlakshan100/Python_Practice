# Conditions

'''marks = float(input("Enter Your Marks:"))

if marks <= 0 and marks >= 100:
    print("INVALIED")

if marks <= 50 and marks >= 0:
    print("W")
elif marks <= 75:
    print("C")
elif marks <= 100:
    print("A")'''


'''marks = float(input("Enter Your Marks:"))
if marks <= 50 and marks >= 0:
    print("W")
elif marks > 50 and marks <= 75:
    print("C")
elif marks > 75 and marks <= 100:
    print("A")
else:
    print("INVALIED")'''


# Ternary operater
height = 180
msg = "Your Job Is" + (" Security" if height > 150 else " larber")
print(msg)
