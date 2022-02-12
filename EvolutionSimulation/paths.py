from os import path

class Paths:
    CURRENT = path.dirname(__file__)
    MAPS = path.join(CURRENT, "maps")
    TEXT = path.join(CURRENT, "assets/text")

    def read_text(file_path):
        file = open(file_path, "r")
        data = file.read()
        file.close()
        return data
    
    def write_text(file_path, data):
        with open(file_path, "w") as f:
            f.write(data)