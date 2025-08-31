import os


def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.join(abs_working_directory, file_path)
    abs_file_dir = os.path.dirname(abs_file_path)

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    try:
        if not os.path.exists(abs_file_dir):
            os.makedirs(abs_file_dir)

        with open(abs_file_path, "w") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except EOFError as e:
        return f"Error: {e}"
