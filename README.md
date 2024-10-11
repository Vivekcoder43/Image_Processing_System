
# Image Processing Backend System

## Overview
This project processes image data from CSV files asynchronously and provides APIs for users to check the status of processing. Once images are processed, they are stored, and a webhook is triggered.

## Components
1. **API Endpoints**: Upload API to receive CSV files, and Status API to check processing status.
2. **Image Processing**: Asynchronous processing of images using Celery.
3. **Webhook Handling**: Trigger webhook upon completion of image processing.
4. **Database**: Store and track the status of processing requests and image URLs.

## Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure PostgreSQL database:
   ```sql
   CREATE DATABASE mydatabase;
   CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
   GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
   ```

3. Initialize the database:
   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   ```

4. Start Redis server:
   ```bash
   redis-server
   ```

5. Run Celery worker:
   ```bash
   celery -A folder4.celery_worker worker --loglevel=info
   ```

6. Start the Flask application:
   ```bash
   python app.py
   ```

## API Endpoints
1. **Upload API** (`POST /upload`): Accepts a CSV file and returns a request ID.
2. **Status API** (`GET /status/<request_id>`): Returns the processing status of a request.

## Project Structure
- **app.py**: Main Flask entry point.
- **Documentation/**: Has Api Documentation , Asynchronous Workers Documentation , Database schema documentation , Lowlevel design documentation
- **Dockerfile**: For containerizing the application.
- **requirements.txt**: Python dependencies.
