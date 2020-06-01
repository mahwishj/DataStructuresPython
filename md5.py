import hashlib

with open('testfile.txt') as file1:
    text = file1.read()

    file1Hash = hashlib.md5(text.encode('utf-8')).hexdigest()

with open('testfile2.txt') as file2:
    text2 = file2.read()

    file2Hash = hashlib.md5(text2.encode('utf-8')).hexdigest()

if(file1Hash == file2Hash):
    print('Files have same content!')
else:
    print('Files are different!')
