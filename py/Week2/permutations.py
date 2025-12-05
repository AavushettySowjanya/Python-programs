def permutation(s,result=""):
    #if no char in string print completed permutation
    if len(s) ==0:
        print(result)
        return
    
    #loop through each char
    for i in range(len(s)):
        ch=s[i]
        #remove current char from the string
        #left+right(excluding s[i])
        remaining=s[:i]+s[i+1:]

        #recursive call
        permutation(remaining,result+ch)
permutation("abc")