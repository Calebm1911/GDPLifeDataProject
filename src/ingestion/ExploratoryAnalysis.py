# ExploratoryAnalysis.py - script to do EDA (exploratory data analysis) on the two primary data sets for the project. 
import pandas as pd
from ydata_profiling import ProfileReport

gdp_df = pd.read_csv("./Data/gdp_per_capita.csv")
life_df = pd.read_csv("./Data/lifeexpectancy.csv")

#Create HTML Reports for analysis
gdp_profile = gdp_df.profile_report()
gdp_profile.to_file(output_file="GDP_Profile.html")
life_profile = life_df.profile_report()
life_profile.to_file(output_file="Life_Profile.html")

