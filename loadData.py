import pickle


# load data from data.pkl
def load_data_2000():
    f = open('data_2000_200.pkl', 'rb')
    [training, training_result, test, test_result] = pickle.load(f, encoding="latin1")
    f.close()
    return [training, training_result, test, test_result]


def load_data_5000():
    f = open('data_5000_200.pkl', 'rb')
    [training, training_result, test, test_result] = pickle.load(f, encoding="latin1")
    f.close()
    return [training, training_result, test, test_result]
