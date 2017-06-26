import math


# compute the distance between two input vector
# a and b are both a list of 784 floats
# ^^^^^^^^^^^^^ method 1 ^^^^^^^^^^^^^^
# distance = sum(|ai - bi|)
def compute_distance_1(a, b):
    result = 0.0
    length = a.__len__()
    for i in range(length):
        result += math.fabs(a[i] - b[i])
    return result


# ^^^^^^^^^^^^^ method 2 ^^^^^^^^^^^^^^
# distance = sqrt(sum[(ai - bi)*(ai - bi)])
def compute_distance_2(a, b):
    result = 0.0
    length = a.__len__()
    for i in range(length):
        result += (a[i] - b[i])*(a[i] - b[i])
    result = math.sqrt(result)
    return result


# naive_knn: brute search
# input: training, test, k
# output: accuracy rate([0,1])
def knn_algorithm(training, training_result, test, test_result, k):
    # constant definition
    training_length = training.__len__()
    test_length = test.__len__()
    accuracy = 0.0
    # travel test set
    for i in range(test_length):
        # A list which includes all distances.Every element is a dictionary(index: distance)
        distances_all = []
        # calculate distances_all
        for p in range(training_length):
            # x = compute_distance_1(training[p], test[i])
            x = compute_distance_2(training[p], test[i])
            d = (p, x)
            distances_all.append(d)
        # rank distances_all, and get the first K elements
        distances_all = sorted(distances_all, key=lambda index_distance: index_distance[1])
        distances_k = []
        for q in range(k):
            distances_k.append(distances_all[q])

        # ----------------------------- naive KNN -----------------------------
        type_list = []
        for(q) in range(k):
            type_list.append(training_result[distances_k[q][0]])
        type_number = []
        for item in type_list:
            type_number.append(
                type_list.count(item))
        m = max(type_number)
        index_max = type_number.index(m)
        prediction_type = type_list[index_max]
        if prediction_type == test_result[i]:
            accuracy += 1.0
    return accuracy/test_length

