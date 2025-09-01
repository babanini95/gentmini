import os


def get_files_info(working_directory, directory="."):
    abs_full_path = os.path.abspath(os.path.join(working_directory, directory))
    abs_working_directory = os.path.abspath(working_directory)

    if (
        os.path.commonpath([abs_working_directory, abs_full_path])
        != abs_working_directory
    ):
        return f'   Error: Cannot list "{directory}" as it is outside the permitted working directory\n'

    if not os.path.isdir(abs_full_path):
        return f'   Error: "{directory}" is not a directory\n'

    files_info = ""
    try:
        for path in os.listdir(abs_full_path):
            abs_path = os.path.join(abs_full_path, path)
            files_info += f"    - {path}: file_size={os.path.getsize(abs_path)}, is_dir={os.path.isdir(abs_path)}\n"
    except OSError as e:
        return f"   Error: {e}\n"

    return files_info
