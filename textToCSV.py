import os
import re
import csv

# Define the folder path containing input text files
input_folder_path = r"C:\Users\graysonl\Documents\code\pythonStuff\inputDocs\text"

# Define the folder path to write the output file
output_folder_path = r"C:\Users\graysonl\Documents\code\pythonStuff\outputDocs"

# Define the regex patterns to search for
patterns = [
    
    r"application\s*#\s*(\d+-?\d*)"
,  # Replace with your first pattern
    r"(?<=Resolution #)\d+\/?\d*",
    r"(?<=Minutes of ).*?(?=Meeting)",
    r"(?<=on the).*(?=Present)",
    r"(?<=application from\s).*?(?=\sfor)",
    r"(?<=pursuant\sto\s).*?(?=\sof)",
    r"described([\s\S]*)more particularly",
    r"Commission with(.*?)\.",   
    r"(?<=THAT\s).*?(?=\son\sthe\sgrounds)", 
    r"(?:accepted|refused)\s*(.+)", 
    # Add additional patterns as needed
]

# Define the headers for the CSV file
headers = ["Application Number", "Resolution Number", "Title", "Date", "Applicants",
           "Proposal Type", "Legal Description", "Proposal Description", "Decision", "Conditions", "Filename"]

# Create a list to store the results
results = []

# Loop through all text files in the selected folder
for filename in os.listdir(input_folder_path):
    if filename.endswith(".txt"):
        # Read the contents of the file
        with open(os.path.join(input_folder_path, filename), "r") as f:
            text = f.read()

        # Search for each pattern in the text and store the results in the list
        matches = []
        for pattern in patterns:
            pattern_matches = re.findall(pattern, text)
            if pattern_matches:
                pattern_matches = [match.replace(",", " ") for match in pattern_matches]
                matches.append(pattern_matches)
            else:
                matches.append([""])
        
        # Add the matches for this file to the results list, with filename as the last element
        results.append([item for sublist in matches for item in sublist] + [filename])

# Write the results to a CSV file
output_file_path = os.path.join(output_folder_path, "results.csv")
with open(output_file_path, "w", newline="") as f:
    writer = csv.writer(f)
    
    # Write the header row
    writer.writerow(headers)
    
    # Write the data rows
    for row in results:
        writer.writerow(row)

print(f"Results written to {output_file_path}")
