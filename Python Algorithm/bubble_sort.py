import create_random_number_list
import random

random_number_list = create_random_number_list.main()


# 在每一次迭代中，大的，次大的，次次大的元素都会被换到对应的位置，然后最小的元素总是会被放到最上层
# 因为第一次循环之后第二次都是从头开始，所以最小的数在中间也会被换到第一个去

def bubble_sort(test_list):
    list_length = len(test_list)

    for i in range(list_length):
        for j in range(list_length - 1):
            if test_list[i] < test_list[j]:
                test_list[i], test_list[j] = test_list[j], test_list[i]

    return test_list


def main():
    random_number_list = list(range(10))
    random.shuffle(random_number_list)
    result = bubble_sort(random_number_list)
    print(result)


if __name__ == '__main__':
    main()
