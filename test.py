# Hello, my name is Toluwani Adeoti.
# This is the Python Patient Electronic Database.

# This is the testing python file.
# It allows the user to type in the patient's information. 
# # For demo purposes, I'm only allowimg the first name, last name, and ID for myself to type in.

from patient import Patient as PD
from patient import Billing as BD
import pandas as pd
PATIENT = []

Continue = "T" #While Continue is "T", it will keep looping.

while Continue == "T" or Continue == "t":
    Firstname = input("Enter patient's first name: ") # First, I type in the patient's first name...
    Lastname = input("Enter patient's last name: ") # Then, the patient's last name...
    ID = int(input("Enter patient's ID: ")) # and finally, the ID.
    print(f"{ID}: {Firstname} {Lastname}") # This will display the information given so far.
    PATIENT.append(PD(Firstname,Lastname,ID)) # It then goes to the PATIENT array.
    Continue = input("Continue? T = yes, F = no ") # Next, it asks me if I want to make another one. If so, the process will start all over again.
    if Continue == "F" or Continue == "f":  # If not, It will print out end, and...
        print("\nEnd\n")
        break;

PATIENT_DF = pd.DataFrame(columns=["ID", "First Name","Last Name"]) # It makes a DataFrame based on the arrays we've added via PANDAS.
for i in range(len(PATIENT)):
    PATIENT_DF.loc[i+1,"ID"] = PATIENT[i].getID()
    PATIENT_DF.loc[i+1,"First Name"] = PATIENT[i].getFirstName()
    PATIENT_DF.loc[i+1,"Last Name"] = PATIENT[i].getLastName()
print(PATIENT_DF) # It prints out the info...
PATIENT_DF.to_csv("PATIENTS.csv") # And this converts all the information defined into a .csv file.
# Let's test it out, shall we?


# And that is my personal project. It's a bit small for demo purposes, but I hope you thought it was educational.