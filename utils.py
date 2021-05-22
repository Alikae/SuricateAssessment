import sys

def get_input(input_file, eof_allowed):
    try:
        if input_file == None:
            return input()
        else:
            line = input_file.readline()
            if len(line) == 0:
                raise EOFError
            return line
    except EOFError:
        if not eof_allowed:
            print("Unexpected EOF. Exiting.")
        sys.exit(0)

def bad_format(correct_format):
    print(f"Bad Formatting: line should be '{correct_format}'. Exiting.")
    sys.exit(1)

