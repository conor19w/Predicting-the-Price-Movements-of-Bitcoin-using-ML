# Predicting-the-Price-Movements-of-Bitcoin

This was for my final year thesis.
But really this was just to get my foot in the door when it comes to machine learning it was just a fun project for a classification problem, In reality the system wouldn't be profitable when you take into account the trading fees.



Predicting the price move of bitcoin minute by minute using Bitmex Websocket for data
1. Abstract:

Bitcoin is a form of digital currency known as a cryptocurrency, it was invented in 2008, by an unknown person/group of people who are now referred to by the name Satoshi Nakamoto.
Bitcoin is Decentralized meaning there is no single administrator or authority monitoring the network, it is monitored by a large peer to peer network. 
Transactions are verified by this network and recorded on a public ledger known as the blockchain.
This paper explores the accuracy of predicting price movements of XBTUSD (bitcoin against the US Dollar) on the cryptocurrency exchange Bitmex, using machine learning methods.
This is achieved through use of Machine Learning classifiers namely Support Vector Machines, Decision Trees, Neural Networks, Random Forests & the K-Nearest Neighbour algorithm.
The Aim of this paper is to combine Machine Learning & Technical Analysis, in order to predict the price movements of bitcoin and assess the profitability of the Machine Learning models I have developed.
 
2. Introduction:
 2.1 Motivation 
Bitcoin is an extremely volatile asset, its price against the USD often fluctuates thousands of Dollars in a matter of hours. Predicting these moves could be very profitable.
This project aims to do just this and profit on the Margin of increase/decrease the market undergoes.

2.2 Problem Statement
At an abstract level, the goal of this project is to classify movement up or down as a ‘1’ or a ‘0’, respectively.
Then using these classifications the goal is to simulate trading on live data & hopefully profit off the margin by going short (predicting a decrease in price) or going long (predicting an increase in price) if the prediction is correct, we will profit off the margin.

2.3 Approach
The approach of this project was to utilise Technical Analysis which is a methodology for forecasting the direction of prices through the study of past market data.
I collected between 2 & 3 months of data in 1-minute intervals, the data consisted of the Opening price, Closing price, Highest price, Lowest Price & the total Volume over each 1-minute period.
Using this data, I generated a csv file with outputs from 12 technical indicators for each minute interval over the three months & trained various machine learning algorithms on these outputs in order to predict a ‘1’ or a ‘0’ indicating an expected increase or decrease, respectively.
Models were then tested not on their accuracy of predicting 1 minute ahead but instead on their profit if we were to use the ‘1’ classification as a signal to buy/go long & the ‘0’ classification as a signal to sell/go short.

2.4 Metrics
Model Accuracy:
The predictions when classifying up or down were compared against the actual movements to give an accuracy score.


Model Profit:
By simulating the flow of data as if it were live, I evaluated the profitability of each model on the three months of data & chose models which had the highest PV value. Models were trained on 30% of the dataset to avoid overfitting.
 The PV value is a good estimate of the average returns as a percent of your investment.
PV value =  ( (Total Profit)/(Number of Trades)×100)/(Volume Traded) 

3. Technical Background:
Technical Analysis
Technical Analysis is an approach to trading which was first introduced by Charles Dow with the Dow Theory in the late 1800’s.
Assumptions of Technical Analysis introduced by Dow:
	Markets are efficient with values representing factors that influence a security’s price.
	Even random market price movements appear to move in identifiable patterns and trends that tend to repeat over time.
There are three general assumptions that are widely accepted today by technical analysts:
	The market discounts everything:
This assumes that everything from a company’s fundamentals to broad market factors such as market psychology are already accounted for in the price of a stock.

	Price moves in trends:
Prices tend to move in trends and are likely to continue a past trend rather than move erratically.

	History repeats itself:
The repetitive behaviour of a markets price movement is believed to reflect the market psychology.

How can Technical Analysis be used?
Using a broad spectrum of indicators that look at different features of the market.
This project utilises Volume & momentum indicators, Oscillators & moving averages.
A single indicator alone cannot predict market moves very well, but together they confirm each other and provide a more accurate prediction.
