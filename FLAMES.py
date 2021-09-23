#FLAMES game
#Accepting the user's names
print("Welcome to the FLAMES game.\n")

#instructions
print("Give your and the name of your significant other. The machine would then calculate,")
print("your relationship status using the famous and traditional FLAMES method.")
print("Please keep in mind that the results of this game have nothing to do with reality,")
print("and is developed purely for entertainment purposes.\n")


name1=input("Give player1 name: ")
name2=input("Give player2 name: ")

name1=list(name1)
name2=list(name2)

#Checking for similarities in the given inputs.
for i in name1[:]:
    if i in name2:
        name1.remove(i)
        name2.remove(i)

#using the left over words for counting.
turns=len(name1)+len(name2)

flames=list()
flames=['Friends','Lovers','Affectionate','Marriage','Enemies','Siblings']

while(len(flames)>1):
    i=turns%len(flames)-1
    
    if (i>=0):
        r=flames[i+1:]
        l=flames[:i]
        flames=r+l
    else:
        flames=flames[:len(flames)-1]

print("Your relationship status is ",flames)