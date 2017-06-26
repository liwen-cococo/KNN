import knn
import math
import optimization_1


# return a list of 10 elements(Each element is a list of 784 floats)
def calculate_center_vector(training, training_result):
    # result is a 10 * 784 list
    result = []
    for i in range(10):
        x = []
        for j in range(784):
            x.append(0.0)
        result.append(x)
    number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    length = training.__len__()
    for i in range(length):
        number[training_result[i]] += 1
        for j in range(784):
            result[training_result[i]][j] += training[i][j]

    for i in range(10):
        for j in range(784):
            result[i][j] = result[i][j]/number[i]
    return result


def calculate_accuracy(training, training_result, test, test_result):
    center_vectors = calculate_center_vector(training, training_result)

    accuracy = 0.0
    test_length = test.__len__()

    for i in range(test_length):
        # This will include 10 distances
        distances = []
        for j in range(10):
            d = knn.compute_distance_2(test[i], center_vectors[j])
            distances.append(d)
        m = min(distances)
        index = distances.index(m)
        if index == test_result[i]:
            print("yes")
            accuracy += 1.0
        else:
            print("no", "index =", index, "test_result[i] =",test_result[i])
            print(distances)
            print("")

    return accuracy/test_length


def combine_algorithm(training, training_result, test, test_result, kk):
    center_vectors = calculate_center_vector(training, training_result)
    accuracy = 0.0
    test_length = test.__len__()

    for i in range(test_length):
        # This will include 10 distances
        distances = []
        distances_sorted = []
        for j in range(10):
            d = knn.compute_distance_2(test[i], center_vectors[j])
            distances.append(d)
            distances_sorted.append(d)
        distances_sorted = sorted(distances_sorted)

        type_number = []
        for j in range(kk):
            type_number.append(distances.index(distances_sorted[j]))

        training_length = training.__len__()
        new_training = []
        new_training_result = []
        for j in range(training_length):
            flag = 0
            for m in range(kk):
                if training_result[j] == type_number[m]:
                    flag = 1
            if flag == 1:
                new_training.append(training[j])
                new_training_result.append(training_result[j])
        new_test = [test[i]]
        new_test_result = [test_result[i]]
        acc = knn.knn_algorithm(new_training, new_training_result, new_test, new_test_result, 10)
        # acc = optimization_1.knn_optimization1(new_training, new_training_result, new_test, new_test_result, 10)
        accuracy += acc
    return accuracy/test_length
