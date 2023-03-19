'''
application which uses buttons to call 
find_mismatches function and find_mismatched_column function  
'''
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Function to identify mismatches between input DataFrame and lookup DataFrame.
def find_mismatches(input_df, lookup_df):
    # Use merge() method to join the two DataFrames.
    merged_df = pd.merge(input_df, lookup_df[['TAG_CLASS_NAME','CLASS_DESCRIPTION']], how='left', on='TAG_CLASS_NAME')

    # Find rows where the lookup column is null (i.e. not found in the lookup DataFrame).
    mismatches_df = merged_df[merged_df['CLASS_DESCRIPTION'].isnull()]

    return mismatches_df

# Function to identify column names with mismatches between input DataFrame and lookup DataFrame.
def find_mismatched_column(input_df, lookup_df):
    # Create a list of column names that are in the input DataFrame but not in the lookup DataFrame.
    mismatched_columns = list(set(input_df.columns) - set(lookup_df.columns))

    return mismatched_columns

# Define the function to call when the first button is clicked.
def button1_click():
    # Replace 'input_file.csv' with the name of your input CSV file.
    input_df = pd.read_csv('input_file.csv')

    # Replace 'lookup_file.csv' with the name of your lookup CSV file.
    lookup_df = pd.read_csv('lookup_file.csv')

    # Replace 'column_name' with the name of the column to match between the two DataFrames.
    mismatches_df = find_mismatches(input_df, lookup_df)

    # Use tkinter to display the output DataFrame.
    root = tk.Tk()
    root.withdraw()
    output_file = filedialog.asksaveasfilename(defaultextension='.xlsx')
    mismatches_df.to_excel(output_file, index=False)

    # You can print the output DataFrame to see the mismatches.
    print(mismatches_df)

# Define the function to call when the second button is clicked.
def button2_click():
    # Replace 'input_file.csv' with the name of your input CSV file.
    input_df = pd.read_csv('input_file.csv')

    # Replace 'lookup_file.csv' with the name of your lookup CSV file.
    lookup_df = pd.read_csv('lookup_file.csv')

    mismatched_columns = find_mismatched_column(input_df, lookup_df)

    # Use tkinter to display the output.
    root = tk.Tk()
    root.withdraw()
    output_file = filedialog.asksaveasfilename(defaultextension='.txt')
    with open(output_file, 'w') as f:
        for col in mismatched_columns:
            f.write(col + '\n')

    # You can print the output to see the mismatched columns.
    print(mismatched_columns)

# Create the tkinter application.
root = tk.Tk()
root.title('Find Mismatches')

# Create the first button to call the find_mismatches() function.
button1 = tk.Button(root, text='Find Mismatches', command=button1_click)
button1.pack(pady=10)

# Create the second button to call the find_mismatched_column() function.
button2 = tk.Button(root, text='Find Mismatched Columns', command=button2_click)
button2.pack(pady=10)

# Start the tkinter mainloop.
root.mainloop()

