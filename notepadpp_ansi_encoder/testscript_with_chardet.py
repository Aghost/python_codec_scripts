# -*- coding: iso-8859-2 -*-
import os;
import sys;

import chardet;

FROM_DIR ='C:\\Users\\Eigenaar\\Desktop\\encoding\\'
TO_DIR ='C:\\Users\\Eigenaar\\Desktop\\encoding_to\\'

def construct_path(filename):
    #notepad.open(os.path.join(FROM_DIR, filename))
    t_path = os.path.join(TO_DIR, filename)
    filename, extention = os.path.splitext(t_path)
    #i = 0
    #while os.path.exists(t_path):
    #    i += 1
    #    t_path = "{}-{}{}".format(filename, i, extention)
    return t_path

def copy_encode(Path):
    for root, dirs, files in os.walk(Path):
        for filename in files:
            doc_name = construct_path(filename)
            notepad.runMenuCommand("Encoding", "Convert to ANSI")
            notepad.saveAs(doc_name)
            print("SAVED at: {0}".format(doc_name))
    notepad.closeAll()
    notepad.runMenuCommand("File", "Exit")


def detect_enc(string):
    byte_str = str.encode(string)
    return chardet.detect(byte_str)

def detect_enc_file(Path):
    all_data = ""
    i = 0
    for root, dirs, files in os.walk(Path):
        for filename in files:
            doc = construct_path(filename)
            print("detecting encoding of file {0}".format(doc))
            in_file = open(doc, "rb")
            data = in_file.read()
            in_file.close()
            print(chardet.detect(data))

def main():

    print("start")
    doc = os.path.join(TO_DIR, "banaan.csv") 
    print("testing", TO_DIR, doc)

    detect_enc_file(doc)
    detect_enc_file(TO_DIR)

    #print(detect_enc("a"))
    #copy_encode(FROM_DIR)

if __name__ == "__main__":
    main()
