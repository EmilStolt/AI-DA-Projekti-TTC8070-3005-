import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

relative_path = "../data/model_KNN.pkl"
dataset = st.container()

# addind cache so dont need to allways reload the data
@st.cache_data
def get_data(filename):
    df = pd.read_csv(filename,low_memory=False,index_col="vin")
    return df   


# loading everything
if os.path.exists(relative_path):
    # open model
    with open(relative_path, "rb") as file:
        model = pickle.load(file)
else:
    print("No file!", relative_path)

if os.path.exists("../data/le_body_type.pkl"):
    # open body type
    with open("../data/le_body_type.pkl", "rb") as file:
        le_body_type = pickle.load(file)
else:
    print("No file!")

if os.path.exists("../data/le_transmission.pkl"):
    # open transmission
    with open("../data/le_transmission.pkl", "rb") as file:
        le_transmission = pickle.load(file)
else:
    print("No file!")

if os.path.exists("../data/le_fuel_type.pkl"):
    # open fuel type
    with open("../data/le_fuel_type.pkl", "rb") as file:
        le_fuel_type = pickle.load(file)
else:
    print("No file!")

if os.path.exists("../data/le_make_name.pkl"):
    # open make name
    with open("../data/le_make_name.pkl","rb") as file:
        le_make_name = pickle.load(file)
else:
    print("No file!")

if os.path.exists("../data/le_wheel_system.pkl"):
    # open wheel system
    with open("../data/le_wheel_system.pkl","rb") as file:
        le_wheel_system = pickle.load(file)
else:
    print("No file!")

if os.path.exists("../data/scaler_KNN.pkl"):
    # open scaler
    with open("../data/scaler_KNN.pkl","rb") as file:
        scaler = pickle.load(file)
else:
    print("No file!")

# checking inputs
def preprocess(body_type,fuel_type,horsepower,maximum_seating,mileage,make_name,year,transmission,wheel_system,combined_fuel_economy,major_options_count):
    
    body_type_encoded = le_body_type.transform([body_type])[0]
    transmission_encoded = le_transmission.transform([transmission])[0]
    fuel_type_encoded = le_fuel_type.transform([fuel_type])[0]
    make_name_encoded = le_make_name.transform([make_name])[0]
    wheel_system_encoded = le_wheel_system.transform([wheel_system])[0]


    features = np.array([body_type_encoded, fuel_type_encoded, horsepower, maximum_seating, mileage, make_name_encoded, year, transmission_encoded, wheel_system_encoded, combined_fuel_economy, major_options_count]).reshape(1, -1)
    features_scaled = scaler.transform(features)
    return features_scaled

# setting title
st.title("Katsotaan autolle sopivaa myyntihintaa!")



with dataset:
    data = get_data("../data/ready_and_cleaned_used_cars_data.csv")

# header and show 30 first of data
st.header("Näyte olemassa olevasta datasta")
st.dataframe(data.head(30))
    

st.subheader("Täytä tähän auton tiedot:")
# get user inputs
body_type = st.selectbox("Mikä korimalli autossa on?", ["SUV / Crossover","Sedan","Coupe","Hatchback","Pickup Truck","Wagon","Minivan","Convertible","Van"])
year = st.slider("Aseta auton vuosimalli", min_value=1915, max_value=2021, step=1)
mileage = st.number_input("Aseta ajetut mailit", min_value=0)
horsepower = st.slider("Aseta hevosvoimat", min_value=63,max_value=1001, step=10)
transmission = st.selectbox("Valitse vaihteisto", ["A", "CVT", "M", "Dual Clutch"])
combined_fuel_economy = st.slider("Paljonko auto kuluttaa gallonina?", min_value=0,max_value=100,step=1)
fuel_type = st.selectbox("Aseta polttoainetyyppi", ["Gasoline","Diesel","Biodiesel","Flex Fuel Vehicle","Electric","Hybrid","Compressed Natural Gas","Propane"])
maximum_seating = st.slider("Aseta auton istuinpaikkojen määrä", min_value=2, max_value=15, step=1)
make_name = st.selectbox("Auton malli?", ["Jeep","Land Rover","Mazda","Alfa Romeo","BMW","Hyundai","Chevrolet","Lexus","Subaru",
                                          "Cadillac","Chrysler","Dodge","Mercedes-Benz","Nissan","Honda","Kia","Ford","Lincoln",
                                          "Audi","Volkswagen","RAM","Porsche","Jaguar","GMC","Toyota","Maserati","Acura","INFINITI",
                                          "FIAT","Volvo","Mitsubishi","Buick","Mercury","MINI","Ferrari","Genesis","Saturn","Saab",
                                          "Bentley","Suzuki","Tesla","Fisker","Pontiac","Lamborghini","smart","Scion","Hummer",
                                          "Rolls-Royce","Lotus","Spyker","McLaren","Aston Martin","Kaiser","Oldsmobile","Maybach",
                                          "Plymouth","Shelby","Triumph","Pagani","Karma","Datsun","Isuzu","MG","Studebaker","AM General",
                                          "Freightliner","Austin-Healey","AMC","Hudson","Willys","Pininfarina","Sunbeam","Geo","Opel",
                                          "SRT","Edsel","Eagle","Bugatti","Daewoo","VPG","Austin","Packard","DeTomaso","International Harvester",
                                          "Ariel","Allard","Bricklin","DeLorean","Nash","Clenet","Mobility Ventures","Franklin","Jensen",
                                          "Saleen","Morris","Koenigsegg","Rover"])
wheel_system = st.selectbox("Onko auto etuveto vai joku muu?", ["FWD", "AWD", "RWD", "4WD", "4X2"])
major_options_count = st.slider("Aseta auton lisävarusteiden määrä", min_value=1, max_value=59, step=1)


# initialize session state variables if they don"t exist
if "ennusta_pressed" not in st.session_state:
    st.session_state["ennusta_pressed"] = False

# code for prediction
if st.button("Ennusta"):
    st.session_state["ennusta_pressed"] = True

    # preprocess input data and make prediction
    input_data = preprocess(body_type, fuel_type, horsepower, maximum_seating, mileage, make_name, year, transmission, wheel_system, combined_fuel_economy, major_options_count)
    prediction = np.exp(model.predict(input_data))

    # show prediction
    st.success(f"Arvioitu auton hinta on! ${prediction[0]:.2f}")

    # getting 20 closest cars with same price
    df_closest = data.iloc[(data["price"] - prediction[0]).abs().argsort()[:20]]
    st.header("Tästä voi vähän vertailla saman hintaluokan autoja")
    st.dataframe(df_closest)

    

        
        
        
        
    



