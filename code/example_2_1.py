#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # open the file2.txt in read mode. causes error if no such file exists.
    fileptr = open(
        "C:/Users/HAIER/Desktop/Задания/Анализ данных/Data_lr_1/code/file2.txt",
        "r",
    )
    # stores all the data of the file into the variable content
    content = fileptr.read(10)
    # prints the type of the data stored in the file
    print(type(content))
    # prints the content of the file
    print(content)
    # closes the opened file
    fileptr.close()
