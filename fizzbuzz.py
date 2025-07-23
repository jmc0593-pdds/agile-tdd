def fizz_buzz(numbers: list) -> list:
    i = 0
    new_list = []
    while len(numbers) > i:
        is_multiple_of_3 = numbers[i] % 3 == 0
        is_multiple_of_5 = numbers[i] % 5 == 0
        element_to_add = numbers[i]
        if numbers[i] == 0:
            is_multiple_of_3 = is_multiple_of_5 = False
        if is_multiple_of_3 and is_multiple_of_5:
            element_to_add = "FizzBuzz"
        elif is_multiple_of_3:
            element_to_add = "Fizz"
        elif is_multiple_of_5:
            element_to_add = "Buzz"
        new_list.append(element_to_add)
        i+=1
    return new_list

if __name__ == '__main__':
    test_list = list(range(31))
    fizz_buzz_list = fizz_buzz(test_list)                  
    print(fizz_buzz_list)