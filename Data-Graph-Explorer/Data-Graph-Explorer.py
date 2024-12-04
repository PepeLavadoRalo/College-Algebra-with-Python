import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

# CSV data in string format (StringIO simulates a file)
csv_data = """
Date,Value
2024-01-01,100
2024-01-02,150
2024-01-03,200
2024-01-04,250
2024-01-05,300
"""

# Function to load data from the CSV string
def load_data_from_string(csv_data):
    # Use StringIO to read the CSV string as if it were a file
    df = pd.read_csv(StringIO(csv_data))
    return df

# Function to show the first rows and column names
def data_overview(df):
    # Print column names and the first 2 rows of the data
    print("Column names:", df.columns.tolist())
    print("First 2 rows:\n", df.head(2))

# Function to get column names as a list
def get_column_names(df):
    return df.columns.tolist()

# Function to convert selected columns to numpy arrays
def convert_to_numpy(df):
    print("Enter the column name(s) you want to convert to numpy arrays (separate by commas if more than one):")
    columns_input = input().split(',')

    # Convert the selected columns to numpy arrays
    numpy_arrays = [df[col].to_numpy() for col in columns_input]

    return numpy_arrays

# Function to plot the data
def plot_data(df, numpy_arrays):
    print("Type 'scatter' for a scatter plot or 'line' for a line plot:")
    plot_type = input()

    if plot_type.lower() == 'scatter':
        plt.scatter(numpy_arrays[0], numpy_arrays[1] if len(numpy_arrays) > 1 else numpy_arrays[0])
        plt.title('Scatter Plot')
    elif plot_type.lower() == 'line':
        plt.plot(numpy_arrays[0], numpy_arrays[1] if len(numpy_arrays) > 1 else numpy_arrays[0])
        plt.title('Line Plot')

    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1] if len(numpy_arrays) > 1 else df.columns[0])
    plt.show()

# Main function that integrates everything
def main():
    # Load the data directly from the CSV string
    df = load_data_from_string(csv_data)

    # Show a preview of the data
    data_overview(df)

    # Get column names
    column_names = get_column_names(df)

    # Convert the columns to numpy arrays
    numpy_arrays = convert_to_numpy(df)

    # Plot the data
    plot_data(df, numpy_arrays)

# Execute the program
if __name__ == "__main__":
    main()
