from app.io.input import input_text, read_file, read_file_pandas
from app.io.output import output_text, write_file

def main():
    text_from_console = input_text()
    output_text("From console: " + text_from_console)
    write_file(text_from_console, "output_console.txt")

    file_content = read_file()
    output_text("From file: " + file_content)
    write_file(file_content, "output_file.txt")

    data = read_file_pandas()
    output_text("From file using Pandas: " + data)
    write_file(data, "output_file.txt")


if __name__ == "__main__":
    main()
