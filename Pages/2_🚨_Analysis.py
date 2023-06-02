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
        "What type of fire extinguisher should be used for electrical fires?",
        "What are the three main types of fire alarms?",
        "What should you do if a fire alarm goes off?",
        "What is the purpose of a fire evacuation drill?",
        "What is the recommended height for mounting smoke detectors on the ceiling?",
        "What is the acronym used to remember the steps in using a fire extinguisher?",
        "What should you do if your clothes catch fire?",
        "What are the common causes of kitchen fires?",
        "What is the importance of having a fire safety plan at home?",
        "What should you do if you encounter a closed door during a fire evacuation?",
        "What is the recommended way to test the temperature of a door during a fire?",
        "What are the four elements required for a fire to ignite?",
        "What should you do if you see smoke coming from an electrical outlet?",
        "What should you do if you are trapped in a smoke-filled room?",
        "What is the importance of having fire extinguishers in the workplace?",
        "What is the primary cause of home fires during winter months?",
        "What is the recommended distance to keep flammable materials away from a heat source?",
        "What should you do if you discover a fire in your home?",
        "What should you do if you hear a fire alarm while in a hotel?",
        "What is the recommended way to use a fire blanket?",
        "What should you do if a person's clothing catches fire?",
        "What are the different classes of fire extinguishers and their corresponding types of fires?",
        "What is the leading cause of residential fires?",
        "What is the purpose of fire safety inspections?",
        "What should you do if there is a fire in an enclosed space?",
        "What is the recommended placement for fire extinguishers in a commercial building?",
        "What should you do if a fire starts in a microwave oven?",
        "What should you do if you smell gas in your home?",
        "What are the common causes of electrical fires?",
    ]

    answers = [
        "Stay calm, evacuate the building, and call emergency services.",
        "Use the stairs and avoid elevators.",
        "Class C fire extinguisher.",
        "Ionization, photoelectric, and heat detectors.",
        "Follow the evacuation plan and proceed to the designated assembly area.",
        "To practice and prepare individuals for a fire emergency.",
        "On the ceiling, at least 4 inches away from the nearest wall.",
        "PASS: Pull the pin, Aim at the base of the fire, Squeeze the handle, Sweep from side to side.",
        "Stop, drop, and roll.",
        "Unattended cooking, grease fires, electrical malfunctions.",
        "To ensure the safety of all occupants and minimize the risk of fire-related injuries or damage.",
        "Check the door for heat using the back of your hand. If it's hot, do not open it.",
        "Feel the door with the back of your hand. If it's hot, do not open it.",
        "Fuel, heat, oxygen, and a chemical chain reaction.",
        "Disconnect the power source and call emergency services.",
        "Stay low to the ground and crawl to the nearest exit.",
        "To quickly suppress small fires and prevent them from spreading.",
        "Heating equipment and open flames.",
        "At least 3 feet.",
        "Evacuate the building and call emergency services from a safe location.",
        "Follow the evacuation procedures and exit the building calmly.",
        "Place it over the fire to smother it and cut off the oxygen supply.",
        "Cover the person with a heavy, non-flammable object or have them stop, drop, and roll.",
        "Class A: Ordinary combustibles, Class B: Flammable liquids and gases, Class C: Electrical fires, Class D: Combustible metals, Class K: Kitchen fires.",
        "Smoking materials, including cigarettes.",
        "To ensure compliance with fire safety codes and regulations.",
        "Try to escape through the nearest exit or window.",
        "Near exits, in hallways, and in areas prone to fire hazards.",
        "Unplug it, keep the door closed, and call for professional repair.",
        "Leave the premises immediately and contact the gas company or emergency services.",
        "Overloaded circuits, faulty wiring, and electrical equipment malfunctions.",
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

    # app_mode = st.sidebar.selectbox('Choose the App Mode', [ 'Weather Data', 'Email Alert', 'Historical Analysis', 'Fire Safety Quiz'])
    app_mode = st.sidebar.selectbox('Choose the App Mode', [ 'Weather Data', 'Fire Safety Quiz'])

    if app_mode == 'Weather Data':
        st.subheader("Weather Data")

        st.write("Please enter the location:")
        location = st.text_input("Location:")

        if st.button("Get Weather Data"):
            weather_data = get_weather_data(location, api_key)
            if weather_data is not None:
                st.subheader(f"Weather data for {location}:")
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
