import os

def main():
    i = 1

    path      = input("Full folder path: ")
    prefix    = input("Prefix: ")
    sufix     = input("Sufix: ")
    extension = input("File extension: ")

    for filename in os.listdir(path):
        index = str(i)
        if i < 10:
            index = "00" + str(i)
        elif i < 100:
            index = "0" + str(i)

        new_filename = f"{prefix} {str(index)} {sufix}.{extension}"

        source = path + filename
        dest   = path + new_filename

        os.rename(source, dest)

        i += 1

if __name__ == '__main__':
    main()