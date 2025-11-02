import os

def find(path, filename):
    file_paths = []
    for entry in os.listdir(path):
        new_path = os.path.join(path, entry)
        if os.path.isfile(new_path) and entry == filename:
            file_paths.append(new_path)
            #print("returning file", len(file_paths), new_path)
        elif os.path.isdir(new_path):
            file_paths += find(new_path, filename)
            #print("returning folder", len(file_paths), new_path)
    return file_paths

starting_path = "/Users/muszka/PycharmProjects/Algorytmy-i-struktury-danych/Lista 2/folder_find"
if not os.path.exists(starting_path):
    print("starting path not found")
else:
    res = find(starting_path, "text.rtf")
    print("FOUND FILES:")
    for r in res:
        print(r)