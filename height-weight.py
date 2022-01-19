import pandas as pandas
import statistics
import csv
df = pd.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()
#Mean for height and weight
height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)
#Median for height and weight
height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)
#Mode for height and weight
height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)
#Printing mean, median, and mode to validate
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(height_mean, height_median, height_mode))
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(weight_mean, weight_median, weight_mode))