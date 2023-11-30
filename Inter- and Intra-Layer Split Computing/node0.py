import central_node
import add_model
import weight_load
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
if(0 not in central_node.Tier_print[0]):
    print("======================================================================================")
    print("Inter Node 1 Execute")
    print("======================================================================================")

    start_Layer0 = central_node.Tier_print[0][0]
    end_Layer0 = central_node.Tier_print[0][1]
    print("start_Layer :", start_Layer0)
    print("end_Layer :", end_Layer0)

    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    y_train = keras.utils.to_categorical(y_train, 10)
    y_test = keras.utils.to_categorical(y_test, 10)

    # create model
    model = Sequential()

    for i in range (start_Layer0,end_Layer0 + 1):
        model = add_model.add_model(model, i)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    intermediate_result = model.predict(x_train)
    weights0 = model.get_weights()
    temp_weight = weight_load.weight_load()
    model.set_weights(temp_weight[0: len(weights0)])
    
    start_infer = time.time()
    intermediate_result0 = model.predict(x_test)
    end_infer = time.time() - start_infer
    
    latency0 = 0
    
    # computing latency
    compute0 = 0
    for i in range (start_Layer0, end_Layer0 + 1):
        compute0 = compute0 + central_node.F_l[i-1]
    latency0 = round(compute0 / inter_intra.information[0][5])
    print("computing latency :", latency0)
    # transmission latency
    Mbyte = sys.getsizeof(intermediate_result0)/1000000
    Mbit = Mbyte * 8
    latency0 = latency0 + round(Mbit / inter_intra.information[1][1])
    tansmission_latency0 = round(Mbit / inter_intra.information[1][1])
    print('transmission latency :', tansmission_latency0)
    print('inference latency :', latency0)
    
    sleep_time = round(Mbit / inter_intra.information[1][1])
    start = time.ctime()
    print("\n-------------sending:                    ", start, "----------------")
    time.sleep(sleep_time)
    end = time.ctime()
    print("-------------intermediate data sent: ", end, "----------------")
    
    if end_Layer0 == 13:
       eval0 = evaluation.evaluation_for_SC(intermediate_result0, y_test)
