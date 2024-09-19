import pickle
import pandas as pd

def save_data(object, category, file_path):

    with open('..\\save_files\\saved_data.pkl', 'rb') as file:
        saved_data = pickle.load(file)

    if file_path in saved_data['path'].values:
        with open(file_path, 'wb') as file:
            pickle.dump(object, file)
        with open('..\\save_files\\saved_data.pkl', 'wb') as file:
            pickle.dump(saved_data, file)
        print(f'object successfuly saved to: {file_path}')
    else:
        saved_data = pd.concat([saved_data, pd.DataFrame({'path': [file_path], 'object':[object], 'category':[category]})], ignore_index=True)
        with open(file_path, 'wb') as file:
            pickle.dump(object, file)
        with open('..\\save_files\\saved_data.pkl', 'wb') as file:
            pickle.dump(saved_data, file)
        print(f'object successfuly saved to: {file_path}')

def load_data(file_path):

    with open('..\\save_files\\saved_data.pkl', 'rb') as file:
        saved_data = pickle.load(file)

    if file_path in saved_data['path'].values:
        with open(file_path, 'rb') as file:
            result = pickle.load(file)
            return result
    else:
        print('error: no such file')
        return None


