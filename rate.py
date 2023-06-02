import requests
from bs4 import BeautifulSoup
import streamlit as st

# Function to scrape the fires section from the website
def scrape_fires_section():
    url = "https://www.globalforestwatch.org/dashboards/global/?category=fires&dashboardPrompts=eyJzaG93UHJvbXB0cyI6dHJ1ZSwicHJvbXB0c1ZpZXdlZCI6W10sInNldHRpbmdzIjp7Im9wZW4iOmZhbHNlLCJzdGVwSW5kZXgiOjAsInN0ZXBzS2V5IjoiIn0sIm9wZW4iOnRydWUsInN0ZXBzS2V5Ijoidmlld05hdGlvbmFsRGFzaGJvYXJkcyJ9&location=WyJnbG9iYWwiXQ%3D%3D&map=eyJkYXRhc2V0cyI6W3siZGF0YXNldCI6InBvbGl0aWNhbC1ib3VuZGFyaWVzIiwibGF5ZXJzIjpbImRpc3B1dGVkLXBvbGl0aWNhbC1ib3VuZGFyaWVzIiwicG9saXRpY2FsLWJvdW5kYXJpZXMiXSwiYm91bmRhcnkiOnRydWUsIm9wYWNpdHkiOjEsInZpc2liaWxpdHkiOnRydWV9LHsiZGF0YXNldCI6InRyZWUtY292ZXItbG9zcy1maXJlcyIsImxheWVycyI6WyJ0cmVlLWNvdmVyLWxvc3MtZmlyZXMiXSwib3BhY2l0eSI6MSwidmlzaWJpbGl0eSI6dHJ1ZSwicGFyYW1zIjp7InRocmVzaG9sZCI6MzAsInZpc2liaWxpdHkiOnRydWUsImFkbV9sZXZlbCI6ImFkbTAifX1dfQ%3D%3D&showMap=true"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find the fires section in the HTML structure
            fires_section = soup.find('div', class_='dashboard-widget-content')  # Adjust the class name as per the website structure
            
            return fires_section
        else:
            st.error("Failed to retrieve fires section from the website.")
    except requests.RequestException as e:
        st.error("Connection error:", str(e))
    
    return None

# Streamlit app
def main():
    st.title('Fires Dashboard')
    
    # Scrape the fires section from the website
    fires_section = scrape_fires_section()
    
    if fires_section is not None:
        # Display the fires section on Streamlit
        st.markdown(fires_section.prettify(), unsafe_allow_html=True)
    else:
        st.error("Failed to retrieve fires section from the website.")

if __name__ == '__main__':
    main()
