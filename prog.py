from keras.datasets import mnist
import cv2
from keras.models import Sequential
from keras.layers import Dense
from keras.layers.convolutional import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
import os
from keras.optimizers import RMSprop
from keras.utils.np_utils import to_categorical

dataset = mnist.load_data('mymnist.db')

train , test = dataset

X_train , y_train = train

X_test , y_test = test

X_train_1d = X_train.reshape(-1 , 28*28)
X_test_1d = X_test.reshape(-1 , 28*28)

X_train = X_train_1d.astype('float32')
X_test = X_test_1d.astype('float32')
if(os.environ['trial']>='2'):
 X_train = X_train.reshape(-1,28,28,1)
 X_test = X_test.reshape(-1,28,28,1)

from keras.utils.np_utils import to_categorical

y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)

model = Sequential()
if(os.environ['trial']=='1'):
 model.add(Dense(units=512, input_dim=28*28, activation='relu'))
 model.add(Dense(units=256, activation='relu'))
 model.add(Dense(units=10, activation='softmax'))

if(os.environ['trial']>='2'):
 model.add(Conv2D(32,(3,3),input_shape = (28,28,1),activation = 'relu'))
 model.add(MaxPooling2D(pool_size=(6,6)))
 model.add(Flatten())
if(os.environ['trial']>='3'):
 model.add(Dense(units=256, activation='relu'))

model.add(Dense(units=10, activation='softmax'))


model.compile(optimizer='adam', loss='categorical_crossentropy', 
             metrics=['accuracy']
             )

h = model.fit(X_train, y_train_cat,batch_size=512,epochs=1)
test_loss, test_acc = model.evaluate(X_test, y_test_cat)
print(test_acc)
with open('Output.txt', 'x') as f:
  print(test_acc, file=f)
model.save("digit.h5")
