# Serverless Cold Start & Ingestion Live Demonstration

**Cloud Computing Group 50 | Theme 4: Serverless & Startups**  
*Team: Aalok, Bhagya, and Farhan*

This web application provides an interactive front-end and reverse proxy for the AWS Serverless ingestion pipeline deployed in **AWS Mumbai (`ap-south-1`)**:

`Client Browser` $\rightarrow$ `Vercel Python Proxy` $\rightarrow$ `API Gateway (HTTP API)` $\rightarrow$ `AWS Lambda (Python 3.11)` $\rightarrow$ `Amazon DynamoDB`

### Features
- Direct insertion of records into live AWS DynamoDB table (`Submissions`)
- Automatic detection of Cold Start (`_is_cold: true`) vs Warm Invocation
- High-precision round-trip latency measurements
- "Send 3x Burst" mode to demonstrate cold-to-warm latency stabilization
- Live request session history table
