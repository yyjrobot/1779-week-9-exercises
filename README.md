# Week 9 Exercises
This exercise will help you get familiar with AWS Lambda.

## Follow the steps below to complete the Lambda exercise.

#### Create a Lambda Function

1. In your AWS account, search for and navigate to Lambda. 
2. Click the **Create a function** button.
3. Write **DateTime** in the Function name field.
4. Select Python in the **Runtime** dropdown.
5. Click the **Create function** button. 


#### Configure and test your Lambda Function

1. Once you've created the Lambda function, you'll see a **Code source** section, with a **lambda_function** script and an IDE box. By default, you'll see the following code:
```
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```
2. Go to the ***Time_function.py*** script in this repository. Copy the entire script, and paste it into the lambda_function IDE box, replacing all the default code.
3. Click on the **Test** button drop down. Click **Configure test event**.
4. In the **Event JSON** box, paste in the JSON object literal found in ***test-1.json*** from this repository. Name the test and save it.
5. Click the **Deploy** button the deploy the lambda function. 
6. Click the **Test** button.
7. You should get the following **Response**:

```
{
  "statusCode": 200,
  "headers": {
    "Content-type": "application/json"
  },
  "body": "{\"month\":11,\"day\":13,\"year\":2022}"
}
```

#### Create an API Gateway

1. In AWS, navigate to your DateTime Lambda Function page.
3. In the **Function overview** box, choose **Add trigger**. 
4. Select **API Gateway**. 
5. Choose **Create an new API**. 
6. Choose **HTTP API**. 
8. For Security, choose **Open**. 
9. Choose **Add**.


#### Deploy your API Gateway

1. Go to the **API Gateway** page on AWS.
2. Select DateTime-API.
3. Click **Deploy** in the top right corner.
2. Click the **To create a stage, click here** link.
3. Name the stage "testTime".
4. (Do not enable automatic deployment.) 
5. Click **Create**. 
6. Go back to the API Gateway page. 
7. Select **DateTime-API**. 
8. Click **Deploy**. 
9. Select testTime as the stage. 
10. click **Deploy to stage**.

####  Test lambda access with a real link


4. On the API Gateway page, under your DateTime-API, you should see your new stage name in the **Stages for DateTime-API** box. 
5. Click the **Invoke URL** associated with **testTime**.
5. Append the following string to the URL: ```/DateTime?option=date&period=tomorrow```.
6. You should get a response similar to: ```{"month":11,"day":13,"year":2022}```.


_Note: AWS lambda functions & API gateways are priced per-use, so make sure to stay within the Free Tier use limits._


### Once you have finished the exercise, go to [PCRS](https://pcrs.teach.cs.toronto.edu/ECE1779-2022-09/content/quests) to answer the question for Week 9.



