# Retail Discount API Security Project

## Project Overview
This project demonstrates how to build and secure a serverless API using AWS services including API Gateway, Lambda, DynamoDB, and Cognito.

The focus of this project was to identify and fix real-world security vulnerabilities commonly found in cloud applications, including:

- Broken access control
- Lack of authentication
- Unsafe input handling
- Hardcoded secrets
- Missing logging and monitoring

---

## Architecture

User → API Gateway → Lambda → DynamoDB  
↓  
Cognito (Authentication)

---

## Technologies Used
- AWS Lambda
- API Gateway
- DynamoDB
- Cognito (JWT Authentication)
- CloudWatch
- AWS Parameter Store
- Python (boto3)

---

## Security Improvements Implemented

### 1. Authentication (Cognito + JWT)
- Implemented secure user authentication using AWS Cognito
- Protected API endpoints using JWT authorizers

---

### 2. Authorization Fix (Critical)
- Removed reliance on user-controlled input (`userId`)
- Used authenticated identity (`sub`) from JWT
 Prevents broken access control vulnerabilities

---

### 3. Least Privilege IAM
- Replaced overly permissive roles
- Restricted Lambda access to only required DynamoDB actions
 Reduces blast radius if compromised

---

### 4. Input Validation
- Enforced strict validation on discount codes:
  - Alphanumeric only
  - Max length restriction
- Blocked malicious inputs (e.g. `<script>`)

---

### 5. Secrets Management
- Removed hardcoded API keys
- Used AWS Systems Manager Parameter Store
 Ensures secrets are not exposed in code

---

### 6. Logging & Monitoring
- Implemented structured logging in Lambda
- Enabled API Gateway access logging
 Enables detection of suspicious activity

---

### 7. API Protection
- Enabled throttling in API Gateway
- Added request validation
Prevents abuse, brute force, and malformed attacks

---

## Testing

### Valid Request