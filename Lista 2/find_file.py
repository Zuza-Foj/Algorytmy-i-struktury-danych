import os

def find(path, filename):
    found = []
    if not os.path.exists(path):
        return found
    for enrty in os.listdir(path):
        full_path = os.path.join(path, enrty)
        if os.path.isfile(full_path) and entry == filename:
            found.append(full_path)
        elif os.path.isdir(full_path):
            found.extend(find(full_path, filename))

        return found

print(find("PycharmProjects/Algorytmy-i-struktury-danych/folder_find/text/test/text.rtf", "text"))