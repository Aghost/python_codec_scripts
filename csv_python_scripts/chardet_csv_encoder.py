#!/usr/bin/env python3

# splits csv files in lines and columns, checks encoding, converts encoding
# Python 3
# TODO:
#       - check F_DIR, T_DIR in csv_reader
#       - ADD encoding method, OR add encoding options to csv_reader
#       - convert encoding (notepad++ and python2/3)
#       - check for duplicate t_path files, if so, name+1

import os;
import sys;
import csv;
import chardet;

#F_DIR = "C:\\Users\\V\\Desktop\\encoding"
#T_DIR = ""

F_DIR = "."
T_DIR = "./to_dir"

def create_folder(Path):
    if not os.path.exists(Path):
        print("folder does not exists")
        os.mkdir(Path)
    else:
        print("folder exists")

def csv_reader(filename): # path, filename
    file = open(filename, newline='')

    reader = csv.reader(file)
    data = []
    for row in reader:
        # A row contains : id_nr, num, address, name, name2, first_name, last_name, street, street_nr, street_nr2, address2, country
        id_nr, num, address, name, name2 = row[0], row[1], row[2], row[3], row[4]
        first_name, last_name, street, street_nr = row[5], row[6], row[7], row[8]
        street_nr2, address2, country, temp1, endend = row[9], row[10], row[11], row[12], "P3-END"
        # append row to data
        data.append([id_nr, num, address, name, name2, first_name, last_name, street, street_nr, street_nr2, address2, country, temp1, endend])

    # TODO:IF new_path exists, change name+1
    new_path = os.path.join(T_DIR, filename)    #"./returns.csv"
    file = open(new_path, 'w')
    writer = csv.writer(file, lineterminator='\n')
    i = 0
    for line in data:
        print(i, data[i])
        writer.writerow(data[i])
        i += 1

def detect_per_line(Path):
    with open(Path) as fobj:
        data = fobj.read()
        lines = data.split("\n")
        i = 0
        for line in lines:
            print(i, line)
            i += 1
            try:
                print(chardet.detect(bytes(line, "ASCII")))
            except Exception:
                print("not ASCII, trying UTF8")
                try:
                    print(chardet.detect(bytes(line,"UTF8")))
                except Exception:
                    print("not UTF-8, no idea...")

def each_file_detect(Path):
    for root, dirs, files in os.walk(Path):
        for filename in files:
            print(filename)
            #print(detect_per_line(os.path.join(Path, filename)))

def detect_in_files(Path):
    for root, dirs, files in os.walk(Path):
        for filename in files:
            filepath = os.path.join(Path, filename)
            with open(filepath) as fobj:
                data = fobj.read()
                lines = data.split("\n")
                i = 0
                for line in lines:
                    print(i, line)
                    i += 1
                    try:
                        print(chardet.detect(bytes(line, "ASCII")))
                    except Exception:
                        print("not ASCII, trying UTF8")
                        try:
                            print(chardet.detect(bytes(line,"UTF8")))
                        except Exception:
                            print("not UTF-8, no idea...")

def main():
    create_folder(T_DIR)
    input()
    csv_reader("./banaan.csv")
    print("detecting banaan.csv")
    input()
    detect_per_line("./banaan.csv")
    #detect_in_files(F_DIR)
    #each_file_detect(F_DIR)

if __name__ == "__main__":
    main()

# def encode_notepad_pp (Path):
#    return (Path)
