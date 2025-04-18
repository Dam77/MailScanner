def read_txt(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
        return content

