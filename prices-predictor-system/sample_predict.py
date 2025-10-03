import json

import requests

# URL of the MLflow prediction server
url = "http://127.0.0.1:8000/invocations"

# Sample input data for prediction
# Replace the values with the actual features your model expects
# Sample input data for prediction
# This is the corrected "dataframe_split" format
input_data = {
    "dataframe_records": [
        {
            "Order": 2,
            "PID": 5287,
            "MS SubClass": 20,
            "MS Zoning": "RL",
            "Lot Frontage": 80.0,
            "Lot Area": 9600,
            "Street": "Pave",
            "Alley": None,
            "Lot Shape": "Reg",
            "Land Contour": "Lvl",
            "Utilities": "AllPub",
            "Lot Config": "Inside",
            "Land Slope": "Gtl",
            "Neighborhood": "NAmes",
            "Condition 1": "Norm",
            "Condition 2": "Norm",
            "Bldg Type": "1Fam",
            "House Style": "2Story",
            "Overall Qual": 5,
            "Overall Cond": 7,
            "Year Built": 1961,
            "Year Remod/Add": 1961,
            "Roof Style": "Gable",
            "Roof Matl": "CompShg",
            "Exterior 1st": "VinylSd",
            "Exterior 2nd": "VinylSd",
            "Mas Vnr Type": "None",
            "Mas Vnr Area": 0.0,
            "Exter Qual": "TA",
            "Exter Cond": "TA",
            "Foundation": "CBlock",
            "Bsmt Qual": "TA",
            "Bsmt Cond": "TA",
            "Bsmt Exposure": "No",
            "BsmtFin Type 1": "Rec",
            "BsmtFin SF 1": 700.0,
            "BsmtFin Type 2": "Unf",
            "BsmtFin SF 2": 0.0,
            "Bsmt Unf SF": 150.0,
            "Total Bsmt SF": 850.0,
            "Heating": "GasA",
            "Heating QC": "TA",
            "Central Air": "Y",
            "Electrical": "SBrkr",
            "1st Flr SF": 856,
            "2nd Flr SF": 854,
            "Low Qual Fin SF": 0,
            "Gr Liv Area": 1710.0,
            "Bsmt Full Bath": 1,
            "Bsmt Half Bath": 0,
            "Full Bath": 1,
            "Half Bath": 0,
            "Bedroom AbvGr": 3,
            "Kitchen AbvGr": 1,
            "Kitchen Qual": "TA",
            "TotRms AbvGrd": 7,
            "Functional": "Typ",
            "Fireplaces": 2,
            "Fireplace Qu": "TA",
            "Garage Type": "Attchd",
            "Garage Yr Blt": 1961,
            "Garage Finish": "Unf",
            "Garage Cars": 2,
            "Garage Area": 500.0,
            "Garage Qual": "TA",
            "Garage Cond": "TA",
            "Paved Drive": "Y",
            "Wood Deck SF": 210.0,
            "Open Porch SF": 0,
            "Enclosed Porch": 0,
            "3Ssn Porch": 0,
            "Screen Porch": 0,
            "Pool Area": 0,
            "Pool QC": None,
            "Fence": None,
            "Misc Val": 0,
            "Misc Feature": None,
            "Mo Sold": 5,
            "Yr Sold": 2010,
            "Sale Type": "WD",
            "Sale Condition": "Normal"
        }
    ]
}


# Convert the input data to JSON format
json_data = json.dumps(input_data)

# Set the headers for the request
headers = {"Content-Type": "application/json"}

# Send the POST request to the server
response = requests.post(url, headers=headers, data=json_data)

# Check the response status code
if response.status_code == 200:
    # If successful, print the prediction result
    prediction = response.json()
    print("Prediction:", prediction)
else:
    # If there was an error, print the status code and the response
    print(f"Error: {response.status_code}")
    print(response.text)
