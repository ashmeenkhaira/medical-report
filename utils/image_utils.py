import tensorflow as tf
import numpy as np
from PIL import Image

IMG_SIZE = 224

def preprocess_image(image_file):
    """
    image_file: Uploaded file from Streamlit
    returns: (1, 224, 224, 3) float32 tensor
    """
    image = Image.open(image_file).convert("RGB")
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.array(image) / 255.0
    image = image.astype("float32")
    return tf.expand_dims(image, axis=0)
