import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    if args == None:
        args = []

    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))

    if (
        os.path.commonpath([abs_working_directory, abs_file_path])
        != abs_working_directory
    ):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            ["python3", abs_file_path, *args],
            timeout=30,
            capture_output=True,
            text=True,
        )

        output_str = f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}\n"
        if result.returncode != 0:
            output_str += f"Process exited with code {result.returncode}\n"
        if result.stdout == None:
            output_str += "No output produced.\n"
    except subprocess.SubprocessError as e:
        return f"Error: executing Python file: {e}"

    return output_str
