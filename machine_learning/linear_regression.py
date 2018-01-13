import tensorflow as tf
import numpy
from matplotlib import pyplot as plt

x_train = [1, 2, 3]
y_train = [1, 2, 3]

x_train_placeholder = tf.placeholder(tf.float32)
y_train_placeholder = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1], name='bias'))

hypothesis = x_train * W + b

cost = tf.reduce_mean(tf.square(hypothesis - y_train))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

with tf.Session()as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        sess.run(train)
        if step % 50 == 0:
            print(step, sess.run(cost), sess.run(W), sess.run(b))

    print('\n--------------------------\n')

    for steps in range(10001):
        cost_val, W_val, b_val, _ = sess.run([cost, W, b, train],
                                             feed_dict={x_train_placeholder: [1, 2, 3], y_train_placeholder: [1, 2, 3]})

        if steps % 50 == 0:
            print(steps, cost_val, W_val, b_val)
