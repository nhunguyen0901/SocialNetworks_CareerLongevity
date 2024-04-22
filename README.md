# Social Networks and Women Leaders' Career Longevity

This repository hosts the analyses for an ongoing research project exploring the potential of social networks in promoting career success. Using IMDb data, I trace the evolution of networks over time and examine how these changes influence people's career longevity and productivity. I specifically focus on the different impacts networks have on men and women, offering strategies for crafting more beneficial and equitable professional networks.

This repository will be updated periodically as the research evolves.

## Navigating the complexity of large-scale networks

Imagine nearly 5 billion potential connections in a yearly network comprising roughly 100,000 individuals. Over 23 years, this balloons to more than 100 billion potential connections. I find this feature of networks fascinating—as each new individual joins, the possibilities for new links grow exponentially because each newcomer can in theory connect with all the existing members.

Another thing I love about networks is that they are constantly changing, with old ties dissolving and new ones forming. To capture these shifts, I've constructed and analyzed 21 sequential network graphs, each spanning a three-year period. Starting from from 2000-2002 data and moving through to 2020-2022, this method allows me to track the changes in people's social capital up to 2023. 

## Notebooks in this Repository:

1. Phase_1_Tracking_Movie_Directors_Career.ipynb: I identify first-time directors and follow their filmography from 2003 to 2023.
2. Phase_2_Constructing_Filmmaker_Network.ipynb: I build dynamic collaboration networks within the film industry from 2000 to 2023 and calculate the yearly brokerage social capital for every creative workers in the network using a 3-year moving window.
3. Phase_3_Predicting_Director_Gender.ipynb: I use directors' first names from IMDb data and U.S. Social Security data to predict gender.
4. Phase_4_Building_Time_Series_Data.ipynb: I create a dataset that tracks each director's career year by year, setting up for a survival analysis.
- [Additional Notebooks]: As the study progresses, more phases of the analysis will be added. These phases will delve into (a) adding time-varying and time-invariant predictors to the time-series data and (b) survival analysis to explore how connections with network brokers and other factors influence the career longevity of both women and men movie directors.

## Reproducibility and Data Source

This work uses publicly available data from IMDb and the U.S. Social Security Administration. The analyses can be entirely recreated by following the provided Python codes—though keep in mind, results may vary depending on when you access the data, which is updated regularly.