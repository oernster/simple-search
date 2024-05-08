import sys
import os
from collections import OrderedDict


class Main(object):
    def __init__(self, directory):
        self.directory = directory
        self.init()
        self.run()

    def init(self):
        self.num_files = 0
        self.sorted_dict = {}

    def read_files(directory):
        file_word_dicts = {}
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                word_dict = OrderedDict()
                with open(filepath, 'r') as file:
                    for line in file:
                        words = line.split()
                        for word in words:
                            first_letter = word[0].lower()
                            if first_letter in word_dict:
                                word_dict[first_letter].append(word)
                            else:
                                word_dict[first_letter] = [word]
                file_word_dicts[filename] = OrderedDict(sorted(word_dict.items()))
        return file_word_dicts

    def run(self):
        while True:
            self.init()
            self.search()
            self.display_results()

    def display_results(self):
        if len(self.sorted_dict.keys()) == 0:
            print("No matches found.")
        else:
            for k, v in self.sorted_dict.items():
                print(f"{v}: {k}%")
    
    def search(self):
        pc_dict = {}
        file_word_dicts = self.read_files(self.directory)
        search_list = str(input("search>")).split(' ')
        if search_list == ':quit':
            sys.exit(1)
        cnt = 0
        for filename, word_dict in file_word_dicts.items():
            for key, value in word_dict.items():
                for sl in search_list:
                    if sl[:1] == key:
                        for v in value:
                            if sl == value:
                                cnt += 1
            pc = int((cnt / len(search_list)) * 100)
            if pc != 0:
                pc_dict[pc] = f"{filename}"
        
        # do for each filename rank
        sorted_keys = sorted(pc_dict.keys())
        self.sorted_dict = {key: pc_dict[key] for key in sorted_keys}




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python <filename> <pathToDirectoryContainingTextFiles> ")
        sys.exit(1)
   
    directory_path = sys.argv[1]
    m = Main(directory_path)
