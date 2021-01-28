from tensorflow.keras.layers import Conv2D, Dense, MaxPooling2D, concatenate, Flatten,Activation,Lambda,Add
from tensorflow.keras import Input, Model
from tensorflow.keras import backend as K
import numpy as np
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import SGD

def mish(x):
    return Lambda(lambda x: x*K.tanh(K.softplus(x)))(x)
 
def multi_input_model(img_height, img_width, img_channl,num_classes):

    input1_= Input(shape(img_height, img_width, img_channl), name='input1')
    input2_ = Input(shape(img_height, img_width, img_channl), name='input2')

    x1=Conv2D(32,(5,5),strides=(1,1),padding='valid',name='conv1')(input1_)
    x1=Activation(mish)(x1)
    x1=MaxPooling2D((2,2),strides=(2,2))(x1)
    x1=Conv2D(32,(5,5),strides=(1,1),padding='valid',name='conv2')(x1)
 
    x2 = Conv2D(32,(5,5),strides=(1,1),padding='valid',name='conv3')(input2_)
    x2=Activation(mish)(x2)
    x2=MaxPooling2D((2,2),strides=(2,2))(x2)
    x2=Conv2D(32,(5,5),strides=(1,1),padding='valid',name='conv4')(x2)

    x = Add()([x1, x2])
    x = Flatten()(x)

    x=Dense(150,activation=mish,name='fc1')(x)
    x=Dense(num_classes,activation='softmax')(x)
    output_ = Dense(num_classes, activation='sigmoid', name='output')(x)
 
    model = Model(inputs=[input1_, input2_], outputs=[output_])
    model.summary()

    model.compile(optimizer=SGD(lr=0.0001, momentum=0.9), loss='categorical_crossentropy',metrics=['accuracy'])


 
    return model
