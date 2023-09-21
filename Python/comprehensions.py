nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# evens = []
# for num in nums:
#     if num % 2 == 0:
#         evens.append(num)

# print(evens)

# evens = [num for num in nums if num % 2 == 0]

[num * 2 for num in nums] # double num for each num in nums []
['HIIII' for num in nums]

# new_list = []
# for num in nums: 
#     new_list.append(num * 2)

# [what_to_append for thing in list]
    
# [2,4,6,8] # --> [4,16,36,64]
# [n * n for n in [2,4,6,8]]

# [char.upper() + '.' for char in'lmfao']

# [num for num in range(10,20)]

# [num/2 for num in range(10,20)]


def gen_board(size, initial_val=None):
    return[[initial_val for x in range(size)] for y in range(size)]


chickens = [
    {"name": 'Henry', "sex": 'Rooster'},
    {"name": 'Lady Gray', "sex": 'Hen'},
    {"name": 'Junior', "sex": 'Rooster'},
    {"name": 'Stevie Chicks', "sex": 'Hen'},
    {"name": 'Rocket', "sex": 'Hen'},
    {"name": 'Butters', "sex": 'Rooster'}
]

hens = [bird["name"] for bird in chickens if bird["sex"] == 'Hen']


scores = [55, 89, 99, 87, 60, 70, 74, 76, 90, 50, 82]
# ['FAIL', 'PASS', '']
# grades = ['PASS' for score in scores if score >= 70]
# do_this if something else do this for thing in things]
grades = ['PASS' if score >= 70 else 'FAIL' for score in scores]

def get_letter(ltr):
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    return MORSE_CODE_DICT.get(ltr.upper(), '')

msg = [ get_letter(char) for char in 'SOS']

def get_morse_code(phrase):
    return " | ".join([get_letter(char) for char in phrase])