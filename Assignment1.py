#takes in a string argument myStr, which consists of one or more words, and
#returns another string, in which:
#words of myStr are reversed if they have five or more letters, and
#all words with less than five letters in myStr are kept the same in the newly-returned string.


#this function is made to reverse string
def reverse_string(string):
     return string[::-1]


#this function is check number of letters in string
def reverse5(mystr):
 x = l1.split() 
 for i in range(len(x)):
    if len(x[i]) < 5 :
        print(x[i])
    else :
        print(reverse_string(x[i]))


    





l1 = str(input("enter :"))
reverse5(l1)