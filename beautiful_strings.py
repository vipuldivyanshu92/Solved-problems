'''# -*- coding: utf-8 -*-'''
"""When John was a little kid he didn't have much to do. There was no internet, no Facebook, and no programs to hack on. So he did the only thing he could... he evaluated the beauty of strings in a quest to discover the most beautiful string in the world.

Given a string s, little Johnny defined the beauty of the string as the sum of the beauty of the letters in it.

The beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have the same beauty. Johnny doesn't care about whether letters are uppercase or lowercase, so that doesn't affect the beauty of a letter. (Uppercase 'F' is exactly as beautiful as lowercase 'f', for example.)

You're a student writing a report on the youth of this famous hacker. You found the string that Johnny considered most beautiful. What is the maximum possible beauty of this string?

Input
The input file consists of a single integer m followed by m lines.
Output
Your output should consist of, for each test case, a line containing the string "Case #x: y" where x is the case number (with 1 being the first case in the input file, 2 being the second, etc.) and y is the maximum beauty for that test case.
Constraints
5 ≤ m ≤ 50
2 ≤ length of s ≤ 500
Example inputExample output
5
ABbCcc
Good luck in the Facebook Hacker Cup this year!
Ignore punctuation, please :)
Sometimes test cases are hard to make up.
So I just go consult Professor Dalves
Case #1: 152
Case #2: 754
Case #3: 491
Case #4: 729
Case #5: 646
"""
def getpos(charCount,e): # the position of each element
    for i in range(0,len(charCount)):
        if charCount[i][1]==e:
            return i
    else:
        return -1
def main(data):
    #n=int(raw_input())
    countList=[] #hold the results 
    n=int(data[0])
    m=1
    out="" #output
    while n:
        maxVal=26
        count=0
        lenChar=0#strores number of different characters
        charCount=[]   #this variable stores the aplhabet with its count
        #stringInput=str(raw_input()) # stores the raw input string
        stringInput=data[m]
        stringInput=stringInput.lower()#store the whole string in lower form
        for e in stringInput:#loop to append individual alphabets in the lst and update the count
            if e.isalpha(): 
                pos=getpos(charCount,e)
                #print pos,' ',e
                if pos==-1:
                    charCount.append([1,e])
                else:
                    charCount[pos][0]=charCount[pos][0]+1
        
        charCount=sorted(charCount, key=lambda char: char[0],reverse=True)
        lenChar=len(charCount)

        for i in range(0,lenChar):
            count=count+charCount[i][0]*maxVal
            maxVal=maxVal-1
        countList.append(count)
#        print 'Case #'+str(m+1)+':'+str(count)
        n=n-1
        m=m+1
       
    for j in range(0,len(countList)):
        print 'Case #'+str(j+1)+': '+str(countList[j])
        out=out+'Case #'+str(j+1)+': '+str(countList[j])+'\n'
    return out
############ run ##################
##f=open("beautiful_stringstxt_")
##data=f.read()
##data=data.split("\n")
##print data
##f.close()
##out=main(data)
##with open('output.txt', 'w') as fo:
##    fo.write(out)
##print out
##fo.close()

