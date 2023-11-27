import central_node
import add_model
import weight_load
import node0
import node1
import keras
import sys
import evaluation
import inter_intra
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
import numpy as np
from keras import regularizers
from silence_tensorflow import silence_tensorflow
silence_tensorflow()
if(0 not in central_node.Tier_print[2]):
    print("======================================================================================")
    print("Inter Node2 Execute")
    print("======================================================================================")
    start_Layer2 = central_node.Tier_print[2][0]
    end_Layer2 = central_node.Tier_print[2][1]
    print("start_Layer :", start_Layer2)
    print("end_Layer :", end_Layer2)


    # create model
    model = Sequential()

    for i in range (start_Layer2, end_Layer2 + 1):
        model = add_model.add_model(model, i)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    intermediate_result = model.predict(node1.intermediate_result1)

    weights2 = model.get_weights()
    temp_weight = weight_load.weight_load()
    model.set_weights(temp_weight[len(node0.weights0)+len(node1.weights1): len(node0.weights0)+len(node1.weights1)+len(weights2)])

    intermediate_result2 = model.predict(node1.intermediate_result1)
    
    latency2 = 0
    
    # computing latency
    compute2 = 0
    for i in range (start_Layer2, end_Layer2 + 1):
        compute2 = compute2 + central_node.F_l[i-1]
    latency2 = round(compute2 / inter_intra.information[2][5])
    print("computing latency2 :", latency2)
    # transmission latency
    Mbyte = sys.getsizeof(intermediate_result2)/1000000
    Mbit = Mbyte * 8
    latency2 = latency2 + round(Mbit / inter_intra.information[1][4]) + round(Mbit / inter_intra.information[1][3])
    tansmission_latency2 = round(Mbit / inter_intra.information[1][4]) + round(Mbit / inter_intra.information[1][3])
    print('transmission latency2 :', tansmission_latency2)
    print('inference latency2 :', latency2)

    if end_Layer2 == 13:
       eval2 = evaluation.evaluation_for_SC(intermediate_result2, node0.y_test)
