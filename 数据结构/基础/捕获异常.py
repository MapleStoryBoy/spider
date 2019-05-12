'''
语法：
try:
    <statements>
except <exception type>:
    <statement>
'''
#  示列
def safeIntegerInput(prompt):
    inputString = input(prompt)
    try:
        number = int(inputString)
        return number
    except ValueError:
        print('Enter in number format:',inputString)
        return safeIntegerInput(prompt)

if __name__ == '__main__':
    age = safeIntegerInput("Enter your age: ")
    print('You age is ',age)