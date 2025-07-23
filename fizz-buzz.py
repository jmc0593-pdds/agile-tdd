def fizz_buzz(numbers: list) -> None:
    i = 0
    while len(numbers) > i:
        if numbers[i] == 0:
            pass
        elif numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
            numbers[i] = "FizzBuzz"
        elif numbers[i] % 3 == 0:
            numbers[i] = "Fizz"
        elif numbers[i] % 5 == 0:
            numbers[i] = "Buzz"
        i+=1

if __name__ == '__main__':
    test_list = list(range(30))
    fizz_buzz(test_list)
    print(test_list)


