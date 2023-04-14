if __name__ == '__main__':

    list1 = [1, 3, 4, 5]

    list2 = [2, 6, 7, 8]

    result = (list1 + list2)
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]

    print(f'result:=> {result}')