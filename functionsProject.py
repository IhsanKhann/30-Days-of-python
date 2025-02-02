# Function to calculate the average of a list of numbers
def Avg_Cal(marks):
    avg = sum(marks) / len(marks)
    return avg

# Function to get user input and store data in a dictionary
def User_Input():
    Names = []
    Values = []
    
    while True:
        choice = int(input("Press 1 to proceed, 0 to exit: "))
        if choice == 0:
            break
        else:
        # Get student name
            name = input("Enter name: ")
            Names.append(name)
        
        # Get marks for the student (for example, 3 marks)
            Marks = []
            for i in range(3):
                mark = int(input(f"Enter mark {i+1}: "))
                Marks.append(mark)
            Values.append(Marks)
    
    # Create a dictionary mapping names to their marks
    Data = dict(zip(Names, Values))
    return Data

# Function to display each student's details along with their average marks
def Display(Data):
    for name, marks in Data.items():
        average = Avg_Cal(marks)  # Calculate the average for the current student's marks
        print("Name:", name)
        print("Marks:", marks)
        print("Average Marks:", average)
        print("----------")

# Main program: gather data and display results
Data = User_Input()   # Get student data
Display(Data)         # Display student details and average marks
