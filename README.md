# University-Projects
This repo includes projects i have done in the time i learned at University of Information &amp; Technology.
# Project Summarization
## Project 1: Airline Sentiment Classification
In this project, our team includes 3 people downloaded a dataset about British airline's comments on the website. The dataset includes 2 columns are: comments and the rating of the customers.

Our team performed a labeling process which includes creating guidelines, testing the annotators performance and labeling the comments into three sentiments labels: 0 - Negative, 1 - Positive ,2 - Neutral
After that, we trained a model with the comments and ratings at input and the labels at the output.

![alt text](https://github.com/plctrung26/University-Projects/blob/main/images/project1.png?raw=true)

## Project 2: Predict Casio Watch Price
In this project, we perform data collection, data cleaning, data analysis, visualizing the data and running models.

The collection process will include three members collecting from three different e-commerce website with the Casio watch product in Vietnam (Sendo, thegioididong, watchstore). I used Selenium together with BS4 as the packages to crawl data using Python language. As my part is collecting data from Sendo, the code will only presented on this site. 

After the collection step, we will combine the three collected data into one final dataset and perform data cleaning.

Finally the data will be used to train a model to predict the price of a CASIO Watch.

![alt text](https://github.com/plctrung26/University-Projects/blob/main/images/project2.png?raw=true)

## Project 3: Real time inhouse temperature regression
In reality, the temperature in a room or a house can be different from the outdoor temperature. This may bring up many benefits especially in indoor farming. We present a project to predict the inhouse temperature giving outdoor temperature, humidity and indoor humidity. We performed data collection, data cleaning, data analysis and running a model to learn the features. And to be close to reality, we decided to make the predictions real-time, which means the prediction fast only take from 1 to 2 seconds despite the scaling up of data size.

As we do not have the device to correctly calculate the indoor temperature, we decided to use an off-to-shelf dataset on Kaggle which inincludes the temperature collected in a museum of columbia. To correctly collect the outdoor temperature with the corresponding time, we decided to crawl columbia temperature and humidity from a weather website using Selenium and BS4. After that we matched the corresponded time of the ourdoors info and the indoor temperature.

Finally we train them through a deep learning model to predict the inhouse temperature. All the data cleaning process will be performed with pyspark to correctly stimulate the speed when the data scale up in memories

![alt text](https://github.com/plctrung26/University-Projects/blob/main/images/project3.png?raw=true)

## Project 4: Real-time ECG classification
ECG(electrodiagram) measures human heartbeat and analyse them may help patients and doctors to detect anomalies of a disease. So we decided to perform a classification on ECG data to predict anomalies in real-time. In this project, we want to make the prediction global and distributed to be suitable for real-time. That is why we use Aiven cloud as a platform (because it is free) together with Kafka to stimulate the data process sent from place A to place B to be predicted. The data is already provided on Kaggle with more than 100 columns. We then follow the instruction of the dataset to successfully transform into trainable data.

The specialty in this project is that the models will be trained distributedly on different devices (2 GPUs and 8 TPUS) and the data when collected will be sent up to a cloud server to examine by doctors at other places (stimulation).

![alt text](https://github.com/plctrung26/University-Projects/blob/main/images/project4.png?raw=true)
