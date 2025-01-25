import requests
import os
from config import API_KEY, API_URL

# Define headers for the Yelp API, including the API key
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def fetch_restaurants(city, category, limit=50):
    """Fetch restaurant data from the Yelp API."""
    # Debug information for the request
    print(f"Requesting Yelp API for city='{city}', category='{category}', limit={limit}")

    # Set query parameters for the Yelp API
    params = {
        "location": city,      # E.g., "Budapest" or "Budapest Hungary"
        "categories": category,
        "limit": limit
    }

    # Make the API request
    response = requests.get(API_URL, headers=HEADERS, params=params)
    
    if response.status_code == 200:
        print("Success! Yelp API gave data")
        return response.json()  # Return the JSON response
    else:
        print(f"Error {response.status_code}: {response.text}")
        print(f"Response Content: {response.content}")
        return None

def parse_and_insert_data(data):
    """Parse the data fetched from the Yelp API and insert it into the database."""
    from sqlalchemy.orm import Session
    from models import Restaurant, Category, Location
    from db_setup import SessionLocal

    # Start a new database session
    db = SessionLocal()

    for business in data["businesses"]:
        # Insert categories and locations if they don't already exist
        category_name = business["categories"][0]["title"]
        location_data = business["location"]

        # Check if the category already exists
        cat_obj = db.query(Category).filter_by(description=category_name).first()
        if not cat_obj:
            cat_obj = Category(description=category_name)
            db.add(cat_obj)
            db.commit()

        # Check if the location already exists
        loc_obj = db.query(Location).filter_by(
            city=location_data["city"],
            country=location_data["country"]
        ).first()
        if not loc_obj:
            loc_obj = Location(
                city=location_data["city"],
                country=location_data["country"]
            )
            db.add(loc_obj)
            db.commit()

        # Insert the restaurant
        restaurant = Restaurant(
            name=business["name"],
            address=business["location"]["address1"],
            price=business.get("price", "N/A"),
            rating=business["rating"],
            cuisine_type=category_name,
            latitude=business["coordinates"]["latitude"],
            longitude=business["coordinates"]["longitude"],
            id_category=cat_obj.id_category,
            id_location=loc_obj.id_location
        )
        
        db.add(restaurant)
        db.commit()

    db.close()

if __name__ == "__main__":
    city = "Barcelona" 
    category = "italian"  
    data = fetch_restaurants(city, category, limit=10)
    
    if data:
        parse_and_insert_data(data)  
    else:
        print("No data returned from Yelp API")
