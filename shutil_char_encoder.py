#!/usr/bin/env python3

import os;
import sys;
import datetime;
import codecs;

from shutil import copy
from os import path

# set options
from_directory, to_directory = './from_dir/', './to_dir/'
dupmode, dup_dir = False, './dup_dir/'

# python encode to options: mbcs(python ANSI), ISO8859
# https://docs.python.org/2/library/codecs.html#codec-base-classes
doctype, to_doctype = '.type1', '.type2'
enc_from, enc_to = 'UTF-8', 'ANSI'

def make_dir(*directories):
    for directory in directories:
        if os.path.exists(directory):
            print("DIR\t- directory already exists: {0}".format(directory))
        else:
            os.mkdir(directory)
            print("DIR\t+ directory created: {0}".format(directory))

def make_logfile(directory, msg):
    f = open(os.path.join(directory, "logfile.txt"), "a+")
    f.write("{0}{1}\n".format(datetime.datetime.now(), msg))
    f.close

# def full_path(*paths, *filenames):     # Optional: file, extension
#   if filenames
#       for path, filename in paths:
#           path = os.path.abspath(os.path.join(path, filename))
#   else 
#       for path, in paths:
#           path = os.path.abspath(path)

# def rename_extension(target, doc, to_doc):
#   if doc != target:
#       extension = os.path.splitext(target)[1] + to_doc

#def change_encoding(target, from_c, to_c):
#    get_value = codecs.decode(target, from_c)
#    set_value = codecs.encode(target, to_c)
#    print("TEST123 {0}, {1}, {2}".format(get_value, set_value, target))

def name_enum(full_path, nr, filename):
    new_path = os.path.splitext(full_path)
    extension = new_path[1] + str(nr)
    print("TESTTESTTESTTESTTEST{0}{1}{2}".format(extension, nr, filename))
    full_path = os.path.join(new_path, extension)
    print(full_path)
    junk = """
    split( C:\dir\file.ext ) => C:\dir\, file1.ext
    split( file.ext ) => file1, .ext
    if file.endswith( int ):=>  file1 = yes
        split ( file, int ) =>  file = file, file_nr = 1
        file_nr = int       =>  file_nr = 1
        file_nr += 1        =>  file_nr = 2
        join ( file, file_nr )  =>  file2
        join ( file, ext )  =>  file2.ext
        join ( dir, file )  =>  C:\dir\file2.ext
    """
    print(junk)

def encode_and_copy(fromdir, todir, dupdir, filename, enc_from, enc_to):
    fullp_from = os.path.abspath(os.path.join(fromdir, filename))
    fullp_to = os.path.abspath(os.path.join(todir, filename))
    fullp_dup = os.path.abspath(dup_dir)
    print("ENCODE\tfrom\t: ({0})TODO\n\tto\t: ({1})TODO".format(enc_from, enc_to))
#TODO ENCODE FILE #change_encoding(fullp_from, enc_from, enc_to) TODO
    print("  DIR\t> Does the file exist in the target directory?")
    if os.path.isfile(fullp_to): 
        print("\t+ yes, file exists")
        if dupmode == True:
            print("\tC copying to duplicates directory: {0}".format(fullp_dup))
            copy(fullp_from, fullp_dup)
            result = "from: {0}\nto {1}\n".format(fullp_from, fullp_dup) #logile
            print("  COPY\t< from\t: ({0})\n\t> to\t: ({1})".format(fullp_from, fullp_dup))
        else:
            x = 0
            while os.path.isfile(fullp_to):
                # TODO name_enum(fullp_to, x, filename) # Naming method TODO

                extension = os.path.splitext(fullp_to)[1]
                new_path = os.path.splitext(fullp_to)[0] + str(x)
                fullp_to = new_path + extension
                x += 1
            print("\tR renaming and copying to: {0}".format(fullp_to))
            copy(fullp_from, fullp_to)
            result = "from: {0}\nto {1}\n".format(fullp_from, fullp_to) #logfile
            print("  COPY\t< from\t: ({0})\n\t> to\t: ({1})".format(fullp_from, fullp_to))
    else:
        print("\t- no, copying to {0}".format(fullp_to))
        copy(fullp_from, fullp_to)
        result = "from: {0}\nto {1}\n".format(fullp_from, fullp_to) #logfile
        print("  COPY\t< from\t: ({0})\n\t> to\t: ({1})".format(fullp_from, fullp_to))
    make_logfile(todir, result) #LOGFILE

def convert_copy(argv):
    if enumerate(argv) > 1:
        for counter, argument in enumerate(argv):
            print("{0}------------------------>|[command]: {1}".format(counter, argv[counter]))
    to_dir = os.path.abspath(to_directory)
    from_dir = os.path.abspath(from_directory)
    make_dir(to_dir)
    if (dupmode):
        make_dir(os.path.abspath(dup_dir))
    for root, dirs, files in os.walk(from_dir): # For-each file in from_dir
        for filename in files:
            print("\nFILE\t: {0}".format(filename))
            extension = os.path.splitext(filename)[1]
            if extension == doctype:
                print("\t> looking for ({0}), got ({1})".format(doctype, extension))
                print("\t+ doctype = extension")
            else:
                print("\t> looking for ({0}), got ({1})".format(doctype, extension))
                print("\t! doctype != extension")
                print("\tC converting to {0} TODO".format(to_doctype))
                # TODO ENCODING METHOD HERE TODO
            make_logfile(to_dir, "doctype: ({0}) to ({1})".format(extension, to_doctype)) #LOGFILE
            # TODO change_encoding(filename, enc_from, enc_to) # TODO
            encode_and_copy(from_dir, to_dir, dup_dir, filename, enc_from, enc_to)
    print("------ END ------")

def main(argv):
    convert_copy(argv)

if __name__ == "__main__":
    main(sys.argv)

# TODO ADD function to convert extension with optional nr argument TODO
