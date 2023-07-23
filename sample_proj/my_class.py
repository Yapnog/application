
# Create a class that can be called to fix the formatting of the csv in this dir (sample.csv) and return it as a df. 
# BONUS: Return the data grouped in the best manner you see fit.


import os
import pandas as pd

class CSVFormatter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)		# locate the file to be processed

    def browse_file(self):
        try:
            df = pd.read_csv(self.file_dir)
            df = df.fillna(0)		            	# fill NaN values with zeroes in the entire DataFrame
            return df
        except FileNotFoundError:
            print(f"File '{self.file_name}' not found.")

    def fix_formatting_and_group(self):
        df = self.browse_file()
        if df is not None:
            sorted_df = df.groupby(['Master', 'ID'], as_index=False).sum()
            return sorted_df

# Usage
if __name__ == "__main__":
    file_name = 'files.csv'
    formatter = CSVFormatter(file_name)
    cleaned_data = formatter.browse_file()
    sorted_data = formatter.fix_formatting_and_group()
    
    if cleaned_data is not None:
        print("Cleaned DataFrame:")
        print(cleaned_data)
    
    if sorted_data is not None:
        print("\nSorted DataFrame:")
        print(sorted_data)
