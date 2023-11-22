import pandas as pd
from patient import Patient

# Create an empty DataFrame to store patient information
df = pd.DataFrame(columns=["First Name", "Last Name", "ID", "DOB_M", "DOB_D", "DOB_Y", "DOS_M", "DOS_D", "DOS_Y", "Physician", "Gender"])

# Function to add a patient to the DataFrame
def add_patient():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    patient_id = input("Enter ID: ")
    dob_m = int(input("Enter DOB month: "))
    dob_d = int(input("Enter DOB day: "))
    dob_y = int(input("Enter DOB year: "))
    dos_m = int(input("Enter DOS month: "))
    dos_d = int(input("Enter DOS day: "))
    dos_y = int(input("Enter DOS year: "))
    physician = input("Enter physician: ")
    gender = input("Enter gender: ")

    # Add patient information to the DataFrame
    df.loc[len(df)] = [first_name, last_name, patient_id, dob_m, dob_d, dob_y, dos_m, dos_d, dos_y, physician, gender]
    print("Patient added successfully!")

# Main program loop
while True:
    choice = input("Do you want to add a patient? (Y/N): ")

    if choice.upper() == "Y":
        add_patient()
    elif choice.upper() == "N":
        break
    else:
        print("Invalid choice. Please enter Y or N.")

# Convert DataFrame to CSV file
csv_file = input("Enter the CSV filename (e.g., patients.csv): ")
df.to_csv(csv_file, index=False)
print("Data saved to CSV file.")