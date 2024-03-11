def output_text(text):
    """
    Function to print text to the console.
    Args:
        text (str): The text to be printed to the console.
    """
    print(text)

def write_file(data, file):
    """
    Function to write data to a file.
    Args:
        data: The data to be written to the file.
        file (str): The name of the file to write to.
    """
    try:
        with open(file, "w") as f:
            f.write(data)
        print(f"Data written to file '{file}' successfully.")
    except Exception as e:
        print(f"Error writing data to file: {e}")

if __name__ == "__main__":
    pass
