# -*- coding: utf-8 -*-
"""
@author: sriva
"""

import pymupdf  # import the pymupdf library

class AcronymFinder:
    # class variable dictionary to hold acronyms and their counts
    mylist = {}
    
    @classmethod
    def findAcronyms(cls, text):
        """ 
        This function adds acronyms from a page of string text into dictionary and counts their frequency.
        
        Args:
            text (str): A string containing text to search for acronyms.
        """
        # split page of words string into list of words
        words = text.split()
        # traverse through each word
        for word in words:
            # if length of word >35 skip
            if len(word) <= 35:
                # integer to hold num of capital letters in a word
                capitals = 0 
                # index of word
                wordIndex = 0
                # counts capital letters in a word
                while wordIndex < len(word):
                    if word[wordIndex].isupper():
                        capitals += 1
                    wordIndex += 1
                # checks if more than 2 capital letters are present (is an acronym)
                if capitals >= 2:
                    # if first character is punctuation
                    if word[0] in {'.',',',':',';','\'','\"','(','[','{'}:
                        # remove the first character
                        word = word[1:]
                    # if last character is punctuation
                    if word[-1] in {'.',',',':',';','\'','\"',')',']','}'}:
                        # remove the last character
                        word = word[:-1]
                    # strip word of trailing periods
                    word = word.rstrip('.') 
                    # add acronym to dictionary, increment frequency if acronym exists in dict
                    if word in cls.mylist:
                        cls.mylist[word] += 1
                    else:
                        cls.mylist[word] = 1
    @classmethod
    def getList(cls):
        """
        This method returns the dictionary containing acronyms and their frequency.

        Returns:
            dict: The dictionary of acronyms and their counds.

        """
        return cls.mylist

# open a pdf document (edit your pdf name)
pdf = pymupdf.open("Your PDF Name.pdf")

# iterate through each page in pdf
for page in pdf:
    # save plain text page encoded as UTF-8 into string
    text = page.get_text()
    # print text string
    AcronymFinder.findAcronyms(text)
    

# sort and print dictionary by key
print("Acronym List \t\t\t\t\t\t| Count")
print("--------------------------------------------")
myList = AcronymFinder.getList()
for key in sorted(myList):
    print (f"{key:<35} |  {myList[key]}x")
print
# print total number of acronyms
print("\nTotal unique acronyms: " + str(len(myList)))