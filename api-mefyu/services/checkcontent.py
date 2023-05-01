from pathlib import Path
import tensorflow as tf
from tensorflow.python.keras.models import load_model
import numpy as np

data_folder = Path("utils/")
file_to_open = data_folder / "model.h5"

def checkf(fsk):
  c = load_model(file_to_open)
  f = tf.keras.preprocessing.image.load_img(fsk, target_size = (64, 64))
  tensor = tf.keras.preprocessing.image.img_to_array(f)
  tensor = np.expand_dims(tensor, axis = 0)
  tensor /= 255.0

  p = c.predict(tensor)

  if p < .5: return "is meme"
  else: return "is not meme"
