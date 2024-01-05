# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
import re

# SQLalchemy toolkit
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# # reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine) # it doesnt like this

# # Save reference to the table
# climate = Base.classes.climate

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """Sup bruh, welcome to the Hawai'i Climate API"""
    return (
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/start (enter as YYYY-MM-DD) <br/>"
        f"/api/v1.0/start/end (enter as YYYY-MM-DD/YYYY-MM-DD)"
    )


@app.route("/api/v1.0/precipitation")

def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list data from the last 12mo"""
# Convert the query results from your precipitation analysis 
# (i.e. retrieve only the last 12 months of data) to a dictionary
# using date as the key and prcp as the value.
# Return the JSON representation of your dictionary
    target_date = dt.date(2017,8,23) - dt.timedelta(days=365)
    last_year = dt.date(target_date.year, target_date.month, target_date.day)
    
    dates_prcp = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date >= target_date).\
    order_by(measurement.date.desc()).all()
    
    dates_prcp_dict = dict(dates_prcp)
    print("this")
    return jsonify(dates_prcp_dict)
    
    
    
#     # Query all passengers
#     results = session.query(measurement.prcp).all()

#     session.close()

#     # Convert list of tuples into normal list
#     all_names = list(np.ravel(results))

#     return jsonify(all_names)


# @app.route("/api/v1.0/passengers")
# def passengers():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # Query all passengers
#     results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

#     session.close()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_passengers = []
#     for name, age, sex in results:
#         passenger_dict = {}
#         passenger_dict["name"] = name
#         passenger_dict["age"] = age
#         passenger_dict["sex"] = sex
#         all_passengers.append(passenger_dict)

#     return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)

