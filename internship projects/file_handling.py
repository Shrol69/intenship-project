import os

# Function to add employee information
def add_employee(file_name):
    with open(file_name, 'a') as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Employee Position: ")
        salary = input("Enter Employee Salary: ")
        file.write(f"{emp_id},{name},{position},{salary}\n")
        print("Employee added successfully!")

# Function to delete employee information
def delete_employee(file_name):
    emp_id = input("Enter Employee ID to delete: ")
    found = False
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    with open(file_name, 'w') as file:
        for line in lines:
            if line.split(',')[0] != emp_id:
                file.write(line)
            else:
                found = True
    
    if found:
        print("Employee deleted successfully!")
    else:
        print("Employee ID not found.")

# Function to display information of a particular employee
def display_employee(file_name):
    emp_id = input("Enter Employee ID to display: ")
    found = False
    with open(file_name, 'r') as file:
        for line in file:
            if line.split(',')[0] == emp_id:
                emp_details = line.strip().split(',')
                print(f"Employee ID: {emp_details[0]}")
                print(f"Name: {emp_details[1]}")
                print(f"Position: {emp_details[2]}")
                print(f"Salary: {emp_details[3]}")
                found = True
                break
    
    if not found:
        print("Employee ID not found.")

# Main function to interact with the user
def main():
    file_name = "employees.txt"
    
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Display Employee")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee(file_name)
        elif choice == '2':
            delete_employee(file_name)
        elif choice == '3':
            display_employee(file_name)
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
