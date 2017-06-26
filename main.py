import loadData
import knn
import optimization_1
import center_vector
# training_length = 2000 or 5000 test_length = 200
[training, training_result, test, test_result] = loadData.load_data_2000()

# k = [1, 5, 10, 30, 60, 100]
# for i in range(6):
    # ^^^^^^^^^^^^^^^^ naive knn ^^^^^^^^^^^^^^^^
    # accuracy = knn.knn_algorithm(training, training_result, test, test_result, k[i])

    # ^^^^^^^^^^^^^^^^ optimized knn ^^^^^^^^^^^^^^^^
    # accuracy = optimization_1.knn_optimization1(training, training_result, test, test_result, k[i])

    # print("k =", k[i], "acc =", accuracy)

# acc = center_vector.calculate_accuracy(training, training_result, test, test_result)
k = [2, 3, 4, 5, 6]
for i in range(5):
    acc = center_vector.combine_algorithm(training, training_result, test, test_result, k[i])
    print("k = ", k[i], "acc =", acc)
