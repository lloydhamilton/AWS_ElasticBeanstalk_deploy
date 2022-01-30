# Deploying Docker Containerised ML Models on AWS Elastic Beanstalk

![GitHub](https://img.shields.io/github/license/lloydhamilton/AWS_ElasticBeanstalk_deploy?logo=GitHub&style=plastic) ![GitHub Repo stars](https://img.shields.io/github/stars/lloydhamilton/AWS_ElasticBeanstalk_deploy?logo=GitHub&style=plastic) ![](https://img.shields.io/badge/-Docker-blue?style=plastic&logo=Docker) ![](https://img.shields.io/badge/-AWS-orange?style=plastic&logo=Amazon-AWS)


<hr>

This  repository contains source code referenced in the original medium article linked [here](https://medium.com/@lloyd.hamilton/deploying-docker-containerised-ml-models-on-aws-elastic-beanstalk-67cbfbb2def4)

## Introduction

It is without doubt that machine learning has fundamentally transformed how we interact with technology today and will continue to do so in years to come.

My journey into the world of data science has taught me that training a ML model is really only part of any ML solution. Most data enthusiasts are capable of training a model but to deploy that model in order to make it useful is a whole other challenge.

By the end of this guide, I will help you answer the questions I have asked myself countless times:

***How do I deploy my Machine Learning models?***

***How do I serve my models?***

I will help you take your first steps into the growing field of Machine Learning Engineering by showing you how to deploying your ML models on AWS within a Docker container. Here are the key steps we will be taking to deploy our model on AWS Elastic Beanstalk.

1. Train a RandomForest Classifier.
2. Build a simple Flask app with an API endpoint.
3. Containerise our application using Docker.
4. Deploy the containerised application on AWS elastic beanstalk.
5. Serving our model as an API.

