
# typer to tools

a cli that reads your python files and generates a tool array for your openai assistants


## Example

![example](https://github.com/bramses/typer-to-tools/assets/3282661/3c43c8f9-c992-4eb1-bb8e-2fd6e554c35e)

```
(typer-to-tools-py3.9) (base) bram@Brams-Macbook typer-to-tools % python main.py
[?] Select a file: test.py
 > test.py
   main.py

Function 'fib': Skip or Edit?: edit
Description for the function: run fib on a number
Description for parameter 'n': start number
Is the param 'n' required? [y/N]: y
Function 'mergesort': Skip or Edit?: edit
Description for the function: sort a list
Description for parameter 'arr': unsorted arr
Is the param 'arr' required? [y/N]: y
Function 'tomorrow': Skip or Edit?: edit
Description for the function: get tomorrows date
Function 'validate': Skip or Edit?: edit
Description for the function: validate user name and email
Description for parameter 'username': your login id
Is the param 'username' required? [y/N]: y
Description for parameter 'email': your email addr
Is the param 'email' required? [y/N]: n
[
  {
    "type": "function",
    "function": {
      "name": "fib",
      "description": "run fib on a number",
      "parameters": {
        "type": "object",
        "properties": {
          "n": {
            "type": "number",
            "description": "start number"
          }
        },
        "required": [
          "n"
        ]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "mergesort",
      "description": "sort a list",
      "parameters": {
        "type": "object",
        "properties": {
          "arr": {
            "type": "string",
            "description": "unsorted arr"
          }
        },
        "required": [
          "arr"
        ]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "tomorrow",
      "description": "get tomorrows date",
      "parameters": {
        "type": "object",
        "properties": {}
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "validate",
      "description": "validate user name and email",
      "parameters": {
        "type": "object",
        "properties": {
          "username": {
            "type": "string",
            "description": "your login id"
          },
          "email": {
            "type": "string",
            "description": "your email addr"
          }
        },
        "required": [
          "username"
        ]
      }
    }
  }
]
```
