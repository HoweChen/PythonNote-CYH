import create_random_number_list
import random


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        list_length = len(input_list)
        mid = list_length // 2

        left = merge_sort(input_list[:mid:])
        right = merge_sort(input_list[mid::])
        return merge(left, right)


def merge(left, right):
    result = []
    left_ptr = 0
    right_ptr = 0

    while (left_ptr < len(left) and right_ptr < len(right)):
        if left[left_ptr] <= right[right_ptr]:
            result.append(left[left_ptr])
            left_ptr += 1
        else:
            result.append(right[right_ptr])
            right_ptr += 1
    result.extend(left[left_ptr:])
    result.extend(right[right_ptr:])
    return result


def main():
    rand_num_list = create_random_number_list.main()
    # rand_num_list = list(range(0, 10))
    # random.shuffle(rand_num_list)
    print('Before: {0}'.format(rand_num_list))
    result = merge_sort(rand_num_list)
    print('After: {0}'.format(result))
    print(sorted(rand_num_list) == result)


if __name__ == '__main__':
    main()
# def mergesort(seq):
#     if len(seq) <= 1:
#         return seq
#     mid = int(len(seq)/2)
#     left = mergesort(seq[:mid])
#     right = mergesort(seq[mid:])
#     return merge(left, right)
#
#
# def merge(left, right):
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result
#
#
# if __name__ == '__main__':
#     seq = [4, 5, 7, 9, 7, 5, 1, 0, 7, -2, 3, -99, 6]
#     print(mergesort(seq))
