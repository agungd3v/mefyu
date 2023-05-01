import tensorflow as tf
import os
from tensorflow import keras
from tensorflow.python.keras import layers, optimizers, Sequential
from tensorflow.python.keras.layers import Activation , Dropout , Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.python.keras.models import load_model
# from tensorflow.python.keras.utils import load_img, img_to_array
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = "relu"))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Flatten())
model.add(Dense(256, activation = "relu"))
model.add(Dropout(0.2))
model.add(Dense(128, activation = "relu"))
model.add(Dropout(0.2))
model.add(Dense(1, activation = "sigmoid"))
model.summary()

# print(model)

train_datagen = ImageDataGenerator(
  rescale = 1. / 255,
  rotation_range = 30,
  zoom_range = 0.15,
  width_shift_range = 0.10,
  height_shift_range = 0.10,
  horizontal_flip = True
)

test_datagen = ImageDataGenerator(rescale = 1. / 255)

training_set = train_datagen.flow_from_directory(
  directory = "huge", # load from directory
  target_size = (64, 64),
  batch_size = 15,
  class_mode = "binary"
)

test_set = test_datagen.flow_from_directory(
  directory = "huge", # load from directory
  target_size = (64, 64),
  batch_size = 15,
  class_mode = "binary"
)

with tf.device("/GPU:0"):
  history = model.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ["accuracy"])
  model.fit(training_set, steps_per_epoch = 991//15, epochs = 30, validation_data = test_set, validation_steps = 296//15)
  model.save("model.h5")
