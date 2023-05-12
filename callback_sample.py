def func_callback(c):
    print("File Length : ", c)

def file_len(filepath, callback):
    i = open(filepath, "r")
    file_length = len(i.read())
    i.close()
    callback(file_length)

if __name__ == '__main__':
    file_len("test.py", func_callback)
