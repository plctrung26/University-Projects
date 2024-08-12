# University-Projects
This repo includes projects i have done in the time i learned at University of Information &amp; Technology.
# Project Summarization
## Project 1: Airline Sentiment Classification
### Skills:
* Data labeling
* Data cleaning
* Auto-labeling
* Data analysis

### Content:
In this project, our team includes 3 people downloaded a dataset about British airline's comments on Kaggle. The dataset includes 2 columns are: comments and the rating of the customers.

Our team performed a labeling process which includes creating guidelines, testing the annotators performance and labeling the comments into three sentiments labels: 0 - Negative, 1 - Positive ,2 - Neutral
After that, we compared the manually labeled classes to classes created from an off-the-shell model to analyse the performance and quality of the classes. Finally, we trained a model with the data above to classify the sentiment of a comment.

![alt text](https://github.com/plctrung26/University-Projects/blob/main/images/project1.png?raw=true)

## Project 2: Predict Casio Watch Price
### Skills:
* Data collection (web crawling)
* Data cleaning
* Data analysis
* Data visualization

### Content:
In this project, we will train a model to be able to predit the price of a Casio watch based on the meta data of the watch like: the radian of the watch, the water-proof ability, or the brand, etc... To accurately predict the price and information, our team decide to collect the data from three different popular e-commerce websites in Vietnam (Sendo, thegioididong, watchstore) and only focus on the products from CASIO brand.

The collection process will include three main steps: 
* Self collection
* Data conbination
* Data cleaning

As our team has 3 members, each will collect the data from each e-commerce websites with the Casio watch above (Sendo, thegioididong, watchstore). I used Selenium together with BS4 as the packages to crawl data using Python language. As my part is collecting data from Sendo, the crawling method will only present on this site

On the data combination step, we will combine the three collected data into one final dataset and perform data cleaning. The reason for this step is that the metadata of a watch are slightly different on each website and even on different sellers of an e-commerce website. Three members will have to decide with metadata will be kept and which will be skipped. Finally we combine the data from three website into one final data and use it to train the models

Before training, the data will be cleaned, the main cleaning task are dealing with the "null" rows when combined data and the columns name which might be different on each website.

Finally the data will be used to train a model to predict the price of a CASIO Watch.

![alt text](https://github.com/plctrung26/University-Projects/blob/main/images/project2.png?raw=true)

## Project 3: Real time inhouse temperature regression
### Skills:
* Data collection (auto web crawling)
* Distributed Data Transforming (Pyspark)
* Data Cleaning
* Data analysis
* Big data

### Content:
In reality, the temperature in a room or a house can be different from the outdoor temperature. This may bring up many benefits especially in indoor farming. We present a project to predict the inhouse temperature giving outdoor temperature, humidity and indoor humidity. We performed data collection, data cleaning, data analysis and running a model to learn the features. And to be close to reality, we decided to make the predictions real-time, which means the prediction fast only take from 1 to 2 seconds despite the scaling up of data size.

As we do not have the device to correctly calculate the indoor temperature, we decided to use an off-to-shelf dataset on Kaggle which inincludes the temperature collected in a museum of columbia. To correctly collect the outdoor temperature with the corresponding time, we decided to crawl columbia temperature and humidity from a weather website using Selenium and BS4. After that we matched the corresponded time of the ourdoors info and the indoor temperature.

Finally we train them through a deep learning model to predict the inhouse temperature. All the data cleaning process will be performed with pyspark to correctly stimulate the speed when the data scale up in memories

![alt text](https://github.com/plctrung26/University-Projects/blob/main/images/project3.png?raw=true)

## Project 4: Real-time ECG classification
### Skills:
* Distributed Calculating
* Data Collecting (web crawling)
* Distributed Storing
* Data cleaning
* Data analysis

### Content:
ECG(electrodiagram) measures human heartbeat and analyse them may help patients and doctors to detect anomalies of a disease. So we decided to perform a classification on ECG data to predict anomalies in real-time. In this project, we want to make the prediction global and distributed to be suitable for real-time. That is why we use Aiven cloud as a platform (because it is free) together with Kafka to stimulate the data process sent from place A to place B to be predicted. The data is already provided on Kaggle with more than 100 columns. We then follow the instruction of the dataset to successfully transform into trainable data.

The specialty in this project is that the models will be trained distributedly on different devices (2 GPUs and 8 TPUS) and the data when collected will be sent up to a cloud server to examine by doctors at other places (stimulation).

![alt text](https://github.com/plctrung26/University-Projects/blob/main/images/project4.png?raw=true)
