# Over the Rainbow - History of diversity in cinema

## Abstract
---
Since the first moving picture, Roundhay Garden shot in 1888 cinema had an incredible impact on humanity as a whole. Allowing people to see and through movies experience things which wouldn’t ever be possible.
 
But looking at the incredible diversity of our planet, the question we want to answer is how representative is the cinema of this diversity and how much did it change during the 20th and early 21st century.
 
By using CMU movie dataset, we will study how did the diversity of representation changed through time and correlate with changes in society as a whole.


## Research Questions
---
1) What is the evolution of the gender Gap in movies? Is there a significant difference in number of movies directed by men vs women? And does the gender of lead actor or director impact the revenue of a movie?

2) Does diversity impact the financial success of a movie? Using revenue we want to analyze if the most succesful movies are more or less diverse than the average.

3) Lingustic analysis of LGBT characters: How did the terms and tones used changed when talking about a LGBT character? And how did positive LGBT potrayal change over time?

4) Using the ethnicity, gender, height and age in CMU dataset we want to analyze how comparable are movies with the average population of its countries and how did it change over time.

## Additional datasets
---
Additional processed dataset can be accessed at [here](https://drive.google.com/drive/folders/1FycaszmTdI2UjO06tgsg5nqvtpLG_z4s?usp=sharing).
### Wikidata
Using the Freebase IDs from our dataset, we created a script to collect for every movie a .JSON file with the correspond wikidata. 
For this, we first created a SPARQL query using the [Wikidata query builder](https://query.wikidata.org/querybuilder/?uselang=en) and a sample Freebase ID and the ran it for every Freebase ID in our dataset. This data will be mainly used to get some additional information about the movies such as review scores, costs, age rating, assements, etc.

### English subtitles
[OpenSubtitles](https://opus.nlpl.eu/OpenSubtitles-v2018.php) is a collection of subtitiles in various languages. In our case, we are only interested in the english subtitles. The subtitles are contained in .xml files with the correspoinding timestamps. Using a script, we then only collect the content of the files without the timestamps and match the content to our CMU Movie Summary dataset. In total, there were around 27k subtitles that could be matched with IMDB IDs to our dataset. We will then later be able to use matching or nlp models to help answer some of the research questions

## IMDB data
[Freie Universität Berlin IMDB dataset](http://ftp.fu-berlin.de/pub/misc/movies/database/frozendata/) is a collection of various data scrapped from IMDB, if we will be missing some data from CMU or other datasets, we intend to complete it with this.


## Methods
---
> ### 1) What is the evolution of the gender Gap in movies? Is there a significant difference in number of movies directed by men vs women? And does the gender of lead actor or director impact the revenue of a movie?

To analyze the gender gap, we will look at different aspects of gender inequalities. 
The first one will be to compare the gender distribution of the cast over time. Then we will be using 
hypothesis testing to determine if the gender of lead actors or director has a direct impact on the revenue of the movie.

> ### 2) Does diversity impact the financial success of a movie? Using revenue we want to analyze if the most succesful movies are more or less diverse than the average. 

To answer this question, we will compute an *diversity* index (could be similar to [MediaVersity](https://www.mediaversityreviews.com/how-we-grade)) 
which consists of a combination of different features such as e.g. gender, age, height, ethnicity, etc. 
Using this new index, we will be able to compare the diversity with the box office revenue to determine if 
the diversity has an impact on the financial success of a movie by using hypothesis testing.

> ### 3) Lingustic analysis of LGBT characters: How did the terms and tones used changed when talking about a LGBT character? And how did positive LGBT potrayal change over time?

Firstly, we will analyze the occurence of LGBT related terms over time without looking at the connotation using 
matching to analyze if the LGBT topic in general increased in the movies over time.

Then, in a second time, we will be using word embedding techniques such as Word2Vec or FastText for sentiment 
analysis to analyze how the portrayal of LGBT characters changed over time.

> ### 4) Using the ethnicity, gender, height and age in CMU dataset we want to analyze how comparable are movies with the average population of its countries and how did it change over time.

Before analyzing our data, we first need to gather some additional information to compare our data to. This information 
will be the ethnicity distribution and the average height and age of woman and man in the english speaking countries since 
these are the countries for which our data is representative. After that, we can use hypothesis testing to analyze 
if the movie industry in the english speaking countries has similar distributions.


## Proposed timeline
---
* 11.11.22 - Combine subtitle data set with CMU and clean it into an NLP friendly form
* 14.11.22 - Finish the script for getting WikiID from Freebase IDs
* 18.11.22 - Milestone 2
* 20.11.22 - Integration of all datasets together & run initial word embedding/NLP analyses
* 25.11.22 - Finalize all of initial analyzes for the different topics & intial visualisations for textual data
* 04.12.22 - Start writing first draft of the data story
* 13.12.22 - Deadline for adding any additional visualisations and changes to the data story
* 18.12.22 - Complete all code implementations and main visualisations and start finalizing the web interface
* 20.12.22 - Complete analysis and web interface (Buffer time)
* 23.12.22 - Milestone 3 deadline


## Organization within the team
---
| E-mail | Sciper | Tasks |
| ------ | ------ | ----- |
| abdulkadir.gokce@epfl.ch | 336709 | Integrate subtitles to our analysis as well as WikiIDs. Tune and analyze NLP algorithms   |
| chengkun.li@epfl.ch | 340485 | Create impactful visualisations. Develop web interface. Continue exporing different datasets. |
| iana.peix@epfl.ch | 287074 | Create impactful visualisations. Develop web interface and final text for the data story |
| maximilian.gangloff@epfl.ch | 322220 | Create impactful visualisations. Finalize final text for data story. |