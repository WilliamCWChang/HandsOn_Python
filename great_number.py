import random

dict_for_kuo = {
	1:"坤為地",
	2:"山地剝",
	3:"水地比",
	4:"風地觀",
	5:"雷地豫",
	6:"火地晉",
	7:"澤地萃",
	8:"天地否",
	9:"地山謙",
	10: "艮為山",
	11: "水山蹇",
	12: "風山漸",
	13: "雷山小過",
	14: "火山旅",
	15: "澤山咸",
	16: "天山遯",
	17: "地水師",
	18: "山水蒙",
	19: "坎為水",
	20: "風水渙",
	21: "雷水解",
	22: "火水未濟",
	23: "澤水困",
	24: "天水訟",
	25: "地風升",
	26: "山風蠱",
	27: "水風井",
	28: "巽為風",
	29: "雷風恆",
	30: "火風鼎",
	31: "澤風大過",
	32: "天風姤",
	33: "地雷復",
	34: "山雷頤",
	35: "水雷屯",
	36: "風雷益",
	37: "震為雷",
	38: "火雷噬嗑",
	39: "澤雷隨",
	40: "天雷無妄",
	41: "地火明夷",
	42: "山火賁",
	43: "水火既濟",
	44: "風火家人",
	45: "雷火豐",
	46: "離為火",
	47: "澤火革",
	48: "天火同人",
	49: "地澤臨",
	50: "山澤損",
	51: "水澤節",
	52: "風澤中孚",
	53: "雷澤歸妹",
	54: "火澤睽",
	55: "兌為澤",
	56: "天澤履",
	57: "地天泰",
	58: "山天大畜",
	59: "水天需",
	60: "風天小畜",
	61: "雷天大壯",
	62: "火天大有",
	63: "澤天夬",
	64: "乾為天",
}


def control(data):
	left_table = round(data*random.random())
	right_table = data-left_table
	left_table = left_table - 1 
	left_hand = 1
	left_hand = (lambda  x: 4 if x==0 else x)(left_table%4) + left_hand
	right_hand = (lambda  x: 4 if x==0 else x)(right_table%4)
	data = data-left_hand-right_hand
	return data

def get_number():
	data = 50
	data = data-1
	for index in range(3):
		data = control(data)
		# print(index, data)
	return int(data/4)

def get_a_kuo():
	data = []
	for index in range(6):
		data.append(get_number())
	return data

import numpy
def kuo_analysis(kuo):
	if len(kuo) != 6:
		raise AssertionError(kuo, "number fail")
	start = numpy.array(kuo)
	change = numpy.array(kuo)
	start = start%2
	change = (abs(change-7.5)-0.5).astype(int)
	# print(start.tolist(), change.tolist())

	test = numpy.array([5,4,3,2,1,0])	
	start_number = sum(2**test*start)+1

	return start.tolist(), change.tolist(), start_number


kuo = get_a_kuo()
start, change, start_number= kuo_analysis(kuo)
print(start, change, start_number, dict_for_kuo[start_number])
