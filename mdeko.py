import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Logistics and Supply Chain Coordination", layout="wide")

# Title and sidebar filters
st.title("Welcome to Abuti Spinach Marketplace")
st.sidebar.header("User Type")
user_type = st.sidebar.radio("I am a:", ("Farmer", "Buyer"))

# Initialize an empty list to store submitted information
submission_data = []

# Main content area
if user_type == "Farmer":
    st.subheader("Farmer's Dashboard")
    # Farmer inputs for coordination
    farmer_name = st.text_input("Enter your name:")
    produce_type = st.text_input("Type of produce:")
    quantity = st.number_input("Quantity (in kg):", min_value=0)
    pickup_location = st.text_input("Pickup location:")
    pickup_date = st.date_input("Pickup date:", min_value=datetime.today())
    contact_details = st.text_input("Contact details:")
    
    # Submit button
    if st.button("Submit"):
        submission_data.append({
            "User Type": "Farmer",
            "Name": farmer_name,
            "Produce Type": produce_type,
            "Quantity": quantity,
            "Location": pickup_location,
            "Date": pickup_date,
            "Contact": contact_details
        })
        st.success(f"Details submitted for {farmer_name}")

elif user_type == "Buyer":
    st.subheader("Buyer's Dashboard")
    # Buyer inputs for coordination
    buyer_name = st.text_input("Enter your name:")
    required_produce_type = st.text_input("Type of produce required:")
    required_quantity = st.number_input("Required quantity (in kg):", min_value=0)
    delivery_location = st.text_input("Delivery location:")
    delivery_date = st.date_input("Delivery date:", min_value=datetime.today())
    contact_details = st.text_input("Contact details:")
    
    # Submit button
    if st.button("Submit"):
        submission_data.append({
            "User Type": "Buyer",
            "Name": buyer_name,
            "Produce Type": required_produce_type,
            "Quantity": required_quantity,
            "Location": delivery_location,
            "Date": delivery_date,
            "Contact": contact_details
        })
        st.success(f"Details submitted for {buyer_name}")

# Convert submission data to DataFrame
df_submission = pd.DataFrame(submission_data)

# Supply chain tracking section
st.header("Supply Chain Tracking")

if not df_submission.empty:
    # Convert 'Date' column to datetime
    df_submission["Date"] = pd.to_datetime(df_submission["Date"])
    
    # Generate tracking data based on submitted information
    tracking_data = {
        "Shipment ID": [f"SHP00{i+1}" for i in range(len(df_submission))],
        "Status": ["In Transit" if row["User Type"] == "Farmer" else "Pending" for _, row in df_submission.iterrows()],
        "Location": df_submission["Location"].tolist(),
        "Expected Delivery": df_submission["Date"].dt.strftime("%Y-%m-%d").tolist()
    }
    # Display tracking data
    df_tracking = pd.DataFrame(tracking_data)
    st.dataframe(df_tracking)
else:
    st.write("No submissions yet.")

# Map for real-time tracking (similar to Uber's map interface)
st.subheader("Real-time Tracking Map")
# Placeholder map
st.image("https://via.placeholder.com/800x400.png", use_column_width=True, caption="Real-time tracking map")


