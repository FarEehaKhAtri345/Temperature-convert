import streamlit as st

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Main function to create Streamlit app
def main():
    st.title("Interactive Temperature Converter 🌡️")

    st.write("### Choose the conversion type:")
    
    # Dropdown for selecting conversion type
    option = st.selectbox(
        "What would you like to convert?",
        ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
    )
    
    if option == "Celsius to Fahrenheit":
        st.write("### Enter temperature in Celsius (°C) to convert:")
        
        # Slider for input in Celsius, interactive
        celsius = st.slider("Celsius", -100, 100, 0)  # Range from -100°C to 100°C
        st.write(f"You selected: {celsius}°C")

        # Button to trigger conversion
        if st.button("Convert to Fahrenheit"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.write(f"{celsius}°C is {fahrenheit:.2f}°F")
            # Provide some feedback based on the temperature range
            if fahrenheit > 86:
                st.success("It's getting hot! 😎")
            elif fahrenheit < 32:
                st.warning("It's freezing! 🥶")
            else:
                st.info("It's a comfortable temperature. 😊")
        
    elif option == "Fahrenheit to Celsius":
        st.write("### Enter temperature in Fahrenheit (°F) to convert:")
        
        # Slider for input in Fahrenheit, interactive
        fahrenheit = st.slider("Fahrenheit", -150, 200, 32)  # Range from -150°F to 200°F
        st.write(f"You selected: {fahrenheit}°F")

        # Button to trigger conversion
        if st.button("Convert to Celsius"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.write(f"{fahrenheit}°F is {celsius:.2f}°C")
            # Provide some feedback based on the temperature range
            if celsius > 30:
                st.success("It's quite warm! 🌞")
            elif celsius < 0:
                st.warning("It's freezing cold! ❄️")
            else:
                st.info("It's a nice temperature! 😌")

# Running the main function to start the app
if __name__ == "__main__":
    main()
