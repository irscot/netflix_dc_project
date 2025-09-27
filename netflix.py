# Importing pandas, numpy and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1) Filter the data for movies released in the 1990s

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv", index_col = 0)

# creating Boolean Series for 90's content on netflix by using numpy
netflix_release_year = netflix_df['release_year']
nineties = np.logical_and(netflix_release_year >= 1990, netflix_release_year <= 1999)

# using nineties to filter the DataFrame netflix_df to show only 90s content on netflix
netflix_90s = netflix_df[nineties]

# Testing if it works: calling netflix_90s to get the table in DataCamp notebook
# netflix_90s


# 2) Find the most frequent movie duration

# visualizing data with a histogram to view distribution of durations for 90s movies
plt.hist(netflix_90s['duration'], bins = 30) # shows that 100 minutes is the most frequent duration
plt.show()

# setting up duration variable according the distribution that was shown in histogram for most frequent duration
duration = 100


# 3) Count the number of short action movies from the 90s



# using & to combine conditionals for 90s being the release year period and the genre action
genre = netflix_df['genre']
nineties_action = np.logical_and(netflix_release_year >= 1990, netflix_release_year <= 1999) & (genre == 'Action')

# using nineties_action to filter the DataFrame netflix_df to just 90s action films on netflix
netflix_90s_action = netflix_df[nineties_action]

# Testing if it works: calling netflix_90s_action to get the table in DataCamp notebook
# netflix_90s_action


# setting up a counter and setting it to default number 0
short_movie_count = 0


# making a for loop to iterate through the DataFrame filtered for 90s action by using netflix_90s_action DataFrame
for lab, row in netflix_90s_action.iterrows():
    if row['duration'] < 90:
        short_movie_count += 1
    else:
        short_movie_count += 0

print(f"There are {short_movie_count} 90s action films on Netflix.")