# Read a sample CSV
import pandas as pd
import numpy as np
import matplotlib as matplotlib
df = pd.read_csv('SampleCSVFile.csv',encoding = 'utf8')

# Clean the Data - Remove Negative Values, Add Custom Columns, Replace Blan Values with 0.0
df.columns = ['Sl', 'Company', 'Contact', 'Product_id', 'Mean', 'Price', 'Unit', 'Location', 'Category', 'Deviation']
df['Mean'] = df['Mean'].abs()
df['Deviation'] = df['Deviation'].replace(np.nan, 0.0)

# Describe for descriptive analytics
print(df.describe())

# Histogram
histogram = df.hist()
matplotlib.pyplot.show()
