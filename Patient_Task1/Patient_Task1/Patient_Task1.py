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
    print("Patient Name      Date of Birth      Sex      Height(m)      Weight(kg)      BodyBuild        Conditions         BMI")
    for i in range(len(List)):
        print(List[i].Patient_Name + "             " + List[i].DateofBirth + "         " +List[i].Sex +
              "            " + List[i].Height + "         " + List[i].Weight + "            " + List[i].BodyBuild + "            "
              + List[i].Smoker,List[i].Asthmatic,List[i].NJT_NGR,List[i].Hypertension,List[i].RenalRT,List[i].IleostomyColostomy,List[i].ParenteralNutrition,end =" ")
        print("   ",List[i].BMI)

# Display_Patient(Patient) will print on the screen the patient and his/her details.
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
    #Display 10 rows and then break a line
    print("Name     Age     BMI     Classification")
    k = 0 #Count how many rows we have displayed
    for row in TemporaryList:#For each patient
        #Print the name,age, BMI and classification for each patient
        print(row.Patient_Name," ",row.Age,"   ",row.BMI,"    ",row.Classification)
        k = k + 1#Increment the counter
        if( k == 10 ):#If 10 patients were displayed, the break a line and set the counter back to 0
            print()
            k = 0

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
            if( L[i].BMI < L[j].BMI):# Sort the List L by BMI in DESCENDING order
                # After finding the lowest item of the unsorted regions, swap with the first unsorted item
                aux = L[i]
                L[i] = L[j]
                L[j] = aux

# Display_Worst_Underweight_and_Obese(List) will display the worse 5 cases for underweight and obese people , grouped by their sex
def Display_Worst_Underweight_and_Obese(List):
    #Create 2 lists and the counters for each list. We will store the 5 cases in these 2 lists
    Underweight = []
    countUnderweight = 0
    Obese = []
    countObese = 0
    for i in range(len(List)):#for each patients
        if(List[i].Classification == 'Underweight'):#check if the patients is underweight
            #If so, then we will add the patients into underweight list
            countUnderweight = countUnderweight + 1
            Underweight.append(List[i])
        if(List[i].Classification == 'Obese'):#check if the patient is obese
            #If so, then we will add the patients into obese list
            countObese = countObese + 1
            Obese.append(List[i])

    if(countUnderweight == 0):#Check if we have underweight people in the list
        print("No records for underweight people")
    else:#If we do:
        #We sort the list decreasing by BMI
        #Underweight.sort(key = lambda x: x.BMI, reverse = True)
        Selection_Sort(Underweight)
        #Creating a counter to check if we have stored the 5 patients into temporary List
        k = 0
        #Temporary List will store the first 5 patients with the worse condition.
        #Display the women first:
        print("Female with underweight conditions:")
        print("Name     Age     Sex     BMI     Classification")
        for i in range(len(Underweight)):
            if(k == 5):
                   break
            if(Underweight[i].Sex == 'F'):#if the patient sex is Female, then we will display the patient
                print(Underweight[i].Patient_Name," ",Underweight[i].Age,"     ",Underweight[i].Sex,"   ",Underweight[i].BMI,"   ",Underweight[i].Classification)
                k = k + 1
        #Then we display the men
        k = 0
        print("Men with underweight condition")
        print("Name     Age     Sex     BMI     Classification")
        for i in range(len(Underweight)):
             if(k == 5):
                   break
             if(Underweight[i].Sex == 'M'):#if the patient sex is Female, then we will display the patient
                print(Underweight[i].Patient_Name," ",Underweight[i].Age,"     ",Underweight[i].Sex,"   ",Underweight[i].BMI,"   ",Underweight[i].Classification)
                k = k + 1

    BreakLine()
    if(countObese == 0):#Check if we have obese people in the list
        print("No records for obese people")
    else:#If we do:
        #We sort the list decreasing by BMI
        #Obese.sort(key = lambda x: x.BMI, reverse = True)
        Selection_Sort(Obese)
        #Creating a counter to check if we have stored the 5 patients into temporary List
        k = 0
        #Display the women first:
        print("Female with obese conditions:")
        print("Name     Age     Sex     BMI     Classification")
        for i in range(len(Obese)):
            if(k == 5):
                   break
            if(Obese[i].Sex == 'F'):#if the patient sex is Female, then we will display the patient
                print(Obese[i].Patient_Name," ",Obese[i].Age,"     ",Obese[i].Sex,"   ",Obese[i].BMI,"   ",Obese[i].Classification)
                k = k + 1
        print("Men with obese condition")
        print("Name     Age     Sex     BMI     Classification")
        for i in range(len(Obese)):
            if(k == 5):
                   break
            if(Obese[i].Sex == 'M'):#if the patient sex is Male, then we will display the patient
                print(Obese[i].Patient_Name," ",Obese[i].Age,"     ",Obese[i].Sex,"   ",Obese[i].BMI,"   ",Obese[i].Classification)
                k = k + 1

def main():
    print("Coursework B - Task 1")
    read_csv_file()
    #print("Displaying the data")
    #Print_Data(Patient_List)
    #BreakLine()
    #Calculating the BMI and adding the value into the data structure
    Calculate_BMI_and_Classification(Patient_List)
    #Displaying the data after Classification and BMI were added into the class Patient
    print("Displaying the data after it was added the BMI")
    Print_Data_with_BMI_and_Classification(Patient_List)
    BreakLine()
    #Display the patient details (name,age,BMI and weight classification)
    print("Display the patient name, age, BMI, and weight classification.")
    Classification(Patient_List)
    BreakLine()
    #Display the worst cases of underweight and obese people by categories , Male and Female
    print("Print on screen the worst 5 underweight and the worst 5 obese patients in two groupings, male and female. ")
    BreakLine()
    Display_Worst_Underweight_and_Obese(Patient_List)
    BreakLine()

if __name__ == "__main__":
    main()
