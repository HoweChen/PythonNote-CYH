import random


def create_sorted_list(size):
    return list(range(int(size)))


def binary_search(created_list, target_number, left, right):
    mid = int((left + right) / 2)
    if target_number > created_list[mid]:
        return binary_search(created_list, target_number, mid + 1, right)
    elif target_number < created_list[mid]:
        return binary_search(created_list, target_number, left, mid - 1)
    else:
        # target number is found which is mid
        return mid


def main():
    size = input("What size of list do you want?\n")
    size = int(size)
    created_list = create_sorted_list(size)
    print(created_list)

    # we randomize a target number, since randint use [a,b] so size should minus one
    random_number = random.randint(0, size - 1)
    print("The random number this program needs to find is: " + str(random_number))
    result = binary_search(created_list, random_number, 0, len(created_list) - 1)
    print("The index of this number would be: " + str(result))


if __name__ == '__main__':
    main()
