## Find the prime number
def find_prime_number(number):
    if number == 1:
        print('This is not prime number')
    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print('This in not prime number')
                break

        else:
                print('This in prime number')

## how many prime number in your number

def prime_number_number_limit(start, end):
    list_of_prime_number = []
    if start > end:
        print('Enter the correct number')
    if start <= end:
        for i in range(start,end + 1):
            if 

