# 📰 News Sentiment Analysis Using AWS

## 📌 Project Overview

This project collects the latest news articles using NewsAPI and performs sentiment analysis to classify news as Positive, Negative, or Neutral.

The collected news data is stored in a PostgreSQL database and visualized using an interactive Streamlit dashboard.

AWS services are used to automate news collection, store data, and deploy the application in the cloud.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **API:** NewsAPI
- **Sentiment Analysis:** VADER Sentiment Analysis
- **Database:** PostgreSQL
- **Dashboard:** Streamlit
- **Version Control:** Git & GitHub
- **Cloud Platform:** AWS
- **AWS Services:** Lambda, EventBridge, S3, RDS, ECR, ECS
- **Containerization:** Docker

## 🔄 Project Workflow

1. Fetch the latest news articles using NewsAPI.
2. Analyze the sentiment of news articles using Python and VADER.
3. Classify articles as Positive, Negative, or Neutral.
4. Store the processed data in PostgreSQL.
5. Display news articles and sentiment results using Streamlit.
6. Automate news collection using AWS Lambda and EventBridge.
7. Store raw news data in Amazon S3.
8. Use Amazon RDS PostgreSQL for cloud database storage.
9. Containerize the Streamlit application using Docker.
10. Deploy the application using Amazon ECR and ECS.

## 📸 Project Dashboard

The Streamlit dashboard displays the latest news articles and their sentiment analysis results.

![News Sentiment Dashboard](images/dashboard.png)

## 📂 Project Structure

```text
news-sentiment-project/
│
├── collector/
│   └── collector.py
│
├── dashboard/
│   └── app.py
│
├── lambda/
│   └── lambda_function.py
│
├── images/
│   └── dashboard.png
│
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## ☁️ AWS Services

- **AWS Lambda:** Executes the news collection process.
- **Amazon EventBridge:** Schedules automatic execution.
- **Amazon S3:** Stores raw news data in JSON format.
- **Amazon RDS:** Stores processed news data in PostgreSQL.
- **Amazon ECR:** Stores Docker container images.
- **Amazon ECS:** Runs the containerized Streamlit dashboard.

## 🎯 Project Objective

The main objective of this project is to build an automated news sentiment analysis pipeline using Python, PostgreSQL, and AWS cloud services.

## 🚀 Project Status

🚧 Currently under development.