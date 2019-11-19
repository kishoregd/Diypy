# Reading CSV files 
# Using Pandas & Numpy and verify the data types
# By the way Pandas is the short form for Panel Data

# CSV file can be downloaded here
# https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.csv?accessType=DOWNLOAD


# This example demonstrates how to read CSV file and initialize a Data Frame using Pandas
import pandas as p
dframe = p.read_csv("Demographic_Statistics_By_Zip_Code.csv")
print(dframe)
# verify the data type by using type function
print(type(dframe))

# This example demonstrates how to read CSV file and initialize an array using Numpy
import numpy as np
array_np = np.genfromtxt("Demographic_Statistics_By_Zip_Code.csv", delimiter=',')
print(array_np)

# verify the data type by using type function
print(type(array_np))