# :100: years of cinema - The History of Diversity in Cinema


### Disclaimer
The following content may be disturbing or triggering to some viewers. It includes themes of violence, abuse, and trauma. If you feel that this content may be disturbing to you, please exercise caution before continuing.

## Abstract
---
The movie industry has long been criticized for its lack of diversity both **on** and **off** screen. Representation of marginalized groups remains inadequate, with many voices and perspectives still underrepresented or completely absent from mainstream films. This lack of diversity not only perpetuates harmful stereotypes and biases, but it also limits the stories and perspectives that are told and negatively impacts the creativity of movie making. For a better visualization of our porject, please refer to our [data story](https://imdbmi.github.io).

## Data
---
### CMU Movie Summary Corpus
The [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) contains over 40,000 movie plot summaries extracted from Wikipedia and also metadata such as characters, genre, release date information.

### Wikidata
Using the Freebase IDs from our dataset, we created a script to collect for every movie a .JSON file with the correspond wikidata. 
For this, we first created a SPARQL query using the [Wikidata query builder](https://query.wikidata.org/querybuilder/?uselang=en) and a sample Freebase ID and the ran it for every Freebase ID in our dataset. This data will be mainly used to get some additional information about the movies such as review scores, costs, age rating, assements, etc.

### English subtitles
[OpenSubtitles](https://opus.nlpl.eu/OpenSubtitles-v2018.php) is a collection of subtitiles in various languages. In our case, we are only interested in the english subtitles. The subtitles are contained in .xml files with the correspoinding timestamps. Using a script, we then only collect the content of the files without the timestamps and match the content to our CMU Movie Summary dataset. In total, there were around 27k subtitles that could be matched with IMDB IDs to our dataset. We will then later be able to use matching or nlp models to help answer some of the research questions

### Consumer Price Index for All Urban Consumers
To study the revenue we first need to adjust the revenue according to the inflation rate. To this end we use the inflation rate data from [Federal Reserve Economic Data](https://fred.stlouisfed.org/series/CPIAUCNS). Since this inflation data goes all the way back to 1913, therefore, it lends itself to our analysis of film revenues beginning in the early 19th century.

## Research Questions
---
we divided our reseach questions into two categories: **On screen** and **Off screen** where we will take a deeper look at the diversity in the movie industry.

### Off screen
- Does the gender of lead actors, director or producer impact the revenue of a movie ?
- Are the Hollywood stars just like us ?
- Would a more diverse cast in terms of age help achieve higher box office revenues ?

### On screen
- How did the terms and tones used changed when talking about a LGBT character? And how did positive LGBT potrayal change over time?


## Project structure
---
    ├── data                    # download your train and test dataset here
    │   ├── processed           # Contains processed .csv and .json files
    |   ├── raw                 # Contains the raw data
    ├── data_collection         # Contains the scripts that were used to gather the data found under /data/raw
    ├── data_preprocessing      # Contains the scripts that were used to create the files under /data/processed
    ├── models                  # Contains the NLP models used
    ├── plots                   # Contains all the plots that were created
    ├── Final.ipynb             # The notebook containing our results
    └── README.md               # README

The source code of [data story](https://imdbmi.github.io) can be found under [this](https://github.com/imdbmi/imdbmi.github.io) repository and the additional processed datasets can be accessed at [here](https://drive.google.com/drive/folders/1FycaszmTdI2UjO06tgsg5nqvtpLG_z4s?usp=sharing).

## Methods
---
## Off screen
> ### 1) Does the gender of lead actors, director or producer impact the revenue of a movie?

To analyze the gender gap, we looked at different aspects of gender inequalities. We divided the genders into either ```male``` or ```female``` since we do not have enough data to include other genders.

The first step was to compare the gender distribution of the cast over time and also by genre. Then, we use a linear regression model to try to fit the box office value using the ratio of males. Afterwards, we used hypothesis testing to determine if the gender has an impact on the revenue. For this we divided the data into 2 populations, one that is not diverse (ratio of male or female is either below 40% or above 60%) and one which is diverse and the used the following hypotheses:
- $H_0: p \leq .05$ Whethever a cast is diverse or not **has no** effect on the box office value
- $H_a: p \gt .05$ A not diverse cast **has** a higher box office value

> ### 2) Are the Hollywood stars just like us?

Before analyzing our data, we first need to gather some additional information to compare our data to. This information 
will be the ethnicity distribution and the average height and age of woman and man in the english speaking countries since 
these are the countries for which our data is representative. After that, we plot the distributions of the ethnicity, gender, height and age in CMU dataset over time and compare them to the gathered information.

> ### 3) Would a more diverse cast in terms of age help achieve higher box office revenues? 

Similar to the first research question ```Does the gender of lead actors, director or producer impact the revenue of a movie?```, we will analyze how the age affects the revenue of movies. 
To begin with let's define two metrics that reflect the diversity in age of the cast members: mean age and max difference in age. And then we performed a regression analysis to study the correlation between mean cast age, max cast age, and the movie box revenue. And we study the movie for every ten years and anylze them in their own genere.

## On screen

> ### 4) How did the terms and tones used changed when talking about a LGBT character? And how did positive LGBT potrayal change over time?

We perform the analysis using two different models on two different data modalities. The first model is VADER (Valence Aware Dictionary for Sentiment Reasoning) which is a lexicon and rule-based sentiment analysis tool. The second model is a transformer based sentiment analyzer, roBERTa-base, that is trained on ~124M tweets from January 2018 to December 2021. Although we don't classify tweets, a conversation in a subtitle usually reflects the characteristics of daily language used in public. In addition, an advantage of a transformer-based model over lexicon & rule-based method is that transformers can also capture the contextual information thank to the self-attention mechanism where each token interacts with each others. Hence we hypothesized that this model should be good enough capture sentiment scores of conversations in subtitles.

In terms of data modalities, we both used raw text inputs (not tokenized&lemmatized) and tokenized context windows to the models. In the context window approach, we start with tokenized subtitle documents and search for occurrences of a keyword. For each occurrence, we extract a context window around the keyword. In the other approach, we first identify a keyword occurs in the list of tokens of a document. If it does, we read the raw subtitle file and return the sentences containing the keyword. However, this approach is not precises as we look at the whole text, rather than tokens, hence a sentence containing woman can be return for the keyword man, since man is 'suffix' of woman. To remove false positives, we feed sentences through an NLP tokenization pipeline and check whether a keyword is actually a token of the sentence.


## Contributions
---
| E-mail | Sciper | Contributions |
| ------ | ------ | ----- |
| abdulkadir.gokce@epfl.ch | 336709 | Responsible for the repo structure, sentiment analysis and evolution of words which includes the integration of subtitles to the analysis as well as WikiIDs and the tuning and analyze of the NLP algorithms.   |
| chengkun.li@epfl.ch | 340485 | Responsible for the adaption of the revenue to inflation, the analysis between age and revenue and the web interface. |
| iana.peix@epfl.ch | 287074 | Responsible for the ethnicity analysis, data story and web interface |
| maximilian.gangloff@epfl.ch | 322220 | Responsible for the repo structure and gender analysis which includes which includes the processing of the gathered wikidata. |