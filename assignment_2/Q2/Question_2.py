import pandas as pd

# 1. Create the parent class 'Person'
class Person:
    def __init__(self, id, name, age, amount):
        self.id = id
        self.name = name
        self.age = int(age)
        self.amount = float(amount)

# 2. Create the Member subclass
class Member(Person):
    def __init__(self, id, name, age, amount):
        super().__init__(id, name, age, amount)

    def print(self):
        print(f"{self.name} is {self.age} years old. His monthly fee is Rs {self.amount:.2f}.")

# 3. Create the Staff subclass
class Staff(Person):
    def __init__(self, id, name, age, amount):
        super().__init__(id, name, age, amount)

    def print(self):
        print(f"{self.name} is {self.age} years old. His monthly remuneration is Rs {self.amount:.2f}.")

# 4. Function to read CSV and create objects based on the data
def read_and_create_objects(csv_file):
    persons = [] 
    
    try:
    
        df = pd.read_csv(csv_file)

      
        #print("Columns in the CSV file:", df.columns)

       
        required_columns = {'ID', 'Name', 'Age', 'Amount', 'Type'}
        if not required_columns.issubset(df.columns):
            print(f"CSV file missing required columns. Expected columns: {required_columns}")
            return persons

        # Iterate over the rows of the DataFrame
        for _, row in df.iterrows():
            try:
                id = row['ID']
                name = row['Name']
                age = row['Age']
                amount = row['Amount']
                person_type = row['Type'].strip().lower()  

                # Create Member or Staff object based on the 'Type' column
                if person_type == 'member':
                    person = Member(id, name, age, amount)
                elif person_type == 'staff':
                    person = Staff(id, name, age, amount)
                else:
                    print(f"Unknown person type: {person_type}")
                    continue  
                        
                persons.append(person)

            except Exception as e:
                print(f"Error processing row {row}: {e}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return persons


if __name__ == "__main__":
  
    csv_file = 'C:/Users/Namratha Kaipa/Downloads/assignment_2/assignment_2/Q2/club.csv'  # Update the path to where your CSV file is located
    
 
    persons = read_and_create_objects(csv_file)
    
  
    for person in persons:
        person.print()
