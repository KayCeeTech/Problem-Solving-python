def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique


if __name__ == '__main__':
    numbers = [9, 2, 3, 2, 6, 6]
    print(get_unique_numbers(numbers))
