import numpy as np

# two methods: Euclidean Distance, Cosine Similarity and Manhattan Distance


def create_random_matrix(size, feature_length, element_scale):
    matrix = np.random.randint(element_scale, size=(size, feature_length))
    return matrix


def knn_euclidean_distance(zipped_data, distance=0):
    for j in zipped_data:
        distance += np.power((j[0] - j[1]), 2)
    distance = np.sqrt(distance)
    return distance


def knn_manhattan_distance(zipped_data, distance=0):
    for j in zipped_data:
        distance += np.abs(j[0] - j[1])
    return distance


def knn_cosine_similarity(zipped_data, sub_data, testing_data, vector_product=0, norm_of_data=0, norm_of_input=0):
    for j in zipped_data:
        vector_product += j[0] * j[1]

    for norm_data_loop in list(map(lambda x: np.power(x, 2), sub_data)):
        norm_of_data += norm_data_loop
    for norm_input_loop in list(map(lambda x: np.power(x, 2), testing_data)):
        norm_of_input += norm_input_loop

    cosine_similarity = vector_product / \
        (np.sqrt(norm_of_data) + np.sqrt(norm_of_input))
    return cosine_similarity


def knn_algorithm(data, testing, k):
    # declaration of dictionary
    output_dict_euclidean_distance = {}
    output_dict_manhattan_distance = {}
    output_dict_cosine_similarity = {}
    output_result = {}

    # declaration of list
    output_index_euclidean_distance = []
    output_index_manhattan_distance = []
    output_index_cosine_similarity = []

    index = 0
    for i in data:
        zipped_data = np.dstack((i, testing))[0]

        euclidean_distance = knn_euclidean_distance(zipped_data)
        manhattan_distance = knn_manhattan_distance(zipped_data)
        cosine_similarity = knn_cosine_similarity(zipped_data, i, testing[0])

        output_dict_euclidean_distance[euclidean_distance] = index
        output_dict_manhattan_distance[manhattan_distance] = index
        output_dict_cosine_similarity[cosine_similarity] = index

        index += 1

    # get index through the sorted result
    # Euclidean Distance
    for i in sorted(output_dict_euclidean_distance.keys())[0:k]:
        output_index_euclidean_distance.append(
            output_dict_euclidean_distance.get(i))
    output_result['Euclidean Distance'] = output_index_euclidean_distance
    # Manhattan Distance
    for i in sorted(output_dict_manhattan_distance.keys())[0:k]:
        output_index_manhattan_distance.append(
            output_dict_manhattan_distance.get(i))
    output_result['Manhattan Distance'] = output_index_manhattan_distance
    # Cosine Similarity
    for i in sorted(output_dict_cosine_similarity.keys())[0:k]:
        output_index_cosine_similarity.append(
            output_dict_cosine_similarity.get(i))
    output_result['Cosine Similarity'] = output_index_cosine_similarity

    return output_result


def main():
    size = int(input('How many cases do you want?\n'))
    feature_length = int(
        input('What is the length of features do you want?\n'))
    element_scale = int(input('Please input the scale of element\n'))
    top_k = int(input('Please define the number of top-k\n'))
    matrix_data = create_random_matrix(size, feature_length, element_scale)
    matrix_input = create_random_matrix(1, feature_length, element_scale)

    print('\nAuto-created sample data is:')
    print(matrix_data)
    print('\nAuto-created input data is:')
    print(matrix_input[0])
    result = knn_algorithm(matrix_data, matrix_input, top_k)
    print('\nThe top ' + str(top_k) + ' index using Euclidean Distance would be:')
    print(result['Euclidean Distance'])
    print('\nThe top ' + str(top_k) + ' index using Manhattan Distance would be:')
    print(result['Manhattan Distance'])
    print('\nThe top ' + str(top_k) + ' index using Cosine Similarity would be:')
    print(result['Cosine Similarity'])


if __name__ == '__main__':
    main()
