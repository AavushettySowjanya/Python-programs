def anagram(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    if len(str1)!=len(str2):
        return False
    #sorting the Strings 
    a=sorted(str1)
    b=sorted(str2)
    return a==b
string1="Listen"
string2="silent"
if anagram(string1,string2):
    print("Anagram")
else:
    print("not anagram")