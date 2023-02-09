""" 
File m4.py for exam 2022-10-28


Name: Joakim Svensson


"""
import random
import math
import json

# A7
def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

def birthdays(n_people):
    '''Modify this method'''
    fx = lambda n_people : 1-fac(365)/fac(365-n_people)/(365**n_people)
    fx_solve = fx(n_people)
    if random.random() < fx_solve:
        return 1
    else:
        return 0

# A8


def birthdays_theoretical(n_people):
    '''Use this method if you have not solved A7'''
    return 1 if random.random() < 1-math.factorial(365)/math.factorial(365-n_people)/(365**n_people) else 0


# def print_birthday_statistics(n_peoples, n_samples, n_processes):
#     '''Modify this method'''
#     import concurrent.futures as future
#     with future.ThreadPoolExecutor() as ex:
#         result = list(ex.map(birthdays_theoretical, n_processes))
#         print(result)

#B4


def get_name(index):
    '''
    Example code how to extract a field (here 'name') for a person with index 'index' from customers.json file (index is 0,...,111 for the different people).
    '''
    with open('/Users/jockepolis/Desktop/UPPSALA/År 4/Progg 2/Tentamen/customers.json') as f:
        data = json.load(f)
        return data[index]['name']

def get_gender(index):
    import json
    with open('/Users/jockepolis/Desktop/UPPSALA/År 4/Progg 2/Tentamen/customers.json') as f:
        data = json.load(f)
        if data[index]['gender'] == 'male':
            return 0 
        else:
            return 1

def get_favoriteFruit(index):
    import json
    with open('/Users/jockepolis/Desktop/UPPSALA/År 4/Progg 2/Tentamen/customers.json') as f:
        data = json.load(f)
        return str(data[index]['favoriteFruit'])
    
def print_favoriteFruits_per_gender(jsonfile, n, n_processes):
    '''Modify this method'''
    fruits_male = {}
    fruits_female = {}
    for index in range(112):
        gender = get_gender(index)
        favoriteFruit = get_favoriteFruit(index)
        if gender == 0:
            fruits_male += favoriteFruit
        else:
            fruits_female += favoriteFruit
    for key, value in fruits_male():
        print(key, ' : ', value)
    for key, value in fruits_female():
        print(key, ' : ', value)

    


if __name__ == '__main__':
    print('\n-------\nA7:\n-------')
    print(birthdays(5))   # most probably 0
    print(birthdays(23))  # about 50/50 0 or 1
    print(birthdays(100))  # most probably 1

    print('\n-------\nA8:\n-------')
    # print_birthday_statistics(range(15, 30), 10000, 4)

    print('\n-------\nB4:\n-------')
    # print_favoriteFruits_per_gender('customers.json', 112, 5)
    print(print_favoriteFruits_per_gender)
