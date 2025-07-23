def fizz_buzz(numbers: list) -> None:
    i = 0
    while len(numbers) > i:
        is_multiple_of_3 = numbers[i] % 3 == 0
        is_multiple_of_5 = numbers[i] % 5 == 0
        if numbers[i] == 0:
            pass
        elif is_multiple_of_3 and is_multiple_of_5:
            numbers[i] = "FizzBuzz"
        elif is_multiple_of_3:
            numbers[i] = "Fizz"
        elif is_multiple_of_5:
            numbers[i] = "Buzz"
        i+=1

if __name__ == '__main__':
    test_list = list(range(30))
    fizz_buzz(test_list)
    print(test_list)


