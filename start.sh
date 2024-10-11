
#!/bin/bash

service redis-server start
celery -A celery_worker worker --loglevel=info &
python app.py
