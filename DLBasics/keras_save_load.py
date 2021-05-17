#Saving a Keras model:

model = ...  # Get model (Sequential, Functional Model, or Model subclass)
model.save('path/to/location')


#Loading the model back 
from tensorflow import keras
model = keras.models.load_model('path/to/location')

