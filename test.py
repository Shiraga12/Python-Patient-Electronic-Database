# Hello, my name is Toluwani Adeoti.
#
# I'm sorry, my computer didn't come with a microphone.
# But the show must go on.
# This is the Python Patient Electronic Database.

# This is the testing python file.
# It allows the user to type in the patient's information. 
# # For demo purposes, I'm only allowimg the first name, last name, and ID for myself to type in.

from patient import Patient as PD
from patient import Billing as BD
import pandas as pd
PATIENT = []

Continue = "T"

while Continue == "T" or Continue == "t":
    Firstname = input("Enter patient's first name: ") # First, I type in the patient's first name...
    Lastname = input("Enter patient's last name: ") # Then, the patient's last name...
    ID = int(input("Enter patient's ID: ")) # Finally the ID.
    print(f"{ID}: {Firstname} {Lastname}") # This will display the information given so far.
    PATIENT.append(PD(Firstname,Lastname,ID)) # It then goes to the PATIENT array.
    Continue = input("Continue? T = yes, F = no ") # Next, it asks me if I want to make another one. If so, the process will start all over again. If not, It will print out end, and...
    if Continue == "F" or Continue == "f":
        print("\nEnd\n")
        break;

PATIENT_DF = pd.DataFrame(columns=["First Name","Last Name", "ID"]) # It makes a DataFrame via PANDAS.
for i in range(len(PATIENT)):
    PATIENT_DF.loc[i+1,"First Name"] = PATIENT[i].getFirstName()
    PATIENT_DF.loc[i+1,"Last Name"] = PATIENT[i].getLastName()
    PATIENT_DF.loc[i+1,"ID"] = PATIENT[i].getID()
print(PATIENT_DF)


