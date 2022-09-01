# ==================================== #
#               charting               #
# ==================================== #

# ------------ import libs ----------- #

import time # calculate script's run time
from datetime import datetime # generate timestamp for saving data
# import sys # terminate script
# from inspect import cleandoc # clean up whitespace in multiline strings
import csv # save & read .csv files
import os # create folders

# charts
import pandas # TODO:
# import matplotlib.pyplot as draw # TODO:
import plotly.express as px # TODO: 

# --------- start + run time --------- #

start_time = time.time() # run time start
print("Starting the script...") # status

# ----- timestamp for saving data ---- #

this_run_datetime = timestamp = datetime.strftime(datetime.now(), '%y%m%d-%H%M%S') # eg. 210120-173112

# ----- check and create folders ----- #

# files
if not os.path.isdir("files"):
    os.mkdir("files")
    print(f"Folder created: files")

# ---------- fun begins here --------- #

# ------------ clean file ------------ #
# NOTE: file doesn't have column names so let's rewrite it

filePath = '../forex-notifier/comparison_files/csv/EUR.csv' # using data from forex-notifier repo: https://github.com/vardecab/forex-notifier/tree/main/comparison_files/csv

# TODO: download it instead of taking local file + process below
# filePath = 'https://raw.githubusercontent.com/vardecab/forex-notifier/main/comparison_files/csv/EUR.csv'

# read file
with open(filePath,newline='') as file: # open file 
    readFile = csv.reader(file) # read file
    data = list(readFile) # read data to a list 
# write file
with open('files/EUR.csv','w',newline='') as file: # create file
    writeFile = csv.writer(file)
    writeFile.writerow(['Timestamp','Rate']) # write column names to file
    writeFile.writerows(data) # save back everything else 

# ------------ do drawing ------------ #

# TODO: select hours or days instead of multiple runs in an hour

file = pandas.read_csv('files/EUR.csv')
chart = px.line(file, x = 'Timestamp', y = 'Rate', title="Title") # draw a line chart with xy names and title
chart.show() # show the chart in a browser tab

# ----------- fun ends here ---------- #

# ------------- run time ------------- #

end_time = time.time() # run time end 
total_run_time = round(end_time-start_time,2)
print(f"Total script run time: {total_run_time} seconds.")