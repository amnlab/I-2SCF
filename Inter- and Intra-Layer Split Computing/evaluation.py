import numpy as np

def evaluation_for_SC (output_results, test_label):
    prediction_digit = []
    label_digit= []
    for output_result in output_results:
        output_index = np.argmax(output_result)
        prediction_digit.append(output_index)
    for test_val in test_label:
        test_index = np.argmax(test_val)
        label_digit.append(test_index)
    prediction_digit = np.array(prediction_digit)
    label_digit = np.array(label_digit)
    accuracy = (prediction_digit == label_digit).mean()
    return accuracy
