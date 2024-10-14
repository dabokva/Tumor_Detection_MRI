import os
import pickle
import pandas as pd
from keras.models import load_model

def save_data(object, category, file_path):

    with open('..\\save_files\\saved_data.pkl', 'rb') as file:
        saved_data = pickle.load(file)

    if file_path in saved_data['path'].values:
        with open(file_path, 'wb') as file:
            pickle.dump(object, file)
        with open('..\\save_files\\saved_data.pkl', 'wb') as file:
            pickle.dump(saved_data, file)
        print(f'object successfully saved to: {file_path}.')
    else:
        saved_data = pd.concat([saved_data, pd.DataFrame({'path': [file_path], 'object':[object], 'category':[category]})], ignore_index=True)
        with open(file_path, 'wb') as file:
            pickle.dump(object, file)
        with open('..\\save_files\\saved_data.pkl', 'wb') as file:
            pickle.dump(saved_data, file)
        print(f'object successfully saved to: {file_path}.')

def load_data(file_path):

    with open('..\\save_files\\saved_data.pkl', 'rb') as file:
        saved_data = pickle.load(file)

    if file_path in saved_data['path'].values:
        with open(file_path, 'rb') as file:
            result = pickle.load(file)
            print(f'the object from {file_path} has been successfully loaded.')
            return result
    else:
        print(f"error: no such file with given path - {file_path}.")
        return None
    

def load_ml_model(file_path):
    
    if os.path.exists(file_path):
        model = load_model(file_path)
        print(f'the model from {file_path} has been successfully loaded.')
        return model
    else:
        print(f"error: no such file with given path - {file_path}.")
        return None
