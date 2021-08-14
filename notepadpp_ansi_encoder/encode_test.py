import os;
import sys;
import time;

FROM_DIR ='C:\\Users\\Eigenaar\\Desktop\\encoding2\\'
TO_DIR ='C:\\Users\\Eigenaar\\Desktop\\encoding_to2\\'

def construct_path(filename):
    t_path = os.path.join(TO_DIR, filename)
    filename, extention = os.path.splitext(t_path)
    i = 0
    while os.path.exists(t_path):
        i += 1
        t_path = "{}-{}{}".format(filename, i, extention)
    return t_path

def copy_encode(Path):
    for root, dirs, files in os.walk(Path):
        for filename in files:
            notepad.open(os.path.join(FROM_DIR, filename))
            doc_name = construct_path(filename)
            notepad.runMenuCommand("Encoding", "Convert to ANSI")
            notepad.saveAs(doc_name)
            print("SAVING at: {0}".format(doc_name))
    print("\n done")
    time.sleep(3)
    notepad.closeAll()
    # notepad.runMenuCommand("File", "Exit")

def main():
    copy_encode(FROM_DIR)

if __name__ == "__main__":
    main()
