# Data Processing and Visualization Example

This project demonstrates how to process data, convert it into numpy arrays, and visualize it using Python. 
The code reads data from a CSV string, allows the user to select columns to convert to numpy arrays, and then generates either a scatter plot or a line plot.

## Example CSV Data

```python
csv_data = """
Date,Value
2024-01-01,100
2024-01-02,150
2024-01-03,200
2024-01-04,250
2024-01-05,300
"""
```

## Output Example

### Column Names:
```css
['Date', 'Value']
```
### First 2 Rows:
```yaml
         Date  Value
0  2024-01-01    100
1  2024-01-02    150
```

### User Input Example:
Column to convert to numpy array: Value
Plot Type: line
Plot Result
Based on the user input, the program generates a line plot with "Date" on the x-axis and "Value" on the y-axis.

### Instructions for Running the Code
The program will load the data directly from the CSV string.
It will display a preview of the data, including column names and the first two rows.
You will be prompted to input the name of the column you want to convert to a numpy array.
Next, you will choose between a scatter plot or a line plot for data visualization.
