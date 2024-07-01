# Acronym-List-Generator
Generates an Acronym List for your PDF quickly and locally for over 200 pages of text

![Example Run](https://github.com/Srivacthi/Acronym-List-Generator/assets/154648927/6741e863-d4a5-4931-b716-9d442c15d79a)

### Description:
Run this acronym generator locally with no data leaving your device. To use, pip install PyMuPDF in command prompt. Then edit the input pdf name in the code to the pdf you want to retrieve a list of acronyms from. Outputs a list of acronyms + frequency of which they are present. Detects alphanumeric or irregular acronyms like EC2 and mRNA. This tool is perfect to help create an acronym glossary for long pieces of writing including reports, theses, or proposals!

![Edit pdf file name](https://github.com/Srivacthi/Acronym-List-Generator/assets/154648927/0b22e2e4-1af9-4544-8635-4b7d01ffcafb)

### How it works:
Uses a dictionary data structure in python that contains acronym + frequency pairs to hold acronym list. Uses the PyMuPDF library to extract each page in a pdf into a string of words. The words in each string of words are then evaluated as an acronym if it contains atleast 2 uppercase characters.

### Future Upgrades:
Implement AI locally to fill in a new definitions column, allow input word documents.
