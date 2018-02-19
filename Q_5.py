class Student:
    def __init__(self, name, sec):
        self.name = name
        self.sec = sec


    @classmethod
    def gen_stu_from_string(cls, inp):
        name, sec = inp.split("-")
        return cls(name, sec)


stu1 = Student.gen_stu_from_string(input("Enter input in the form of 'Name-Sec': "))

print(stu1.__dict__)
