# Social Networks and Career Longevity

This repository chronicles my ongoing research into the role of social networks in fostering career longevity and productivity. Using IMDb data, I trace the evolution of networks over time and examine how these changes influence people's career longevity and productivity. I specifically focus on the different impacts networks have on men and women, offering strategies for crafting more beneficial and equitable professional networks.

## Navigating the complexity of large-scale networks

Imagine a network comprising about 100,000 individuals. Annually, this network could potentially foster nearly 5 billion connections, which baloons to over 100 billion across two decades. This staggering complexity stems from two inherent features of networks. First is exponential growth: each time a new individual joins, the network's potential connections expand exponentially; every newcomer brings the possibility to connect with all existing members. Second is constant flux: like the ebb and flow of the ocean, networks are never static; old connections dissolve and new ones emerge continually. 

To capture these shifts, I've constructed and analyzed 21 sequential network graphs. Each graph spans a three-year period, starting from 2000-2002 and stretching to 2020-2022. This methodological approach allows me to track the evolution of social capital up to the year 2023, providing a longitudinal view of how connections impact career trajectories.

## Notebooks in this Repository:

1. Phase_1_Tracking_Movie_Directors_Career.ipynb: I identify first-time directors and follow their filmography from 2003 to 2023.
2. Phase_2_Building_Time_Series_Data.ipynb: I create a dataset that tracks each director's career year by year, as well as a dataset that summarizes each director's first career decade.
3. Phase_3_Constructing_Filmmaker_Network.ipynb: I build dynamic collaboration networks within the film industry from 2000 to 2023 and calculate the yearly brokerage social capital for every creative workers in the network using a 3-year moving window.
4. Phase_4_Incorporating_Network_Variables_to_Career_Data.ipynb: I map the pre-calculated brokerage scores to directors and their collaborators at the time of their collaboration.
5. Phase_5_Predicting_Gender_From_Names.ipynb: I use directors' first names from IMDb data and U.S. Social Security data to predict gender.

- [Additional Notebooks]: As the study progresses, more phases of the analysis will be added. These phases will (a) add control variables to directors' career data and (b) survival analysis to explore how connections with network brokers and other factors influence the career longevity of both women and men movie directors.

## Reproducibility and Data Source

This work uses publicly available data from IMDb and the U.S. Social Security Administration. The analyses can be entirely recreated by following the provided Python codes—though keep in mind, results may vary depending on when you access the data, which is updated regularly.