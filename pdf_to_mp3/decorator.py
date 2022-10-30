def text_decorator(input_func):    
    def output_func(*args):
        print("*" * 50)
        print("*" * 50)
        input_func(*args)
        print("*" * 50)
        print("*" * 50)
    return output_func

@text_decorator
def print_text(text):
    count = (50 - len(text)) // 2
    output = "*" * count + text + "*" * count
    while len(output) < 50:
        output += "*" 
    print(output)