# Sypht Coding Challenge

## Sentiment Analysis
In this task we tried two approaches. 
1. Create a tfidf matrix by lemmatising (using spacy) and removing stop words. We then used keras to create a logistic model with 0 hidden layers and two hidden layers of 10 nodes each. The maximum accuracy achieved on the amazon dataset was 65%.
2. We used the Ulmfit model. Ulmfit is mainly a many to many stacked LSTM model which was trained on the wikipedia corpus to predict the next word. We initially fine tune the last few layers of the model to create a language model for reviews. We then use this LSTM and add a hidden layer to the final output to get a classifier, which is tuned. This way we achieve an accuracy of 79%.

## Date difference
The main idea here was to convert any date to the number of days from 1/1/0000. Then a simple difference would give the number of days between.

### Usage:
```
python date_diff.py --date1 23/03/2020 --date2 25/03/2020
```