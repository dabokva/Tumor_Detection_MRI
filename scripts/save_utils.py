import os
import pickle

default_value = 0

def save_data(file_path, *variables):
    try:
        with open(file_path, 'wb') as file:
            if len(variables) == 1:
                pickle.dump(variables[0], file)
            else:
                pickle.dump(variables, file)
        print(f"all variables have been successfully saved to {file_path}.")
    except Exception as e:
        print(f"an error occurred while saving data: {e}")

def loader(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'rb') as file:
                variables = pickle.load(file)
                return variables
        except Exception as e:
            print(f"an error occurred while loading data: {e}")
            return default_value
    else:
        print(f'file not found: {file_path}')
        return default_value