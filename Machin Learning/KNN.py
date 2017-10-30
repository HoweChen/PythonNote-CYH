import numpy as np


def create_random_matrix(size, feature_length, element_scale):
    matrix = np.random.randint(element_scale, size=(size, feature_length))
    return matrix


def knn_algorithm(data, testing, k):
    output_dict = {}
    output_index = []
    index = 0
    for i in data:
        zipped_data = np.dstack((i, testing))
        distance = 0
        for j in zipped_data[0]:
            distance += (j[0] - j[1]) ** 2
        distance = np.sqrt(distance)
        output_dict[distance] = index
        index += 1
    for i in sorted(output_dict.keys())[0:k]:
        output_index.append(output_dict.get(i))
    return output_index
    # sorted_keys = sorted(output_dict.keys(), reverse=True)
    # for i in sorted_keys[0:k]:
    #     output_index.append(output_dict.get(i))
    # return output_index


def main():
    size = int(input('How many cases do you want?\n'))
    feature_length = int(input('What is the length of features do you want?\n'))
    element_scale = int(input('Please input the scale of element\n'))
    top_k = int(input('Please define the number of top-k\n'))
    matrix_data = create_random_matrix(size, feature_length, element_scale)
    matrix_input = create_random_matrix(1, feature_length, element_scale)

    print('\nAuto-created sample data is:')
    print(matrix_data)
    print('\nAuto-created input data is:')
    print(matrix_input[0])
    result = knn_algorithm(matrix_data, matrix_input, top_k)
    print('\nThe top ' + str(top_k) + ' index would be:')
    print(result)


if __name__ == '__main__':
    main()
