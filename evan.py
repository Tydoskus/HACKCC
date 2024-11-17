# PROGRAMMER: Lewis Nguyen

# IMPORT STATEMENTS
import requests
from twilio.rest import Client
import math

class Evans :
    # CONSTRUCTOR
    def __init__(self, ambulance_latitude, ambulance_longitude) :
        URL = "https://ipgeolocation.abstractapi.com/v1/?api_key="
        GEOLOCATION_KEY = "Your key here"
        response = requests.request("GET", URL + GEOLOCATION_KEY)
        status = response.status_code
        if status != 200 :
            raise ValueError("Get request error code:", status)
        retrieved_data = response.json()
        
        self.__ambulance_latitude = ambulance_latitude
        self.__ambulance_longitude = ambulance_longitude
        
        self.__car_latitude = retrieved_data["latitude"]
        self.__car_longitude = retrieved_data["longitude"]
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        TWILIO_ACCOUNT_SSID = "Your SSID here"
        TWILIO_AUTH_TOKEN = "Your Authentication Token here"
        self.__client = Client(TWILIO_ACCOUNT_SSID, TWILIO_AUTH_TOKEN)
        self.__recipient_phone_number = str(input("Thanks for signing up with EVAN! Please enter your phone number: "))
        
    # INSTANCE METHODS 
    def get_ambulance_latitude(self) :
        return self.__ambulance_latitude
    
    def set_ambulance_latitude(self, ambulance_latitude) :
        self.__ambulance_latitude = ambulance_latitude
    
    def get_ambulance_longitude(self) :
        return self.__ambulance_longitude
    
    def set_ambulance_longitude(self, ambulance_longitude) :
        self.__ambulance_longitude = ambulance_longitude       
    
    def get_car_latitude(self) :
        return self.__car_latitude
    
    def set_car_latitude(self, car_latitude) :
        self.__car_latitude = car_latitude    
    
    def get_car_longitude(self) :
        return self.__car_longitude
    
    def set_car_longitude(self, car_longitude) :
        self.__car_longitude = car_longitude

    def distance(self) :
        # convert all latitudes and longitudes to radians
        self.__ambulance_latitude = math.radians(self.__ambulance_latitude)
        self.__ambulance_longitude = math.radians(self.__ambulance_longitude)        
        self.__car_latitude = math.radians(self.__car_latitude)
        self.__car_longitude = math.radians(self.__car_longitude)                  
        # differences in coordinates
        longitude_difference = self.__car_longitude - self.__ambulance_longitude
        latitude_difference = self.__car_latitude - self.__ambulance_latitude        
        # Harversine Formula
        part_a = math.sin(latitude_difference / 2) ** 2 + math.cos(self.__ambulance_latitude) * math.cos(self.__car_latitude) * math.sin(longitude_difference / 2) ** 2        
        part_b = 2 * math.atan2(math.sqrt(part_a), math.sqrt(1 - part_a))
        RADIUS_OF_EARTH_IN_MILES = 3959
        distance = RADIUS_OF_EARTH_IN_MILES * part_b
        
        if distance <= 1 :
            message = self.__client.messages.create(
                from_ = "+17145532408",
                to = self.__recipient_phone_number,
                body = "Alert!!! An ambulance is less than a mile away. Pull over to the right.",
                media_url=["https://www.shutterstock.com/shutterstock/photos/2206350353/display_1500/stock-photo-ambulance-on-emergency-vehicle-in-motion-blur-2206350353.jpg"])
