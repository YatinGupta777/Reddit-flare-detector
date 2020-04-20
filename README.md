# Reddit-flare-detector
 
The best model found here is used in Web App : https://reddit-flare-detector.herokuapp.com/

Details about the Web App : https://github.com/YatinGupta777/Reddit-Flare-Detector-Web-App
(A separate Repo to have clean heroku builds, easy to use both the projects if anyone wishes and proper organization)

Files info : 

1. Flare Detector : Main Code that perform data collection, exploratory data analysis and model building
2. **Experiment Log : Summarizes the various approaches, models, results , data etc.**
3. Requirements.txt : Libraires required to run the project
4. Images : Images used in experiment log

[These 3 files can be directly downloaded to us in an application if required]

1. Classes.npy : Encoder's details to directly use in Web App
2. Model.pkl : Best model used in Web App
3. tfidf.pickly : TfIdf to be used in Web App

Overview of model's accuracies :

I. ** Data : Top 15 flares , ~1800 Total posts ** 

| Model        | Accuracy       | 
| ------------- |:-------------:| 
| Naive Bayes     | 52% | 
| SVM      | 56%      |   
| Random Forest | 55%      |    
| SGD | 54%     |    
| Logistic Regression | 53%     |    

II. ** Data : Top 4 flares , ~1800 Total posts ** 

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

III. ** Data : Top 4 flares , Over Sampling the data ** 

Each flare had 400-500 posts

| Model        | Accuracy       | 
| ------------- |:-------------:| 
| Naive Bayes     | 63% | 
| SVM      | 75%      |   
| Random Forest | 71%      |    
| SGD | 73%     |    
| Logistic Regression | 72%     |   

IV. ** Data downloaded : (400,000+ posts )**
Top 11 flares taken with 3000+ posts.
Random undersampling to equate data count.

| Model        | Accuracy       | 
| ------------- |:-------------:| 
| Naive Bayes     | 55% | 
| SVM      | (TBD : Taking long time to train)       |   
| Random Forest |  52%   |    
| SGD | 54%     |    
| Logistic Regression | (TBD : Taking long time to train)  |   


(Accuracies were measured by 30% split between training and test data)
