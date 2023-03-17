# Vocabulary of Josh Waitzkin

(In Progress)

In this project, I scraped three podcast transcripts from the Tim Ferriss Show, seperated the guest's dialogue from the host's, and removed common words to reveal Mr. Waitzkin's nuanced vocabulary.

## Sources
The podcast transcripts were retrieved from
* https://tim.blog/2020/03/14/josh-waitzkin-transcript-412/
* https://tim.blog/2021/02/18/josh-waitzkin-2-transcript/
* https://tim.blog/2019/07/03/the-tim-ferriss-show-transcripts-josh-waitzkin-how-to-cram-2-months-of-learning-into-1-day-375/

The GRE list was retrieved from
* https://github.com/omkark96/gre-word-list-utils/blob/master/combined_word_list.csv

The list of all words was retreived from
* https://github.com/dwyl/english-words

The list of 10k most used words was retrieved from
* https://github.com/first20hours/google-10000-english

## Project Goal
As a long time listener of the Tim Ferriss show, I have especially enjoyed episodes where Josh Waitzkin is a guest. Josh Waitzkin was a chess prodigy, martial artist, and the author of one of my favorite books - "the Art of Learning". Mr. Waitzin is a very intelligent and introspective person who has been influenced heavily by asian philosophies. Because of this, he has a very interesting way to talking about things and ideas. I started this project hoping that I could dig into what it is about his language that makes him unique. After web scraping the transcripts I quickly realized that I was in over my head and lacked the background in linguistics needed to conduct the anlaysis that I wanted. Instead, I decided to conduct an audit of sorts on the vocabulary of Mr. Waitzkin as displayed in the three interviews which combined for roughly 3.5 hours of dialogue.

## Scraping
To scrape the data I used the python lxml library to pull the static page html for me to parse through. 
First I used the code below to remove the strings in my list that had no value.
![1](https://user-images.githubusercontent.com/94634170/225784306-d3439f94-b054-42d5-ac94-223a53caf8d6.png)

Next, I needed to seperate Mr. Waitzkin's dialogue from the host's. Using the below text, I am confident that what I ended up with was 90%+ Waitzkin. 
![Screenshot 2023-03-16 205651](https://user-images.githubusercontent.com/94634170/225784897-7478f75a-c6bc-48bc-8d02-c542e9fa60f6.png)

The logic is as follows: As my program iterates through the list, if the string signifies that Josh Waitzkin is the speaker, then it adds the following strings to a list until a string has "Tim Ferris" or "Josh Waitzkin" in it. 

Afterward, I removed duplicates that could have crept in, sorted the new list to make it less readable, and exported the text as a .txt file. 

For the most part, each episode followed that process.



## Cleaning


## Reduction



## Learning Outcomes
Far from the results I had imagined when I thought up the project, I at least have a nice list of words that I can work into my vocabulary. I got a lot of good practice scraping and cleaning data, so to that end this was a very valuable project. 
