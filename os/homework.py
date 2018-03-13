import os
def find(keyword, path = '.'):
    for x in os.listdir(path):
        sub_path = os.path.join(path, x)
        if os.path.isdir(sub_path):
            find(keyword, sub_path)
        else:
            if keyword in x:
                print(sub_path)
if __name__ == ' __main__':
    find('homework')