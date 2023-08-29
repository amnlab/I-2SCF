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
def add_model(mod, l): # layer 별 코드를 가져올 수 있는 함수
        model = mod
        n = l

        if n == 1:
                # layer1 32*32*3
                model.add(Conv2D(64, (3, 3), padding='same', input_shape=(32, 32, 3), kernel_regularizer=regularizers.l2(weight_decay)))
                model.add(Activation('relu'))
                model.add(BatchNormalization())
                model.add(Dropout(0.3))
                # layer2 32*32*64
                model.add(Conv2D(64, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
                model.add(Activation('relu'))
                model.add(BatchNormalization())
                model.add(MaxPooling2D(pool_size=(2, 2)))
        if n == 2:
                # layer3 16*16*64
                model.add(Conv2D(128, (3, 3), input_shape=(16, 16, 64), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
                model.add(Activation('relu'))
                model.add(BatchNormalization())
                model.add(Dropout(0.4))
        if n == 3:
                # layer4 16*16*128
                model.add(Conv2D(128, (3, 3), input_shape=(16, 16, 128), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
                model.add(Activation('relu'))
                model.add(BatchNormalization())
                model.add(MaxPooling2D(pool_size=(2, 2)))
        if n == 4:
                # layer5 8*8*128
                model.add(Conv2D(256, (3, 3), input_shape=(8, 8, 128), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
                model.add(Activation('relu'))
                model.add(BatchNormalization())
                model.add(Dropout(0.4))
        if n == 5:
                # layer6 8*8*256
                model.add(Conv2D(256, (3, 3), input_shape=(8, 8, 256), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
                model.add(Activation('relu'))
                model.add(BatchNormalization())
                model.add(Dropout(0.4))
        if n == 6:
                # layer7 8*8*256
                model.add(Conv2D(256, (3, 3), input_shape=(8, 8, 256), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
                model.add(Activation('relu'))
                model.add(BatchNormalization())
                model.add(MaxPooling2D(pool_size=(2, 2)))
        if n == 7:
                # layer8 4*4*256
                model.add(Conv2D(512, (3, 3), input_shape=(4, 4, 256), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
                model.add(Activation('relu'))
                model.add(BatchNormalization())
                model.add(Dropout(0.4))
        if n == 8:
                # layer9 4*4*512
                model.add(Conv2D(512, (3, 3), input_shape=(4, 4, 512), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
                model.add(Activation('relu'))
                model.add(BatchNormalization())
                model.add(Dropout(0.4))
        if n == 9:
                # layer10 4*4*512
                model.add(Conv2D(512, (3, 3), input_shape=(4, 4, 512), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
                model.add(Activation('relu'))
                model.add(BatchNormalization())
                model.add(MaxPooling2D(pool_size=(2, 2)))
        if n == 10:
                # layer11 2*2*512
                model.add(Conv2D(512, (3, 3), input_shape=(2, 2, 512), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
                model.add(Activation('relu'))
                model.add(BatchNormalization())
                model.add(Dropout(0.4))
        if n == 11:
                # layer12 2*2*512
                model.add(Conv2D(512, (3, 3), input_shape=(2, 2, 512), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
                model.add(Activation('relu'))
                model.add(BatchNormalization())
                model.add(Dropout(0.4))
        if n == 12:
                # layer13 2*2*512
                model.add(Conv2D(512, (3, 3), input_shape=(2, 2, 512), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
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
                model.add(Dropout(0.5,))
                model.add(Dense(10))
                model.add(Activation('softmax'))

        return model
