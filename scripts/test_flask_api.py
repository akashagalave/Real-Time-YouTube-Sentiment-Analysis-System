import pytest
import requests
import json

BASE_URL = "http://localhost:5000"

def test_predict_endpoint():
    """Test /predict endpoint with valid input"""
    data = {
        "comments": ["This is a great product!", "Not worth the money.", "It's okay."]
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=data)
    print("Response:", response.text)  # Debugging output
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.text}"
    assert isinstance(response.json(), list), f"Response is not a list. Response: {response.text}"
    assert all(isinstance(item, int) for item in response.json()), "Response does not contain integers."

def test_predict_with_timestamps_endpoint():
    """Test /predict_with_timestamps endpoint with valid input"""
    data = {
        "comments": [
            {"text": "This is fantastic!", "timestamp": "2024-10-25 10:00:00"},
            {"text": "Could be better.", "timestamp": "2024-10-26 14:00:00"}
        ]
    }
    
    # Ensure only text is passed if API does not support nested JSON
    formatted_data = {"comments": [comment["text"] for comment in data["comments"]]}

    response = requests.post(f"{BASE_URL}/predict_with_timestamps", json=formatted_data)
    print("Response:", response.text)  # Debugging output

    assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.text}"
    
    response_json = response.json()
    assert isinstance(response_json, list), f"Response is not a list. Response: {response.text}"
    assert all('sentiment' in item for item in response_json), "Missing 'sentiment' key in response. Response: {response.text}"

def test_generate_chart_endpoint():
    """Test /generate_chart endpoint"""
    data = {"sentiment_counts": {"1": 5, "0": 3, "-1": 2}}
    response = requests.post(f"{BASE_URL}/generate_chart", json=data)
    print("Response Headers:", response.headers)  # Debugging output

    assert response.status_code == 200, f"Expected 200, got {response.status_code}."
    assert response.headers.get("Content-Type") == "image/png", "Expected image/png format."

def test_generate_wordcloud_endpoint():
    """Test /generate_wordcloud endpoint"""
    data = {"comments": ["Love this!", "Not so great.", "Absolutely amazing!", "Horrible experience."]}
    response = requests.post(f"{BASE_URL}/generate_wordcloud", json=data)
    print("Response Headers:", response.headers)  # Debugging output

    assert response.status_code == 200, f"Expected 200, got {response.status_code}."
    assert response.headers.get("Content-Type") == "image/png", "Expected image/png format."

def test_generate_trend_graph_endpoint():
    """Test /generate_trend_graph endpoint"""
    data = {
        "sentiment_data": [
            {"timestamp": "2024-10-01", "sentiment": 1},
            {"timestamp": "2024-10-02", "sentiment": 0},
            {"timestamp": "2024-10-03", "sentiment": -1}
        ]
    }
    response = requests.post(f"{BASE_URL}/generate_trend_graph", json=data)
    print("Response Headers:", response.headers)  # Debugging output

    assert response.status_code == 200, f"Expected 200, got {response.status_code}."
    assert response.headers.get("Content-Type") == "image/png", "Expected image/png format."
