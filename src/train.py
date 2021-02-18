import pandas as pd
import numpy as np
import joblib
import os 

base_dir = os.getcwd()
input_dir = base_dir + '/input/'

if __name__ == "__main__":
    reviews_df = pd.read_csv(input_dir + 'Musical_instruments_reviews.csv')
    print(reviews_df.head())