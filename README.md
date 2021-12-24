# Deploying Docker Containerised ML Models on AWS Elastic Beanstalk

<hr>

This  repository contains source code referenced in the original medium article linked [here](https://medium.com/@lloyd.hamilton/deploying-docker-containerised-ml-models-on-aws-elastic-beanstalk-67cbfbb2def4)

##Introduction
What do an iPhone photo library, an Amazon shopping basket and a Netflix home page all have in common?

One way or another, each of these applications interacts with a Machine Learning model to improve user experience and to better serve end users.

It is without doubt that machine learning has fundamentally transformed how we interact with technology today and will continue to do so in years to come.

My journey into the world of data science has taught me that training a ML model is really only part of any ML solution. ML models in production requires a lot of aftercare as they degrade over time. ML models are dynamic and sensitive to change in the real world. Therefore, the deployment of a ML model into production requires complementary infrastructure to manage its production life cycle.

This guide is not going to detail the intricacies of managing the life cycles of ML models in production. It will however help you answer the questions I have asked myself countless times:

How do I deploy my Machine Learning models?

How do I serve my models?

I will help you take your first steps into the growing field of Machine Learning Engineering by showing you how to deploying your ML models on AWS within a Docker container. 

Here are the key steps we will be taking to deploy our model on AWS.

1. Train a RandomForest Classifier.
2. Build a simple Flask app with an API endpoint.
3. Containerise our application using Docker.
4. Deploy the containerised application on AWS elastic beanstalk.
5. Serving our model as an API.

