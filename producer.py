import json
import time
import random
from kafka import KafkaProducer
from faker import Faker

# Initialize Faker to create realistic names/data
fake = Faker()

# Initialize Kafka Producer
# 'localhost:9092' is where our Kafka Docker container is listening
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_transaction():
    """Create a single fake transaction."""
    return {
        "transaction_id": fake.uuid4(),
        "user_id": random.randint(100, 150), # Simulating 50 unique users
        "amount": round(random.uniform(10.0, 5000.0), 2),
        "merchant": fake.company(),
        "timestamp": time.time(),
        "card_type": random.choice(["Visa", "MasterCard", "Amex"]),
        "location": fake.city()
    }

if __name__ == "__main__":
    print("🚀 Kafka Producer started... Sending transactions to Kafka.")
    try:
        while True:
            # Create a transaction
            tx = generate_transaction()
            
            # Send to Kafka topic 'transactions'
            producer.send('transactions', value=tx)
            
            print(f"✅ Sent: {tx['transaction_id']} | User: {tx['user_id']} | Amt: ${tx['amount']}")
            
            # Send a transaction every 1 second (adjust for speed)
            time.sleep(1) 
    except KeyboardInterrupt:
        print("Producer stopped.")