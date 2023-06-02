import streamlit as st
import requests
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

# Function to fetch weather data based on location using the WeatherAPI
def get_weather_data(location, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=yes"

    # Make a request to the WeatherAPI
    response = requests.get(url)

    # Process the response and extract relevant weather information
    if response.status_code == 200:
        weather_data = response.json()
        current = weather_data['current']
        wind_speed = current['wind_kph']
        wind_direction = current['wind_degree']
        temperature = current['temp_c']
        humidity = current['humidity']

        return {
            'Wind Speed (kph)': wind_speed,
            'Wind Direction (degree)': wind_direction,
            'Temperature (°C)': temperature,
            'Humidity (%)': humidity
        }
    else:
        # Handle API request error
        st.error("Error fetching weather data.")
        return None

# Placeholder function to calculate rate of spread based on weather data
def calculate_rate_of_spread_formula(wind_speed, wind_direction, temperature, humidity):
    # Placeholder calculation
    rate_of_spread = wind_speed * temperature / humidity #

    return rate_of_spread

# Function to calculate rate of spread based on weather data
def calculate_rate_of_spread(location, api_key):
    # Fetch weather data based on location and API key
    weather_data = get_weather_data(location, api_key)

    if weather_data:
        # Extract relevant weather information
        wind_speed = weather_data['Wind Speed (kph)']
        wind_direction = weather_data['Wind Direction (degree)']
        temperature = weather_data['Temperature (°C)']
        humidity = weather_data['Humidity (%)']

        # Calculate rate of spread using predefined formulas or algorithms
        rate_of_spread = calculate_rate_of_spread_formula(wind_speed, wind_direction, temperature, humidity)
        return rate_of_spread 
    else:
        return None

# Function to send email alert
def send_email_alert(recipient_email, subject, message):
    # Setup email content
    msg = MIMEMultipart()
    msg['From'] = 'firedetection1234@gmail.com'  # Replace with your email address
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('firedetection1234@gmail.com', 'Fire$19891981')  # Replace with your email address and password
        server.send_message(msg)
        server.quit()
        st.success("Email alert sent successfully.")
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")

# Function to perform historical analysis on fire data
def perform_historical_analysis():
    # Add your historical analysis implementation here
    # This is a placeholder function
    st.write("Performing historical analysis...")

    # Simulating some analysis results
    df = pd.DataFrame({
        'Date': [date(2021, 1, 1), date(2021, 1, 2), date(2021, 1, 3)],
        'Fire Count': [10, 5, 12]
    })

    st.write("Historical Fire Data:")
    st.dataframe(df)

# Function to run the fire safety quiz
def run_fire_safety_quiz():
    # Fire safety quiz questions and answers
    questions = [
        "What should you do in case of a fire?",
        "What is the recommended escape plan for a multi-story building?",
        "What type of fire extinguisher should be used for electrical fires?"
    ]
    answers = [
        "Stay calm, evacuate the building, and call emergency services.",
        "Use the stairs and avoid elevators.",
        "Class C fire extinguisher."
    ]

    # Display quiz questions and answers
    for i, (question, answer) in enumerate(zip(questions, answers)):
        st.write(f"Question {i+1}: {question}")
        st.write(f"Answer: {answer}")
        st.write("---")

# Streamlit app
def main():
    st.title('Fire Detection Project')

    # Placeholder for API key
    api_key = "90c5fffcc6694af2ae394044232105"

    app_mode = st.sidebar.selectbox('Choose the App Mode', [ 'Weather Data', 'Email Alert', 'Historical Analysis', 'Fire Safety Quiz'])

    if app_mode == 'Weather Data':
        st.subheader("Weather Data")

        st.write("Please enter the location:")
        location = st.text_input("Location:")

        if st.button("Get Weather Data"):
            weather_data = get_weather_data(location, api_key)
            if weather_data is not None:
                st.success(f"Weather data for {location}:")
                for param, value in weather_data.items():
                    st.write(f"{param}: {value}")

                # Calculate rate of spread based on weather data
                rate_of_spread = calculate_rate_of_spread(location, api_key)
                if rate_of_spread is not None:
                    st.success(f"Rate of Spread: {rate_of_spread} Miles per hour")

    if app_mode == 'Email Alert':
        st.subheader("Email Alert")

        st.write("Please enter the recipient email:")
        recipient_email = st.text_input("Recipient Email:")

        if st.button("Send Email Alert"):
            subject = "Fire Alert"
            message = "There is a fire detected in your area. Please take necessary precautions."
            send_email_alert(recipient_email, subject, message)

    if app_mode == 'Historical Analysis':
        st.subheader("Historical Analysis")

        st.write("Perform analysis on historical fire data:")
        perform_historical_analysis()

    if app_mode == 'Fire Safety Quiz':
        st.subheader("Fire Safety Quiz")

        st.write("Test your fire safety knowledge:")
        run_fire_safety_quiz()

   

   


if __name__ == '__main__':
    main()
