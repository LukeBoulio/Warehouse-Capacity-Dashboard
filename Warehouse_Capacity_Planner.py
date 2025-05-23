
import streamlit as st
import math

st.set_page_config(page_title="Warehouse Capacity Planner", layout="centered")
st.title("🏭 Warehouse Capacity Planning Dashboard")

st.header("1️⃣ Warehouse Layout Inputs")
total_area = st.number_input("Total Warehouse Area (sq ft)", min_value=1000, value=10000, step=500)
aisles = st.number_input("Aisles and Walkways (sq ft)", min_value=0, value=1500)
staging = st.number_input("Staging and Packing Zones (sq ft)", min_value=0, value=1200)
office = st.number_input("Office/Admin Space (sq ft)", min_value=0, value=800)
dock = st.number_input("Dock/Loading Zones (sq ft)", min_value=0, value=500)
hvac = st.number_input("HVAC/Mechanical Areas (sq ft)", min_value=0, value=300)
restrooms = st.number_input("Restrooms/Breakrooms (sq ft)", min_value=0, value=200)

non_storage_area = aisles + staging + office + dock + hvac + restrooms
usable_area = total_area - non_storage_area
suf = usable_area / total_area if total_area > 0 else 0

st.markdown(f"**Usable Storage Area:** {usable_area} sq ft")
st.markdown(f"**Space Utilization Factor (SUF):** {suf:.2f}")

st.divider()

st.header("2️⃣ Vending Unit Dimensions")
width = st.number_input("Unit Width (ft)", min_value=1.0, value=3.0, step=0.5)
depth = st.number_input("Unit Depth (ft)", min_value=1.0, value=2.5, step=0.5)
front = st.number_input("Front Clearance (ft)", min_value=0.0, value=2.0, step=0.5)
side = st.number_input("Side Clearance (ft, per side)", min_value=0.0, value=1.0, step=0.5)
rear = st.number_input("Rear Clearance (ft)", min_value=0.0, value=1.5, step=0.5)

sfu = (width + 2 * side) * (depth + front + rear)

st.markdown(f"**Square Feet per Unit (SFU):** {sfu:.2f} sq ft")

st.divider()

st.header("3️⃣ Estimated Capacity")
capacity = math.floor(usable_area / sfu) if sfu > 0 else 0
st.success(f"Estimated Warehouse Capacity: {capacity} vending units")
