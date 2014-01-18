def isPrime(a):
    if not a & 1:
        #Checks if a is even.
        #Prevents unneeded running of the loop.
        #2 is the only even prime and we will not see that here.
        return False
    for i in range(3,int(a**.5)+1,2):
        if a%i==0:
            return False
    return True

def isPalindrome(a):
    x = decTobin(a)
    y = str(a)
    if x == x[::-1] and y == y[::-1]:
        return True
    else:
        return False

def decTobin(a):
    #removed the str() call, because bin() returns a string.
    #removed int() call, because you want a string for this.
    return bin(a).replace('0b', '')

def getAnswer():
    a=11
    print (a)
    while a >= 11:
        if isPrime(a): #if isPrime() returns True will evaluate True.
            if isPalindrome(a):
                return a  #This is the only time you need to return 'a'
        a+=2


if __name__ == '__main__':
    print (getAnswer())
