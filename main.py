import inspect
import json
import typer
from typing import List, Dict, Any
import os
import inquirer

def get_functions_from_file(filename: str) -> List:
    # logic to parse file and return a list of functions
    filename_without_ext = os.path.splitext(filename)[0]
    return [func for func in inspect.getmembers(__import__(filename_without_ext)) if inspect.isfunction(func[1])]

# https://chat.openai.com/share/ba42c1ef-c614-4caf-9d25-4a15afefedcc
def get_param_type(param):
    # Check if param has a type annotation
    if param.annotation != inspect._empty:
        param_type = str(param.annotation)
        
        # Check for common types and convert them
        if 'int' in param_type:
            return 'number'
        elif 'float' in param_type:
            return 'number'
        elif 'str' in param_type:
            return 'string'
        elif 'bool' in param_type:
            return 'boolean'
        elif 'list' in param_type:
            return 'array'
        elif 'dict' in param_type:
            return 'object'
        elif 'datetime.date' in param_type or 'datetime.datetime' in param_type:
            return 'date-time'
        # Add more type checks here if needed
        
        # Fallback for any other types
        return param_type
    else:
        # Default to string if no type annotation is provided
        return "string"

def main():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.py')]
    questions = [
        inquirer.List('file',
                    message="Select a file",
                    choices=files,
                ),
    ]
    answers = inquirer.prompt(questions)
    
    functions = get_functions_from_file(answers['file'])
    functions_info = []
    
    for func in functions:
        function_name = func[0]
        skip_or_edit = typer.prompt(f"Function '{function_name}': Skip or Edit?", type=str)

        if skip_or_edit.lower() == 'skip':
            continue

        description = typer.prompt("Description for the function", type=str)
        parameters = {
            "type": "object",
            "properties": {}
        }

        for param in inspect.signature(func[1]).parameters.values():
            param_name = param.name
            # if annotation is _empty, then it is not annotated, and use str as default
            param_type = get_param_type(param)
            param_desc = typer.prompt(f"Description for parameter '{param_name}'", type=str)
            is_required = typer.confirm(f"Is the param '{param_name}' required?", default=False)
            
            parameters["properties"][param_name] = {
                "type": param_type,
                "description": param_desc
            }

            if is_required:
                if 'required' not in parameters:
                    parameters['required'] = []
                parameters['required'].append(param_name)

        function_info = {
            "type": "function",
            "function": {
                "name": function_name,
                "description": description,
                "parameters": parameters
            }
        }

        functions_info.append(function_info)

    print(json.dumps(functions_info, indent=2))

if __name__ == "__main__":
    typer.run(main)
