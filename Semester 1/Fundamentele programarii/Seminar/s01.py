from math import sqrt

#Set 1
# 1) sum of 1...n 
'''we dont see type, but they exist'''

def sum_of_first_n_number(n): #snake case, nagy betu camel case -- convention 
    """
    It computes the sum of the first n natural numbers. //(summa of the functions, capital letter, and dot! at the end!)
    //Detailed description here -->>
 -->Given a natural number [n], computes the sum of the first natural numbers    (brackets!!)

    :param: n: natural number //essential to write this input --> no need to check if its indeed natural nm -> it is already checked somewhere else
    :return n: sum of the first [n] natural numbers //essential .. output
    

    //So: description, each argument, input data described + what it returns!
    """

    sum = 0
    for i in range(n):#0...n
        sum += i
    return sum 

# 2)check if n is prime
def prime(n):
    """
    Decides if n is prime or not.

    :param: n - int
    :return: True/False
    """
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):   # n // 2 integer division!
        if n % i == 0:
            return False
    return True


# 3) greatest lnko
def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b #//ugyanaz mint az euklideszi algorithm
    return a if a > 0 else -a #// not "f statement" --> but the "if expression"

# 4)
def find_greater_prime_than(n):
    i = n
    while prime(i) == False:
        i += 1
    return i


if __name__ == '__main__': #our new main() like c/c++
    # n = int(input("n = "))
    # print(sum_of_first_n_number(n))
    # print(greatest_common_divisor(0, 0))
    #print(prime(17))
    print(find_greater_prime_than(16))





