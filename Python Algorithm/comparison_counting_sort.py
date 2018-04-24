import create_random_number_list
import random


def comparison_counting_sort(input_list):
    list_length = len(input_list)
    result = list(range(list_length))
    for i in range(list_length):
        count = 0
        for j in range(list_length):
            if i == j:
                continue
            else:
                if input_list[j] < input_list[i]:
                    count += 1
        result[count] = input_list[i]
    return result


def main():
    rand_num_list = create_random_number_list.main()
    # rand_num_list = list(range(10))
    random.shuffle(rand_num_list)
    result = comparison_counting_sort(rand_num_list)
    print(result)
    backup = rand_num_list.copy()
    print(sorted(backup) == result)


if __name__ == '__main__':
    main()
