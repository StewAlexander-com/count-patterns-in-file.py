#!/usr/bin/env python3
import os
import sys

#if file "line_numbers.txt" exists delete it
if os.path.exists("line_numbers.txt"):
    os.remove("line_numbers.txt")

# This file counts the number of times a string appears in a filename, prints the result then saves the line numbers found
# to a file called "line_numbers.txt" - Created by Stewart Alexander, 10/29/2021
print ("\n\nThis program finds the number of times a pattern exists in a file, \nand prints the count of the pattern, plus it will create a file \nlisting where the pattern was found.")

#open a path to the current directory
path = os.path.dirname(os.path.realpath(__file__))
#show the contents of the curent directory
print ("\n\nThe current directory is: " + path, ", and the list of contents are:\n")
print(os.listdir())
#ask the user to enter the a file name
file_name = input("\nEnter the the file name you wish to search: ")

# while loop to check if the file exists
while True:
    if os.path.isfile(file_name):
        break
    else:
        print("\n=== The File you entered does not exist!===")
        file_name = input("\nPlease, enter the file name you wish to search: ")

#open the file
file = open(file_name, "r") 
#read the file
file_contents = file.read()

#search for the string
string = input("\nEnter the pattern to search for: ")

#count the number of times the string appears in the file
count = file_contents.count(string)

#if the string appears in the file, print the number of times it appears
if count > 0:
    print("\n\nThe pattern appears " + str(count) + " times in the file")
#if the string does not appear in the file, print the string does not appear
else:
    print("\n\nThe pattern does not appear in the file")

#if count > 0 print the line number where the string appears
if count > 0:
    #split the file contents into a list
    file_contents_list = file_contents.split("\n")
    #loop through the list
    for i in range(len(file_contents_list)):
        #if the string appears in the list, save the line numbers to a file called "line_numbers.txt"
        if string in file_contents_list[i]:
            #open the file
            file = open("line_numbers.txt", "a")
            #write the line number, and line to the file
            file.write(str(i+1) + " " + file_contents_list[i] + "\n")
            #close the file
            file.close()
        else:
            continue
else:
    print ("")

#if the file called "line_numbers.txt" exists, print that the file exists
if os.path.isfile("line_numbers.txt"):
    print("\n\nA file called \"line_numbers.txt\" was created that has \nthe list of the line numbers where \"" + string + "\" appears\n")
else:
    print("")

print ("Exiting the program....\n")

#close the file
file.close()