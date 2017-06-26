import knn


def knn_optimization1(training, training_result, test, test_result, k):
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
            x = knn.compute_distance_2(training[p], test[i])
            d = (p, x)
            distances_all.append(d)
        # rank distances_all, and get the first K elements
        distances_all = sorted(distances_all, key=lambda index_distance: index_distance[1])
        distances_k = []
        for q in range(k):
            distances_k.append(distances_all[q])

        # -----------------------------KNN: modify the evaluation rule -----------------------------
        type_list = []
        number = [0, 0, 0, 0, 0,  0, 0, 0, 0, 0]
        distance_10 = [0.0, 0.0, 0.0, 0.0, 0.0,  0.0, 0.0, 0.0, 0.0, 0.0]
        for(q) in range(k):
            c = training_result[distances_k[q][0]]
            type_list.append(c)
            number[c] += 1
            distance_10[c] += distances_k[q][1]

        # print("number = ", number)
        # print("distance = ", distance_10)
        preference = []
        for q in range(10):
            if number[q] > 0.0:
                x = distance_10[q] / (number[q] * number[q])
            else:
                x = -1.0
            preference.append(x)
        # print("preference = ", preference)

        min_value = -1.0
        min_index = -1
        for q in range(10):
            if 0.0 < preference[q] < min_value or (min_value < 0.0 < preference[q]):
                min_index = q
                min_value = preference[q]
        # print("prediction_type = ", min_index)

        if min_index == test_result[i]:
            accuracy += 1.0
    return accuracy/test_length
