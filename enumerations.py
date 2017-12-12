from enum import Enum, auto, unique
@unique
class Shake(Enum):
    VANILLA = auto()
    CHOCOLATE = auto()
    COOKIES = 5
    MINT = 5



def main():
	list(Shake)
	for shake in Shake:
	    print(repr(shake))



if __name__ == "__main__":
    main()