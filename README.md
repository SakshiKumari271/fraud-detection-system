🛡️ FinShield — Real-Time AI Fraud Detection System

FinShield is a production-grade, real-time fraud detection pipeline designed to ingest, analyze, and flag suspicious financial transactions with sub-200ms latency.
Built on a distributed microservices architecture, it combines streaming, in-memory state, and machine learning to detect fraud as it happens.

🚀 Tech Stack










🏗️ System Architecture

FinShield follows a decoupled microservices architecture to ensure scalability, fault tolerance, and low latency.

🔁 Data Flow Overview

Transaction Producer

Simulates real-time financial transactions

Fields: User ID, Amount, Merchant, Location, Timestamp

Apache Kafka (Event Backbone)

transactions → raw incoming events

fraud-alerts → AI-evaluated fraud decisions

Redis Feature Store

Maintains real-time state

Tracks transaction velocity (number of transactions per user in last 60 seconds)

AI Processor

Consumes transactions from Kafka

Fetches real-time features from Redis

Uses an XGBoost model to predict fraud probability

FinShield Dashboard

Built with Streamlit + Plotly

Live monitoring of transactions and fraud alerts

🧠 Why This Architecture?

Sub-200ms inference latency

Stateful fraud detection (velocity attacks)

Horizontally scalable services

Production-ready streaming design

🛠️ Technology Breakdown
Component	Technology	Purpose
Streaming	Apache Kafka	Distributed message broker
Feature Store	Redis	In-memory, real-time feature tracking
ML Model	XGBoost	High-performance fraud classification
Dashboard	Streamlit	Live monitoring & alerts
Infrastructure	Docker	Containerized services

📂 Project Structure
fraud-detection-system/
├── docker-compose.yml    # Kafka, Zookeeper & Redis setup
├── producer.py           # Simulates live transactions
├── processor.py          # Kafka consumer + ML inference + Redis features
├── dashboard.py          # Real-time monitoring UI
├── train_model.py        # Train & save XGBoost fraud model
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

⚙️ Full Setup & Configuration
1️⃣ Clone the Repository
git clone https://github.com/SakshiKumari271/fraud-detection-system.git
cd fraud-detection-system

2️⃣ Start Infrastructure (Docker)

Make sure Docker Desktop is running.

docker compose up -d


⏳ Wait ~20 seconds for Kafka and Redis to fully initialize.

3️⃣ Install Python Dependencies
pip install -r requirements.txt

4️⃣ Train the AI Model

Generate synthetic historical data and train the fraud detection model:

python train_model.py

5️⃣ Run the FinShield Pipeline

Open three terminals (VS Code recommended):

🏦 Terminal 1 — Transaction Producer
python producer.py

🤖 Terminal 2 — AI Fraud Engine
python processor.py

📊 Terminal 3 — Dashboard
streamlit run dashboard.py

🚨 Key Features

✅ Real-Time Fraud Detection
Sub-200ms AI inference on every transaction

✅ Stateful Analysis with Redis
Detects velocity-based fraud patterns

✅ Event-Driven Microservices
Highly scalable and fault-tolerant design

✅ Live Dashboard & Alerts
Interactive Plotly charts with instant updates

📈 Use Cases

Banking fraud detection

Payment gateway monitoring

Credit card transaction analysis

Real-time risk scoring systems

👩‍💻 Author & Contact

Sakshi Kumari

🔗 LinkedIn:
https://www.linkedin.com/in/sakshisingh271

📧 Email:
271sakshi.kumari@gmail.com