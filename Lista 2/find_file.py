import os

def find(path, filename):
    found = []
    if not os.path.exists(path):
        return found
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path) and entry == filename:
            found.append(full_path)
        elif os.path.isdir(full_path):
            found.extend(find(full_path, filename))

    return found

res = find("/Users/muszka/PycharmProjects/Algorytmy-i-struktury-danych/Lista 2/folder_find", "text.rtf")
for r in res:
    print(r)