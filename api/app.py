from flask import Flask, jsonify, request
from flasgger import Swagger
import numpy as np
import tensorflow as tf

app = Flask(__name__)
swagger = Swagger(app)

# Load your trained model
# model = tf.keras.models.load_model('models/recommendation_model')

@app.route('/recommend', methods=['POST'])
def recommend():
    """
    Endpoint for generating recommendations based on user ID.
    ---
    parameters:
      - name: user_id
        in: body
        type: integer
        required: true
        description: ID of the user for whom recommendations are requested.
    responses:
      200:
        description: JSON object with recommendations.
        schema:
          properties:
            recommendations:
              type: array
              description: List of recommended item IDs.
              items:
                type: integer
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    user_id = request.json.get('user_id')

    if not isinstance(user_id, int):
        return jsonify({"error": "Invalid user_id"}), 400

    # Predict recommendations using the model
    # predictions = model.predict(user_id)

    # recommended_item_ids = [item_mapping[item_idx] for item_idx in predictions]
    recommended_item_ids = [1, 2, 3]

    return jsonify({'recommendations': recommended_item_ids})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
