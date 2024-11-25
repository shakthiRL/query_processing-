# Import Libraries
import os
import pandas as pd
import numpy as np
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from elasticsearch import Elasticsearch
from sqlalchemy import create_engine
from flask import Flask, request, jsonify

# Initialize Components
app = Flask(__name__)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

intent_model_name = "bert-base-uncased"  # Replace with your fine-tuned model
intent_classifier = pipeline("text-classification", 
                             model=AutoModelForSequenceClassification.from_pretrained(intent_model_name),
                             tokenizer=AutoTokenizer.from_pretrained(intent_model_name))

# Define Classes
class IntentDetection:
    def __init__(self, model_pipeline):
        self.model_pipeline = model_pipeline

    def detect_intent(self, query):
        prediction = self.model_pipeline(query)
        intent = prediction[0]['label']
        confidence = prediction[0]['score']
        return intent, confidence

class QueryOptimizer:
    def __init__(self, es_client):
        self.es_client = es_client

    def optimize_query(self, intent, query):
        if intent == "FUNDING_SEARCH":
            query_body = {
                "query": {
                    "match": {
                        "abstract": query
                    }
                }
            }
        elif intent == "PI_SEARCH":
            query_body = {
                "query": {
                    "match": {
                        "principal_investigator": query
                    }
                }
            }
        else:
            query_body = {
                "query": {
                    "multi_match": {
                        "query": query,
                        "fields": ["title", "abstract", "keywords"]
                    }
                }
            }
        return query_body

    def execute_query(self, query_body):
        results = self.es_client.search(index="nsf_awards", body=query_body)
        return results

# Initialize Intent Detection and Query Optimization
intent_detection = IntentDetection(intent_classifier)
query_optimizer = QueryOptimizer(es)

# Flask Routes
@app.route('/search', methods=['POST'])
def search():
    data = request.json
    user_query = data.get('query', '')

    # Step 1: Detect Intent
    intent, confidence = intent_detection.detect_intent(user_query)

    # Step 2: Optimize Query
    query_body = query_optimizer.optimize_query(intent, user_query)

    # Step 3: Execute Query
    search_results = query_optimizer.execute_query(query_body)

    # Return Results
    return jsonify({
        "query": user_query,
        "intent": intent,
        "confidence": confidence,
        "results": search_results['hits']['hits']
    })

# Main Execution
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
