import inter_intra
import central_node
import split_model
import weight_load
import padding_add
import Tier0

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
if(0 not in central_node.Tier_[1]):
    print("\n\n=========================================================")
    print("====================Tier1 execute========================")
    print("=========================================================")

    start_Layer1 = central_node.Tier_[1][0]
    end_Layer1 = central_node.Tier_[1][1]
    end_Layer1_print = central_node.Tier_print[1][1]
    print("start_Layer", start_Layer1)
    print("end_Layer", end_Layer1_print)
    
    splitpoint = central_node.Node_[1]#[TierNum][layerNum][nodeNum]
    print("intra_splitpoint", splitpoint)
    
    
    intermediate_result = Tier0.intermediate_result
    weight_len = Tier0.weight_len
    temp_compute = 0 # computing latency measure
    temp_sleep_time = 0
    for i in range(start_Layer1, end_Layer1 + 1):
        print(i)
        split_point = central_node.Node_[1][i - (Tier0.end_Layer0 + 1)][0] #[TierNum][layerNum][nodeNum]
        input_data = intermediate_result
        # create model
        print("node0 execute")
        model1 = Sequential()
        model1 = split_model.add_model(model1, i, split_point, 0)
        model1.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        #print(input_data.shape)
        input_data = padding_add.add_padding(input_data, split_point, 0)
        #print(input_data.shape)
        none = model1.predict(input_data)
        weights0 = model1.get_weights()
        # exit(1)
        temp_weight = weight_load.weight_load()
        model1.set_weights(temp_weight[weight_len:weight_len + len(weights0)])
        intermediate_result0 = model1.predict(input_data)
        input_data = intermediate_result
        # create model
        print("node1 execute")
        model2 = Sequential()
        model2 = split_model.add_model(model2, i, split_point, 1)
        model2.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        #print(input_data.shape)
        input_data = padding_add.add_padding(input_data, split_point, 1)
        #print(input_data.shape)
        none = model2.predict(input_data)
        weights1 = model2.get_weights()
        
        # exit(1)
        model2.set_weights(temp_weight[weight_len:weight_len + len(weights1)])
        weight_len = weight_len + len(weights0)
        intermediate_result1 = model2.predict(input_data)
        
        intermediate_result = []
        intermediate_result = np.concatenate((intermediate_result0, intermediate_result1), axis = 1)
        
    if(end_Layer1 == 9):     
        model = Sequential()
        split_point = -1
        for i in range(10,14):
            print(i)
            model = split_model.add_model(model, i, split_point, -1)
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        none = model.predict(intermediate_result)
        weights = model.get_weights()
        model.set_weights(temp_weight[weight_len:weight_len + len(weights)])
        intermediate_result = model.predict(intermediate_result)    
    Mbyte = sys.getsizeof(intermediate_result)/1000000
    Mbit = Mbyte * 8
    
    if(end_Layer1 == 9):
    	sleep_time_ap_node = round(Mbit / inter_intra.information[0][4])
    	sleep_time_ue_ap = round(Mbit / inter_intra.information[0][3])
    	sleep_time = sleep_time_ap_node + sleep_time_ue_ap
    	start = time.ctime()
    	print("\n-------------sending:                    ", start, "----------------")
    	time.sleep(sleep_time)
    	end = time.ctime()
    	print("-------------intermediate data send OK: ", end, "----------------")
    else:
        sleep_time_node_node = round(Mbit / inter_intra.information[1][2])
        sleep_time = sleep_time_node_node
        start = time.ctime()
        print("\n-------------sending:                    ", start, "----------------")
        time.sleep(sleep_time)
        end = time.ctime()
        print("-------------intermediate data send OK: ", end, "----------------")
    
    
    check = []
    for i in range(start_Layer1 - start_Layer1, end_Layer1 - start_Layer1 + 1):
        if 0 in central_node.Node_[1][i]:
            check.append(True)
        else:
            check.append(False)
    
    
    inference_Latency = 0
    for i in range(start_Layer1 - start_Layer1, end_Layer1 - start_Layer1 + 1):
        if check[i] == True:	
            #print("max", max(central_node.power[1]))
            inference_Latency = inference_Latency + round(central_node.F_l[i + start_Layer1 - 1]/max(central_node.power[1])) + round(central_node.padding[i + start_Layer1 - 1]/max(central_node.power[1]))
            #print("inference_Latency", inference_Latency)
        else:
            inference_Latency0 = round((central_node.F_l[i + start_Layer1 - 1]/(central_node.power[1][0] + central_node.power[1][1]))) + round(central_node.padding[i + start_Layer1 - 1]/central_node.power[1][0])
            inference_Latency1 = round((central_node.F_l[i + start_Layer1 - 1]/(central_node.power[1][0] + central_node.power[1][1]))) + round(central_node.padding[i + start_Layer1 - 1]/central_node.power[1][1])
            inference_Latency_select = [inference_Latency0, inference_Latency1]
            #print("max", max(inference_Latency_select))
            inference_Latency = inference_Latency + (max(inference_Latency_select))
            
    if end_Layer1 == 9:
        inference_Latency = inference_Latency + round(central_node.F_l[9]/max(central_node.power[1]))
        inference_Latency = inference_Latency + round(central_node.F_l[10]/max(central_node.power[1]))
        inference_Latency = inference_Latency + round(central_node.F_l[11]/max(central_node.power[1]))
    #print("computing_Laytency", inference_Latency)
    #print("trans_Laytency", sleep_time)
    inference_Latency = inference_Latency + sleep_time
    #print("inference_Latency", inference_Latency)
    
else:
    inference_Latency = 0       
    
    
    
    
    
    
    
    
    
