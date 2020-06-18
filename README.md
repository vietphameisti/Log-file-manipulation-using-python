# Logfile manipulation using python
This tool is used to manipulate the logfile in python3,the logfile contains data in which each row of data is separated by a vertical bar.
>The tool is built by Python programing language and pandas library which have a data frame to process quickly tabular data.
First, a regular expression is used to finding the pattern of log data, 
then each row of data was split into the corresponding column of the panda's data frame. 
The groupby function is used to group data and using method to_csv export data to .txt file

<br>To run the program, please following steps:
>
_1. Clone, download the git_
<br>_2. Open the logfile.py file and change the value of 'filepath' variable 
which is the absolute path of the example logfile.txt included in the code folder to the appropriate path_
<br>_3. Open the terminal (or window powershell), move to the folder and run the command "python logfile.py" to run the program_
