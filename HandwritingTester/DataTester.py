import numpy as np
import theano as th

#Need to tweak backend using this fix: https://github.com/keras-team/keras/issues/13684

np.random.seed(123)

from matplotlib import pyplot as plt

from keras.models import Sequential

from keras.layers import Dense, Dropout, Activation, Flatten, Convolution2D, MaxPooling2D

from keras.utils import np_utils

from keras.datasets import mnist


def test1():
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
    X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    X_train /= 255
    X_test /= 255
    Y_train = np_utils.to_categorical(y_train, 10)
    Y_test = np_utils.to_categorical(y_test, 10)

    model = Sequential()
    
    model.add(Convolution2D(32, (3, 3), activation='relu', input_shape=(1, 28, 28), data_format= 'channels_first'))
    model.add(Convolution2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation='softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    # 9. Fit model on training data
    model.fit(X_train, Y_train,
              batch_size=32, nb_epoch=10, verbose=1)

    # 10. Evaluate model on test data
    score = model.evaluate(X_test, Y_test, verbose=0)

    print(score)


