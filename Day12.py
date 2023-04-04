# selection sort
def selectionSort(array,size):
    for step in range(size): # 0 [20,12,10,15,2]
        min_idx = step # min_idex = 0
        for i in range(step+1,size): # i =1
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i]< array[min_idx]:
                min_idx=i # 1 2 4
        # put minimum at the correct position
        (array[step],array[min_idx])=(array[min_idx],array[step])

data = [20,12,10,15,2]
size = len(data)
selectionSort(data,size)
print("Sorted array in Ascending order: ")
print(data)

#----------------------------------------------------------------------------------------------------------------------

class Employee:
    def __init__(self, emp_id, emp_name, basic_salary, qualification):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.basic_salary = basic_salary
        self.qualification = qualification

    def validate_basic_salary(self):
        if self.basic_salary > 3000:
            return True
        else:
            return False

    def validate_qualification(self):
        if self.qualification.lower() == "bachelors" or self.qualification.lower() == "masters":
            return True
        else:
            return False


class Graduate(Employee):
    def __init__(self, emp_id, emp_name, basic_salary, qualification, job_band, cgpa):
        super().__init__(emp_id, emp_name, basic_salary, qualification)
        self.job_band = job_band
        self.cgpa = cgpa

    def validate_job_band(self):
        if self.job_band.upper() in ["A", "B", "C"]:
            return True
        else:
            return False

    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.basic_salary
            incentive = 0
            if self.job_band.upper() == "A":
                incentive = 0.04 * self.basic_salary
            elif self.job_band.upper() == "B":
                incentive = 0.06 * self.basic_salary
            elif self.job_band.upper() == "C":
                incentive = 0.1 * self.basic_salary

            if self.cgpa >= 4 and self.cgpa <= 4.25:
                tpi = 1000
            elif self.cgpa > 4.25 and self.cgpa <= 4.5:
                tpi = 1700
            elif self.cgpa > 4.5 and self.cgpa <= 4.75:
                tpi = 3200
            elif self.cgpa > 4.75 and self.cgpa <= 5:
                tpi = 5000

            gross_salary = self.basic_salary + pf + tpi + incentive
            return gross_salary
        else:
            return -1

    def display(self):
        print("Employee Name: ",self.emp_name)
        print("Employee Id: ",self.emp_id)
        print("Employee Qualification: ",self.qualification)
        print("Employee Job_band: ",self.job_band)
        print("Employee CGPA: ",self.cgpa)
        print("Employee gross_Salary: ",self.calculate_gross_salary())


class Lateral(Employee):
    def __init__(self, emp_id, emp_name, basic_salary, qualification, job_band, skill_set):
        super().__init__(emp_id, emp_name, basic_salary, qualification)
        self.job_band = job_band
        self.skill_set = skill_set

    def validate_job_band(self):
        if self.job_band.upper() in ["D", "E", "F"]:
            return True
        else:
            return False

    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.basic_salary
            incentive = 0
            if self.job_band.upper() == "D":
                incentive = 0.13 * self.basic_salary
            elif self.job_band.upper() == "E":
                incentive = 0.16 * self.basic_salary
            elif self.job_band.upper() == "F":
                incentive = 0.2 * self.basic_salary

            sme_bonus = 0
            if self.skill_set.lower() == "agp":
                sme_bonus = 6500
            elif self.skill_set.lower() == "agpt":
                sme_bonus = 8200
            elif self.skill_set.lower() == "agdev":
                sme_bonus = 11500

            gross_salary = self.basic_salary + pf + sme_bonus+ incentive
            return gross_salary
        else:
            return -1

    def display(self):
        print("Employee Name: ",self.emp_name)
        print("Employee Id: ",self.emp_id)
        print("Employee Qualification: ",self.qualification)
        print("Employee Job_band: ",self.job_band)
        print("Employee Skill: ",self.skill_set)
        print("Employee gross_Salary: ",self.calculate_gross_salary())

e = Employee(101,"Ashirbad",10000,"bachelors")
g = Graduate(101,"Ashirbad",10000,"bachelors","A",5)
l = Lateral(102,"Sapana",15000,"bachelors","D","agp")
g.calculate_gross_salary()
g.display()
print("\nLateral Employee")
l.calculate_gross_salary()
l.display()

#----------------------------------------------------------------------------------------------------------------------

# Write a python program to implement BakeHouse class
class BakeHouse:
    def __init__(self):
        self.occupied_table_list = []

    def get_occupied_table_list(self):
        return self.occupied_table_list

    def allocate_table(self):
        for table_number in range(1, 11):
            if table_number not in self.occupied_table_list:
                self.occupied_table_list.append(table_number)
                return table_number
        return None

    def deallocate_table(self, table_number):
        if table_number in self.occupied_table_list:
            self.occupied_table_list.remove(table_number)

bh = BakeHouse()
print(bh.allocate_table())
print(bh.get_occupied_table_list())

print(bh.allocate_table())
print(bh.get_occupied_table_list())

bh.deallocate_table(1)
print(bh.get_occupied_table_list())

# --------------------------------------------------------------------------------------------------------------------

class ChildrenCamp:
    def __init__(self, child_id, chocolates_received):
        self.child_id = child_id
        self.chocolates_received = chocolates_received

    def calculate_total_chocolates(self):
        return sum(self.chocolates_received)

    def reward_child(self, child_id_rewarded, extra_chocolates):
        if extra_chocolates < 1:
            return "Extra chocolates is less than 1"
        if child_id_rewarded not in self.child_id:
            return "Child id is invalid"
        index = self.child_id.index(child_id_rewarded)
        self.chocolates_received[index] += extra_chocolates
        return self.chocolates_received

child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]

camp = ChildrenCamp(child_id, chocolates_received)
print(camp.calculate_total_chocolates())

print(camp.reward_child(30, 2))
print(camp.calculate_total_chocolates())

print(camp.reward_child(60, 2))

print(camp.reward_child(40, 0))

# --------------------------------------------------------------------------------------------------------------------

def partition(array,low,high): # [8,7,6,1,0,9,2]
    pivot = array[high] # 2
    i = low-1 # i=-1
    for j in range(low,high): # 0 to 5
        if array[j]<=pivot:
            i = i+1
            (array[i],array[j])=(array[j],array[i])

    # swap the pivot element with the graeter element specified between
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1
# function to perform quicksort
def quicksort(array,low,high): # low=0 high=6
    if low<high:
        # find pivot element such that element smaller than pivot are on the left and element greater than pivot are on the right
        pi = partition(array,low,high)

        # recursive call on the left of the pivot
        quicksort(array,low,pi-1)

        # recursive call on the left of the pivot
        quicksort(array,pi+1,high)

data=[8,7,6,1,0,9,2]
print("Unsorted Array")
print(data)
size = len(data)
quicksort(data,0,size-1)
print("Sorted Array in asscending order:")
print(data)
