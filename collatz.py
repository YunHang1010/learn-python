print('Enter number:')

try:
    number = int(input())
except ValueError:
    print('Please enter a valid INTER')
    # modify: continue instead of break

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = (number // 2)
            print(int(number))
        elif number % 2 == 1:
            number = (3 * number + 1)
            print(int(number))
        continue
        
collatz(number)