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
def weight_load():
    # get weight
    temp_model = Sequential()
    # layer1 32*32*3
    temp_model = Sequential()
    temp_model.add(Conv2D(64, (3, 3), padding='same',
                 input_shape=(32, 32, 3), kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    temp_model.add(Dropout(0.3))
    # layer2 32*32*64
    temp_model.add(Conv2D(64, (3, 3), padding='same',         kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    temp_model.add(MaxPooling2D(pool_size=(2, 2)))
    # layer3 16*16*64
    temp_model.add(Conv2D(128, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    temp_model.add(Dropout(0.4))
    # layer4 16*16*128
    temp_model.add(Conv2D(128, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    temp_model.add(MaxPooling2D(pool_size=(2, 2)))
    # layer5 8*8*128
    temp_model.add(Conv2D(256, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    temp_model.add(Dropout(0.4))
    # layer6 8*8*256
    temp_model.add(Conv2D(256, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    temp_model.add(Dropout(0.4))
    # layer7 8*8*256
    temp_model.add(Conv2D(256, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    temp_model.add(MaxPooling2D(pool_size=(2, 2)))
    # layer8 4*4*256
    temp_model.add(Conv2D(512, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    temp_model.add(Dropout(0.4))
    # layer9 4*4*512
    temp_model.add(Conv2D(512, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    temp_model.add(Dropout(0.4))
    # layer10 4*4*512
    temp_model.add(Conv2D(512, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    temp_model.add(MaxPooling2D(pool_size=(2, 2)))
    # layer11 2*2*512
    temp_model.add(Conv2D(512, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    temp_model.add(Dropout(0.4))
    # layer12 2*2*512
    temp_model.add(Conv2D(512, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    temp_model.add(Dropout(0.4))
    # layer13 2*2*512
    temp_model.add(Conv2D(512, (3, 3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    temp_model.add(MaxPooling2D(pool_size=(2, 2)))
    temp_model.add(Dropout(0.5))
    # layer14 1*1*512
    temp_model.add(Flatten())
    temp_model.add(Dense(512, kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    # layer15 512
    temp_model.add(Dense(512, kernel_regularizer=regularizers.l2(weight_decay)))
    temp_model.add(Activation('relu'))
    temp_model.add(BatchNormalization())
    # layer16 512
    temp_model.add(Dropout(0.5))
    temp_model.add(Dense(10))
    temp_model.add(Activation('softmax'))
    temp_model.load_weights('/home/inter-intra/ns-allinone-3.30/ns-3.30/examples/tutorial/VGG16_cifar_weight')
    temp_weight = temp_model.get_weights()
    return temp_weight



