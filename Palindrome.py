# Kobe Luna
# StudentID: P21590963
# Homework 2: problem 2a/2b
import string

def BackSent(sentence): #problem 2a  
  
    words = sentence.split(' ')  
    readback = ' '.join(reversed(words))  
    return readback 

def palindrome(string): #problem 2b
    first = 0
    last = len(string) - 1

    while last >= first:
        if not string[first] == string[last]:
            return False 
        first += 1
        last -= 1
    return True 
  
print("Problem 2a")
mystring = "My name is Kobe"
print(mystring)
print (BackSent(mystring))

print("\n")

print ("Problem 2b")
palin = "hannah"
print(palin)
print(palindrome(palin))
