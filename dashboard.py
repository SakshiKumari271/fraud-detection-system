import streamlit as st
import pandas as pd
import json
from kafka import KafkaConsumer
import plotly.express as px
from datetime import datetime
import time

# 1. Page Configuration
st.set_page_config(page_title="FinTech Shield | AI Dashboard", layout="wide")

# Dark Mode CSS
st.markdown("""<style>.stApp { background-color: #0e1117; }</style>""", unsafe_allow_html=True)

st.title("🛡️ AI Fraud Command Center")
st.markdown("---")

# 2. Initialize Session State
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['arrival_time', 'user_id', 'amount', 'ai_probability', 'is_fraud'])

# 3. Kafka Consumer - Listening to the AI conclusions
try:
    consumer = KafkaConsumer(
        'fraud-alerts',
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='latest',
        consumer_timeout_ms=1000
    )
except Exception as e:
    st.error(f"Kafka Connection Error: {e}")
    st.stop()

# 4. Dashboard Layout
m1, m2, m3 = st.columns(3)
total_placeholder = m1.empty()
fraud_placeholder = m2.empty()
avg_val_placeholder = m3.empty()

st.subheader("AI Risk Probability (Live Spike Monitor)")
chart_placeholder = st.empty()

st.subheader("Live AI Transaction Stream")
table_placeholder = st.empty()

# 5. Real-Time Update Loop
while True:
    for message in consumer:
        data = message.value
        
        new_entry = {
            'arrival_time': datetime.now().strftime("%H:%M:%S"),
            'user_id': data['user_id'],
            'amount': data['amount'],
            'ai_probability': data.get('ai_probability', 0),
            'is_fraud': "YES" if data.get('ai_prediction') == 1 else "NO"
        }
        
        # --- THE FIX IS HERE: ignore_index=True ---
        st.session_state.history = pd.concat(
            [pd.DataFrame([new_entry]), st.session_state.history], 
            ignore_index=True
        ).head(30)
        
        # Update Metrics
        total_tx = len(st.session_state.history)
        fraud_tx = len(st.session_state.history[st.session_state.history['is_fraud'] == "YES"])
        total_placeholder.metric("AI Scanned", total_tx + 500)
        fraud_placeholder.metric("AI Blocked", fraud_tx, delta=f"{fraud_tx}", delta_color="inverse")
        avg_val_placeholder.metric("Current Risk", f"{st.session_state.history['ai_probability'].mean():.2f}")

        # Update Chart
        if not st.session_state.history.empty:
            fig = px.bar(st.session_state.history, x='arrival_time', y='ai_probability', 
                         color='is_fraud', color_discrete_map={'YES':'#ff4b4b', 'NO':'#00f2ff'},
                         template="plotly_dark")
            fig.update_layout(height=250, margin=dict(l=0, r=0, t=0, b=0))
            chart_placeholder.plotly_chart(fig, use_container_width=True)

        # Update Table with Row Highlighting
        def highlight_fraud(row):
            return ['background-color: #440000' if row.is_fraud == "YES" else '' for _ in row]
        
        # Apply the style and display
        if not st.session_state.history.empty:
            styled_df = st.session_state.history.style.apply(highlight_fraud, axis=1)
            table_placeholder.dataframe(styled_df, use_container_width=True)

        # Alert if fraud found
        if new_entry['is_fraud'] == "YES":
            st.toast(f"🚨 AI DETECTED FRAUD: User {data['user_id']}", icon="❌")

    time.sleep(0.1)