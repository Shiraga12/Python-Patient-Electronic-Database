from patient import Patient as PD
from patient import Billing as BD
import pandas as pd
PATIENT = []

Continue = "T"

while Continue == "T" or Continue == "t":
    Firstname = input("Enter patient's first name: ")
    Lastname = input("Enter patient's last name: ")
    ID = input("Enter patient's ID: ")
    PATIENT.append(PD(Firstname,Lastname,ID))
    Continue = input("Continue? T = yes, F = no ")
    if Continue == "F" or Continue == "f":
        print("\nEnd")
        break;

PATIENT_DF = pd.DataFrame(columns=["First Name","Last Name", "ID"])
for i in range(len(PATIENT)):
    PATIENT_DF.loc[i+1,"First Name"] = PATIENT[i].getFirstName()
    PATIENT_DF.loc[i+1,"Last Name"] = PATIENT[i].getLastName()
    PATIENT_DF.loc[i+1,"ID"] = PATIENT[i].getID()
print(PATIENT_DF)