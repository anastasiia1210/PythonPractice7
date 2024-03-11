import pandas as pd

def input_text():
    """
    Function to input text from the console.
    Returns:
        str: The text inputted from the console.
    """
    return input("Enter text: ")

def read_file():
    """
    Function to read from a file.
    Returns:
        str: The content read from the file.
    """
    try:
        with open("input_file.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return ""

def read_file_pandas():
    """
    Function to read from a file using Pandas.
    Returns:
        pandas.DataFrame: The data read from the file as a DataFrame, or None if file not found.
    """
    try:
        df = pd.read_csv("input_file.txt")
        return df
    except FileNotFoundError:
        print("File not found pandas.")
        return None

if __name__ == "__main__":
    pass
