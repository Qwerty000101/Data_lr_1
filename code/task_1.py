#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re

if __name__ == "__main__":
    address = (
        "C:/Users/HAIER/Desktop/Задания/Анализ данных/" + "Data_lr_1/code/task1.txt"
    )
    with open(address, "r", encoding="utf-8") as fileptr:
        sentences = fileptr.readlines()

    for sentence in sentences:
        result = (re.sub("\D", " ", sentence).strip()).split()
        variable = True

        for i in result:
            if int(i) < 100 and int(i) >= 10:
                variable = False
                break

        if variable:
            print(sentence)
