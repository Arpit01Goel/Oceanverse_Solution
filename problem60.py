import string
#This is a python code to define some functions which can be used to encrypt and decrypt

def textstrip(filename):
    '''This takes the file and converts it to a string with all the spaces and other
    special characters removed. What remains is only the lower case letters,
    retain only the lowercase letters'''

    #First open and read file and save it in a variable named b
    a=open(filename)
    b=a.read()

    #to identify the special characters (lowercase letters) add them all in a list named i
    i=list()
    for j in range(97,123):
        i.append(chr(j))
    
    #to do instant search use set
    data=set(i)

    #save answer in a variable named answer
    answer=''

    #iterate whole text and if the character is in data then add it to answer
    for k in b:
        if k in data:
            answer+=k

    #return the answer
    return answer




def letter_distribution(s):
    '''Consider the string s which comprises of only lowercase letters. Count
    the number of occurrences of each letter and return a dictionary'''
    #create required dictionary
    d={}

    #for distribution we wil also need to calculate the total no of characters 
    no_of_char=0

    #initialize all the values of dictionary to 0 and update them when iterating s
    for i in range(97,123):
        d[chr(i)]=0

    #now update data by iterating s
    for i in s:
        d[i]+=1;no_of_char+=1
    #d is containing the no of times each letter occurs in s.divide all values with total no of characters.
    for i in d:
        d[i]=d[i]/no_of_char
    #d is now created
    return d





def substitution_encrypt(s,d):
    '''encrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    #store answer in a variable named a 
    a=''
    #iterate text and add substitution in a.    For every key , its value in d is its substitution
    for i in s:
        a+=d[i]
    return a






def substitution_decrypt(s,d):
    '''decrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    #store answer in a variable named a 
    a=''
    #iterate text and add substitution in a.   For every key , its value in d is its substitution
    for i in s:
        a+=d[i]
    return a





def cryptanalyse_substitution(s):
    '''Given that the string s is given to us and it is known that it was
    encrypted using some substitution cipher, predict the d'''
    d1=letter_distribution(s)
    answer={}
    #data have the frequency distribution of letters in english language
    data=letter_distribution(textstrip("english_random.txt"))
    a1=sort_dict(d1)
    a2=sort_dict(data)
    for i in range(26):
        answer[str(a2[i])]=a1[i]
    return answer


def sort_dict(dic):
    #this funciton sort the dictionary keys on the basis of their values.returns a list of keys

    #first create a dictionary with values as keys and keys as values (as per algorithm)
    d1={}
    for i in dic:
        d1[dic[i]]=i

    #now create list
    l=[]

    #now append all the keys of d1 in list and sort it.     (original dictionary values are sorting)
    for i in d1:
        l.append(i)
    l.sort()

    #initialize answer list
    ans=[]
    

    #now append the original dictionary keys in answer list in sorted order
    for i in l:
        ans.append(d1[i])

    return ans






def vigenere_encrypt(s,password):
    '''Encrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    #initialise answer string
    ans=''

    #create a string of all the alphabets(we will need it to create a cycle)
    a='abcdefghijklmnopqrstuvwxyz'
    n=len(password)
    for i in range(len(s)):
        ans+=a[(a.find(s[i])+(a.find(password[i%n])+1))%26]
    return ans




def vigenere_decrypt(s,password):
    '''Decrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''

    #just like encryption but in reverse order so subtracting instead of adding
    ans=''
    a='abcdefghijklmnopqrstuvwxyz'
    n=len(password)
    for i in range(len(s)):
        ans+=a[(a.find(s[i])-(a.find(password[i%n])+1))%26]
    return ans

print(vigenere_decrypt(vigenere_encrypt('chaitanya','chaitanya'),'chaitanya'))
def rotate_compare(s,r):
    '''This rotates the string s by r places and compares s(0) with s(r) and
    returns the proportion of collisions'''
    
    #create new string
    new_str=''
    
    #for whole string add the next rth character in new string.In wnding it will create index out of range error. So solve it by try and except method. Aslo use exception to add the first r characters in new string

    try:
        for i in range(len(s)):
            new_str+=s[i+r]
    except IndexError:
        new_str+=s[0:r:1]

    
    #now calculate the no of collisions
    collisions=0
    for i in range(len(s)):
        if s[i]==new_str[i]:
            collisions+=1
    
    #colloison percentage is asked so divide it by length of string
    return collisions/len(s)





def most_freq(s):
    #this function returns the most frequent letter of given string
    
    #first find frequency of all letters . then arrange keys in sorted order of values. Then return the last key
    d=letter_distribution(s)
    d1=sort_dict(d)
    ans=d1[-1]

    return ans



def cryptanalyse_vigenere_afterlength(s,k):
    '''Given the string s which is known to be vigenere encrypted with a
    password of length k, find out what is the password'''
    answer=''

    for i in range(k):

        #take the subset of string s which are shifted by same gap.Then in the subset, the most frequenct letter is substitution for e. We will calculate shift and hence the character which was added. This character is the key for that subset. Add it to answer
        e=most_freq(s[i::k])
        #now e stores the character which represents e in meaningful english
        shift=ord(e)-ord('e')
        key='abcdefghijklmnopqrstuvwxyz'[shift-1]
        answer+=key

    return answer





def cryptanalyse_vigenere_findlength(s):
    '''Given just the string s, find out the length of the password using which
    some text has resulted in the string s. We just need to return the number
    k'''
    #as per algorithmn we will rotate the string by 1 place and compare it with original string. If the collision percentage is less than 6% then rotate it by 2 places and so on. When the collision percentage is greater than 6% then return the number of rotations. (6% is calculated based on frequency)
    
    #start i with 1 as 0 will show 100% collision
    i=1

    while rotate_compare(s,i)<.06:
        i+=1
    #when loop ends , i will satisfy colloison frequency condition , hence passowrd is of i length
    return i





def cryptanalyse_vigenere(s):
    '''Given the string s cryptanalyse vigenere, output the password as well as
        the plaintext'''
    #using above functions we can easily find the password and plaintext
    #first find the length of password
    #then find the password
    #then decrypt the string using password

    k=cryptanalyse_vigenere_findlength(s)
    password=cryptanalyse_vigenere_afterlength(s,k)
    ans=vigenere_decrypt(s,password)
    return password,ans
