# Social Networks and Women Leaders' Career Longevity

This repository hosts the analyses for an ongoing research project exploring the potential of social networks in promoting career longevity for women in leadership positions. Specifically, I examine the question: can connections with network brokers foster longer and more prolific careers for women movie directors? Does this network effect differ from their men counterparts? 

This repository will be updated periodically as the research evolves.

## Project Motivation

This project is inspired by a puzzling finding in social capital research. Typically, being a network broker — a person who connects different social circles — is associated with career advancement. However, this doesn't seem to hold true for women. In fact, evidence suggests that such roles might actually impede women's careers. For my PhD dissertation, I want to explore an alternative pathway for women to benefit from brokerage networks - by forming connections to network brokers. 

To do this, I use IMDb data to construct dynamic collaboration networks of filmmakers from 2000 to 2023 and examine the influence of collaborators' brokerage social capital on career longevity of directors who made their debut between 2003 and 2013.

## Notebooks in this Repository:

1. Phase_1_Tracking_Movie_Directors_Career.ipynb: This notebook details the initial phase of the research, with Python code for identifying of first-time directors and tracking their filmography from 2000 to 2023. This notebook lays the foundation for constructing collaboration networks and analyzing career longevity.
2. Phase_2_Constructing_Filmmaker_Network.ipynb: This notebook focuses on constructing dynamic collaboration networks among creative workers in the film industry from 2000 to 2023 and calculating brokerage social capital for everyone in the network, year by year. From there, we can extract the brokerage scores of the collaborators of the directors in our study. 
- [Additional Notebooks]: As the study progresses, subsequent phases of the analysis will be added. These will include (a) predicting the gender of filmmakers based on their first names, using IMDb data and US Social Security Administration records and (b) survival analysis to explore how connections with network brokers affect the career longevity of both women and men movie directors. 

## Reproducibility 

The analyses and results presented in this repository can be entirely recreated by following the provided Python codes in the Jupyter notebooks. Results may vary slightly depending on when the IMDb data is accessed, as it is updated regularly.

## Data Source
 
The primary data source for this project includes the following IMDb's datasets: 'title.basics', 'title.principals', 'title.ratings', and 'name.basics.tsv.gz'. These datasets provide comprehensive information about movies, key personnel, movie ratings, and filmmaker demographics. Additionally, I use data from the US Social Security Administration to predict the gender of filmmakers. 