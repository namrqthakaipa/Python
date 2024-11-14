import pandas as pd


file_path = 'C:/Users/Namratha Kaipa/Downloads/assignment_2/assignment_2/Q3/club.csv'  
df = pd.read_csv(file_path)

# Split the dataframe based on the 'Type' column
members_df = df[df['Type'] == 'Member']
staff_df = df[df['Type'] == 'Staff']


output_excel_file = 'output_file.xlsx'  # Output file name
with pd.ExcelWriter(output_excel_file, engine='openpyxl') as writer:
    members_df.to_excel(writer, sheet_name='Members', index=False)
    staff_df.to_excel(writer, sheet_name='Staff', index=False)

print(f"Data has been saved to {output_excel_file} with two worksheets: 'Members' and 'Staff'.")
