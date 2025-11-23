import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Set page config
st.set_page_config(page_title="SkyBook - HYD to GOA", page_icon="✈️", layout="wide")

# --- Mock Data ---
def get_flights_hyd_to_goa():
    data = [
        {"Airline": "IndiGo", "Flight No": "6E-554", "Departure": "06:30 AM", "Duration": "1h 15m", "Price": 4500},
        {"Airline": "SpiceJet", "Flight No": "SG-102", "Departure": "09:15 AM", "Duration": "1h 20m", "Price": 4200},
        {"Airline": "Air India", "Flight No": "AI-885", "Departure": "01:45 PM", "Duration": "1h 10m", "Price": 5100},
        {"Airline": "Vistara", "Flight No": "UK-992", "Departure": "05:20 PM", "Duration": "1h 25m", "Price": 6500},
        {"Airline": "IndiGo", "Flight No": "6E-778", "Departure": "09:00 PM", "Duration": "1h 15m", "Price": 4800},
    ]
    return pd.DataFrame(data)

def get_flights_goa_to_hyd():
    data = [
        {"Airline": "IndiGo", "Flight No": "6E-223", "Departure": "08:00 AM", "Duration": "1h 15m", "Price": 4600},
        {"Airline": "Air India", "Flight No": "AI-445", "Departure": "11:30 AM", "Duration": "1h 10m", "Price": 5200},
        {"Airline": "SpiceJet", "Flight No": "SG-304", "Departure": "03:15 PM", "Duration": "1h 25m", "Price": 4100},
        {"Airline": "Vistara", "Flight No": "UK-881", "Departure": "07:45 PM", "Duration": "1h 20m", "Price": 6700},
        {"Airline": "IndiGo", "Flight No": "6E-990", "Departure": "10:30 PM", "Duration": "1h 15m", "Price": 4400},
    ]
    return pd.DataFrame(data)

# --- Helper Functions ---
def format_flight_option(row):
    return f"{row['Airline']} ({row['Flight No']}) - {row['Departure']} - ₹{row['Price']}"

# --- Main App Layout ---

st.title("✈️ SkyBook: Hyderabad to Goa")
st.markdown("Book your flights easily from **Hyderabad (HYD)** to **Goa (GOI)** and back.")
st.markdown("---")

# Date Selection
col1, col2 = st.columns(2)
with col1:
    dep_date = st.date_input("Departure Date", min_value=datetime.today())
with col2:
    ret_date = st.date_input("Return Date", min_value=dep_date)

st.markdown("---")

# Flight Selection
st.subheader("Select Your Flights")

df_hyd_goa = get_flights_hyd_to_goa()
df_goa_hyd = get_flights_goa_to_hyd()

col_out, col_in = st.columns(2)

# Outbound Flights
with col_out:
    st.info(f"🛫 Hyderabad (HYD) → Goa (GOI) | {dep_date.strftime('%d %b %Y')}")
    # Create a list of formatted strings for the radio button
    outbound_options = [format_flight_option(row) for index, row in df_hyd_goa.iterrows()]
    selected_outbound_str = st.radio("Choose Outbound Flight:", outbound_options)
    
    # Find the selected row based on the string
    selected_outbound_idx = outbound_options.index(selected_outbound_str)
    selected_outbound_flight = df_hyd_goa.iloc[selected_outbound_idx]
    
    # Display details card
    st.dataframe(df_hyd_goa[["Airline", "Departure", "Duration", "Price"]], hide_index=True, use_container_width=True)


# Return Flights
with col_in:
    st.info(f"🛬 Goa (GOI) → Hyderabad (HYD) | {ret_date.strftime('%d %b %Y')}")
    return_options = [format_flight_option(row) for index, row in df_goa_hyd.iterrows()]
    selected_return_str = st.radio("Choose Return Flight:", return_options)
    
    selected_return_idx = return_options.index(selected_return_str)
    selected_return_flight = df_goa_hyd.iloc[selected_return_idx]

    st.dataframe(df_goa_hyd[["Airline", "Departure", "Duration", "Price"]], hide_index=True, use_container_width=True)

st.markdown("---")

# Booking Section
total_price = selected_outbound_flight['Price'] + selected_return_flight['Price']

st.subheader("Booking Summary")
st.write(f"**Total Price:** ₹{total_price}")

if st.button("Book Ticket", type="primary", use_container_width=True):
    st.balloons()
    st.success("✅ Booking Confirmed! Have a safe trip.")
    
    # Summary Card
    with st.container(border=True):
        st.markdown(f"### 🧾 Ticket Details")
        st.markdown(f"**Passenger Name:** Guest User") # Placeholder
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### Outbound")
            st.write(f"**Date:** {dep_date.strftime('%d %b %Y')}")
            st.write(f"**Flight:** {selected_outbound_flight['Airline']} {selected_outbound_flight['Flight No']}")
            st.write(f"**Time:** {selected_outbound_flight['Departure']}")
            st.write(f"**Price:** ₹{selected_outbound_flight['Price']}")
        
        with c2:
            st.markdown("#### Return")
            st.write(f"**Date:** {ret_date.strftime('%d %b %Y')}")
            st.write(f"**Flight:** {selected_return_flight['Airline']} {selected_return_flight['Flight No']}")
            st.write(f"**Time:** {selected_return_flight['Departure']}")
            st.write(f"**Price:** ₹{selected_return_flight['Price']}")
            
        st.divider()
        st.markdown(f"### **Grand Total: ₹{total_price}**")

