# Example 1, do not modify!
import pandas as pd
import matplotlib.pyplot as plt

netflix=pd.read_csv("netflix_titles.csv")

netflix_by_year=netflix.sort_values("release_year")
print(netflix_by_year.isnull().sum())

M_night=netflix[netflix["director"]== "M. Night Shyamalan"]
print(M_night)

movies=netflix[netflix["type"]=="Movie"]
print(movies.isnull().sum())

Full_movies=movies.fillna("unknown")
print(Full_movies.info())

Full_movies.to_csv("Full_netflix-movies.csv")







