
# API Documentation

## 1. Upload API
- **URL**: `/upload`
- **Method**: `POST`
- **Description**: Upload a CSV file containing product names and image URLs.
- **Request Body**:
  - File: A CSV file with the following columns: Serial Number, Product Name, Input Image URLs.
  
- **Response**:
  - `200 OK`: Returns a unique `request_id` to track processing.
  - `400 Bad Request`: If the CSV format is invalid or the file is missing.

### Example:
```bash
curl -X POST http://localhost:5000/upload -F 'file=@products.csv'
```

Response:
```json
{
  "request_id": "123e4567-e89b-12d3-a456-426614174000"
}
```

## 2. Status API
- **URL**: `/status/<request_id>`
- **Method**: `GET`
- **Description**: Retrieve the processing status of a request.
  
- **Response**:
  - `200 OK`: Returns the status of the request (`processing`, `completed`).
  - `404 Not Found`: If the request ID is invalid.

### Example:
```bash
curl http://localhost:5000/status/123e4567-e89b-12d3-a456-426614174000
```

Response:
```json
{
  "request_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "processing"
}
```
