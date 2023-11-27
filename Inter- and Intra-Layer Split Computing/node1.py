import central_node
import add_model
import weight_load
import node0
import keras
import time
import evaluation
import sys
import inter_intra
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
import numpy as np
from keras import regularizers
from silence_tensorflow import silence_tensorflow
silence_tensorflow()
if(0 not in central_node.Tier_print[1]):
    print("======================================================================================")
    print("Inter Node1 Execute")
    print("======================================================================================")

    start_Layer1 = central_node.Tier_print[1][0]
    end_Layer1 = central_node.Tier_print[1][1]
    print("start_Layer :", start_Layer1)
    print("end_Layer :", end_Layer1)


    # create model
    model = Sequential()

    for i in range (start_Layer1, end_Layer1 + 1):
        model = add_model.add_model(model, i)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    intermediate_result = model.predict(node0.intermediate_result0)

    weights1 = model.get_weights()
    temp_weight = weight_load.weight_load()
    model.set_weights(temp_weight[len(node0.weights0): len(node0.weights0)+len(weights1)])

    intermediate_result1 = model.predict(node0.intermediate_result0)
    
    latency1 = 0
    
    # computing latency
    compute1 = 0
    for i in range (start_Layer1, end_Layer1 + 1):
        compute1 = compute1 + central_node.F_l[i-1]
    latency1 = round(compute1 / inter_intra.information[1][5])
    print("computing latency1 :", latency1)
    # transmission latency
    Mbyte = sys.getsizeof(intermediate_result1)/1000000
    Mbit = Mbyte * 8
    latency1 = latency1 + round(Mbit / inter_intra.information[1][2])
    tansmission_latency1 = round(Mbit / inter_intra.information[1][2])
    print('transmission latency1 :', tansmission_latency1)
    print('inference latency1 :', latency1)
      
    sleep_time = round(Mbit / inter_intra.information[1][2])
    start = time.ctime()
    print("\n-------------sending:                    ", start, "----------------")
    time.sleep(sleep_time)
    end = time.ctime()
    print("-------------intermediate data sent: ", end, "----------------")
    
    if end_Layer1 == 13:
       eval1 = evaluation.evaluation_for_SC(intermediate_result1, node0.y_test)
