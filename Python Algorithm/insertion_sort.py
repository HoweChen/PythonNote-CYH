import create_random_number_list
import random


def binary_search(target_list, target_number, left, right):
    if right - left == 1:
        if target_list[left] < target_number < target_list[right]:
            return right  # target number is within the scale
        else:
            return left  # the target number is smaller then the
    elif left == right:
        return left
    else:
        mid = int((left + right) / 2)
        if target_list[mid] < target_number:
            return binary_search(target_list, target_number, mid, right)
        elif target_number < target_list[mid]:
            return binary_search(target_list, target_number, left, mid)


def binary_search_insertion_sort(input_list):
    # if input_list[1] < input_list[0]:
    #     input_list[1], input_list[0] = input_list[0], input_list[1]
    list_length = len(input_list)
    for i in range(1, list_length):
        # when current number is smaller, do the binary_search to find the best location to insert
        if input_list[i] < input_list[i - 1]:
            index = binary_search(input_list, input_list[i], 0, i - 1)
            for j in range(i, index, -1):
                input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]
        else:
            continue
    return input_list


def insertion_sort(input_list):
    list_length = len(input_list)
    for i in range(1, list_length):
        for j in range(i, 0, -1):
            if input_list[j] < input_list[j - 1]:
                # do the insert job by swapping the element inside the list
                input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]
            else:

                break
    return input_list


def main():
    random_number_list = create_random_number_list.main()

    # setup a random list from 0 to 10
    # random_number_list = list(range(10))
    # random.shuffle(random_number_list)

    random_number_list_copy = random_number_list.copy()
    # print(random_number_list)

    # insertion_sort
    # random_number_list = [6, 2, 8, 4, 1, 3, 0, 5, 7, 9]
    print(insertion_sort(random_number_list))

    # binary_search_insertion_sort
    # random_number_list_copy = [6, 2, 8, 4, 1, 3, 0, 5, 7, 9]
    # print(random_number_list_copy)
    print(binary_search_insertion_sort(random_number_list_copy))


if __name__ == '__main__':
    main()
