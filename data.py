# from students import Students


class Data:
    def __init__(
        self, iid, name, age, grade, number, email, department, year, checked, courses
    ):
        self.iid = iid
        self.name = name
        self.age = age
        self.grade = grade
        self.number = number
        self.email = email
        self.department = department
        self.year = year
        self.checked = checked
        self.courses = courses
        # Students.update_table(Students)


# data_std = {}
# data_std[255] = Student_Data(
#     255, "omnia", "age", "4", "number", "email", "department", 5, "male", []
# )
# data_std[66] = Student_Data(
#     255, "omnia", "age", "4", "number", "email", "department", 5, "male", []
# )
# print(len(data_std))
# print("data: ", data_std[255].grade)
