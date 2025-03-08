import json  # Library for working with JSON data (saving and loading)
import os    # Library for interacting with the operating system (file handling)

# Function to display the main menu
def display_menu():
    """
    Displays the main menu options for the Student Grade Tracker.
    Users can choose from options like adding grades, viewing grades,
    calculating averages, saving/loading data, or exiting the program.
    """
    print("\n--- Student Grade Tracker ---")
    print("1. Add Grades for a Student")
    print("2. View Grades")
    print("3. Calculate Averages")
    print("4. Save Data to File")
    print("5. Load Data from File")
    print("6. Exit")

# Function to add grades for a student
def add_grades(students):
    """
    Allows the user to input grades for a specific student and their subjects.
    The grades are stored in a dictionary where the student's name is the key,
    and the value is another dictionary mapping subjects to grades.
    """
    name = input("Enter student name: ").strip()  # Get the student's name
    if name not in students:
        students[name] = {}  # Initialize an empty dictionary for the student if they don't exist
    
    while True:
        subject = input("Enter subject name (or type 'done' to finish): ").strip()  # Get the subject name
        if subject.lower() == 'done':  # Exit the loop if the user types 'done'
            break
        try:
            grade = float(input(f"Enter grade for {subject}: "))  # Get the grade as a float
            if 0 <= grade <= 100:  # Ensure the grade is within the valid range
                students[name][subject] = grade  # Store the grade in the dictionary
            else:
                print("Grade must be between 0 and 100.")  # Error message for invalid range
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")  # Error message for non-numeric input

# Function to view grades
def view_grades(students):
    """
    Displays all the grades entered so far for each student and their subjects.
    If no grades have been entered, it notifies the user.
    """
    if not students:  # Check if the students dictionary is empty
        print("No grades available.")
        return
    
    print("\n--- Grades ---")
    for name, subjects in students.items():  # Loop through each student and their subjects
        print(f"\nStudent: {name}")  # Display the student's name
        for subject, grade in subjects.items():  # Loop through each subject and grade
            print(f"{subject}: {grade}")  # Display the subject and grade

# Function to calculate averages
def calculate_averages(students):
    """
    Calculates and displays the average grade for each student.
    If a student has no grades, it notifies the user.
    """
    if not students:  # Check if the students dictionary is empty
        print("No grades available.")
        return
    
    print("\n--- Averages ---")
    for name, subjects in students.items():  # Loop through each student and their subjects
        if subjects:  # Check if the student has any grades
            average = sum(subjects.values()) / len(subjects)  # Calculate the average grade
            print(f"{name}: {average:.2f}")  # Display the student's name and average
        else:
            print(f"{name}: No grades available.")  # Notify if no grades are available

# Function to save data to a file
def save_data(students):
    """
    Saves the current data (students and their grades) to a JSON file.
    The user specifies the filename, and the data is written in JSON format.
    """
    filename = input("Enter filename to save data (e.g., data.json): ").strip()  # Get the filename from the user
    try:
        with open(filename, 'w', encoding='utf-8') as file:  # Open the file in write mode with UTF-8 encoding
            json.dump(students, file, indent=4)  # Write the data to the file in JSON format with indentation
        print(f"Data saved to {filename}.")  # Confirm successful save
    except Exception as e:
        print(f"Error saving data: {e}")  # Handle errors during saving

# Function to load data from a file
def load_data():
    """
    Loads previously saved data (students and their grades) from a JSON file.
    The user specifies the filename, and the data is read into the program.
    Handles issues like missing files, invalid JSON, empty files, and hidden characters.
    """
    filename = input("Enter file Path to load data (e.g., data.json): ").strip()  # Get the filename from the user
    
    # Check if the file exists
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return {}
    
    # Check if the file is empty
    if os.path.getsize(filename) == 0:
        print(f"File '{filename}' is empty.")
        return {}
    
    try:
        print(f"Attempting to open file: {filename}")
        with open(filename, 'r', encoding='utf-8') as file:  # Open the file in read mode with UTF-8 encoding
            print("File opened successfully. Parsing JSON...")
            students = json.load(file)  # Parse the JSON data into a Python dictionary
            print(f"Data loaded successfully from {filename}.")
            return students
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format in file: {filename}. Error: {e}")
    except Exception as e:
        print(f"Error loading data from file: {filename}. Error: {e}")
    
    return {}

# Main function
def main():
    """
    The main function controls the flow of the program.
    It displays the menu, processes user choices, and calls the appropriate functions.
    The program runs in a loop until the user chooses to exit.
    """
    students = {}  # Dictionary to store student grades (student_name -> {subject -> grade})
    
    while True:
        display_menu()  # Display the main menu
        choice = input("Enter your choice: ").strip()  # Get the user's choice
        
        if choice == '1':
            add_grades(students)  # Call the function to add grades
        elif choice == '2':
            view_grades(students)  # Call the function to view grades
        elif choice == '3':
            calculate_averages(students)  # Call the function to calculate averages
        elif choice == '4':
            save_data(students)  # Call the function to save data to a file
        elif choice == '5':
            students = load_data()  # Call the function to load data from a file
        elif choice == '6':
            print("Exiting the program. Goodbye!")  # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

# Run the program
if __name__ == "__main__":
    main()  # Start the program by calling the main function