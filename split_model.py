import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
import numpy as np
from keras import regularizers
weight_decay = 0.0005
nb_epoch = 100
batch_size = 64
def add_model(mod, l, split_point, index): # layer 별 코드를 가져올 수 있는 함수
    model = mod
    n = l
    if n == 1:
        # layer1 32*32*3
        model.add(Conv2D(64, (3, 3), padding='same',
                                 input_shape=(32, 32, 3), kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.3))
        # layer2 32*32*64
        model.add(Conv2D(64, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=(2, 2)))

    if n == 2:
        if index == 0:
            # layer3 16*16*64
            model.add(Conv2D(128, (3, 3), input_shape=(split_point + 2, 16 + 2, 64),
                                 kernel_regularizer=regularizers.l2(weight_decay)))
        if index == 1:
            # layer3 16*16*64
            model.add(Conv2D(128, (3, 3), input_shape=(16 - split_point + 2, 16 + 2, 64),
                             kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.4))
    if n == 3:
        if index == 0:
            # layer4 16*16*128
            model.add(Conv2D(128, (3, 3), input_shape=(split_point + 2, 16 + 2, 128),
                             kernel_regularizer=regularizers.l2(weight_decay)))
        if index == 1:
            # layer4 16*16*128
            model.add(Conv2D(128, (3, 3), input_shape=(16 - split_point + 2, 16 + 2, 128),
                             kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=(2, 2)))
    if n == 4:
        if index == 0:
            # layer5 8*8*128
            model.add(Conv2D(256, (3, 3), input_shape=(split_point + 2, 8 + 2, 128),
                                kernel_regularizer=regularizers.l2(weight_decay)))
        if index == 1:
            # layer5 8*8*128
            model.add(Conv2D(256, (3, 3), input_shape=(8 - split_point + 2, 8 + 2, 128),
                             kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.4))
    if n == 5:
        if index == 0:
            # layer6 8*8*256
            model.add(Conv2D(256, (3, 3), input_shape=(split_point + 2, 8 + 2, 256),
                         kernel_regularizer=regularizers.l2(weight_decay)))
        if index == 1:
            # layer6 8*8*256
            model.add(Conv2D(256, (3, 3), input_shape=(8 - split_point + 2, 8 + 2, 256),
                         kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.4))
    if n == 6:
        if index == 0:
            # layer7 8*8*256
            model.add(Conv2D(256, (3, 3), input_shape=(split_point + 2, 8 + 2, 256),
                         kernel_regularizer=regularizers.l2(weight_decay)))
        if index == 1:
            # layer7 8*8*256
            model.add(Conv2D(256, (3, 3), input_shape=(8 - split_point + 2, 8 + 2, 256),
                             kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=(2, 2)))
    if n == 7:
        if index == 0:
            # layer8 4*4*256
            model.add(Conv2D(512, (3, 3), input_shape=(split_point + 2, 4 + 2, 256),
                         kernel_regularizer=regularizers.l2(weight_decay)))
        if index == 1:
            # layer8 4*4*256
            model.add(Conv2D(512, (3, 3), input_shape=(4 - split_point + 2, 4 + 2, 256),
                             kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.4))
    if n == 8:
        if index == 0:
            # layer9 4*4*512
            model.add(Conv2D(512, (3, 3), input_shape=(split_point + 2, 4 + 2, 512),
                         kernel_regularizer=regularizers.l2(weight_decay)))
        if index == 1:
            # layer9 4*4*512
            model.add(Conv2D(512, (3, 3), input_shape=(4 - split_point + 2, 4 + 2, 512),
                             kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.4))
    if n == 9:
        if index == 0:
            # layer10 4*4*512
            model.add(Conv2D(512, (3, 3), input_shape=(split_point + 2, 4 + 2, 512),
                         kernel_regularizer=regularizers.l2(weight_decay)))
        if index == 1:
            # layer10 4*4*512
            model.add(Conv2D(512, (3, 3), input_shape=(4 - split_point + 2, 4 + 2, 512),
                             kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=(2, 2)))
    if n == 10:
        # layer11 2*2*512
        model.add(Conv2D(512, (3, 3), input_shape=(2, 2, 512), padding='same',
                         kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.4))
    if n == 11:
        # layer12 2*2*512
        model.add(Conv2D(512, (3, 3), input_shape=(2, 2, 512), padding='same',
                             kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.4))

    if n == 12:
        # layer13 2*2*512
        model.add(Conv2D(512, (3, 3), input_shape=(2, 2, 512), padding='same',
                             kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.5))

    if n == 13:
        # layer14 1*1*512
        model.add(Flatten(input_shape=(1, 1, 512)))
        model.add(Dense(512, kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        # layer15 512
        model.add(Dense(512, kernel_regularizer=regularizers.l2(weight_decay)))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        # layer16 512
        model.add(Dropout(0.5))
        model.add(Dense(10))
        model.add(Activation('softmax'))
        
    return model
