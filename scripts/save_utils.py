import os
import pickle
import pandas as pd
import tensorflow as tf
from keras.models import load_model

# --- EXPERIMENTAL ---

# options = tf.saved_model.LoadOptions(experimental_io_device='/job:localhost')
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disables GPU

# --------------------


def save_data(object, category, file_path):

    with open('..\\save_files\\saved_data.pkl', 'rb') as file:
        saved_data = pickle.load(file)

    if file_path in saved_data['file_path'].values:
        with open(file_path, 'wb') as file:
            pickle.dump(object, file)
        with open('..\\save_files\\saved_data.pkl', 'wb') as file:
            pickle.dump(saved_data, file)
        print(f'object successfully saved to: {file_path}.')
    else:
        saved_data = pd.concat([saved_data, pd.DataFrame({'object':[object], 'category':[category], 'file_path': [file_path]})], ignore_index=True)
        with open(file_path, 'wb') as file:
            pickle.dump(object, file)
        with open('..\\save_files\\saved_data.pkl', 'wb') as file:
            pickle.dump(saved_data, file)
        print(f'object successfully saved to: {file_path}.')

def load_data(file_path):

    with open(r'..\save_files\saved_data.pkl', 'rb') as file: # changed \\ to \ and added r
        saved_data = pickle.load(file)

    if file_path in saved_data['file_path'].values:
        with open(file_path, 'rb') as file:
            result = pickle.load(file)
            print(f'the object from {file_path} has been successfully loaded.')
            return result
    else:
        print(f"error: no such file with given path - {file_path}.")
        return None
    

def load_ml_model(file_path):
    
    if os.path.exists(file_path):
        loaded_model = load_model(file_path, options=options)
        #model = load_model(file_path)
        print(f'the model from {file_path} has been successfully loaded.')
        return loaded_model
    else:
        print(f"error: no such file with given path - {file_path}.")
        return None