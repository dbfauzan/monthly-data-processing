# monthly-data-processing
This is a collection of tools that I create and use to help me semi-automate the monthly report data gathering and processsing

## What was your motivation?
My motivation for making this tool is that I want to implement my python skills, especially in data processing on the work I am working on.

## Why did you build this project?
I made this tool because I want my work to be done faster. To compile a monthly report, I need to extract data from more than 500 text files and process data from about 30 CSV files. If I do it manually, it will take a lot of time and effort. Therefore, I took the initiative to create tools that can make this work easier.

## What problem does it solve?
The problem that can be overcome by this tool is the efficiency of data collection and processing to compile monthly reports. By using this tool, the process can be completed within 1 hour.

## What did you learn?
From working on this project, I learned about the glob library for reading and writing to a file. In addition, I also learned how to process data in python using the pandas and NumPy libraries.

## List of tools:
1. read all file.py
2. convert csv to excel.py
3. data processing.ipynb

## read all file.py
### description & usage
this tools is used to gather data from a specific line of a text file
### input & output
the input of this tools is (a) textfile(s)
the output of this tools is a textfile
### how to use
- put the tools on the same directory as the input textfile(s)
- create a blank textfile for the output
- open the source code (I prefer to open it with VS Code)
- the "i" variable on line 9 is representing the specific line on the textfile you want to extract => change it to your need
- the path on line 14 represent the directory where the output textfile is located => YOU MUST CHANGE THIS
- run the tools

## convert csv to excel.py
### description & usage
this tool is simply convert the csv file to xlsx file
### input & output
the input is (a) csv file(s)
the output is (a) xlsx file(s)
### how to use
- put the tool ont the same directory as the input file
- run the tool (I prefer to run it from VS Code)

## data processing.ipynb 
### description & usage
this tool is used to:
- get the detailed data of top 10 job with longest elapsed time within the close of business process
- get the average close of business process elapsed time
### input & output
- the input of this tool is JT file
- the output of this tool is a table containing information state above
### how to use
DO THIS ONCE
- put the file in the same directory as the JT file
- run the first cell => it return all the csv (JT) file in the directory
DO THIS FOR THE FIRST FILE
- change the file name on the second cell in "read the dataset" section
- make sure to un-comment the line code on "USE THIS FOR FIRST ITERATION" section
- make sure to comment the line code on "USE THIS FOR NEXT ITERATION" section
- run the second cell
DO THIS FOR THE SECOND AND FOLLOWING FILE
- change the file name on the second cell in "read the dataset" section as of the output of the first cell
- make sure to comment the line code on "USE THIS FOR FIRST ITERATION" section
- make sure to un-comment the line code on "USE THIS FOR NEXT ITERATION" section
- run the second cell
DO THIS ONCE
- run the third cell to create a pivot table
- run the forth cell to get the top 10 job duration
- run the fifth cell to get the average COB duration
- run the sixth cell to get the top 10 job details
