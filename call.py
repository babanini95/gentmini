import config
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

function_dict = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file": write_file,
    "run_python_file": run_python_file,
}


def call_function(function_call_part: types.FunctionCall, verbose=False):
    function_name = function_call_part.name
    args = function_call_part.args
    if verbose:
        print(
            f" - Calling function: {function_call_part.name}({function_call_part.args})"
        )
    else:
        print(f" - Calling function: {function_call_part.name}")

    content = types.Content(role="tool")
    function_to_call = function_dict.get(function_call_part.name)

    if function_to_call == None:
        content.parts = [
            types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"},
            )
        ]
        return content

    result = function_to_call(config.WORKING_DIRECTORY, **args)
    content.parts = [
        types.Part.from_function_response(
            name=function_name, response={"result": result}
        )
    ]
    return content
