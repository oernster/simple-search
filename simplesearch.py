import sys
import os
from collections import OrderedDict


class QuitSearch(Exception):
    pass


class SimpleSearch(object):
    def __init__(self, directory):
        self.directory = directory
        self.init()
        self.run()

    def init(self):
        self.num_files = 0
        self.sorted_dict = {}

    def read_files(self, directory):
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
            try:
                self.search()
                self.display_results()
            except QuitSearch:
                break
            
    def display_results(self):
        if len(self.sorted_dict.keys()) == 0:
            print("No matches found.")
        else:
            sorted_results = sorted(self.sorted_dict.items(), key=lambda x: int(x[1]), reverse=True)
            cnt = 0
            for filename, percentage in sorted_results:
                cnt += 1
                if cnt == 10:
                    break
                print(f"{filename}: {percentage}%")

    
    def search(self):
        pc_dict = {}
        self.sorted_dict.clear()  # Clearing sorted_dict at the beginning
        file_word_dicts = self.read_files(self.directory)
        source_data = input("search>")
        if source_data == ':quit':
            sys.exit(1)        
        search_list = str(source_data).split(' ')
        for filename, word_dict in file_word_dicts.items():
            matched_words = []
            for key, value in word_dict.items():
                for sl in search_list:
                    if sl[:1].lower() == key.lower():
                        for v in value:
                            if sl.lower() == v.lower():
                                matched_words.append(v.lower())
            if matched_words:  # Check if any matched words found
                pc = int((len(set(matched_words)) / len(set(search_list))) * 100)
                if pc != 0:
                    if pc > 100:
                        pc = 100
                    pc_dict[filename] = f"{pc}"
        sorted_values = sorted(pc_dict.values())
        self.sorted_dict.update({filename: value for filename, value in pc_dict.items()})


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python <filename> <pathToDirectoryContainingTextFiles> ")
        sys.exit(1)
   
    directory_path = sys.argv[1]
    m = SimpleSearch(directory_path)
