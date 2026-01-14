import json
import redis
import pickle
import pandas as pd
from kafka import KafkaConsumer, KafkaProducer # Added Producer

# 1. Load AI model
with open('fraud_model.pkl', 'rb') as f:
    model = pickle.load(f)

# 2. Connections
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# NEW: Producer to send alerts to the dashboard
alert_producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🧠 AI Processor is running and sending alerts to 'fraud-alerts' topic...")

for message in consumer:
    tx = message.value
    user_id = tx['user_id']
    amount = tx['amount']
    
    # Feature Engineering via Redis
    redis_key = f"user_count:{user_id}"
    current_count = r.incr(redis_key)
    if current_count == 1: r.expire(redis_key, 60)
    
    features = pd.DataFrame([{
        'amount': amount,
        'tx_count_1m': current_count,
        'is_weekend': 0,
        'is_night': 1 if amount > 3000 else 0
    }])
    
    # AI Prediction
    prediction = int(model.predict(features)[0])
    probability = float(model.predict_proba(features)[0][1])

    # Combine original data with AI results
    alert_data = tx.copy()
    alert_data['ai_prediction'] = prediction
    alert_data['ai_probability'] = probability
    
    # NEW: Send the result to the 'fraud-alerts' topic
    alert_producer.send('fraud-alerts', value=alert_data)
    
    status = "🚨 FRAUD" if prediction == 1 else "✅ OK"
    print(f"Processed: User {user_id} | {status} (Prob: {probability:.2f})")