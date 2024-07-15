# src/main.py
import os
from data_processing import load_data, aggregate_session_data
from feature_engineering import create_user_item_mappings, generate_features
from train_model import train_and_save_model

# Define file paths
DATA_PATH = os.path.join('data', 'clickstream_data.parquet')
MODEL_PATH = os.path.join('models', 'recommendation_model.h5')
USER_MAP_PATH = os.path.join('models', 'user_mapping.csv')
ITEM_MAP_PATH = os.path.join('models', 'item_mapping.csv')


def main():
    print("Loading data...")
    data = load_data(DATA_PATH)
    print("Data loaded successfully.")

    print("Aggregating session data...")
    session_data = aggregate_session_data(data)
    print("Session data aggregated successfully.")

    print("Creating user and item mappings...")
    user_mapping, item_mapping = create_user_item_mappings(session_data)
    print("User and item mappings created successfully.")

    print("Generating features...")
    X, y = generate_features(session_data, user_mapping, item_mapping)
    print("Features generated successfully.")

    print("Training and saving the model...")
    train_and_save_model(X, y, len(user_mapping), len(item_mapping), MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}.")

    user_mapping.to_csv(USER_MAP_PATH, index=False)
    item_mapping.to_csv(ITEM_MAP_PATH, index=False)
    print(f"User and item mappings saved to {USER_MAP_PATH} and {ITEM_MAP_PATH} respectively.")


if __name__ == '__main__':
    main()
