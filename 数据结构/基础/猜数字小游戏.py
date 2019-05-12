import random

def main():
    smaller = int(input('Enter your smaller number: '))
    larger = int(input('Enter your larger number: '))
    myNumber = random.randint(smaller,larger)
    count = 0

    while True:
        count += 1
        userNumber = int(input('Enter your guess: '))
        if userNumber < myNumber:
            print('Too smaller')
        elif userNumber > myNumber:
            print('Too larger')
        else:
            print("You've got it in",count,"tries")
            break

if __name__ == '__main__':
    main()






