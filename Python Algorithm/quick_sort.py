import create_random_number_list
import random
import sys

random_number_list = create_random_number_list.main()


def quick_sort(random_number_list):
    result = []
    if len(random_number_list) < 2:
        return random_number_list
    else:
        less = []
        greater = []
        pivot = random_number_list[int(len(random_number_list) / 2)]
        for i in random_number_list:
            if i == pivot:
                continue
            else:
                if i < pivot:
                    less.append(i)
                else:
                    greater.append(i)
        result = quick_sort(less) + [pivot] + quick_sort(greater)
        return result


def inplace_quick_sort_partition(target_list, begin, end, pivot_index):
    pivot = target_list[pivot_index]

    # move the pivot number to the end of the list
    target_list[pivot_index], target_list[end] = target_list[end], target_list[pivot_index]
    store_index = begin
    for i in range(begin, end):
        if target_list[i] <= pivot:
            # if i != store_index:
            target_list[store_index], target_list[i] = target_list[i], target_list[store_index]
            store_index += 1
    # swap back the pivot
    target_list[end], target_list[store_index] = target_list[store_index], target_list[end]
    return store_index


def inplace_quick_sort(target_list, begin, end):
    if begin < end:
        pivot_index = int((end - begin) / 2)
        pivot_index_new = inplace_quick_sort_partition(target_list, begin, end, pivot_index)
        inplace_quick_sort(target_list, begin, pivot_index_new - 1)
        inplace_quick_sort(target_list, pivot_index_new + 1, end)
    return target_list


def main():
    # get random 10 test case
    random_number_list = list(range(5))
    random.shuffle(random_number_list)
    print(random_number_list)

    # quick_sort not inplace
    result = quick_sort(random_number_list)
    print(result)

    # in-place quick sort
    # # create a new copy since in_place quick sort would change the value of random_number_list
    # random_number_list_copy = random_number_list.copy()
    # result = inplace_quick_sort(random_number_list_copy, 0, len(random_number_list_copy) - 1)
    # print(result)


if __name__ == '__main__':
    main()
