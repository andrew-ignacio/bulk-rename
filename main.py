import os

def main():
    path      = input("Folder path (with '/' separating folders): ")
    prefix    = input("Prefix: ")
    index     = int(input("Index: "))
    sufix     = input("Sufix: ")
    extension = input("File extension (without '.'): ")

    index -= 1
    for filename in os.listdir(path):
        index_str = str(index)
        if index < 10:
            index_str = "00" + str(index)
        elif index < 100:
            index_str = "0" + str(index)

        tokens = [prefix, index_str, sufix]

        new_filename = append_if_not_empty(tokens, "")
        new_filename += f".{extension}"

        source = path + filename
        dest   = path + new_filename

        os.rename(source, dest)
        index += 1

def append_if_not_empty(tokens: list, text: str) -> str:
    new_text = text
    for token in tokens:
        if token != "":
            if new_text == "":
                new_text += token
            else:
                new_text += f" {token}"
    return new_text

if __name__ == '__main__':
    main()