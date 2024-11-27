# Modules
import random
import pandas as pd


# Main Code
class Employee:
    """Represents an employee with ID, name, and salary details."""

    def __init__(self, id_no, name, basic, gross=0, net=0):
        self.id_no = id_no
        self.name = name
        self.basic = basic
        self.gross = gross
        self.net = net

    def calc_salary(self):
        """Calculate gross and net salary for the employee."""

        hra = 0.5 * self.basic
        da = 0.5 * self.basic
        pf = 0.12 * (self.basic + da)
        pt = 200
        travel = 0.1 * self.basic
        bonus = (1 / 12) * self.basic
        other = 0.2 * self.basic
        tax = 0.1 * self.basic

        self.gross = round(self.basic + hra + da + travel + bonus + other, 2)
        self.net = round(self.gross - tax - pf - pt, 2)

    def display(self):
        """Returns the gross and net salary of the employee."""

        return f"ID: {self.id_no}, Name: {self.name}, Gross: {self.gross}, Net: {self.net}"


def read_data(path):
    """Reads employee data from a CSV file and returns a list of Employee objects."""

    # Variables Initialization
    empty_cells, neg_sal, diff_datatype = 0, 0, 0
    employees = []

    # Load the data set
    try:
        df = pd.read_csv(path)
    except:
        return [], [empty_cells, neg_sal, diff_datatype]  # Return Empty if the file does not exist

    entries = len(df)
    df = df.dropna()  # Removes rows with missing entries
    valid_entries = len(df)

    empty_cells = entries - valid_entries

    # valid entries separated into respected list of variables
    id_no, names, basic = list(df[df.columns[0]]), list(df[df.columns[1]]), list(df[df.columns[2]])

    for i in range(len(id_no)):
        # Check the datatype of the inputs
        if isinstance(id_no[i], int) and isinstance(names[i], str) and isinstance(basic[i], float):
            if basic[i] > 0:  # Removes the non-positive salaries
                emp = Employee(id_no[i], names[i], basic[i])
                emp.calc_salary()
                employees.append(emp)
            else:
                neg_sal += 1
        else:
            diff_datatype += 1

    return employees, [empty_cells, neg_sal, diff_datatype]


def divide(array):
    """Recursively divides an array to find the minimum and maximum values."""

    if len(array) == 1:
        return [array[0], array[0]]

    mid = len(array) // 2

    left, right = array[:mid], array[mid:]
    min1, max1 = divide(left)
    min2, max2 = divide(right)

    return [min(min1, min2), max(max1, max2)]


def random_sampling(employees):
    """Selects a random sample of 10 employees and displays the ones with minimum and maximum gross salaries."""

    employees_list = random.sample(employees, 10)
    gross_salaries = []

    for i in employees_list:
        gross_salaries.append(i.gross)

    min_sal, max_sal = divide(gross_salaries)

    for i in employees_list:
        if min_sal == i.gross:
            print(f"Min Salary: {i.display()}")
        if max_sal == i.gross:
            print(f"Max Salary: {i.display()}")


def main():
    """Main execution block."""

    file_path = [r"C:\Users\Krish\Downloads\Salary.csv",
                 r"C:\Users\Krish\Downloads\Empty.csv",
                 r"C:\Users\Krish\Downloads\Reversed.csv",
                 r"C:\Users\Krish\Downloads\Negative Salary.csv",
                 r"C:\Users\Krish\Downloads\Salary 2.csv"]

    for i in range(len(file_path)):
        employee_list, errors = read_data(file_path[i])
        print("TestCase " + str(i + 1) + ": ")
        if len(employee_list) >= 1:
            random_sampling(employee_list)
        else:
            print("The file does not contain valid data!!")

        print(f"Empty Cells: {errors[0]}, Non Positive Salaries: {errors[1]}, Invalid Datatypes: {errors[2]}")
        print()


if __name__ == "__main__":
    main()
