
import re
print("\n***** Start Programm *****")
fileopen_name = input("Enter Opening File name, with or without localization: \n") #"emails_list200.txt"
filesave_name = input("Enter Saving file name, with or without localization: \n") #"Email.txt"

opened_readfile = open(fileopen_name, mode="r", encoding="latin_1")
opened_writefile = open(filesave_name, mode ="w", encoding = "latin_1")
b = input("Type a Regular expression: \n")
#"[\w.-]+\w+\@[A-Za-z.-]+"
# [\w.-]+@(?!ya\.ru)[\w.]+
lookingfor = r"{a}".format(a=b)

read_file = opened_readfile.read()

def printing_items(items):
    y = []
    for item in items:
        print(item)
        y.append(item)
    print('\n'+"found: "+str(len(items)))
    print("\nThe End of Process")

def writing_files(items):
    for item in items:
        opened_writefile.write(item+"\n")
    opened_writefile.close()
    print("*** Finish ***")

find_all = re.findall(lookingfor,read_file)
find_all.sort()

writing_files(find_all)
opened_readfile.close()

