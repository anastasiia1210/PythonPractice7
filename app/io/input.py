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
    with open("app/io/input_file.txt", "r") as file:
        return file.read()

def read_file_pandas():
    """
        Function to read text from a file using pandas.
        Returns:
            str: The text read from the file.
    """
    text = pd.read_csv("app/io/input_file.txt", sep='\t', header=None)
    text_str = text.to_string(index=False, header=False)
    return text_str

if __name__ == "__main__":
    pass