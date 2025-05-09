import pandas as pd
import os
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

#
def run(csv_file):
  # load csv into pandas
  data = pd.read_csv(csv_file)
  data = data.dropna()
  dosage = data["Dosemgkg"]
  conc = data["Conc"]

  popt, pcov = curve_fit(four_param_logistic, dosage, conc)
  # response from csv
  lower_limit, upper_limit, ec50, hill_slope = popt
  fitted_response = four_param_logistic(dosage, *popt)

  # Plot the data and fitted curve
  plt.scatter(dosage, conc, label="Data")
  plt.plot(dosage, fitted_response, label="Fitted Curve", color="red")
  plt.xscale("log")
  plt.xlabel("Dose")
  plt.ylabel("Conc")
  plt.legend()
  plt.show()


def four_param_logistic(x, lower_limit, upper_limit, ec50, hill_slope):
  return lower_limit + (upper_limit - lower_limit) / (1 + (x / ec50)**(-hill_slope))


if __name__ == "__main__":
  root_directory = os.path.abspath(os.curdir)
  csv_file = root_directory + "/pk_data.csv"
  run(csv_file)
