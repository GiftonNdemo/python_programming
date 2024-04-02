import os

def search_files(directory, phrase):
    files_found = []
    for filename in os.listdir(directory):
        if filename.endswith(".htm"):  
            with open(os.path.join(directory, filename), 'r') as f:
                contents = f.read()
                if phrase in contents:
                    files_found.append(filename)
    return files_found if files_found else "nothing found"

directory = r'/mnt/c/Users/User/Downloads/house_srt'  

while True:
    phrase = input("Enter a phrase to search: ")
    result = search_files(directory, phrase)
    if result != "nothing found":
        print("Files containing the phrase:")
        for file in result:
            print(file)
            #break
    else:
        print(result)


