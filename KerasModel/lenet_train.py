# -*- coding: utf-8 -*-
"""LeNet_train.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jg2Gsrf4ykveOXGshlgsZdNN4jaxeKnR
"""

!git clone https://github.com/worldstar/ultrasoundSoundAugmentation.git

!wget https://github.com/OlafenwaMoses/IdenProf/releases/download/v1.0/idenprof-jpg.zip
!unzip -qq idenprof-jpg.zip

from ultrasoundSoundAugmentation.core.CustomDataGenerator import CustomDataGenerator
from ultrasoundSoundAugmentation.core.Model.LeNet_Functional_Model import buildLeNetModel
# from ultrasoundSoundAugmentation.core.Model.LeNet_Sequential_Model import buildLeNetModel

# 影像大小
inputs=(256,256,3)

# 若 GPU 記憶體不足，可調降 batch size 或凍結更多層網路
batch_size=32

# Epoch 數
epochs=10

# 影像類別數
num_classes = 10

# log_dir="./model/"

#選擇資料增強的方法
datagen=CustomDataGenerator(fun="Opening_operation",kernel=10,dtype=int)

train_generator = datagen.flow_from_directory(
    './idenprof/train',
    target_size=(256, 256),
    batch_size=32,
    class_mode='categorical')

val_generator = datagen.flow_from_directory(
        './idenprof/test',
        target_size=(256, 256),
        batch_size=32,
        class_mode='categorical')

model = buildLeNetModel(inputs, num_classes)

# checkpoint = ModelCheckpoint(log_dir + "ep{epoch:03d}-loss{loss:.3f}-val_loss{val_loss:.3f}.h5",
#     monitor='val_loss', save_weights_only=True, save_best_only=True, period=1)

# callbacks_list = [checkpoint]

model.fit_generator(
      train_generator,
      steps_per_epoch=10,
      epochs=epochs,
      validation_data=val_generator,
      validation_steps=10
      # ,callbacks=[callbacks_list]
      )