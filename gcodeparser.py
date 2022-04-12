# author Molokov Alexander
# lisence: GPLv3

import string
import sys
import os

def parserList(inList: list, inSeparator: string) -> list:
    outList = []
    for j in range(0,len(inList),1):
        stringLine = inList[j]
        outList = outList + parserString(stringLine, inSeparator)
    return outList

def parserString(inString: string, inSeparator: string) -> list:
    tempString = ''
    tempList = []
    length = len(inString)
    for i in range(0, length, 1):
        if inString[i] == inSeparator:
            tempList.append(tempString)
            tempString = ''
        elif inString[i] == "\n":
            tempList.append(tempString)
            tempString = ''
            tempString = inString[i]
            tempList.append(tempString)
            tempString = ''
        else:
            tempString = tempString + inString[i]
        
        if i == len(inString)-1:                # дошли до конца строки, стоим на последнем символе
            tempList.append(tempString)
            tempString = ''
    
    return tempList




print(os.getcwd())          # print current directory
"""
cwd - сокращение от current working directory - текущая рабочая директория.
Поменять текущую директорию из Python можно так:

import os
os.chdir('c:\\python370')

В итоге, если текущая рабочая директория не совпадает с директорией, где лежит файл, то вы не сможете открыть файл просто по его имени. Нужно или указать полный (абсолютный) путь, или изменить текущую директорию.
Кстати, чтобы не экранировать обратные слеши в строке пути, можно использовать "сырые" (raw) строки, с буквой r перед кавычками, например:
import os
os.chdir(r'c:\python370')
"""


fileName = "scamv9.txt"
os.chdir(r'G:\NO_Work\Phyton\program\prim001')       # change dir
print(os.getcwd())          # print current directory

with open(fileName) as openfile:
    openFile = open(fileName, 'r')
    lines = []
    lines = openFile.readlines()        # read _all_ string line from file
#openFile.close()

print(lines)

list_for_analiz = parserList(lines, " ")                # parser 'lines' в списке 'list_for_analiz' с разделителем
print (list_for_analiz)

