import os
# import shutil
# path ="E:\\Safae\PyCharm\\pythonProject\\pythonProject1\\files\\test.txt"
#
# try:
#     with open(path) as file:
#         print(file.read())
# except FileExistsError:
#     print("not exist")
#copy file into another
#shutil.copyfile(path,'E:\\Safae\PyCharm\\pythonProject\\pythonProject1\\files\\copy.txt')# takes 2 args src ,dest
#shutil.copyfile('E:\\Safae\PyCharm\\pythonProject\\pythonProject1\\files\\copy.txt','E:\\Safae\PyCharm\\pythonProject\\pythonProject1\\files\\copy2.txt')
# deleting files
path2='E:\\Safae\PyCharm\\pythonProject\\pythonProject1\\files\\copy.txt'
destination='E:\\Safae\PyCharm\\pythonProject\\pythonProject1\\files2\\removedfile.txt'
path3='E:\\Safae\PyCharm\\pythonProject\\pythonProject1\\files\\copy2.txt'
try:
    if os.path.exists(path2):
        print('file does exists')
        os.replace(path2,destination)
        print(path2+" the file was moved")
    if os.path.exists(path3):
        os.remove(path3)

except FileNotFoundError:
    print("this file does not exist ")