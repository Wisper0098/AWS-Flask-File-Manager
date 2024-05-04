# Flask App with AWS RDS and S3 Integration

This Flask web application allows users to upload and manage files. It integrates with Amazon RDS for PostgreSQL to store user data and metadata, and Amazon S3 to store uploaded files securely.

## Features

- **User Authentication:** Users can sign up, log in, and log out securely.
- **File Management:** Users can upload, view, and delete their files.
- **Public/Private Files:** Users can choose to make their files public or private.
- **Pagination:** Files are displayed with pagination for better user experience.
- **AWS Integration:** Utilizes AWS RDS for PostgreSQL to store user data and AWS S3 to store uploaded files.
- **Secure File Upload:** Files are securely uploaded to AWS S3 bucket.

## Setup Instructions

1. **Clone Repository**, Install Dependencies, Set Up AWS Resources, Environment Variables, Run Flask App, Access the Application:
   ```bash
   git clone https://github.com/Wisper0098/AWS-Flask-File-Manager
   ```

   # Set up AWS Resources:
   -- Create an Amazon RDS Instance for PostgreSQL and note down the connection details.
   -- Create an S3 Bucket for file storage and configure access permissions.

   -- Environment Variables: Set up AWS credentials, database connection details, and Flask app configuration. Refer to `.env`.

2. Build and run a Docker container
   ```bash
   docker-compose build
   docker-compose up -d
   ```
## Test your application
  # Access at `http://localhost:5000`


