import tensorflow as tf
import os
from tensorflow import keras
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Activation , Dropout , Conv2D, MaxPooling2D, Dense, Flatten

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
model.add(Dense(units = 256, activation = "relu"))
model.add(Dropout(0.2))
model.add(Dense(units = 128, activation = "relu"))
model.add(Dropout(0.2))
model.add(Dense(units = 1, activation = "sigmoid"))
model.summary()

train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
  rescale = 1. / 255, 
  rotation_range = 30,  
  zoom_range = 0.15,  
  width_shift_range = 0.10,  
  height_shift_range = 0.10,  
  horizontal_flip = True
)

training_set = train_datagen.flow_from_directory(
  directory = "huge",
  target_size = (64, 64),
  batch_size = 15,
  class_mode = "binary"
)

test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale = 1. / 255)

test_set = test_datagen.flow_from_directory(
  directory = "tmp",
  target_size = (64, 64),
  batch_size = 15,
  class_mode = "binary"
)

with tf.device("/GPU:0"):
  history = model.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ["accuracy"])
  model.fit(training_set, steps_per_epoch = 991//15, epochs = 30, validation_data = test_set, validation_steps = 296//15)

model.save("model.h5")
