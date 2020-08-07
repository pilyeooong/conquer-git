def fizzbuzz(number):
    if number % 15 == 0:
        return 'Fizz Buzz'
    if number % 5 == 0:
        return 'Buzz'
    if number % 3 == 0:
        return 'Fizz'
    return str(number)

if __name__ == '__main__':
    assert fizzbuzz(15) == 'Fizz Buzz', '15 is divisible by 3 and 5'
    assert fizzbuzz(6) == 'Fizz', '6 is divisible by 3'
    assert fizzbuzz(5) == 'Buzz', '5 is divisible by 5'
    assert fizzbuzz(7) == '7', '7 is not divisible by 3 or 5'