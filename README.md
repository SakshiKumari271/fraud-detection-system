# 🛡️ FinShield: Real-Time AI Fraud Detection System

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Kafka](https://img.shields.io/badge/Streaming-Apache%20Kafka-red.svg)](https://kafka.apache.org/)
[![Redis](https://img.shields.io/badge/Cache-Redis-orange.svg)](https://redis.io/)
[![ML](https://img.shields.io/badge/ML-XGBoost-green.svg)](https://xgboost.readthedocs.io/)

**FinShield** is a production-grade, distributed pipeline designed to ingest, analyze, and flag fraudulent financial transactions in real-time. By leveraging a microservices architecture, the system achieves sub-200ms latency for AI-driven anomaly detection.

## 🏗️ System Architecture

The system is composed of four decoupled microservices communicating via high-throughput message brokers:

1.  **The Transaction Producer:** A high-frequency simulator generating synthetic financial events (Amount, Merchant, User ID, Location).
2.  **Streaming Ingestion (Kafka):** Acts as the central nervous system, handling data distribution between services with zero data loss.
3.  **The AI Processor (XGBoost + Redis):** 
    -   **Redis** acts as a high-speed Feature Store to calculate "Transaction Velocity" (e.g., *Has this user made 5 transactions in the last minute?*).
    -   **XGBoost** performs real-time inference to predict the probability of fraud.
4.  **The Command Center (Streamlit):** A live dashboard that consumes AI-processed alerts and provides visual monitoring and instant notifications.

---

## 🛠️ Technical Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Language** | Python 3.11 | Core logic and ML implementation |
| **Message Broker** | Apache Kafka | Distributed event streaming |
| **Feature Store** | Redis | In-memory state management for velocity features |
| **ML Model** | XGBoost | Gradient-boosted decision trees for classification |
| **UI Framework** | Streamlit | Real-time data visualization |
| **Containerization** | Docker & Docker Compose | Infrastructure orchestration |

---

## 🚀 Key Features

-   **Real-Time Latency:** End-to-end processing (Ingestion to Prediction) in <200ms.
-   **Stateful Feature Engineering:** Unlike static models, this system tracks user behavior windows in real-time using Redis.
-   **AI-Driven Inference:** Moves beyond simple "if-else" rules to detect complex fraud patterns using Machine Learning.
-   **Microservices Decoupling:** Services are independent; if the UI goes down, the AI continues to catch and log fraud in Kafka.
-   **Live Monitoring:** Dynamic charts showing risk probabilities and instant "Toast" notifications for high-risk events.

---

## 📦 Installation & Setup

### 1. Prerequisites
-   Docker & Docker Compose
-   Python 3.9+

### 2. Infrastructure Setup
Spin up the Kafka and Redis environment:
```bash
docker-compose up -d