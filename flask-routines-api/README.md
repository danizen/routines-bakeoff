# routines-api

A serverless Flask application that can be deployed with zappa (or serverless)

## Data Model

A routine is a list of activities that are displayed as checkboxes each day

```javascript
{
   name: "Morning",
   description: "Getting up and out the door",
   items: [
     "Shower",
     "Get dressed",
     "Take pills",
     "Make coffee",
     "Make breakfast",
     "Eat breakfast",
     "Get badge",
  ]
}
```

Routines are associated with users.

## Requirements and Constraints

- It must be possible to run the application on a Windows Desktop without using Docker
- It must be possible to use RDS and DynamoDB from the Desktop
- It must be possible to deploy the application with an existing role, rather than having the
  application framework create a role.
- It must be possible to package the application as a ZIP without deploying, allowing DevOps
  to deploy however they wish.
- The API is implemented in Python for 2 reasons:
   - Preserve the capabilities of the team
   - I am who I am

## Current Architecture

- Flask - Since we do not have Docker, we cannot use the local versions of API Gateway available with AWS SAM CLI.  Because of this, we need to choose an application framework that will route our URLs, but maybe not much more, so that we can run our application on the desktop without Docker.  This also gives some other benefits:
  - The application is not tied to AWS - it can be deployed elsewhere, at least if it is using RDS or Elastic 
    rather than DynamoDB for its data store.
  - The application can be moved within AWS to an EC2 environment, or from API Gateway to an ALB.
  - A lambda development environment supporting Flask will also support Django.

- Zappa - the [serverless framework](https://serverless.com/framework/docs/providers/aws/) has a
  [plugin for python requirements](https://github.com/UnitedIncome/serverless-python-requirements); however, 
  as you can see in the section on "Cross compiling!, this plugin "cross compiles" using Docker, which 
  violates the current requirements.  Perhaps we can revisit this if we will only ever deploy into AWS using 
  Bamboo - Bamboo runs pip in docker, and that should work, right?  zappa also automatically creates a 
  CloudWatch Event to keep the Lambda running.

- Pynamodb - if we are to be deployed in AWS Lambda, any database connection pooling goes out the window, 
  unless the application is very busy.  So, we need a data store designed to need not much more than a TCP/IP
  connection, such as DynamoDB.  For python, we need some layer on top of DynamoDB that acts sort of like an Object-Relational Mapper (ORM), e.g. a Object-Document Mapper (ODM). PynamoDB supports definitation of tables, global secondary indexes, and local secondary indexes. It is less complete than Django's ORM, because Django's ORM is integrated all the way to the RESTful views via Django Rest Framework, but it is
  pretty good.

## How To

Dependencies are installed as follows:

```
pip install -r requirements_dev.txt
```

Using `pip-tools`, we have that "requirements.in" is like package.json, and "requirements.txt" is like package-lock.json.   If changed, runtime can be "re-frozen" by running:

```
pip-compile requirements.in -o requirements.txt
```

The DynamoDB table can be built and then removed as follows:

```
manage.py create-tables
manage.py delete-tables
```

A zip can be generated with:

```
zappa package
```

The application can be deployed in development with:

```
set AWS_PROFILE=sbox-ab-django
getawscreds -p
zappa deploy dev
```
