# Read in the Titanic Disaster dataset csv file
import matplotlib as matplotlib
import pandas as pd

titanic = pd.read_csv('https://vincentarelbundock.github.io/' + 'Rdatasets/csv/carData/TitanicSurvival.csv')


# Set precision to 2 decimal places and view the head and tail of the file

pd.set_option('precision', 2)
print(f'Titanic Head :')
print(titanic.head())
print(f'Titanic Tail :')
print(titanic.tail())

# Customize the fields

titanic.columns = ['Name', 'Survived', 'Sex', 'Age', 'Class']
print(f'Titanic Head with Custom Columns :')
print(titanic.head())

# Titanic Describe

print(f'Titanic Describe :')
print(titanic.describe())

# Titanic Describe for Survived

print(f'Titanic Describe for Survived:')
print((titanic.Survived == 'yes').describe())

# Enable MatplotLib

histogram = titanic.hist()
matplotlib.pyplot.show()





