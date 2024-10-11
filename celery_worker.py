
from services.image_processing import celery_app

if __name__ == "__main__":
    celery_app.start()
