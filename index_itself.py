def element_of_product(number):
    new_arr = []
    for i in range(len(number)):
        product = 1
        for j in range(len(number)):
            if number[i] != number[j]:
                product *= number[j]
        new_arr.append(product)

    return new_arr


if __name__ == '__main__':
    arr = [4, 2, 1, 5, 0]
    result = element_of_product(arr)
    print(result)
