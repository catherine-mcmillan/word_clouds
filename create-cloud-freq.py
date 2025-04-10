import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import warnings
import random

input_file = 'testingvariables.csv'
frequency = 'Bigram_Frequency'
grams = 'Bigram'
word_color = "rgb(21, 42, 122)"
bg = 'white'
cloud_width = 1920 #width
cloud_height = 1080 # height
cloud_font = '/Library/Fonts/Arial.ttf'

warnings.filterwarnings("ignore")

# Load the dataset
df = pd.read_csv(input_file, index_col=0)

# Ensure to use the frequencies listed in the "Frequency" column
# Convert frequencies to numeric and drop rows with missing values
df[frequency] = pd.to_numeric(df[frequency], errors='coerce')
df = df.dropna(subset=[grams, frequency])

# Combine multiple text entries to ensure enough bigrams
bigrams = df[grams][:1000]  # Adjust the range as needed
frequencies = df[frequency][:1000]

# Create a dictionary of bigrams and their frequencies
bigrams_freq_dict = dict(zip(bigrams, frequencies))

# Function to generate a random color in shades of grey and white
#def grey_white_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
#    grey_shade = random.randint(200, 255)
#    return f"rgb({grey_shade}, {grey_shade}, {grey_shade})"

# Function to set the word color to blue
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return word_color

# Create and generate a word cloud image using bigrams and their frequencies
wordcloud = WordCloud(
    collocations=False,
    normalize_plurals=True,
    background_color=bg,  # Set background color to white
    color_func=color_func,  # Set word color to blue
    prefer_horizontal=1.0,  # Ensure all words are horizontal
    width=cloud_width,
    height=cloud_height,
    font_path= cloud_font # Path to Arial or Calibri font
).generate_from_frequencies(bigrams_freq_dict)


# Display the generated image
plt.figure(figsize=(19.2, 10.8))  # Adjust the figure size to match the word cloud dimensions
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
