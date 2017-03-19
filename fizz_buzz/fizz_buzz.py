def fizz_buzz(number):
    """ 
    Check whether a number is divisible by either 3 or 5 or both
    """
    
    if number % 3 == 0 and number % 5 == 0:
        number ='FizzBuzz'
    elif number % 3 == 0:
        number = 'Fizz'
    elif number % 5 == 0:
        number = 'Buzz'
    return (number)