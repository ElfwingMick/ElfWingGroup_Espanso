import os
    
def main():
    try:
        myvar = os.environ['ESPANSO_MYVAR']
    except Exception as e:
        print( f'【Input Error: {str(e)}】')
        return
    input_str = myvar
    input_num = float(input_str)
    result = input_num * 0.03
    result = "{:.2f}".format(result)
    result = str(result)

    print(result)


if __name__ == "__main__":
    main()