class Patient:
    def __init__(self, firstname, lastname, ID, DOB_M = -1, DOB_D = -1, DOB_Y = -1, DOS_M = -1, DOS_D = -1, DOS_Y = -1, physician = None, gender = None):
        self.firstname = firstname
        self.lastname = lastname        
        self.ID = ID        
        self.DOB_M = DOB_M        
        self.DOB_D = DOB_D        
        self.DOB_Y = DOB_Y        
        self.DOS_M = DOS_M                
        self.DOS_D = DOS_D                
        self.DOS_Y = DOS_Y                
        self.physician = physician
        self.gender = gender

    def getFirstName(self):
        return self.firstname
    def getLastName(self):
        return self.lastname
    def getID(self):
        return self.ID
    def getDOB_M(self):
        if self.DOB_M < 10:
            return f"0{self.DOB_M}"
        elif self.DOB_M >= 10:
            return self.DOB_M
    def getDOB_D(self):
        if self.DOB_D < 10:
            return f"0{self.DOB_D}"
        elif self.DOB_D >= 10:
            return self.DOB_D
    def getDOB_Y(self):
        return self.DOB_Y
    def getDOS_M(self):
        if self.DOS_M < 10:
            return f"0{self.DOS_M}"
        elif self.DOS_M >= 10:
            return self.DOS_M
    def getDOS_D(self):
        if self.DOS_D < 10:
            return f"0{self.DOS_D}"
        elif self.DOS_D >= 10:
            return self.DOS_D
    def getDOS_Y(self):
        return self.DOS_Y
    def getPhysician(self):
        return self.physician
    def getGender(self):
        return self.gender

    def setFirstName(self, firstname):
        self.firstname = firstname
    def setLastName(self, lastname):
        self.lastname = lastname
    def setID(self, ID):
        self.ID = ID
    def setDOB_M(self, DOB_M):
        self.DOB_M = DOB_M
    def setDOB_D(self, DOB_D):
        self.DOB_D = DOB_D
    def setDOB_Y(self, DOB_Y):
        self.DOB_Y = DOB_Y
    def setDOS_M(self, DOS_M):
        self.DOS_M = DOS_M
    def setDOS_D(self, DOS_D):
        self.DOS_D = DOS_D
    def setDOS_Y(self, DOS_Y):
        self.DOS_Y = DOS_Y
    def setPhysician(self, physician):
        self.physician = physician
    def setGender(self, gender):
        self.gender = gender
    
    def getFullName(self):
        return f"{self.firstname} {self.lastname}"
    def getDOB_Full(self):
        if (self.getDOB_M() == -1) or (self.getDOB_D() == -1) or (self.getDOB_Y() == -1):
            return None;
        else:
            return f"{self.getDOB_M()}/{self.getDOB_D()}/{self.getDOB_Y()}"
    def getDOS_Full(self):
        if (self.getDOS_M() == -1) or (self.getDOS_D() == -1) or (self.getDOS_Y() == -1):
            return None;
        else:
            return f"{self.getDOS_M()}/{self.getDOS_D()}/{self.getDOS_Y()}"
    def getAge(self):
        if (self.getDOB_Y() == -1) or (self.getDOS_Y() == -1):
            return None;
        else:
            return int(self.getDOS_Y()-self.getDOB_Y())
    def getCurrentAge(self):
        import datetime
        today = datetime.date.today()
        year = today.year
        
        if (self.getDOB_Y() == -1):
            return None;
        else:
            return int(year-self.getDOB_Y())

class Billing:
    def __init__(self, name, hospital, doctor, diagnosis, month, day, year, procedure):
        self.name       = name
        self.hospital   = hospital
        self.doctor     = doctor
        self.diagnosis  = diagnosis
        self.month      = month
        self.day        = day
        self.year       = year
        self.procedure  = procedure

    def getName(self):
        return self.name
    def getHospital(self):
        return self.hospital
    def getDoctor(self):
        return self.doctor
    def getDiagnosis(self):
        return self.diagnosis
    def getMonth(self):
        return self.month
    def getDay(self):
        return self.day
    def getYear(self):
        return self.year
    def getProcedure(self):
        return self.procedure

    def setName(self, name):
        self.name       = name
    def setHospital(self, hospital):
        self.hospital   = hospital
    def setDoctor(self, doctor):
        self.doctor     = doctor
    def setDiagnosis(self, diagnosis):
        self.diagnosis  = diagnosis
    def setMonth(self, month):
        self.month      = month
    def setDay(self, day):
        self.day      = day
    def setYear(self, year):
        self.year       = year
    def setProcedure(self, procedure):
        self.procedure  = procedure
