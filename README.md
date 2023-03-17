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
On a separate python file, I read in and combined the .txt files to make one big string, and then split it by spaces so each word would be different string. 

![Screenshot 2023-03-16 210932](https://user-images.githubusercontent.com/94634170/225786609-c7421158-1d9b-4239-9238-2a59d3ea4554.png)

Next, I made all words lowercase to ensure that duplicates are removed, removed numbers from the list (some still remained), and removed periods, commas, exclamations, etc. from the strings. Afterwards, I removed duplication.

![Screenshot 2023-03-16 211211](https://user-images.githubusercontent.com/94634170/225786935-899216c4-9152-4302-9024-3d7e2f34979e.png)

## Reduction
After the set of words was clean and duplicates were removed, I began to create lists of increasingly less common words. First, I checked to make sure that the words were indeed words as there were some typos in the transcript. 

![Screenshot 2023-03-16 211505](https://user-images.githubusercontent.com/94634170/225787229-4022f1d9-fd42-4d6e-824a-d31ea603fcc1.png)

This resulted in a real word set of 3251 distinct words.

Next, I removed the words that were in a list of top 10,000 used words.
![Screenshot 2023-03-16 211702](https://user-images.githubusercontent.com/94634170/225787463-9a1e777e-8077-4090-a987-8f57deaf6416.png)
This resulted in a remaining 983 words.

Finally, I utilized a GRE vocabulary set of over 1,000 words. Since the GRE is notorious for using obscure and very uncommon words I figured this would serve as dataset to tease out the more nuanced vocabulary choices.

![Screenshot 2023-03-16 211919](https://user-images.githubusercontent.com/94634170/225787714-96018c5e-16fb-4620-af21-49f1b1438f6e.png)

This resulted in 34 words:
impeccable, complementary, intrinsic, expedient, complacent, fanciful, correlate, reiterate, mitigate, deliberate, intertwined, affinity, profound, manifest, inclined, polymath, repertoire, strife, eccentric, olfactory, fallacy, disabuse, foil, detachment, predilection, mundane, lionize, virtuoso, resilient, underscore, nuance, propensity, profundity, lethargic


## Learning Outcomes
This project allowed me to spend a lot more time working with and cleaning large strings of data, but I must admit that I have been overall underwhelmed. I think by utilizing the GRE dataset I probably missed out on some interesting words, but it did serve as a good reduction tool. I did however end up with a few interesting words that I can begin to work into my vocabulary, such as "lionize", "profundity", and "redilection". I would like to do more work using linguistics tools in the future, so I think I'll be able to build on work completed in the is project at a later date. 
