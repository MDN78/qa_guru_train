import math


def points(games):
    counter = 0
    for i in games:
        resp = i.split(':')
        if int(*resp[0]) > int(*resp[1]):
            counter += 3
        elif int(*resp[0]) == int(*resp[1]):
            counter += 1
    return counter


points(["3:1", "3:2", "4:1"])

'''
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
'''


def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'


'''
The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.
'''


def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    arr.sort()
    highest = arr[-1]
    lowest = arr[0]
    arr.remove(highest)
    arr.remove(lowest)
    return sum(i for i in arr)


p = sum_array([6, 0, 1, 10, 10])
print(p)


def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)


def feast(beast, dish):
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False


feast("great blue heron", "garlic naan")


def feast(beast, dish):
    return beast.startswith(dish[0]) and beast.endswith(dish[-1])


def count_sheep(n):
    count = ''
    if n > 0:
        for i in range(1, n + 1):
            str = f'{i} sheep...'
            count += str
    else:
        return count
    return count


f = count_sheep(0)
print(f)


def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n + 1))


def square_sum(numbers):
    counter = 0
    for i in numbers:
        counter += i ** 2
    return counter


t = square_sum([0, 3, 4, 5])
print(t)


def square_sum(numbers):
    return sum(x ** 2 for x in numbers)


def are_you_playing_banjo(name):
    if name.lower().startswith('r'):
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'


t = are_you_playing_banjo('Rex')
print(t)

array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]


def count_sheeps(sheep):
    counter = 0
    for i in sheep:
        if i == True:
            counter += 1
        elif i == 'null' or i == 'undefined':
            pass
    return counter


t = count_sheeps(array1)

print(t)


def add_binary(a, b):
    return format((a + b), 'b')


t = add_binary(1, 1)
print(t)


def digitize(n):
    arr = []
    for i in str(n):
        arr.append(int(i))
    return arr[::-1]


t = digitize(5434)

print(t)


def filter_list(l):
    lst = []
    for i in l:
        if type(i) is int:
            lst.append(i)

    return lst


t = filter_list([1, 2, 'a', 'b'])
print(t)


def filter_list(l):
    'return a new list with the strings filtered out'
    return [i for i in l if not isinstance(i, str)]


def lovefunc(flower1, flower2):
    return (flower1 % 2 == 0) != (flower2 % 2 == 0)


t = lovefunc(0, 0)
print(t)


def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
        else:
            return False
    else:
        return False


t = validate_pin('1234')
print(t)


def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


def solution(text, ending):
    n = len(ending)
    if text[-n:] == ending:
        return True
    else:
        return False
    # print(text[-2:])


e = solution('tort', 'ort')
print(e)


def solution(string, ending):
    return string.endswith(ending)


def make_negative(number):
    return int(abs(number) / -1)


t = make_negative(0)
print(t)


def make_negative(number):
    # return negative of number. BUT: negative in = negative out. zero remains zero
    return -abs(number)


def get_sum(a, b):
    if a == b:
        return a
    elif abs(a) > abs(b):
        start = b
        end = a
    else:
        start = a
        end = b
    total = 0
    for i in range(start, end + 1):
        total += i
    return total


def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


t = get_sum(-1, 2)
print(t)


def repeat_str(repeat, string):
    # for i in range(repeat):
    return ''.join(f'{string}' for i in range(repeat))


t = repeat_str(4, 'a')
print(t)


def repeat_str(repeat, string):
    return repeat * string


def find_smallest_int(arr):
    return min(arr)


t = find_smallest_int([78, 56, 232, 12, 11, 43])
print(t)


def findSmallestInt(arr):
    arr.sort()
    return arr[0]


def no_space(x):
    lst = []
    for i in x:
        if i == ' ':
            pass
        else:
            lst.append(i)

    my_string = ''.join(map(str, lst))

    return my_string


t = no_space("8 j 8   mBliB8g  imjB8B8  jl  B")
print(t)


def no_space(x):
    return x.replace(' ', '')


def no_space(x):
    return "".join(x.split())


def maps(a):
    return [i * 2 for i in a]


t = maps([1, 2, 3])

print(t)


def litres(time):
    return math.floor(time * 0.5)


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if mpg * fuel_left >= distance_to_pump else False


t = zero_fuel(50, 25, 2)
print(t)


def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def positive_sum(arr):
    counter = 0
    for i in arr:
        counter += abs(i)
    return counter


def positive_sum(arr):
    return sum(x for x in arr if x > 0)


def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"


def array_diff(a, b):
    lst = []
    for i in a:
        if i != b[0]:
            lst.append(i)
    return lst


t = array_diff([1, 2], [1])
print(t)


# def square_digits(num):
#     n = []
#     while num > 0:
#         n.append(num % 10)
#         num = num // 10
#
#     return int(''.join(f'{int(i) ** 2}' for i in n))

def square_digits(num):
    r = ''
    for i in str(num):
        r = r + str((int(i)) ** 2)
    return int(r)


t = square_digits(9119)
print(t)


# def order(sentence):
#   t = sentence.split(' ')
#
#   return t

def order(sentence):
    words = []
    for i in range(1, 10):
        for word in sentence.split():
            if str(i) in word:
                words.append(word)
    return " ".join(words)


t = order('"is2 Thi1s T4est 3a"')
print(t)


def binary_array_to_number(arr):
    st = ''
    for i in arr:
        st += str(i)
    return int(st, 2)


t = binary_array_to_number([0, 0, 1, 0])
print(t)

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]


def comp(a1, a2):
    try:
        return sorted([i * 2 for i in a1]) == sorted(a2)
    except:
        return False


t = comp(a1, a2)
print(t)


def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    arr = []
    # arr.append(x)
    for i in range(1, n + 1):
        arr.append(x * i)
    return arr


t = count_by(100, 5)
print(t)


# short version
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]


# tribonacci

def tribonacci(signature, n):
    tribonacci = []
    for i in range(n):
        new_elm = signature[-1] + signature[-2] + signature[-3]
        signature.append(new_elm)
        elm = signature.pop(0)
        tribonacci.append(elm)

    return tribonacci


def get_middle(s):
    length = len(s)
    middle_len = length // 2
    lt = (length - 1) // 2
    if len(s) % 2 == 0:
        return s[middle_len - 1: middle_len + 1]
    else:
        return s[lt]


t = get_middle("testqqq")
print(t)

'''camel Case'''


def solution(s):
    return "".join([" " + c if c.isupper() else c for c in s])


t = solution("camelCasing")
print(t)

'''Else solution'''


def solution(s):
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += " "
        newStr += letter
    return newStr


def descending_order(num):
    if num == 0:
        return num
    else:
        lst = str(num)
        n = int(lst[::-1])
        return n


t = descending_order(15)
print(t)

'''
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
'''


def descending_order(num):
    sp = []
    if num == 0:
        return num
    else:
        lst = str(num)
        for i in lst:
            sp.append(i)
    sp.sort(reverse=True)

    return int(''.join(i for i in sp))


t = descending_order(1201)
print(t)

'''best solution'''


def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


def DNA_strand(dna):
    new_side = ''
    for i in dna:
        if i == 'A':
            new_side += 'T'
        elif i == 'T':
            new_side += 'A'
        elif i == 'C':
            new_side += 'G'
        elif i == 'G':
            new_side += 'C'
    return new_side


t = DNA_strand('AT')
print(t)


def persistence(n):
    if n // 10 == 0:
        return 0
    result = 1
    while True:
        result *= n % 10
        n //= 10
        if n == 0:
            break
    return persistence(result) + 1


'''additional answer'''


def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count


t = persistence(999)
print(t)


def remove_exclamation_marks(s):
    lst = ''
    for i in s:
        if i == '!':
            pass
        else:
            lst += i
    return lst


t = remove_exclamation_marks("Hello World!")
print(t)

'''best solution'''


def remove_exclamation_marks(s):
    return s.replace('!', '')


str1 = "abcdefghijklmnopqrstuvwxyz"


def high(x):
    str1 = "abcdefghijklmnopqrstuvwxyz"
    lst = []
    res = {index: i for index, i in enumerate(str1, start=1)}
    res1 = {v: k for k, v in res.items()}
    value = 0
    for i in x:
        value += res1[i]
    return value


t = high('abad')
print(t)


def high(x):
    alp = "abcdefghijklmnopqrstuvwxyz"
    counter = [sum([alp.find(i) + 1 for i in w]) for w in x.split()]
    return x.split()[counter.index(max(counter))]


def high(x):
    words = x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]


'''reverse string by word'''


def reverse_words(text):
    t = text[::-1]
    s = t.split(' ')
    s.reverse()
    l = ' '.join(s)
    # l = ''
    # for i in s:
    #     l+=i

    return l
    # return ''.join(reversed(text))


t = reverse_words("This is an example!")
print(t)

'''best practice'''


def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))


'''uniq letters in string'''


def is_isogram(string):
    l = []
    counter = 0
    for i in string.lower():
        if i not in l:
            l.append(i)
        else:
            counter += 1
    return True if counter == 0 else False


t = is_isogram("Dermatoglyphics")
print(t)

'''best practice'''


def is_isogram(string):
    return len(string) == len(set(string.lower()))


def likes(names):
    if names == []:
        return 'no one likes this'
    if len(names) == 1:
        return f'{names[0]} likes this'
    if len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


t = likes(['Jacob', 'Alex'])
print(t)
'''best practice'''


def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n - 2)


def likes(names):
    match names:
        case []:
            return 'no one likes this'
        case [a]:
            return f'{a} likes this'
        case [a, b]:
            return f'{a} and {b} like this'
        case [a, b, c]:
            return f'{a}, {b} and {c} like this'
        case [a, b, *rest]:
            return f'{a}, {b} and {len(rest)} others like this'


def set_alarm(employed, vacation):
    alarm = False
    if employed is True and vacation is False:
        alarm = True
    return alarm

t = set_alarm(True, True)
print(t)

'''best practice'''
def set_alarm(employed, vacation):
    return employed and not vacation

'''
Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

("Hello", 'o')  =>  1
("Hello", 'l')  =>  2
("", 'z')       =>  0
'''

def strCount(string, letter):
    return string.count(letter)

'''
-----------------
'''

lines = ["a", "b", "c"]

def number(lines):
    #your code here
    p = {j: i for (i, j) in enumerate(lines)}
    print(p)
