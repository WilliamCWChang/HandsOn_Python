class chicken:
    legs = 2

class rabbit:
    legs = 4

def chicken_and_rabbit(heads, legs):
    print("Heads = {0}, legs = {1}".format(heads, legs))
    for chicken_heads in range(heads+1):
        rabbit_heads = heads - chicken_heads
        if (rabbit_heads*rabbit.legs)+(chicken_heads*chicken.legs) is legs:
            print("chicken heads = {0}, rabbit heads = {1}".
                  format(chicken_heads, rabbit_heads))

if __name__ == "__main__":
    heads = 10
    legs = 24
    chicken_and_rabbit(heads, legs)
