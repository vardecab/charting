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
if not os.path.isdir("files"): # if folder doesn't exist
    os.mkdir("files") # create folder 
    print("Folder created: files") # status

# ---------- fun begins here --------- #

# --------- get & clean file --------- #

def cleanFile (currency):
    
    # NOTE: local
    # build path
    # TODO: try/except
    folderPath = "../forex-notifier/comparison_files/csv/"
    filePath = f"{folderPath}{currency}.csv"
    # print(filePath) # debug
    
    # NOTE: remote 
    # TODO: download it instead of taking local file + process below
    # filePath = 'https://raw.githubusercontent.com/vardecab/forex-notifier/main/comparison_files/csv/EUR.csv'
    
    # NOTE: file doesn't have column names so let's rewrite it
    # read file
    # TODO: try/except
    with open(filePath,newline='') as file: # open file 
        readFile = csv.reader(file) # read file
        data = list(readFile) # read data to a list 
    # write file
    # TODO: try/except
    with open('files/' + currency.upper() + '.csv','w',newline='') as file: # create and save file
        writeFile = csv.writer(file)
        writeFile.writerow(['Timestamp','Rate']) # write column names to file
        writeFile.writerows(data) # save back everything else
        
def draw (currency):
    
    # TODO: select hours or days instead of multiple runs in an hour

    # TODO: try/except
    file = pandas.read_csv('files/' + currency + '.csv') # read file
    chart = px.line(file, x = 'Timestamp', y = 'Rate', title= currency.upper()) # draw a line chart with xy names and title
    chart.show() # show the chart in a browser tab

# --------- choose currencies -------- #

cleanFile('eur'), draw('eur')
# cleanFile('usd'), draw('usd')
# cleanFile('gbp'), draw('gbp')
# cleanFile('doteur'), draw('doteur')
# cleanFile('btcusdt'), draw('btcusdt')

# ----------- fun ends here ---------- #

# ------------- run time ------------- #

end_time = time.time() # run time end 
total_run_time = round(end_time-start_time,2)
print(f"Total script run time: {total_run_time} seconds.")

# ==================================== #
#                 notes                #
# ==================================== #

# NOTE
# https://plotly.com/python/plot-data-from-csv/