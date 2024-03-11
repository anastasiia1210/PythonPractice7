from app.io.input import input_text, read_file, read_file_pandas
from app.io.output import output_text, write_file

def main():
    text_from_console = input_text()
    output_text("Text from console: " + text_from_console)
    write_file(text_from_console, "output_console.txt")

    file_content = read_file()
    if file_content is not None:
        output_text("Content read from file:\n" + file_content)
        write_file(file_content, "output_file.txt")
    else:
        output_text("File not found.")

    data = read_file_pandas()
    if data is not None:
        output_text("Data read from file using Pandas:\n")
        output_text(data.to_string())
        write_file(data, "output_file.txt")
    else:
        output_text("File not found.")

if __name__ == "__main__":
    main()
