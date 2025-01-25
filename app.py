from flask import Flask, render_template
from db_setup import SessionLocal
from models import Restaurant  # Import 'Restaurant' to display data from the database

app = Flask(__name__)

@app.route("/")
def home():
    
    # Connect to the database
    db = SessionLocal()
    # Fetch the first 10 restaurants from the database
    restaurants = db.query(Restaurant).limit(10).all()
    db.close()
    
    # Render the template and pass the list of restaurants
    return render_template("index.html", restaurants=restaurants)

if __name__ == "__main__":
    # Run the Flask application in debug mode for development
    app.run(debug=True)
