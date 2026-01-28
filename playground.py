

"import module"
# import mathmodule
#
# res=mathmodule.add_numbers(3,4)
# print(res)

"2- import part of the module ?"
# from mathmodule import div_numbers
# print(div_numbers(2,3))


"3- import module from package ?"
# import BI.inputsModule
#
# print(BI.inputsModule.ask_for_number("please enter age"))

"4*- alias variable name "
# import BI.inputsModule as str_in
#
# print(str_in.ask_for_number("please enter age"))

"5- import block from inputsmodule in BI package ?"

from BI.inputsModule import  ask_for_string

# print(ask_for_string("Please enter a name"))

from BI.inputsModule import coursename

""" package and __init__"""
# from iti.greeting import  say_hi
# say_hi("Noha")

# import iti
# iti.say_hi("noha")
#
# from iti import say_hi
# say_hi("test")

# import os
# print(os.getcwd())
import re
# regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"
#
# email = input("Please enter your email address: ")
# print(email)
#
# "noha@gmail.com@iti.com"
# matched = re.match(regex, email) # return with match object --> the first part of the string matches the object
# print(matched)

##############
""" I need to make sure that all the string parts not the first part """

regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"

email = "noha@gmail.com@iti.com"
print(email)
matched = re.fullmatch(regex, email) # return with match object --> the first part of the string matches the object
print(matched)

