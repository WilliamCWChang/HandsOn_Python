from pprint import pprint
'''
Give Head and leg number, this program return
the animal number to fit answer
'''
head = 10
leg = 24
# User can add mode animal in this dict.
animal = {
    # animal    : number
    "chicken"   : 2,
    "rabbit"    : 4,
    "ant"       : 6,
    "spider"    : 8,
    # "octopus" /   : 10
}
# head_weight = [2,4,6,8]
head_weight = animal.values()


#-Plan A-------------------------------------------------------------------------------------
all_possibles = [[]]
for animal_num in range(1,len(animal.values())+1):
    possible_buffer = []
    for head_possible in range(0,head+1):
        for possible in all_possibles:
            new_possible = possible[:]
            new_possible.append(head_possible)
            possible_buffer.append(new_possible)
    all_possibles = possible_buffer[:]



print("We have {0} heads, and {1} legs.".format(head, leg))
print("answer is ...")
answer = []
for possible in all_possibles:
    weight_number = [weight*pattern for weight, pattern in zip(animal.values(),possible)]
    if sum(weight_number) is leg and sum(possible) is head:
        answer.append(possible)
        print(possible)

print("We Get {0} answers.".format(len(answer)))

print("-------------------------------------------------------------------------------------")


#-Plan B-------------------------------------------------------------------------------------
import itertools
x = [[i for i in range(head)] for j in range(len(animal.values()))]
all_possibles = list(itertools.product(*x))



print("We have {0} heads, and {1} legs.".format(head, leg))
print("answer is ...")
answer = []
for possible in all_possibles:
    weight_number = [weight*pattern for weight, pattern in zip(animal.values(),possible)]
    if sum(weight_number) is leg and sum(possible) is head :
        answer.append(possible)
        print(possible)

print("We Get {0} answers.".format(len(answer)))