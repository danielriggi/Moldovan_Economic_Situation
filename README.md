 # Republic of Moldova Economic Situation
![](images/moldova_flag.png)
![](images/Location_Moldova_Europe.png)
 ## Background and Motivation
 The Republic of Moldova is a landlocked country in Eastern Europe bordered by Romania to the west and Ukraine to the north,east, and south. Moldova is also the <a href="https://www.jagranjosh.com/general-knowledge/top-10-poorest-countries-in-europe-1538044990-1">poorest country in Europe</a>, as well as the country with the lowest  <a href=https://en.wikipedia.org/wiki/Human_Development_Index> Human Development Index</a>. The territory of Moldova 
has changed hands often throughout history. Most recently, during the dissolution of the Soviet Union, Moldova declared independence on 27 August 1991. Like many former Soviet countries, the fall of the USSR ushered in a period of economic and civil unrest. I'm interested in Moldova because it was my last deployment as a soldier. I was there during a period leading up to an election, and political opinions starkly varied between pro Western and pro Russian candidates. I wanted to see what type of effect Russia has had since the breakup of the Soviet Union on it's neighboring countries. 
## The Data
The data was collected from <a href=https://data.humdata.org/>humdata.org</a>, a website with a wide variety of humanitarian data. I used a dataset containing informaiton about twenty eight economic and social indicators. I collected this information about Moldova and it's neighboring countries, as well as a few larger European economies, specifically Moldova, Romania, Ukraine, Belarus, Georgia, Russia, Germany, France, and Great Britain. Some of the indicators had information back to 1960, however, there were many incomplete columns and data beginning in the 90's were more common. Luckily however, each dataset was formatted the same, allowing me to apply the same pipeline I used on the Moldova dataset to all others. 
## Exploratory Data Analysis
The first indicator I looked at was Gross Domestic Product <a href=https://en.wikipedia.org/wiki/Gross_domestic_product>(GDP)</a> per capita in <a href=https://en.wikipedia.org/wiki/International_United_States_dollar>international dollars</a>. For all countries but Moldova this was available since 1990. For Moldova it was available beginning in 1995. Besides Romania, the prior Soviet countries experienced significant declines in GDP in the 90's, followed by steady economic growth. The recession of 2008 is also visible for all countries. 
![](images/gdp_bar.png)

I wanted to visualize this information on the same plot, to see how Russia's neighbor's economies behaved in relation to Russia. Again, the effect of the recession of 2008 is visible. In addition, there is a visible downturn following international sanctions on Russia following the <a href=https://en.wikipedia.org/wiki/Annexation_of_Crimea_by_the_Russian_Federation>annexation of Crimea</a>. However, this effect is only seen on Russia, Belarus, and Ukraine, while Moldova appeared to avoid it. 

![](images/gdp_line_neighbors.png)

Now adding the large economies:

![](images/gdp_line_all)
