def removeVowel(str):
    vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
    for i in str:
        if i in vowels:
            str = str.replace(i,"")
    return str
    
def StringManipulation(str):
    lst=[]
    for i in str:
        if i.isalpha() and i!='z' and i!='Z':
            lst.append(chr(ord(i)+1))
        elif i=='z':
            lst.append('a')
        elif i=='Z':
            lst.append('A')
        else:
            lst.append(i)
    output1=''.join(lst) 
    print("\nOutput1: \n",output1)
    output1=removeVowel(output1)
    output2=output1[::-1]
    output3=str[::2]

   
    print("\nOutput2:    \n",output2)
    print("\nOutput3: \n",output3)
    print("\n")

userIn = input("\nEnter a string: ")
StringManipulation(userIn)

      

            
        
            