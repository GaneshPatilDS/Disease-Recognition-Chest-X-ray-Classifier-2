# Disease Recognition Using X-ray plates
### This repository contains a project for to classify X-ray images into three categories (COVID-19, Normal, and Pneumonia). The goal of this project is to develop a Deep learning model  that Accurately classify X-ray images into three categories: COVID-19, Normal, and Pneumonia through multiclass classification.

# The task involves assigning each image to one of the following groups:


1. COVID-19: X-ray images with manifestations of COVID-19 and associated lung abnormalities.


2. Normal: X-ray images depicting normal lung conditions without significant abnormalities.


3. Pneumonia: Images showing X-ray findings indicative of pneumonia, including lung infiltrates and opacities.

----------------------------------------------------------------------------------------------------------------


# Dataset Description:

The project uses an X-ray dataset sourced from Kaggle, containing images categorized into COVID-19, Normal, and Pneumonia classes.




--------------------------------------------------------------------------------------------------------------

  #  Architecture diagram  :

--------------------------------------------------------------------------------------------------------------                                        

                                      +----------------------+
                                      |      Data Source     |
                                      +----------------------+
                                               |
                                               |
                                      +----------------------+
                                      |     Data Ingestion   |
                                      +----------------------+
                                               |
                                               |
                                      +----------------------+
                                      |  Prepare Base Model  |
                                      +----------------------+
                                               |
                                               |
                                      +----------------------+
                                      |    Model Training    |
                                      +----------------------+
                                               |
                                               |
                                      +----------------------+
                                      |   Model Evaluation   |
                                      +----------------------+
                                               |
                                               |
                                      +----------------------+
                                      |   Model Deployment   |
                                      +----------------------+
                                               |
                                               |
                                      +----------------------+
                                      |     Prediction      |
                                      +----------------------+


----------------------------------------------------------------------------------------------------------------

# ❖User Input / Output Flow : 

--------------------------------------------------------------------------------------------------------------


       +---------------------------------------+
         | User Input (X-ray image) |
       +---------------------------------------+
               |
               |
       +--------------------------------------+
         |        Submit Image            |     
       +--------------------------------------+
               |
               |
       +--------------------------------------+
        |        Predicted Disease      |
       +--------------------------------------+

# In this flow:

  ### User Input (X-ray image): 
     The user provides an X-ray image for disease recognition. 

  ### Submit Image: 
     The input image is submitted for processing.

  ### Predicted Disease: 
     The system predicts the disease category (COVID-19, Normal, or Pneumonia) corresponding to the submitted X-ray image.
     
-------------------------------------------------------------------------------------------------------     

![f](https://github.com/GaneshPatilDS/Disease-Recognition-Chest-X-ray-Classifier-2/assets/123234894/35c066bf-3ee9-44f1-8338-1850b0793fda)

—-----------------------------------------------------------------------------------------------------

# Homepage: 
                                  
           Displays the disease recognition web app initial  interface.


—-----------------------------------------------------------------------------------------------------


![s](https://github.com/GaneshPatilDS/Disease-Recognition-Chest-X-ray-Classifier-2/assets/123234894/63e1757c-397b-49c4-881a-57cf7b7b7a94)


—----------------------------------------------------------------------------------------------------
# Image Input Options:

   ### Browse Button: 
            Allows users to select an image from their device using a file explorer.

   ###  Drag and Drop:
            Permits users to directly drop an image file onto the specified area for seamless upload.

—---------------------------------------------------------------------------------------------------


![t](https://github.com/GaneshPatilDS/Disease-Recognition-Chest-X-ray-Classifier-2/assets/123234894/4a6b0e99-cb58-46e1-9b16-b511957321dd)


—----------------------------------------------------------------------------------------------------

# Image Upload: 

          Once an image is chosen, it efficiently uploads to the app's server for prompt 

          processing.


—---------------------------------------------------------------------------------------------------


![four](https://github.com/GaneshPatilDS/Disease-Recognition-Chest-X-ray-Classifier-2/assets/123234894/5c70a2fa-237f-451b-b340-6e15e564a3e8)
![last](https://github.com/GaneshPatilDS/Disease-Recognition-Chest-X-ray-Classifier-2/assets/123234894/d5a78dcc-9921-490a-b510-19fd622eef24)

—-----------------------------------------------------------------------------------------------------

# Result Screen:


          After we upload your image successfully, the app quickly shows you the 

          final result. It clearly tells you what disease.


—------------------------------------------------------------------------------------------------------------------

# Please see the video below :

   ### The YouTube link is: 

--------------------------------------------------------------------------------------------------------------------

### How to Run
       conda create -n env python=3.8 -y
       conda activate env
       pip install -r requirements.txt
       streamlit run app.py
       open in browser: http://localhost:8501  (Local URL)
       
------------------------------------------------------------------------------------------------------------------       
       
### AWS-CICD-Deployment-with-Github-Actions
       1. Login to AWS console.
       2. Create IAM user for deployment
       
-----------------------------------------------------------------------------------------------------------------

### with specific access

       1. EC2 access : It is virtual machine

       2. ECR: Elastic Container registry to save your docker image in aws
       
------------------------------------------------------------------------------------------------------------------

### Description: About the deployment

      1. Build docker image of the source code

      2. Push your docker image to ECR

      3. Launch Your EC2 

      4. Pull Your image from ECR in EC2

      5. Lauch your docker image in EC2

### Policy:

      1. AmazonEC2ContainerRegistryFullAccess

      2. AmazonEC2FullAccess
      
      3. Create ECR repo to store/save docker image
      - Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/simple-app
      
      4. Create EC2 machine (Ubuntu)
      
      5. Open EC2 and Install docker in EC2 Machine:

          ---------------------------------------------------------------------------------------------
          ### optinal

         sudo apt-get update -y

         sudo apt-get upgrade

          ### required

          1. curl -fsSL https://get.docker.com -o get-docker.sh

          2. sudo sh get-docker.sh

          3. sudo usermod -aG docker ubuntu

          4. newgrp docker


          6. Configure EC2 as self-hosted runner:
            setting>actions>runner>new self hosted runner> choose os> then run command one by one
            
         7. Setup github secrets:
         
               AWS_ACCESS_KEY_ID=

               AWS_SECRET_ACCESS_KEY=

               AWS_REGION =

               AWS_ECR_LOGIN_URI = 

               ECR_REPOSITORY_NAME = 

         -------------------------------------------------------------------------------------------------------------








