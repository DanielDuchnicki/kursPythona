import os
import os.path


def przegladanie(root, file_dictionary):
    file_list = os.listdir(root)
    dir_list = []
    for item in file_list:
        if os.path.isfile(os.path.join(root, item)):
            full_name = os.path.join(root, item)
            file_size = os.path.getsize(full_name)
            if file_size in file_dictionary:
                file_dictionary[file_size].append(full_name)
            else:
                file_dictionary[file_size] = [full_name]
            print(full_name, file_size)

        if os.path.isdir(os.path.join(root, item)):
            dir_list.append(item)
    for dirname in dir_list:
        przegladanie(os.path.join(root, dirname), file_dictionary)

    file_dictionary_keys = list(file_dictionary.keys())
    file_dictionary_keys.sort()
    file_dictionary_sorted = {}
    for key in file_dictionary_keys:
        file_dictionary_sorted[key] = file_dictionary[key]
    return file_dictionary_sorted


def znajdz_pliki_o_tym_samym_rozmiarze(file_dictionary):
    for key in file_dictionary:
        if len(file_dictionary[key]) > 1:
            print("Pliki o tym samym rozmiarze to: ")
            print("Rozmiar: " + str(key))
            for item in files_dictionary[key]:
                print(item)


files_dictionary = {}
przegladanie('.', files_dictionary)
print(files_dictionary)
znajdz_pliki_o_tym_samym_rozmiarze(files_dictionary)
