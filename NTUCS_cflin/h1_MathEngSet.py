math = {"Tom", "John", 'Mary', 'Jimmy', 'Sunny', 'Amy'}
eng = {'John', 'Mary','Tony' ,'Bob' ,'Pony', 'Tom' , 'Alice'}


member = math | eng
allpass = math & eng
print("-Q1------------------------------------------")
print("math pass", end=" = ")
print(math)
print("eng pass" , end = " = ")
print(eng)
print("math is pass and eng is not pass")
print(math - allpass)
print("math is not pass and eng is pass")
print(eng - allpass)
print("All pass")
print(allpass)
print("How many people in our class")
print(len(member))
print("-Q2------------------------------------------")

score = {'Tom':[80, 100, 90, 95], 'John':[100,93,75,80]}
for name in score:
    print(name, end=" = ")
    avg = 0
    for data in score[name]:
        avg += (data/len(score[name]))
    print(str(avg) + ' in ' + str(score[name]))





