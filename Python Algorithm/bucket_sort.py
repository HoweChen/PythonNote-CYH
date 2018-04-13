import create_random_number_list
import random


def bucket_sort(rand_num_list):
    list_length = len(rand_num_list)
    bucket_size = 10
    bucket_list = []
    result = []
    for i in range(bucket_size):
        temp_list = []
        bucket_list.append(temp_list)
    # cannot use "bucket_list = [[]] * bucket_size" because all sublist reference to the same block of memory, the
    # insertion would insert value to all
    for num in rand_num_list:
        bucket_index = int(num * bucket_size)
        bucket_list[bucket_index].append(num)

    for index in range(bucket_size):
        if bucket_list[index]:
            bucket_list[index] = insertion_sort(bucket_list[index])
            result.extend(bucket_list[index])
    return result


def insertion_sort(input_list):
    length = len(input_list)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if input_list[i] < input_list[j - 1]:
                input_list[i], input_list[j - 1] = input_list[j - 1], input_list[i]
    return input_list


def main():
    # rand_num_list = create_random_number_list.main()
    size = int(input('Please input the size you want to generate: '))
    rand_num_list = []
    for i in range(size):
        rand_num_list.append(random.uniform(1, 10) / 10)
    random.shuffle(rand_num_list)
    backup = rand_num_list.copy()
    result = bucket_sort(rand_num_list)
    print(result)
    print(result == sorted(backup))


if __name__ == '__main__':
    main()
