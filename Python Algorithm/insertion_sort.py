import create_random_number_list
import random


def insertion_sort(input_list):
    list_length = len(input_list)
    for i in range(1, list_length):
        for j in range(i, -1, -1):
            if input_list[j] < input_list[j - 1]:
                # do the insert job by swapping the element inside the list
                input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]
            else:
                break
    return input_list


def main():
    random_number_list = create_random_number_list.main()

    # # setup a random list from 0 to 10
    # random_number_list = list(range(10))
    # random.shuffle(random_number_list)
    print(random_number_list)
    result = insertion_sort(random_number_list)
    print(result)


if __name__ == '__main__':
    main()
