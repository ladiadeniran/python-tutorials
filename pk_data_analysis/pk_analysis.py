import pandas as pd
import matplotlib.pyplot as plt
import os
# import statsmodel.api as sm


def analyze_pk_data(csv_file):
  # we read the data using pandas
  pk_data= pd.read_csv(csv_file)



  # we calculate important PK values
  # cmax that is maximum concentration
  cmax = pk_data['Conc'].max()
  tmax = pk_data['Time'].max()
  cmax_row = pk_data[pk_data['Conc'] == cmax].index.values[0] + 2
  tmax_row = pk_data[pk_data['Time'] == tmax].index.values[0] + 2

  # Assignment print all the lines with tmax == 24
  print(cmax_row)
  print(tmax_row)
  #  print the cmax and tmax line from csv
  print(f"Cmax: {cmax} ug/mL on line {cmax_row}  and tmax: {tmax} hr(s) on line {tmax_row}")
  # visulization
  plt.figure(figsize=(10, 5))
  plt.plot(pk_data['Time'], pk_data['Conc'], marker='o', linestyle='-')
  plt.title('Concentration-Time Profile Mentorship')
  plt.xlabel('Time (hr)')
  plt.ylabel('Concentration (ug/mL)')
  plt.grid(True)
  plt.show()

  # assignment analysis

if __name__ == "__main__":
  # get the root of the project
  root_directory = os.path.abspath(os.curdir)
  csv_file = root_directory + "/pk_data.csv"
  analyze_pk_data(csv_file)
