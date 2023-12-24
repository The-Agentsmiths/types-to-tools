
# typer to tools

a cli that reads your python files and generates a tool array for your openai assistants


## Example

```
$ python main.py
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
```

results in:

```json
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


## In the OpenAI Assistants Playground

![Screenshot 2023-12-24 18-45-55](https://github.com/The-Agentsmiths/typer-to-tools/assets/3282661/487606b6-6be3-4a2d-865e-66324c96e951)

