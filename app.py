import streamlit as st

st.title("🌍 Unit Converter App")
st.markdown("### Converts Length, Weight And Time Instantly ")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "kilograms to pounds":
            return value * 2.20462
        elif unit == "pounds to kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes": 
            return value * 60
        elif unit == "Hours to Day":
            return value / 24
        elif unit == "Day to Hours":
            return value * 24
    
    return None

if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["kilometers to miles", "Miles to kilometers"])
    
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["kilograms to pounds", "pounds to kilograms"])

elif category == "Time":
    unit = st.selectbox("⏰ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Day", "Day to Hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid conversion.")
