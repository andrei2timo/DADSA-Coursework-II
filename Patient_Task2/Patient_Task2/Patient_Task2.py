import csv
import datetime
from datetime import date
file = "DADSA 2021 CWK B DATA COLLECTION.csv"

# Creating a class named Patient that will store the info for a person
class Patient:
    Patient_Name: str
    DateofBirth: datetime
    Sex: str
    Height: float
    Weight: int
    BodyBuild: str
    Smoker: str
    Asthmatic: str
    NJT_NGR: str
    Hypertension: str
    RenalRT: str
    IleostomyColostomy: str
    ParenteralNutrition: str
    #Constructor of the class to prepare the object to be used
    def __init__(self, Patient_Name, DateofBirth, Sex, Height, Weight, BodyBuild, Smoker, Asthmatic, NJT_NGR, Hypertension, 
                 RenalRT, IleostomyColostomy, ParentalNutrition):
        self.Patient_Name = Patient_Name
        self.DateofBirth = DateofBirth
        self.Sex = Sex
        self.Height = Height
        self.Weight = Weight
        self.BodyBuild = BodyBuild
        self.Smoker = Smoker
        self.Asthmatic = Asthmatic
        self.NJT_NGR = NJT_NGR
        self.Hypertension = Hypertension
        self.RenalRT = RenalRT
        self.IleostomyColostomy = IleostomyColostomy
        self.ParenteralNutrition = ParentalNutrition
    # display method will print on the screen the details of a patient
    def display(self):
        print(self.Patient_Name, self.DateofBirth, self.Sex, self.Height, self.Weight, self.BodyBuild, self.Smoker,
            self.Asthmatic, self.NJT_NGR, self.Hypertension, self.RenalRT, self.IleostomyColostomy,
            self.ParenteralNutrition)

# The array of objects called Patient_List
Patient_List = []

# read_csv_file() will read the input file and will store the information into Patient_List
def read_csv_file():
    # skip first line i.e. read header first and then iterate over each row od csv as a list
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_file)
        # Check file as empty
        if header != None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                bmi = 0.0
                p = Patient(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12])
                Patient_List.append(p)
                for i in range(len(Patient_List)):
                    bmi = int(Patient_List[i].Weight) / (float(Patient_List[i].Height) * float(Patient_List[i].Height))
                    setattr(Patient_List[i],'BMI',round(bmi,2))
                    setattr(Patient_List[i],'Age',calculateAge(date(int(Patient_List[i].DateofBirth[-4:]),int(Patient_List[i].DateofBirth[3:5]),int(Patient_List[i].DateofBirth[:2]))))

# Print_Data(List) will display the information found on the List. In our case, it will display the patients stored in Patient_List
def Print_Data(List):
    for i in range(len(List)):
        List[i].display()

# Print_Data_with_BMI_and_Classification(List) will display the information found on the List and the BMI for each patient. 
def Print_Data_with_BMI_and_Classification(List):
    for i in range(len(List)):
        print(List[i].Patient_Name,List[i].DateofBirth,List[i].Sex,List[i].Height
        ,List[i].Weight,List[i].Smoker,List[i].Asthmatic,List[i].NJT_NGR
        ,List[i].Hypertension,List[i].RenalRT,List[i].IleostomyColostomy,List[i].ParenteralNutrition,List[i].BMI)

# Display_Patient(Patient) will print on the screen on patient and his/her details.
def Display_Patient(Patient):
    print(Patient.Patient_Name,calculateAge(date(int(Patient.DateofBirth[-4:]),int(Patient.DateofBirth[3:5]),int(Patient.DateofBirth[:2]))),
         Patient.Sex,Patient.Height
        ,Patient.Weight,Patient.Smoker,Patient.Asthmatic,Patient.NJT_NGR
        ,Patient.Hypertension,Patient.RenalRT,Patient.IleostomyColostomy,Patient.ParenteralNutrition,Patient.BMI
        ,Patient.Classification)

# Calculate_BMI_and_Classification(List) will calculate the BMI and will classify the patients according to it.
def Calculate_BMI_and_Classification(List):

    for i in range(len(List)):# for each patient in the list
        #Create a new attribute in the class , named Classification and store the string for each classification into it
        setattr(List[i],'Classification','')
        if(List[i].BodyBuild == 'Slim'):
            if(List[i].BMI < 18.5):
                List[i].Classification = 'Underweight'
            elif(List[i].BMI >= 18.5 and List[i].BMI < 25):
                List[i].Classification = 'Normal'
            elif(List[i].BMI >= 25 and List[i].BMI < 28):
                List[i].Classification = 'Overweight'
            else:
                List[i].Classification = 'Obese'

        if(List[i].BodyBuild == 'Regular'):
            if(List[i].BMI < 18.5):
                List[i].Classification = 'Underweight'
            elif(List[i].BMI >= 18.5 and List[i].BMI < 25):
                List[i].Classification = 'Normal'
            elif(List[i].BMI >= 25 and List[i].BMI < 29):
                List[i].Classification = 'Overweight'
            else:
                List[i].Classification = 'Obese'

        if(List[i].BodyBuild == 'Athletic'):
            if(List[i].BMI < 18.5):
                List[i].Classification = 'Underweight'
            elif(List[i].BMI >= 18.5 and List[i].BMI < 25):
                List[i].Classification = 'Normal'
            elif(List[i].BMI >= 25 and List[i].BMI < 30):
                List[i].Classification = 'Overweight'
            else:
                List[i].Classification = 'Obese'

# Print_Classification(List,classification,TemporaryList) will create a temporary list which will store the patients in order of the classification
# Obese first, then Underweight, Overweight followed by Normal patients
def Print_Classification(List,classification,TemporaryList):
    for i in range(len(List)):
        if(List[i].Classification == classification):
                TemporaryList.append(List[i])

# Classification(List) will print 10 patients. After 10 patients will be displayed, a break line will occur.
def Classification(List):
    # Creating the temporary_List
    TemporaryList = []
    #Call the Print_Classification method to instantiate the Temporary_List
    Print_Classification(List,'Obese',TemporaryList)#Put the Obese people into Temporary_List
    Print_Classification(List,'Underweight',TemporaryList)#Put the Underweight people into Temporary_List
    Print_Classification(List,'Overweight',TemporaryList)#Put the Overweight people into Temporary_List
    Print_Classification(List,'Normal',TemporaryList)#Put the Normal people into Temporary_List

# calculateAge(birthDate) will calculate the age for a person related to their birth date
def calculateAge(birthDate): 
    days_in_year = 365.2425    # The number of days in a year
    # age is calculated related to the difference between today's date,birth date and the number of days in a year
    age = int((date.today() - birthDate).days / days_in_year)
    #return the calculated value
    return age 

# BreakLine() will break 2 rows. This function helps displaying information 'more clearly'
def BreakLine():
    print()
    print()

# Selection_Sort(L) will sort the list L using the Selection Sort algorithm
def Selection_Sort(L):
    # i indicates how many items were sorted
    for i in range(len(L)):
        # We then use j to loop through the remaining elements
        for j in range(i+1,len(L)):
            if( L[i].Age < L[j].Age):# Sort the List L by Age in DESCENDING order
                # After finding the lowest item of the unsorted regions, swap with the first unsorted item
                aux = L[i]
                L[i] = L[j]
                L[j] = aux

# Selection_Sort(L) will sort the list L using the Selection Sort algorithm
def Selection_Sort_Order(L):
    # i indicates how many items were sorted
    for i in range(len(L)):
        # We then use j to loop through the remaining elements
        for j in range(i+1,len(L)):
            if( L[i].Order > L[j].Order):# Sort the List L by Age in DESCENDING order
                # After finding the lowest item of the unsorted regions, swap with the first unsorted item
                aux = L[i]
                L[i] = L[j]
                L[j] = aux
# Referring_To_Dietitian(List) will check the patients by Number of conditions of each patient and BMI.
# If two patients has the same order , then it will be checked their age to determine the order.
def Referring_To_Dietitian(List):
    #Sort the List decreasing by Age
    Selection_Sort(List)
    #Create a Temporary List to insert the patients based on their Order number.
    Temporary_List = []
    for i in range(len(List)):#For each patient i in List
        for j in range(i+1,len(List)):#For each patient j in List
            if(int(List[i].Order) == int(List[j].Order)):#Check if they have the same order number
                if(int(List[i].Age) > int(List[j].Age) or List[i].BMI > List[j].BMI or List[i].NoConditions > List[j].NoConditions):#If so, check who is the eldest, who has the greater BMI and No. of conditions
                    Temporary_List.append(List[i])#In this case, patient i is the eldest
                else:
                    Temporary_List.append(List[j]) #Otherwise, patient j is the eldest

    #Delete the duplicates from Temporary_List
    Temporary_List = list(dict.fromkeys(Temporary_List))
    #Sort the Temporary List by Order number
    Selection_Sort_Order(Temporary_List)
    k = 0#Set the counter to 0. This variable will indicate how many patients were displayed
    print("Patient name | Age | Number_of_Conditions | BMI | Order Number")
    for i in range(len(Temporary_List)):#For each Patient in Temporary List
        #Print Patient name,age,number of conditions,bmi and their order number
        if(Temporary_List[i].Order < 4):
            print(Temporary_List[i].Patient_Name,"       ",Temporary_List[i].Age,
                "          ",Temporary_List[i].NoConditions,"           ",Temporary_List[i].BMI,
                "      ",Temporary_List[i].Order)
            k = k + 1#Incremenet the counter
            if( k == 10 ):#If 10 rows were displayed
                print()#Break a line
                k = 0#Set the counter back to 0


# RankOrder(List) will determine the order number for each patient based on their conditions, age and BMI
def RankOrder(List):
    Temporary_List = List.copy()#Make a copy of Patient_List
    for i in range(len(List)):#for each patient
        #Set a new attribute called Order. It will store the order number
        setattr(Temporary_List[i],'Order',0)
        #Patients with these conditions are classified at top priority (order = 1 is top priority)
        if((List[i].Asthmatic == 'Y' or List[i].Smoker == 'Y') and List[i].Age > 55):
            Temporary_List[i].Order = 1 #Set the order number to 1
            #Patients who are obese and have hypertension will be classified as top priority as well
        elif(List[i].Classification == 'Obese' and List[i].Hypertension == 'Y'):
            Temporary_List[i].Order = 1#Set the order number to 1
    
    for i in range(len(Temporary_List)):
        #Set a new attribute called NoConditions. It will store the number of conditions for each patient.
        #It will help the user to determine the order number for the rest of the patients
        setattr(Temporary_List[i],'NoConditions',0)
        if(Temporary_List[i].Smoker == 'Y'):
            Temporary_List[i].NoConditions = Temporary_List[i].NoConditions + 1
        if(Temporary_List[i].Asthmatic == 'Y'):
            Temporary_List[i].NoConditions = Temporary_List[i].NoConditions + 1
        if(Temporary_List[i].NJT_NGR == 'Y'):
            Temporary_List[i].NoConditions = Temporary_List[i].NoConditions + 1
        if(Temporary_List[i].Hypertension == 'Y'):
            Temporary_List[i].NoConditions = Temporary_List[i].NoConditions + 1
        if(Temporary_List[i].RenalRT == 'Y'):
            Temporary_List[i].NoConditions = Temporary_List[i].NoConditions + 1
        if(Temporary_List[i].IleostomyColostomy == 'Y'):
            Temporary_List[i].NoConditions = Temporary_List[i].NoConditions + 1
        if(Temporary_List[i].ParenteralNutrition == 'Y'):
            Temporary_List[i].NoConditions = Temporary_List[i].NoConditions + 1
    
    #Setting the order number for patients with zero conditions, one conditions, two conditions or more than two conditions
    for i in range(len(Temporary_List)):
        if(Temporary_List[i].NoConditions == 3):
            List[i].Order = 1#Top Priority
        if(Temporary_List[i].NoConditions == 2):
            List[i].Order = 2#Less priority,but they still have to refer to a dietitian
        if(Temporary_List[i].NoConditions == 1):
            List[i].Order = 3#Patients with 1 condition
        if(Temporary_List[i].NoConditions == 0):
            List[i].Order = 4#Low Priority
        

           
def main():
    print("Coursework B - Task 2")
    #Read the csv file
    read_csv_file()
    #Calculate the BMI
    Calculate_BMI_and_Classification(Patient_List)
    #Classify the patients
    Classification(Patient_List)
    print("Establish which patients need to be referred to a dietitian.")
    print("The patients assessed for a referral are the patients who has one from the following conditions: ",end = ' ')
    print("Obese OR Underweight, Hypertension, Asthmatic OR Smoker, NJT OR NGR, Renal Replacement Therapy, Ileostomy / Colostomy, Parenteral Nutrition")
    #Ranking the order of priority according to the rules given
    RankOrder(Patient_List)
    BreakLine()
    print("Print on Screen patient names of those that need to be referred to a dietitian")
    #Display the patients grouped by order number
    Referring_To_Dietitian(Patient_List)

    
if __name__ == "__main__":
    main()

