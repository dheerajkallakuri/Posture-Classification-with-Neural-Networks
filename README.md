# Posture Classification using Machine Learning

## Overview

This project extends the work done in the previous lying posture tracking project by incorporating more classes, collecting additional data, and designing a machine learning algorithm for posture classification. The goal is to build and evaluate a machine learning model offline using collected IMU sensor data, focusing on five postures: supine, prone, side (either right or left side), sitting, and an unknown posture.

## Project Phases

### Phase 1: Reading IMU Sensor Data
Run `readData.ino` code to read the IMU sensor data from the Arduino board and store the signal readings.

### Phase 2: Data Collection
Run `readData.py` to collect data for different scenarios by simulating various postures without actually wearing the board. Ensure to collect data for each posture in multiple orientations to ensure robustness.

### Phase 3: Dataset Construction
Create `SampleData.csv` combination of all postures dataset from the collected data and split it into training, validation, and test sets.

### Phase 4: Model Architecture Selection
Decide on a neural network architecture to train your model for posture classification. Consider architectures suitable for processing sequential data.

### Phase 5: Model Training and Evaluation
Train your chosen neural network model on the training data and evaluate its performance using the validation set. Make adjustments to the architecture and dataset as needed to prevent overfitting or underfitting.

### Phase 6: Testing
Test your final model on the test dataset to assess its performance and generalization capabilities.

## Robustness Considerations

- Ensure that the model is insensitive to changes in sensor orientations by collecting data with various orientations representing the same posture.
- Label signals with the same class label for similar postures in different orientations (e.g., 'side' for both right and left side lying).
- Make assumptions about possible ways the sensor unit can be worn and discuss these assumptions, operating points, and corner cases in the project report.

## Results
1. Activation function: ReLU<br>
Layers: 3 inputs, 16 neurons in the first layer, and 5 neurons in the second layer(output).<br>
Test accuracy for this model on test data was about 99.55% and the validation loss was about 0.0018.<br>
<img width="535" alt="r1" src="https://github.com/dheerajkallakuri/Posture-Classification-with-Neural-Networks/assets/23552796/9e0b8bd7-7419-48d6-974d-3a0ac95f673b"><br>

2. Activation function: ReLU<br>
Layers: 3 inputs, 16 neurons in the first layer, 16 neurons in 2nd layer, and 5 neurons in the third layer(output).<br>
Test accuracy for this model on test data was about 99.89% and the validation loss was about 7.2*10-5.<br>
<img width="530" alt="r2" src="https://github.com/dheerajkallakuri/Posture-Classification-with-Neural-Networks/assets/23552796/214aeb51-9f92-4582-9947-76a4d223a716"><br>
This model was overfitting<br>

3. Activation function: ReLU<br>
Layers: 3 inputs, 16 neurons in the first layer, 8 neurons in 2nd layer, and 5 neurons in the third layer(output).<br>
Test accuracy for this model on test data was about 99.89% and the validation loss was about 0.0011.<br>
<img width="540" alt="r3" src="https://github.com/dheerajkallakuri/Posture-Classification-with-Neural-Networks/assets/23552796/65a12acd-ce4b-44d0-97e9-ef513cec45f6"><br>

4. Activation function: Sigmoid<br>
Layers: 3 inputs, 16 neurons in the first layer, and 5 neurons in the second layer(output).<br>
Test accuracy for this model on test data was about 99.79% and the validation loss was about 0.0023.<br>
<img width="537" alt="r4" src="https://github.com/dheerajkallakuri/Posture-Classification-with-Neural-Networks/assets/23552796/33a0bda2-3e85-4d99-a569-7968d13df46d"><br>

5. Activation function: Tanh<br>
Layers: 3 inputs, 16 neurons in the first layer, and 5 neurons in the second layer(output).<br>
Test accuracy for this model on test data was about 99.69% and the validation loss was about 0.0034.<br>
<img width="652" alt="r5" src="https://github.com/dheerajkallakuri/Posture-Classification-with-Neural-Networks/assets/23552796/76b9a987-f8e9-4140-a2b8-923522c0c8c4"><br>








