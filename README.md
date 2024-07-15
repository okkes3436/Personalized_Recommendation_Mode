# Insider Case Study: Personalized Recommendation API

This project is part of the Insider case study, focusing on building a personalized recommendation system. It involves two main parts:

## Building a Machine Learning Model for Recommendations

This part of the project focuses on developing a machine learning model that provides personalized recommendations based on user behavior data.

### Features

- **Data Loading**: Load session-based aggregated data from a Parquet file.
- **Data Processing**: Aggregate session data to extract relevant features.
- **Feature Engineering**: Create mappings for user and item IDs, and generate features for model training.
- **Model Training**: Build and train a recommendation model using TensorFlow/Keras.

### Implementation Details

- **Technologies Used**: Python, Pandas, TensorFlow/Keras.
- **Tools**: Jupyter Notebook for exploration and development.

## Serving the Model through a Flask API

In this part, we build a Flask API to serve the trained recommendation model and provide recommendations based on user input.

### Features

- **API Development**: Develop a Flask application to host the recommendation model.
- **Endpoint**: Implement an endpoint `/recommend` to receive user ID and return personalized recommendations.
- **Swagger Integration**: Use Swagger UI for API documentation and interactive exploration.

### Implementation Details

- **Technologies Used**: Python, Flask, Swagger, Docker.
- **Testing**: Unit tests for API endpoints to ensure functionality.
- **Dockerization**: Dockerize the Flask application for easy deployment.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [API Documentation](#api-documentation)
4. [Testing](#testing)
5. [Dockerization](#dockerization)

---

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <project-directory>

2. Install the required dependencies:

	```bash
	pip install -r requirements.txt

3. Ensure you have Python 3.x installed on your system.


## Usage
	
	To run the Flask application locally:

	```bash
	python app.py

	This will start the Flask server locally. You can then send requests to the API endpoints to receive personalized recommendations.


## API Documentation

	The API is documented using Swagger UI. Once the Flask application is running, you can navigate to /apidocs in your browser to view the Swagger UI. This UI provides detailed information about the API endpoints, parameters, and responses based on the annotations in the code.

## Testing
	
	Unit tests are provided to ensure the functionality of the API endpoints. To run the tests:

	```bash
	python -m unittest discover

	This command discovers and runs all the unit tests defined in the project.


## Dockerization

	The Flask application can be Dockerized for easier deployment. To build a Docker image:

1. Create a Dockerfile in the project root directory:
	
	```bash
	FROM python:3.9-slim
	WORKDIR /app
	COPY . .
	RUN pip install -r requirements.txt
	CMD ["python", "app.py"]

2. Build the Docker image:
	
	```bash
	docker build -t recommendation-api .

3. Run the Docker container:
	
	```bash
	docker run -p 5000:5000 recommendation-api

This will run the Flask application inside a Docker container, accessible on **'http://localhost:5000'**.

















