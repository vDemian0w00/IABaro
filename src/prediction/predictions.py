import math
import pandas_datareader as web
import numpy as np
import pandas as pd
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt 
plt.style.use('fivethirtyeight')

# Dataframe
df=pd.read_csv('PRUEBA.csv')

# Create a dataframe with only the close column
data=df.filter(['Monto'])
# Convert the dataframe to a numpy array
dataset=data.values
# print('ETOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
# print(dataset)
# Get the number of rows to train the model on
training_data_len=math.ceil(len(dataset)*.8)
# print('TRAINIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIING')
# print(training_data_len)

# print(training_data_len)

# Scale the data
scaler=MinMaxScaler(feature_range=(0,1))
scaled_data=scaler.fit_transform(dataset)


# print(scaled_data)

# Create the training data
# Create the scaled train data
train_data=scaled_data[0:training_data_len, :]

x_train=[]
y_train=[]

for x in range(60, len(train_data)):
    x_train.append(train_data[x-60:x, 0])
    y_train.append(train_data[x, 0])
    print('ETO'+str(x))
    print(train_data[x-60:x, 0])
    print(train_data[x, 0])
    # if x<=60:
    #     print(x_train)
    #     print(y_train)
    #     print()

# Convert the data into numpy arrays
x_train, y_train=np.array(x_train), np.array(y_train)

# Reshape the data
x_train=np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_train.shape

# Build the LSTM model
model=Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1],1)))
model.add(LSTM(50, return_sequences=False)) 
model.add(Dense(25))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, batch_size=1, epochs=1)

# Create a new array containing scaled values from index 1543 to 2003
test_data=scaled_data[training_data_len-60:, :]

# Create the datasets x_test and y_test
x_test=[]
y_test=dataset[training_data_len:, :]
for x in range(60, len(test_data)):
    x_test.append(test_data[x-60:x, 0])

# Convert the data to a numpy array
x_test=np.array(x_test)

# Reshape the data
x_test=np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# Get the models predicted price values
predictions=model.predict(x_test)
predictions=scaler.inverse_transform(predictions)

print('AQUIEEEEFMEWFEWFwDADJKNAJDAWBJNUD PENDEJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
print(predictions-y_test)

# Get the root mean squared error (RMSE)
rmse=np.sqrt(np.mean(predictions-y_test)**2)
# print(rmse)

# Plot the data
train=data[:training_data_len]
valid=data[training_data_len:]
valid['Predictions']=predictions
print('*****************************************************************')
print(predictions)
print('*****************************************************************')

# Visualize the data
plt.figure(figsize=(16,8))
plt.title('Model Amazon')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Gasto', fontsize=18)
plt.plot(train['Monto'])
plt.plot(valid[['Monto', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='upper left')
plt.show()

# Predicted values
print(valid)