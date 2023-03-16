#-----------------------------------------
#---------- Set Up -----------------------
#-----------------------------------------

#Read in relevant Libraries
import pandas as pd
from lxml import html
from lxml import etree
import requests
import os
import numpy as np

# Set working directory
os.chdir("C:\\Users\\grant\\OneDrive\\Documents\\Personal Projects\\Programming Projects\\Josh_Waitzkin_Language")


#-----------------------------------------
#----------Episode 412 -------------------
#-----------------------------------------

timurl1 = "https://tim.blog/2020/03/14/josh-waitzkin-transcript-412/" 
resp = requests.get(timurl1)
tagtree = html.fromstring(resp.content)

#Grab all text
xp_alltext = "//main/article/div//text()"
all_text = tagtree.xpath(xp_alltext)
print("\nThe length of the text list before cleaning is:",(len(all_text)),"\n")

#Now I have a list with all strings, including Tim's dialogue and new line tags

#To get rid of odd strings
for x in all_text:
    if "\n" in x or "\t" in x:
        all_text.remove(x) # removing \n or \t
    if x == " ":
        all_text.remove(x) # removing empty strings
    if x == ".":
        all_text.remove(x) # removing period-only strings
    if x == ", ":
        all_text.remove(x) #removing comma-only strings


#Taking only Josh Waitzkin dialogue from the text
Waitzkin_Only = []
for piece in all_text:
    x = all_text.index(piece)
    if piece == "Josh Waitzkin: " or "Josh Waitzkin:":
            try:
                if "Tim Ferriss" not in all_text[x+1]:
                    Waitzkin_Only.append(all_text[x+1])
            except:
                continue
            try:
                if "Tim Ferriss" not in all_text[x+2]:
                    if "Josh Waitzkin" not in all_text[x+2]:
                        Waitzkin_Only.append(all_text[x+2])
            except:
                continue
            try:
                if "Tim Ferriss" not in all_text[x+3]:
                    if "Josh Waitzkin" not in all_text[x+3]:
                        Waitzkin_Only.append(all_text[x+3])
            except:
                continue
            try:
                if "Tim Ferriss" not in all_text[x+4]:
                    if "Josh Waitzkin" not in all_text[x+4]:
                        Waitzkin_Only.append(all_text[x+4])
            except:
                continue


#Now we have most of Waitzkin's text, but we have multiples, so we should fix that
Waitzkin_Only = list(set(Waitzkin_Only))

#Sort alphabetically to make it less readable
Waitzkin_Only.sort() 

#export as a text file
ExportEpisode412 = pd.DataFrame(Waitzkin_Only)
np.savetxt(r"C:\\Users\\grant\\OneDrive\\Documents\\Personal Projects\\Programming Projects\\Josh_Waitzkin_Language\\Episode412.txt", ExportEpisode412.values, fmt='%s')


#-------------------------------------------------
#---------- Episode 498 --------------------------
#-------------------------------------------------

#SetUp - Episode 498
timurl2 = "https://tim.blog/2021/02/18/josh-waitzkin-2-transcript/" 
resp2 = requests.get(timurl2)
tagtree2 = html.fromstring(resp2.content)

#Grab all text
xp_alltext = "//main/article/div//text()"
all_text2 = tagtree2.xpath(xp_alltext)
print("\nThe length of the text list before cleaning is:",(len(all_text2)),"\n")

#To get rid of odd strings
for x in all_text2:
    if "\n" in x or "\t" in x:
        all_text2.remove(x) # removing \n or \t
    if x == " ":
        all_text2.remove(x) # removing empty strings
    if x == ".":
        all_text2.remove(x) # removing period-only strings
    if x == ", ":
        all_text2.remove(x) #removing comma-only strings

#Taking only Josh Waitzkin dialogue from the text
Waitzkin_Only = []
for piece in all_text2:
    x = all_text2.index(piece)
    if piece == "Josh Waitzkin: " or "Josh Waitzkin:":
            try:
                if "Tim Ferriss" not in all_text2[x+1]:
                    Waitzkin_Only.append(all_text2[x+1])
            except:
                continue
            try:
                if "Tim Ferriss" not in all_text2[x+2]:
                    if "Josh Waitzkin" not in all_text2[x+2]:
                        Waitzkin_Only.append(all_text2[x+2])
            except:
                continue
            try:
                if "Tim Ferriss" not in all_text2[x+3]:
                    if "Josh Waitzkin" not in all_text2[x+3]:
                        Waitzkin_Only.append(all_text2[x+3])
            except:
                continue
            try:
                if "Tim Ferriss" not in all_text2[x+4]:
                    if "Josh Waitzkin" not in all_text2[x+4]:
                        Waitzkin_Only.append(all_text2[x+4])
            except:
                continue

#remove intro portion that wasn't removed
Waitzkin_Only = Waitzkin_Only[121:]
Waitzkin_Only = Waitzkin_Only[:-45]

for x in Waitzkin_Only:
    if x == "Josh Waitzkin: " or x == "Josh Waitzkin:":
        Waitzkin_Only.remove(x)

Waitzkin_Only = list(set(Waitzkin_Only)) #remove duplicates

Waitzkin_Only.sort() #make less readable

#export as a text file
ExportEpisode498 = pd.DataFrame(Waitzkin_Only)
np.savetxt(r"C:\\Users\\grant\\OneDrive\\Documents\\Personal Projects\\Programming Projects\\Josh_Waitzkin_Language\\Episode498.txt", ExportEpisode498.values, fmt='%s')


#---------------------------------------------
#--------------- Episode 375 -----------------
#---------------------------------------------

#SetUp - Episode 375
timurl3 = "https://tim.blog/2019/07/03/the-tim-ferriss-show-transcripts-josh-waitzkin-how-to-cram-2-months-of-learning-into-1-day-375/" 
resp3 = requests.get(timurl3)
tagtree2 = html.fromstring(resp3.content)

#Grab all text
xp_alltext = "//main/article/div//text()"
all_text3 = tagtree2.xpath(xp_alltext)
print("\nThe length of the text list before cleaning is:",(len(all_text3)),"\n")

#To get rid of odd strings
for x in all_text3:
    if "\n" in x or "\t" in x:
        all_text3.remove(x) # removing \n or \t
    if x == " ":
        all_text3.remove(x) # removing empty strings
    if x == ".":
        all_text3.remove(x) # removing period-only strings
    if x == ", ":
        all_text3.remove(x) #removing comma-only strings


#Taking only Josh Waitzkin dialogue from the text
Waitzkin_Only3 = []
for piece in all_text3:
    x = all_text3.index(piece)
    if piece == "Josh Waitzkin: " or "Josh Waitzkin:":
            try:
                if "Tim Ferriss" not in all_text3[x+1]:
                    Waitzkin_Only3.append(all_text3[x+1])
            except:
                continue
            try:
                if "Tim Ferriss" not in all_text3[x+2]:
                    if "Josh Waitzkin" not in all_text3[x+2]:
                        Waitzkin_Only3.append(all_text3[x+2])
            except:
                continue
            try:
                if "Tim Ferriss" not in all_text3[x+3]:
                    if "Josh Waitzkin" not in all_text3[x+3]:
                        Waitzkin_Only3.append(all_text3[x+3])
            except:
                continue
            try:
                if "Tim Ferriss" not in all_text3[x+4]:
                    if "Josh Waitzkin" not in all_text3[x+4]:
                        Waitzkin_Only3.append(all_text3[x+4])
            except:
                continue

#remove intro portion that wasn't removed
Waitzkin_Only3 = Waitzkin_Only3[121:]
Waitzkin_Only3 = Waitzkin_Only3[:-45]

for x in Waitzkin_Only3:
    if x == "Josh Waitzkin: " or x == "Josh Waitzkin:":
        Waitzkin_Only3.remove(x)

Waitzkin_Only3 = list(set(Waitzkin_Only3)) #remove duplicates

Waitzkin_Only3.sort()#make less readable

#export as a text file
ExportEpisode375 = pd.DataFrame(Waitzkin_Only3)
np.savetxt(r"C:\\Users\\grant\\OneDrive\\Documents\\Personal Projects\\Programming Projects\\Josh_Waitzkin_Language\\Episode375.txt", ExportEpisode375.values, fmt='%s')