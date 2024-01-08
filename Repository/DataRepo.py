import os
import pickle

class DataRepo:
    def __init__(self, filename):
        self.filename = filename

    def save(self, list):
        file = open(self.filename, 'wb')
        pickle.dump(list, file)
        file.close()

    def load(self):
        if os.path.isfile(self.filename):
            file = open(self.filename, 'rb')
            elems = pickle.load(file)
            if not(type(elems) == list):
                elems=[elems]
            file.close()
        else:
            elems=[]
        return elems

    def readfile(self):
        file = open(self.filename, 'rb')
        content = file.read()
        return content

    def write_to_file(self, string):
        f = open(self.filename, 'wb')
        f.write(string)
        f.close()

    def convert_to_string(self, list):
        pass

    def convert_from_string(self, string):
        pass




