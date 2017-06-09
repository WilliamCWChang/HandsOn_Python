class student:

    def __init__(self, n, g):
        self.name = n
        self.gender = g
        self.grades = []

    def add(self,grade):
        #do something.
        self.grades.append(grade)

    def avg(self):
        #do something.
        #return avg_grade
        if self.grades:
            return sum(self.grades)/len(self.grades)

    def fcount(self):
        #do something.
        #return fail_count
        cnt = 0
        for data in self.grades:
            if data < 60:
                cnt += 1
        return cnt

s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

print(s1.name + " " + s1.gender + ' ' + str(s1.avg()) + ' ' + str(s1.fcount()))
print(s1.grades)
print(s2.name + " " + s2.gender + ' ' + str(s2.avg()) + ' ' + str(s2.fcount()))
print(s2.grades)
print(s3.name + " " + s3.gender + ' ' + str(s3.avg()) + ' ' + str(s3.fcount()))
print(s3.grades)
print(s4.name + " " + s4.gender + ' ' + str(s4.avg()) + ' ' + str(s4.fcount()))
print(s4.grades)
print(s5.name + " " + s5.gender + ' ' + str(s5.avg()) + ' ' + str(s5.fcount()))
print(s5.grades)
