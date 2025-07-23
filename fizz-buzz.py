def is_multiple_of_3(number: int) -> bool:
    return number % 3 == 0

def is_multiple_of_5(number: int) -> bool:
    return number % 5 == 0

def fizz_buzz(numbers: list) -> None:
    i = 0
    while len(numbers) > i:
        if numbers[i] == 0:
            pass
        elif is_multiple_of_3(numbers[i]) and is_multiple_of_5(numbers[i]):
            numbers[i] = "FizzBuzz"
        elif is_multiple_of_3(numbers[i]):
            numbers[i] = "Fizz"
        elif is_multiple_of_5(numbers[i]):
            numbers[i] = "Buzz"
        i+=1

if __name__ == '__main__':
    test_list = list(range(30))
    fizz_buzz(test_list)
    print(test_list)


