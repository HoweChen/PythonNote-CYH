import create_random_number_list
import random


def shell_sort(input_list):
    list_length = len(input_list)
    if list_length <= 1:
        return input_list
    else:
        step = list_length // 2
        while step > 0:
            for index in range(step, list_length):
                temp = index #先记录下来
                for jump2index in range(index - step, -1, -step):
                    if input_list[temp] < input_list[jump2index]:
                        # 之所以是用temp的来比，是因为temp所在的index会被更新，这样小的数字会被一直交换下去
                        input_list[temp], input_list[jump2index] = input_list[jump2index], input_list[temp]
                        temp = jump2index # 更新temp到已经换到的jump2index位置，以供下次交换
            step = step // 2
        return input_list


def main():
    # rand_num_list = create_random_number_list.main()
    # rand_num_list = list(range(1, 11))
    # random.shuffle(rand_num_list)
    rand_num_list = [9, 6, 4, 8, 2, 10, 5, 3, 1, 7]
    result = shell_sort(rand_num_list)
    print(result)


if __name__ == '__main__':
    main()
