import os
import re

def calculate_expression(input_str):
    # Validate the input using regular expression
    pattern = re.compile(r'[^0-9+\-*/().]')
    if pattern.search(input_str):
        return "Invalid input"

    try:
        # Use eval to calculate the result
        result = eval(input_str)
        return result
    except ZeroDivisionError:
        return "Division by zero error"
    except Exception as e:
        return f"Error: {str(e)}"
    
def main():
    try:
        myvar = os.environ['ESPANSO_MYVAR']
    except Exception as e:
        print( f'【Input Error: {str(e)}】')
        return
    input_str = myvar

    # Calculate and print the result
    output = calculate_expression(input_str)
    result = "{:,.2f}".format(round(output, 2))
    print(result)


if __name__ == "__main__":
    main()
    
