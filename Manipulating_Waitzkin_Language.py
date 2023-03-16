#--------------
#----Set Up----
#--------------

#Read in relevant Libraries
import os
import re
# Set working directory
os.chdir("C:\\Users\\grant\\OneDrive\\Documents\\Personal Projects\\Programming Projects\\Josh_Waitzkin_Language")



#------------------------------------
#----Read in and combine episodes----
#------------------------------------

#Read in episode 375
with open('Episode375.txt', 'r') as file1:
    E375 = file1.read()
#Read in episode 412
with open('Episode412.txt', 'r') as file2:
    E412 = file2.read()
#Read in episode 498
with open('Episode498.txt', 'r') as file3:
    E498 = file3.read()
#Combine episodes
combined = E375 + E412 + E498



#---------------------------------------
#----clean up combined list-------------
#---------------------------------------

combined = combined.split() #turn long string into a list

#Make all words lowercase
combined_lower = [] #initialize list
for x in combined:
        combined_lower.append(x.lower())

#Remove numbers from list
combined_NoNumbers = [] #initialize list
for x in combined_lower: 
    try:
        int(x) #if not a number, will go to except
    except:
        combined_NoNumbers.append(x)
#This brought our list length down by roughly 100 values

#remove periods and commas using regex
combined_NoSymbols = [] #initialize list
for x in combined_NoNumbers:
    x = re.sub(r'[^\w\s]', '', x) #regex
    combined_NoSymbols.append(x)

#Get a distinct count of different words (will include names, and plural forms )
distinct_Words = list(set(combined_NoSymbols)) #3566 distinct words



#--------------------------------------------------------
#------Create Lists of words with increasing rarity------
#--------------------------------------------------------

#Check to see if what we have are actually words
with open('all_words.txt', 'r') as file1:
    all_Words = file1.read()
all_Words = all_Words.split() #Split by space

actual_Words = [] #3251 distinct real words
for x in distinct_Words:
    if x in all_Words:
        actual_Words.append(x)

#The next Goal is to see what words in this list are considered "uncommon"
#open the top 10,000 used words text file
with open('top_10k_words.txt', 'r') as file1:
    top10k = file1.read()
top10k = top10k.split() #make it a list

#Make a list of Waitzkin's words that are not in the to 10,000
uncommon_Words = [] #983 distinct, real, and "uncommon" words
for x in actual_Words:
    if x not in top10k:
        uncommon_Words.append(x)

#Bring in GRE word file
with open('GRE_Words.txt', 'r') as gre:
    gre_Words = gre.read()
gre_Words = gre_Words.split()

#Find Waitzkin words that are in the GRE list
rare_Words = [] #34
for x in uncommon_Words:
    if x in gre_Words:
        rare_Words.append(x)
 


#---------------------------------------------
#--------Export Lists as .txt files-----------
#---------------------------------------------
#export distinct
with open("Waitzikin_Dsitinct.txt", "w") as output:
    output.write(str(actual_Words))

#export uncommon
with open("Waitzkin_Uncommon.txt", "w") as output:
    output.write(str(uncommon_Words))

#export rare
with open("Waitzkin_Rare.txt", "w") as output:
    output.write(str(rare_Words))

#sort and export all
combined_lower.sort() #Sort to obfuscate text
with open("Waitzkin_All.txt", "w") as output:
    output.write(str(combined_lower))


