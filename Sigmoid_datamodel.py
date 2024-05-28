import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import accuracy_score

# Reading thee csv file
gdata = pd.read_csv('SampleData.csv', header= 0)
# Shuffling the data rows of csv
shuffled_data = gdata.sample(frac=1).reset_index(drop=True)

# Assign the first three columns to x
x = shuffled_data.iloc[:, :3]

# Assign the fourth column to y
y = shuffled_data.iloc[:, 3]

SAMPLEDATA=10000

# Splitting data as 60% training, 20% each for test and validation 
Train_split=int(0.6*SAMPLEDATA)
Test_split=int(0.2*SAMPLEDATA+Train_split)

x_train,x_validate,x_test=np.split(x,[Train_split,Test_split])
y_train,y_validate,y_test=np.split(y,[Train_split,Test_split])

# Declaring the model
model_1=Sequential()
model_1.add(Dense(16,activation='sigmoid',input_shape=(3,))) # Input layer and first layer
model_1.add(Dense(5)) # Output layer
model_1.compile(optimizer='rmsprop',loss='mse',metrics=['mae']) # Declaring the data model paramaters
model_1.summary()

# Model training on training data ans validating on validation data
history_1= model_1.fit(x_train,y_train ,epochs=1000,batch_size=10,validation_data=(x_validate,y_validate))

# Extract the loss values for training and validation data from the history
training_loss = history_1.history['loss']
validation_loss = history_1.history['val_loss']

# Creating a plot to visualize training and validation loss
epochs_loss = range(1, len(training_loss) + 1)
plt.plot(epochs_loss, training_loss, 'r.',alpha=0.2, label='Training Loss')
plt.plot(epochs_loss, validation_loss, 'b.',alpha=0.5, label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Extract the loss values for training and validation data from the history
mae=history_1.history['mae']
val_mae=history_1.history['val_mae']

# Creating a plot to visualize training and validation loss
epochs_mae = range(1, len(mae) + 1)
plt.plot(epochs_mae, mae, 'r.',alpha=0.2, label='Training MAE')
plt.plot(epochs_mae, val_mae, 'b.',alpha=0.5, label='Validation MAE')
plt.title('Training and Validation MAE')
plt.xlabel('Epochs')
plt.ylabel('MAE')
plt.legend()
plt.show()

# Prediction on test data
predictions=model_1.predict(x_test)
y_pred_classes=list()
for i in range(len(predictions)):
    rval=int(np.round(max(predictions[i])))
    if rval == 0:rval=1
    if rval == 6:rval=5
    y_pred_classes.append(rval)

# Accuracy calcuation of the the test model
accuracy = accuracy_score(y_test, y_pred_classes)
print(f'Test Accuracy: {accuracy}')

# Plotting the prediction vs y_test values for x_test data
plt.clf()
plt.title('Predict vs Actual')
plt.plot(x_test, y_test,'b*',alpha=0.2,label='Actual')
plt.plot(x_test, y_pred_classes,'r.',alpha=0.5,label='Predict')
plt.legend()
plt.show()