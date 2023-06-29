print("*"*10)
print("Hi,I hate with \"ING\" ")
test = str(input("Enter your word :"))
if test.endswith("ing"):
    print(test[:-3])
else:
    print(test)
