
-- PostgreSQL Database Schema for Image Processing

CREATE TABLE requests (
    request_id UUID PRIMARY KEY,
    status VARCHAR(20),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    request_id UUID REFERENCES requests(request_id),
    product_name VARCHAR(100),
    input_image_urls TEXT,
    output_image_urls TEXT
);
