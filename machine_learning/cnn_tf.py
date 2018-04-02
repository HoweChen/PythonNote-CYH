import tensorflow as tf
import numpy
from matplotlib import pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

data = input_data.read_data_sets("data/MNIST/", one_hot=True)

with tf.Session() as sess:
    print(type(data.test.images[:100]))
