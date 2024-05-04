import pickle
import tkinter as tk
from tkinter import ttk
import os

class EmployeeManagementGUI: # Generating a class to print the GUI
    def __init__(self, data_layer):
        self.data_layer = data_layer
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Employee Management System")

        # Add labels and fields for entering employee name.
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)
        # Add labels and fields for entering employee ID.
        self.employee_id_label = tk.Label(self.root, text="Employee ID:")
        self.employee_id_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.employee_id_entry = tk.Entry(self.root)
        self.employee_id_entry.grid(row=1, column=1)
        # Add labels and fields for entering employee department.
        self.department_label = tk.Label(self.root, text="Department:")
        self.department_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.department_entry = tk.Entry(self.root)
        self.department_entry.grid(row=2, column=1)
        # Add labels and fields for entering employee job title.
        self.job_title_label = tk.Label(self.root, text="Job Title:")
        self.job_title_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.job_title_entry = tk.Entry(self.root)
        self.job_title_entry.grid(row=3, column=1)
        # Add labels and fields for entering employee basic salary.
        self.basic_salary_label = tk.Label(self.root, text="Basic Salary:")
        self.basic_salary_label.grid(row=4, column=0, sticky=tk.W, pady=5)
        self.basic_salary_entry = tk.Entry(self.root)
        self.basic_salary_entry.grid(row=4, column=1)
        # Add labels and fields for entering employee age.
        self.age_label = tk.Label(self.root, text="Age:")
        self.age_label.grid(row=5, column=0, sticky=tk.W, pady=5)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=5, column=1)
        # Add labels and fields for entering employee date of birth.
        self.date_of_birth_label = tk.Label(self.root, text="Date Of Birth:")
        self.date_of_birth_label.grid(row=6, column=0, sticky=tk.W, pady=5)
        self.date_of_birth_entry = tk.Entry(self.root)
        self.date_of_birth_entry.grid(row=6, column=1)
        # Add labels and fields for entering employee passport details.
        self.passport_details_label = tk.Label(self.root, text="Passport Details:")
        self.passport_details_label.grid(row=7, column=0, sticky=tk.W, pady=5)
        self.passport_details_entry = tk.Entry(self.root)
        self.passport_details_entry.grid(row=7, column=1)

        # Add employee to the GUI
        self.add_employee_button = tk.Button(self.root, text="Add Employee", command=self.add_employee)
        self.add_employee_button.grid(row=8, column=0, pady=5)
        # Delete employee from the GUI
        self.display_employee_button = tk.Button(self.root, text="Delete Employee ", command=self.delete_employee)
        self.display_employee_button.grid(row=8, column=1, pady=5)
        # Modify employee to the GUI
        self.modify_employee_button = tk.Button(self.root, text="Modify Employee", command=self.modify_employee)
        self.modify_employee_button.grid(row=9, column=0, pady=5)
        # Display employee to the GUI
        self.display_employee_details_button = tk.Button(self.root, text="Display Employee Details", command=self.display_employee)
        self.display_employee_details_button.grid(row=9, column=1, pady=5)

        self.root.mainloop()

    def add_employee(self):
        self.nameEmployee.add_employee(0, tk.END)
        self.employeeID.add_employee(0, tk.END)
        self.department.add_employee(0, tk.END)
        self.jobTitle.add_employee(0, tk.END)
        self.basicSalary.add_employee(0, tk.END)
        self.age.add_employee(0, tk.END)
        self.dateOfBirth.add_employee(0, tk.END)
        self.passportDetails.add_employee(0, tk.END)


    def delete_employee(self):
        self.nameEmployee.delete_employee(0, tk.END)
        self.employeeID.delete_employee(0, tk.END)
        self.department.delete_employee(0, tk.END)
        self.jobTitle.delete_employee(0, tk.END)
        self.basicSalary.delete_employee(0, tk.END)
        self.age.delete_employee(0, tk.END)
        self.dateOfBirth.delete_employee(0, tk.END)
        self.passportDetails.delete_employee(0, tk.END)

    def modify_employee(self):
        self.nameEmployee.modify_employee(0, tk.END)
        self.employeeID.modify_employee(0, tk.END)
        self.department.modify_employee(0, tk.END)
        self.jobTitle.modify_employee(0, tk.END)
        self.basicSalary.modify_employee(0, tk.END)
        self.age.modify_employee(0, tk.END)
        self.dateOfBirth.modify_employee(0, tk.END)
        self.passportDetails.modify_employee(0, tk.END)


    def display_employee(self):
        employee_details = { # Attributes of employee class using getter method
            "Name": self.name_entry.get(),
            "Employee ID": self.employee_id_entry.get(),
            "Department": self.department_entry.get(),
            "Job Title": self.job_title_entry.get(),
            "Basic Salary": self.basic_salary_entry.get(),
            "Age": self.age_entry.get(),
            "Date of Birth": self.date_of_birth_entry.get(),
            "Passport Details": self.passport_details_entry.get()
        }

        display_window = tk.Toplevel(self.root)
        display_window.title("Employee Details")

        employee_table = ttk.Treeview(display_window)
        employee_table['columns'] = tuple(employee_details.keys())
        for column in employee_table['columns']:
            employee_table.heading(column, text=column)
            employee_table.column(column, anchor='center')
        employee_table.grid(row=0, column=0, sticky='nsew')

        employee_table.insert('', 'end', values=tuple(employee_details.values()))

        display_window.mainloop()

class Employee:
    def __init__(self, nameEmployee, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails): # Attributes of employee class
        self.__nameEmployee = nameEmployee
        self.__employeeID = employeeID
        self.__department = department
        self.__jobTitle = jobTitle
        self.__basicSalary = basicSalary
        self.__age = age
        self.__dateOfBirth = dateOfBirth
        self.__passportDetails = passportDetails

    # Setter methods
    def setNameEmployee(self, nameEmployee):
        self.__nameEmployee = nameEmployee

    def setEmployeeID(self, employeeID):
        self.__employeeID = employeeID

    def setDepartment(self, department):
        self.__department = department

    def setJobTitle(self, jobTitle):
        self.__jobTitle = jobTitle

    def setBasicSalary(self, basicSalary):
        self.__basicSalary = basicSalary

    def setAge(self, age):
        self.__age = age

    def setDateOfBirth(self, dateOfBirth):
        self.__dateOfBirth = dateOfBirth

    def setPassportDetails(self, passportDetails):
        self.__passportDetails = passportDetails

    # Getter methods
    def getNameEmployee(self):
        return self.__nameEmployee

    def getEmployeeID(self):
        return self.__employeeID

    def getDepartment(self):
        return self.__department

    def getJobTitle(self):
        return self.__jobTitle

    def getBasicSalary(self):
        return self.__basicSalary

    def getAge(self):
        return self.__age

    def getDateOfBirth(self):
        return self.__dateOfBirth

    def getPssportDetails(self):
        return self.__passportDetails
class DataLayer: # Creating a class to input the pickle file
    def __init__(self, filename):
        self.filename = filename

    # Read all employees data from the pickle file
    def read_all_employees(self):
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'rb') as file:
                employees = pickle.load(file)
            return employees

    # Write employees data to the pickle file
    def write_employees_to_file(self, employees):
        with open(self.filename, 'wb') as f:
            pickle.dump(employees, f)

# Printing the GUI
filename = "employees.pkl"
# Create an instance of the DataLayer class
dt = DataLayer(filename)
# Initialize the EmployeeManagementGUI using the DataLayer instance
management = EmployeeManagementGUI(dt)