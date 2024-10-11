
import requests

def trigger_webhook(request_id):
    webhook_url = "https://example-webhook-url.com"
    payload = {"request_id": request_id, "status": "completed"}
    response = requests.post(webhook_url, json=payload)
    return response.status_code
