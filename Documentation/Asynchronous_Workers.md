
# Asynchronous Workers Documentation

## Worker Function: Image Processing
The image processing tasks are handled asynchronously using Celery. When a CSV file is uploaded, a Celery worker processes each image in the background.

### Workflow:
1. **Download Images**: The worker fetches image URLs provided in the CSV.
2. **Compress Images**: Each image is resized by 50% to reduce quality and size.
3. **Save Processed Images**: The processed images are saved or uploaded, and their new URLs are stored in the database.
4. **Update Status**: The worker updates the request's status to "completed" after processing all images.
5. **Webhook Trigger**: The worker triggers a webhook to notify that processing is done.

### Celery Command:
To start the Celery worker:
```bash
celery -A folder4.celery_worker worker --loglevel=info
```

## Webhook
- After the image processing completes, a webhook is triggered to notify external systems of the completion.
- The webhook URL and payload can be customized.
