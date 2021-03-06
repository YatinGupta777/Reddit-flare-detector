# Reddit-flare-detector
 
The best model found in this repo is used in Web App : https://reddit-flare-detector.herokuapp.com/

Details about the Web App : https://github.com/YatinGupta777/Reddit-Flare-Detector-Web-App
(A separate Repo to have clean heroku builds, easy to use both the projects and proper organization)

Files info : 

1. Flare Detector : Main Code that perform data collection, exploratory data analysis and model building
2. Experiment Log : Summarizes the various approaches, models, results , data etc.**(Detailed Explanation here and in Code)**
3. Requirements.txt : Libraires required to run the project
4. Images : Images used in experiment log

[These 4 files can be directly downloaded to use in an application if required]

1. Classes.npy : Encoder's details to directly use in Web App
2. Model.pkl : Best model used in Web App
3. tfidf.pickly : TfIdf to be used in Web App
4. Original_expanded_data : 400,000+ Reddit posts analyzed here. This data is downloaded so that it can be directly used again.

All the data was downloaded from subreddit r/india.

# Installation

Dependencies are mentioned in requirements.txt

Clone the repo

```
git clone https://github.com/YatinGupta777/Reddit-flare-detector.git
cd Reddit-Flair-Detection/
```
Run
```
pip install -r requirements
```
# Approach

After reading about the various text processing technique and text classification algorithms, Naive-Bayes, SVM, Random Forect, SGD, and Logistic Regression algorithms were used.

#### General points
1. Only title and body of posts are used to train the models.
2. Comments seem irrelevant since flares are supposed to be describing the post

#### Divided into 4 sections :

Section 1, 2, 3 : Data collected using praw. Collecting 1000 top, new and hot posts and after duplicate removal around ~2k posts remained.

Section 1: Target had flares with greater than 3 posts.

Section 2: Target had flares with greater than 100 posts.

Section 3: Data collected above in section 3 is oversampled.

Section 4: 
  * 400,000+ posts downloaded. 
  * Flares with greater than 3000 posts taken. 
  * Data is undersampled. 
  * Final Data had 11 flares, with each around ~3K posts.

# Overview of model's accuracies :

I. **Data : Top 15 flares , ~1800 Total posts** 

| Model        | Accuracy       | 
| ------------- |:-------------:| 
| Naive Bayes     | 52% | 
| SVM      | 56%      |   
| Random Forest | 55%      |    
| SGD | 54%     |    
| Logistic Regression | 53%     |    

II. **Data : Top 4 flares , ~1800 Total posts** 

| Flare        | Posts       | 
| ------------- |:-------------:| 
| Non Political     | ~500 | 
| Politics      | ~400     |   
| Coronavirus | ~400     |    
| AskIndia | ~150     |    

| Model        | Accuracy       | 
| ------------- |:-------------:| 
| Naive Bayes     | 63% | 
| SVM      | 66%      |   
| Random Forest | 56%      |    
| SGD | 66%     |    
| Logistic Regression | 61%     |   

III. **Data : Top 4 flares , Over Sampling the data** 

Each flare had 400-500 posts

| Model        | Accuracy       | 
| ------------- |:-------------:| 
| Naive Bayes     | 60% | 
| SVM      | 78%      |   
| Random Forest | 71%      |    
| SGD | 77%     |    
| Logistic Regression | 77%     |   

IV. **Data downloaded : (400,000+ posts )**
Pushshift Api was repeatedly used to gather the data.

Top 11 flares taken with 3000+ posts.

Random undersampling to equate data count.

| Model        | Accuracy       | 
| ------------- |:-------------:| 
| Naive Bayes     | 53% | 
| SVM      | 54%      |   
| Random Forest |  53%   |    
| SGD | 54%     |    
| Logistic Regression | 50%  |   

Although the last models have lesser accruacy than part III, these are trained on more data and can predict 11 flare types.

As seen in this confusion matrix, this model performs well except for few flares (room for improvement :) )
![Confusion matrix](https://github.com/YatinGupta777/Reddit-flare-detector/blob/master/Images/cm3.png?raw=true)


Final model used : SVM (Part IV )

(Accuracies were measured by 30% split between training and test data)
