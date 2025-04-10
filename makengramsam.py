import nltk
import re
import string
import collections
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer, sent_tokenize
from nltk.util import ngrams

input_file = 'kat.csv' #file with your data
output_file = 'testingvariables.csv' #file where your ngrams will be written 
text_column = 'text' #case sensitive name of column to read and make ngrams out of
no_grams = 200 #number of ngrams to generate
custom_stopwords = ['example_stopword1', 'example_stopword2'] #custom stopwords list

# Download NLTK resources if not already downloaded
# nltk.download('punkt')
# nltk.download('stopwords')

def load_stopwords(custom_stopwords=None):
    stop_words = set(stopwords.words('english'))
    if custom_stopwords:
        stop_words.update(custom_stopwords)
    return stop_words

# Load the CSV data
df = pd.read_csv(input_file)

# Assuming 'text' is the column containing the text data
texts = df[text_column]

# Convert all entries to strings and handle NaN values
texts = texts.astype(str).replace('nan', '')

# Combine all texts into a single string (if you want to analyze across all rows)
combined_text = ' '.join(texts)

# Clean the text (remove XML tags and ENDOFARTICLE, remove punctuation except apostrophes)
cleaned_text = re.sub('<.*?>', '', combined_text)  # Remove XML tags
cleaned_text = re.sub(r'ENDOFARTICLE\.?', '', cleaned_text)  # Remove ENDOFARTICLE
cleaned_text = re.sub(r'[^\w\s\']', '', cleaned_text)  # Remove all punctuation except apostrophes
cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()  # Remove extra spaces and newlines

# Tokenize the text into sentences
sentences = sent_tokenize(cleaned_text)

# Tokenize the text into words using TweetTokenizer to preserve contractions
tokenizer = TweetTokenizer()

# Pass custom stop words list if any
stop_words = load_stopwords(custom_stopwords)

# Process each sentence separately
unigram_freq = collections.Counter()
bigram_freq = collections.Counter()
trigram_freq = collections.Counter()

for sentence in sentences:
    tokenized = tokenizer.tokenize(sentence)
    filtered_tokens = [word for word in tokenized if word.lower() not in stop_words]
    
    # Create unigrams, bigrams, and trigrams for each sentence
    unigrams = ngrams(filtered_tokens, 1)
    bigrams = ngrams(filtered_tokens, 2)
    trigrams = ngrams(filtered_tokens, 3)
    
    # Update frequencies
    unigram_freq.update(unigrams)
    bigram_freq.update(bigrams)
    trigram_freq.update(trigrams)

# Get the top 200 most common n-grams
top_200_unigrams = unigram_freq.most_common(no_grams)
top_200_bigrams = bigram_freq.most_common(no_grams)
top_200_trigrams = trigram_freq.most_common(no_grams)

# Create a single DataFrame for all n-grams
data = {
    'Unigram': [gram[0] for gram, freq in top_200_unigrams],
    'Unigram_Frequency': [freq for gram, freq in top_200_unigrams],
    'Bigram': [' '.join(gram) for gram, freq in top_200_bigrams],
    'Bigram_Frequency': [freq for gram, freq in top_200_bigrams],
    'Trigram': [' '.join(gram) for gram, freq in top_200_trigrams],
    'Trigram_Frequency': [freq for gram, freq in top_200_trigrams]
}

df_ngrams = pd.DataFrame(data)

# Output DataFrame to a single CSV file
df_ngrams.to_csv(output_file, index=False)

print("CSV file generated successfully.")
