# 01 - Error Handling

from os import path

file_name = 'temp.txt'

if path.exists(file_name):
    with open(file_name) as file:
        print(file.readlines())

else:
    print('File does not exist')


'''Certainly! The code you provided demonstrates a basic error handling technique using the os.path.exists() 
function to check if a file exists before attempting to open and read its contents. Here's an explanation of the error 
handling process in the code:
The os.path.exists(file_name) function is used to check if the file with the name temp.txt exists in the current directory.
If the file exists, the code proceeds to open the file using the open() function with the mode 'r' (read mode) as the 
default mode. The file is opened within a with statement, which ensures that the file is properly closed after it is used.

Inside the with statement, the file.readlines() method is called to read all the lines in the file and return them as a list.
The obtained list of lines is then printed using the print() function.
If the file does not exist, the code executes the else block and prints the message 'File does not exist'.
By checking if the file exists before attempting to open it, the code avoids raising an exception when trying to access 
a non-existent file. This approach helps prevent crashes or unexpected behavior in your program.

This code snippet demonstrates a simple form of error handling using conditional statements to handle different scenarios 
based on whether the file exists or not.'''


# 02. Error Handling

x = 10
y = 0

try:
    z = x/y
    print(z)

except:
    print('Error')


''' Certainly! The code you provided demonstrates a basic error handling technique using a try-except block. Here's an 
explanation of the error handling process in the code:

1.	Inside the try block, the code attempts to perform a division operation x/y and assigns the result to the variable z. 
    This is the potentially error-prone part of the code where an exception might be raised if y is zero or if x or y are not 
    valid operands for division.

2.	If no exception occurs during the execution of the try block, the code proceeds to the next line, print(z), and prints 
    the value of z.

3.	If an exception occurs during the execution of the try block, the code jumps to the corresponding except block.

4.	In this case, the except block has a generic except statement without specifying any specific exception type.
    This means it will catch any exception that occurs within the try block.

5.	Inside the except block, the code executes the print('Error') statement, which simply prints the message 'Error'.

By using a try-except block, you can handle potential exceptions that may occur during the execution of the code. 
If an exception occurs in the try block, the execution is transferred to the except block, allowing you to gracefully 
handle the error and take appropriate action.However, it is generally recommended to specify the specific exception types 
that you want to handle in the except block rather than using a generic except statement. This allows for more precise error 
handling and prevents unintentionally catching and suppressing unrelated exceptions.
'''

# 03. Error Handling

try:
    z = 10
    y = 1
    z = z/y
    print(z)

    # can get file not found error
    with open(file_name) as file:
        print(file.readlines())

except ZeroDivisionError as e:
    print('Cannot divide by zero', e)

except FileNotFoundError as e:
    print('File does not exist', e)
except Exception as e:
    print('Something went wrong', e)


# 04. Error Handling

try:
    z = 10
    y = 1
    z = z/y
    print(z)

    # can get file not found error
    with open(file_name) as file:
        print(file.readlines())

except ZeroDivisionError as e:
    print('Cannot divide by zero', e)

except FileNotFoundError as e:
    print('File does not exist', e)
except Exception as e:
    print('Something went wrong', e)

finally:
    # Use for closing files, database connections, etc.
    print("Process completed.")
