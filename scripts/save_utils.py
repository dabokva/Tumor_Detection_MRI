import pickle

def save_data(file_path, *variables):
    try:
        with open(file_path, 'wb') as file:
            if len(variables) == 1:
                pickle.dump(variables[0], file)
            else:
                pickle.dump(variables, file)
        print(f"All variables have been successfully saved to {file_path}.")
    except Exception as e:
        print(f"An error occurred while saving data: {e}")

def load_data(file_path):
    try:
        with open(file_path, 'rb') as file:
            variables = pickle.load(file)
            return variables
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return None