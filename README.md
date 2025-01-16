# Assignment Tasks - AWS Lambda Functions

## Introduction
This repository contains solutions for the AWS-related tasks, including two Lambda functions and their deployment steps. Below is an explanation of the tasks and how to run them.

---

## **Task 1: AWS Lambda Function to Add Two Numbers**

### **Description**
This Lambda function takes two numbers as input, adds them, and returns the result. Input is passed via an event object in JSON format.

### **Steps to Deploy and Test**
1. Open the AWS Management Console and navigate to the Lambda service.
2. Create a new function:
   - Name: `AddTwoNumbers`
   - Runtime: Python 3.9 (or later)
3. Copy the code from `add_two_numbers.py` and paste it into the editor.
4. Test the function with the following sample event:
   ```json
   {
       "number1": 5,
       "number2": 10
   }
   ```
5. Save and deploy the function.

---

## **Task 2: AWS Lambda Function to Store a File in an S3 Bucket**

### **Description**
This Lambda function uploads a document or PDF file to a specified S3 bucket. The file content must be provided as a base64-encoded string in the event object.

### **Steps to Deploy and Test**
1. Open the AWS Management Console and navigate to the Lambda service.
2. Create a new function:
   - Name: `StoreFileInS3`
   - Runtime: Python 3.9 (or later)
3. Attach the `AmazonS3FullAccess` policy to the Lambda execution role.
4. Copy the code from `store_file_in_s3.py` and paste it into the editor.
5. Test the function with the following sample event:
   ```json
   {
       "bucket_name": "your-bucket-name",
       "file_name": "example.pdf",
       "file_content": "BASE64_ENCODED_FILE_CONTENT"
   }
   ```
   - Replace `your-bucket-name` with the name of your S3 bucket.
   - Replace `BASE64_ENCODED_FILE_CONTENT` with the base64-encoded string of your file.
6. Save and deploy the function.

---

## **Task 3: Frontend Development**

### **Description**
This task involves creating a responsive webpage with a fixed navbar, collapsible menu, and dynamic resizing based on screen width.

### **Steps to Deploy and Test**
1. Write the HTML, CSS, and JavaScript code as specified.
2. Test the responsiveness by resizing the browser window.
3. Optionally, host the webpage on a platform like AWS S3 (Static Website Hosting) or PythonAnywhere.

---

## **Task 4: Backend Development**

### ***Description** 
Django based application file have own README.md file. 

---

## **Repository Structure**
```
├── add_two_numbers.py          # Lambda function to add two numbers
├── store_file_in_s3.py         # Lambda function to upload a file to S3
├── frontend_task/              # Folder containing frontend code
│   ├── index.html              # Main HTML file
│   ├── styles.css              # Stylesheet
│   └── script.js               # JavaScript logic
├── README.md                   # Instructions and documentation
```

---

## **Submission Guidelines**
1. Ensure all code files are uploaded to a GitHub repository.
2. Include this `README.md` file in the root of the repository.
3. Host the Django or frontend project on PythonAnywhere or AWS.
4. Share the GitHub and hosting links as specified in the assignment.

---

For any issues or queries, please feel free to contact us!
