
from celery import Celery
from PIL import Image
import requests
from io import BytesIO
from models import db, Image, Request
from services.webhook import trigger_webhook

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def process_images_async(request_id, images_data):
    for image_data in images_data:
        input_urls = image_data["input_urls"]
        processed_urls = []

        for url in input_urls:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            img = img.resize((img.width // 2, img.height // 2))
            output_buffer = BytesIO()
            img.save(output_buffer, format='JPEG')

            output_url = "https://dummy-processed-url.com"
            processed_urls.append(output_url)

        image_record = Image.query.filter_by(product_name=image_data['product_name'], request_id=request_id).first()
        image_record.output_urls = ','.join(processed_urls)
        db.session.commit()

    request_record = Request.query.get(request_id)
    request_record.status = 'completed'
    db.session.commit()

    trigger_webhook(request_id)
