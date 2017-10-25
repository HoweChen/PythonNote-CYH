import create_random_number_list

random_number_list = create_random_number_list.main()


def selection_sort(random_number_list):
    min_number = random_number_list[0]
    result = []
    while len(random_number_list) != 0:
        min_number_index = 0
        for i in range(len(random_number_list)):
            if random_number_list[i] < min_number:
                min_number = random_number_list[i]
                min_number_index = i
        result.append(random_number_list.pop(min_number_index))

    return result


def main():
    result = selection_sort(random_number_list)
    print(result)


if __name__ == '__main__':
    main()
