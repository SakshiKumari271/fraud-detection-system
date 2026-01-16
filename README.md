# 🛡️ FinShield: Real-Time AI Fraud Detection System

**FinShield** is a production-grade, distributed pipeline designed to ingest, analyze, and flag fraudulent transactions in real-time. By leveraging a microservices architecture, the system achieves **sub-200ms latency** for AI-driven anomaly detection.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-fb722e?style=for-the-badge&logo=xgboost&logoColor=white)

---

## 🏗️ System Architecture

FinShield is built as a series of decoupled microservices to ensure high availability and scalability:

1.  **Transaction Producer:** A simulation engine generating a continuous stream of financial events (Amount, User ID, Merchant, Location).
2.  **Apache Kafka (The Backbone):** Manages two data streams:
    -   `transactions`: Raw data from the producer.
    -   `fraud-alerts`: AI-processed conclusions sent to the dashboard.
3.  **Redis Feature Store:** Maintains real-time "state." It tracks **Transaction Velocity** (how many times a user has spent money in the last 60 seconds) with sub-millisecond lookup speeds.
4.  **AI Processor:** A machine learning service that pulls from Kafka, fetches features from Redis, and uses an **XGBoost model** to predict fraud probability.
5.  **FinShield Dashboard:** A professional **Streamlit** interface for live monitoring and instant security alerts.

---

## 🛠️ Technical Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Streaming** | Apache Kafka | Distributed event store and message broker |
| **In-Memory DB** | Redis | Real-time feature storage and window counting |
| **ML Model** | XGBoost | High-performance gradient boosting for classification |
| **Dashboard** | Streamlit | Real-time web UI for security monitoring |
| **Containerization** | Docker | Orchestration of Kafka, Zookeeper, and Redis |

---

## 📂 Project Structure

```text
fraud-detection-system/
├── docker-compose.yml    # Kafka, Zookeeper, & Redis configuration
├── producer.py           # Generates live transaction stream
├── processor.py          # AI Logic: Kafka Consumer + ML Inference + Redis Features
├── dashboard.py          # Real-time UI: Kafka Consumer + Plotly Charts
├── train_model.py        # Script to train and save the XGBoost model
├── requirements.txt      # Python dependencies
└── README.md             # Documentation

👩‍💻 Author & Contact

Sakshi Kumari

🔗 LinkedIn:
https://www.linkedin.com/in/sakshisingh271

📧 Email:
271sakshi.kumari@gmail.com