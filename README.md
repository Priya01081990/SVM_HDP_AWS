# Deploy ML Model (sklearn svm) to AWS Lambda

This project is about how to upload an ml model to aws lambda.

It assumes that user has 
 - AWSCLI installed
 - user runs 'aws configure' to set proper parameters for aws connection
 - user has python 3.9
 - user has 'virtual env'

# Steps

    1. Download the project from git
    2. cd 'project_dir'
    3. Activate 'venv' and install from 'install.txt'
    4. run 'zappa deploy7update '__Project__NAME__' (e.g. dev)
