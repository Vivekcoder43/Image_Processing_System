
from flask import request, jsonify
import uuid
from models import db, Request, Image
from services.image_processing import process_images_async
from services.webhook import trigger_webhook
import csv

def init_routes(app):
    @app.route('/upload', methods=['POST'])
    def upload_csv():
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400

        file = request.files['file']
        request_id = str(uuid.uuid4())

        csv_reader = csv.reader(file.read().decode('utf-8').splitlines())
        headers = next(csv_reader)
        expected_headers = ['Serial Number', 'Product Name', 'Input Image Urls']

        if headers != expected_headers:
            return jsonify({"error": "CSV format invalid"}), 400

        new_request = Request(id=request_id, status='processing')
        db.session.add(new_request)
        db.session.commit()

        images_data = []
        for row in csv_reader:
            new_image = Image(request_id=request_id, product_name=row[1], input_urls=row[2])
            db.session.add(new_image)
            images_data.append({"product_name": row[1], "input_urls": row[2].split(',')})

        db.session.commit()

        process_images_async.delay(request_id, images_data)

        return jsonify({"request_id": request_id}), 200

    @app.route('/status/<request_id>', methods=['GET'])
    def check_status(request_id):
        request_record = Request.query.get(request_id)
        if not request_record:
            return jsonify({"error": "Request ID not found"}), 404

        return jsonify({"request_id": request_id, "status": request_record.status}), 200
