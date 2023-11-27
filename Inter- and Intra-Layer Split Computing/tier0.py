import inter_intra
import central_node
import split_model
import weight_load
import padding_add
import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
import numpy as np
from keras import regularizers
from silence_tensorflow import silence_tensorflow
import time
import sys
silence_tensorflow()
if(0 not in central_node.Tier_[0]):
    print("======================================================================================")
    print("Inter-Intra Tier0 Execute")
    print("======================================================================================")

    start_Layer0 = central_node.Tier_[0][0]
    end_Layer0 = central_node.Tier_[0][1]
    end_Layer0_print = central_node.Tier_print[0][1]
    print("start_Layer :", start_Layer0)
    print("end_Layer :", end_Layer0_print)

    splitpoint = central_node.Node_[0]#[TierNum][layerNum][nodeNum]
    print("intra_splitting point :", splitpoint)
    
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    y_train = keras.utils.to_categorical(y_train, 10)
    y_test = keras.utils.to_categorical(y_test, 10)
    intermediate_result = x_test
    weight_len = 0
    i = 1
    print(" ")
    print("layer ", i)
    split_point1 = central_node.Node_[0][0][0] #[TierNum][layerNum][nodeNum]
    split_point2 = central_node.Node_[0][0][0] + central_node.Node_[0][0][1]  #[TierNum][layerNum][nodeNum]
    
    input_data = intermediate_result
    print("input data shape :", input_data.shape)
    print("-----------node 0 execute-----------")
    # create model
    model1 = Sequential()
    model1 = split_model.add_model(model1, i, split_point1, split_point2, 0)
    model1.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    input_data = padding_add.add_padding(input_data, split_point1, split_point2, 0)
    print("padded data shape :", input_data.shape)
    none = model1.predict(input_data)
    weights0 = model1.get_weights()
    # exit(1)
    temp_weight = weight_load.weight_load()
    model1.set_weights(temp_weight[weight_len:weight_len + len(weights0)])
    # weight_len = weight_len + len(weights0)
    intermediate_result0 = model1.predict(input_data)

    print("-----------node 1 execute-----------")
    input_data = intermediate_result
    # create model
    model2 = Sequential()
    model2 = split_model.add_model(model2, i, split_point1, split_point2, 1)
    model2.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    input_data = padding_add.add_padding(input_data, split_point1, split_point2, 1)
    print("padded data shape :", input_data.shape)
    none = model2.predict(input_data)
    weights1 = model2.get_weights()
    # exit(1)
    temp_weight = weight_load.weight_load()
    model2.set_weights(temp_weight[weight_len:weight_len + len(weights1)])
    # weight_len = weight_len + len(weights1)
    intermediate_result1 = model2.predict(input_data)

    print("-----------node 2 execute-----------")
    input_data = intermediate_result
    # create model
    model3 = Sequential()
    model3 = split_model.add_model(model3, i, split_point1, split_point2, 2)
    model3.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    input_data = padding_add.add_padding(input_data, split_point1, split_point2, 2)
    print("padded data shape :", input_data.shape)
    none = model3.predict(input_data)
    weights2 = model3.get_weights()
    # exit(1)
    temp_weight = weight_load.weight_load()
    model3.set_weights(temp_weight[weight_len:weight_len + len(weights2)])
    weight_len = weight_len + len(weights0)
    intermediate_result2 = model2.predict(input_data)
    intermediate_result = []
    intermediate_result = np.concatenate((intermediate_result0, intermediate_result1, intermediate_result2), axis = 1)
    
    input_data = intermediate_result
    print("input data shape :", input_data.shape)
    print("-----------node 0 execute-----------")
    # create model
    model1 = Sequential()
    model1 = split_model.add_model(model1, i, split_point1, split_point2, 3)
    model1.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    input_data = padding_add.add_padding(input_data, split_point1, split_point2, 0)
    print("padded data shape :", input_data.shape)
    none = model1.predict(input_data)
    weights0 = model1.get_weights()
    # exit(1)
    temp_weight = weight_load.weight_load()
    model1.set_weights(temp_weight[weight_len:weight_len + len(weights0)])
    # weight_len = weight_len + len(weights0)
    intermediate_result0 = model1.predict(input_data)

    print("-----------node 1 execute-----------")
    input_data = intermediate_result
    # create model
    model2 = Sequential()
    model2 = split_model.add_model(model2, i, split_point1, split_point2, 4)
    model2.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    input_data = padding_add.add_padding(input_data, split_point1, split_point2, 1)
    print("padded data shape :", input_data.shape)
    none = model2.predict(input_data)
    weights1 = model2.get_weights()
    # exit(1)
    temp_weight = weight_load.weight_load()
    model2.set_weights(temp_weight[weight_len:weight_len + len(weights1)])
    # weight_len = weight_len + len(weights1)
    intermediate_result1 = model2.predict(input_data)

    print("-----------node 2 execute-----------")
    input_data = intermediate_result
    # create model
    model3 = Sequential()
    model3 = split_model.add_model(model3, i, split_point1, split_point2, 5)
    model3.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    input_data = padding_add.add_padding(input_data, split_point1, split_point2, 2)
    print("padded data shape :", input_data.shape)
    none = model3.predict(input_data)
    weights2 = model3.get_weights()
    # exit(1)
    temp_weight = weight_load.weight_load()
    model3.set_weights(temp_weight[weight_len:weight_len + len(weights2)])
    weight_len = weight_len + len(weights0)
    intermediate_result2 = model2.predict(input_data)
    intermediate_result = []
    intermediate_result = np.concatenate((intermediate_result0, intermediate_result1, intermediate_result2), axis=1)

    if end_Layer0 != 1:
        for i in range(start_Layer0 + 1, end_Layer0 + 1):
            print(" ")
            print("layer ", i)
            split_point1 = central_node.Node_[0][i - 1][0]
            split_point2 = central_node.Node_[0][i - 1][0] + central_node.Node_[0][i - 1][1]
            print(split_point1)
            print(split_point2)
 
            # create model
            if split_point1 != 0:
                input_data = intermediate_result
                print("input data shape :", input_data.shape)
                print("-----------node 0 execute-----------")
                model1 = Sequential()
                model1 = split_model.add_model(model1, i, split_point1, split_point2, 0)
                model1.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
                input_data = padding_add.add_padding(input_data, split_point1, split_point2, 0)
                print("padded data shape :", input_data.shape)
                none = model1.predict(input_data)
                weights0 = model1.get_weights()
                # exit(1)
                temp_weight = weight_load.weight_load()
                model1.set_weights(temp_weight[weight_len:weight_len + len(weights0)])
                # weight_len = weight_len + len(weights0)
                intermediate_result0 = model1.predict(input_data)
            print("-----------node 1 execute-----------")
            input_data = intermediate_result
            # create model
            model2 = Sequential()
            model2 = split_model.add_model(model2, i, split_point1, split_point2, 1)
            model2.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
            input_data = padding_add.add_padding(input_data, split_point1, split_point2, 1)
            print("padded data shape :", input_data.shape)
            none = model2.predict(input_data)
            weights1 = model2.get_weights()
            # exit(1)
            temp_weight = weight_load.weight_load()
            model2.set_weights(temp_weight[weight_len:weight_len + len(weights1)])
            # weight_len = weight_len + len(weights1)
            intermediate_result1 = model2.predict(input_data)
            print("-----------node 2 execute-----------")
            input_data = intermediate_result
            # create model
            model3 = Sequential()
            model3 = split_model.add_model(model3, i, split_point1, split_point2, 2)
            model3.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
            input_data = padding_add.add_padding(input_data, split_point1, split_point2, 2)
            print("padded data shape :", input_data.shape)
            none = model3.predict(input_data)
            weights2 = model3.get_weights()
            # exit(1)
            temp_weight = weight_load.weight_load()
            model3.set_weights(temp_weight[weight_len:weight_len + len(weights2)])
            if split_point1 != 0:
                weight_len = weight_len + len(weights0)
            else:
                weight_len = weight_len + len(weights1)
            intermediate_result2 = model3.predict(input_data)
            
            intermediate_result = []
            if split_point1 != 0:
                intermediate_result = np.concatenate((intermediate_result0, intermediate_result1, intermediate_result2), axis = 1)
            else:
                intermediate_result = np.concatenate((intermediate_result1, intermediate_result2), axis = 1)
    if(end_Layer0 == 9):     
        model = Sequential()
        split_point1 = -1
        split_point2 = -1
        for i in range(10,14):
            print(" ")
            print("layer ", i)
            model = split_model.add_model(model, i, split_point1, split_point2, -1)
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        none = model.predict(intermediate_result)
        weights = model.get_weights()
        temp_weight = weight_load.weight_load()
        model.set_weights(temp_weight[weight_len:weight_len + len(weights)])
        intermediate_result = model.predict(intermediate_result)    
    Mbyte = sys.getsizeof(intermediate_result)/1000000
    Mbit = Mbyte * 8
    
    if(end_Layer0 == 9):
       sleep_time_ap_node = round(Mbit / inter_intra.information[0][4])
       sleep_time_ue_ap = round(Mbit / inter_intra.information[0][3])
       sleep_time = sleep_time_ap_node + sleep_time_ue_ap
       start = time.ctime()
       print("\n-------------sending:                    ", start, "----------------")
       time.sleep(sleep_time)
       end = time.ctime()
       print("-------------intermediate data sent: ", end, "----------------")
    else:
       sleep_time_node_node = round(Mbit / inter_intra.information[0][1])
       sleep_time = sleep_time_node_node
       start = time.ctime()
       print("\n-------------sending:                    ", start, "----------------")
       time.sleep(sleep_time)
       end = time.ctime()
       print("-------------intermediate data sent: ", end, "----------------")
       
    
    check = []
    for i in range(start_Layer0 - start_Layer0, end_Layer0 - start_Layer0 + 1):
        if 0 in central_node.Node_[0][i]:
            check.append(True)
        else:
            check.append(False)
    
    inference_Latency = 0
    for i in range(start_Layer0 - start_Layer0, end_Layer0 - start_Layer0 + 1):
        if check[i] == True:   
            inference_Latency = inference_Latency + round(central_node.F_l[i + start_Layer0 - 1]/max(central_node.power[0]))
        else:
            inference_Latency0 = round((central_node.F_l[i + start_Layer0 - 1]/(central_node.power[0][0] + central_node.power[0][1] + central_node.power[0][2]))) + round(central_node.padding[i + start_Layer0 - 1]/central_node.power[0][0])
            
            inference_Latency1 = round((central_node.F_l[i + start_Layer0 - 1]/(central_node.power[0][0] + central_node.power[0][1] + central_node.power[0][2]))) + round(central_node.padding[i + start_Layer0 - 1]/central_node.power[0][1])
            
            inference_Latency2 = round((central_node.F_l[i + start_Layer0 - 1]/(central_node.power[0][0] + central_node.power[0][1] + central_node.power[0][2]))) + round(central_node.padding[i + start_Layer0 - 1]/central_node.power[0][2])
            
            inference_Latency_select = [inference_Latency0, inference_Latency1, inference_Latency2]
            inference_Latency = inference_Latency + (max(inference_Latency_select))
    
    if end_Layer0 == 9:
        inference_Latency = inference_Latency + round(central_node.F_l[9]/max(central_node.power[0]))
        inference_Latency = inference_Latency + round(central_node.F_l[10]/max(central_node.power[0]))
        inference_Latency = inference_Latency + round(central_node.F_l[11]/max(central_node.power[0]))
    print("computing latency :", inference_Latency)
    print("transmission latency :", sleep_time)
    inference_Latency = inference_Latency + sleep_time

else:
    inference_Latency = 0   
    
    
       
