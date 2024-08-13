import streamlit as st

EMISSION_FACTORS ={
    "India":{
        "Transportation": 0.14, #kgCO2/km
        "Electricity":0.82, #kgCO@/kwH
        "Diet":1.25,#kgCO@/meal
        "Waste": 0.1#kgCO@/kg
    }
}

st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")
st.title("Personal Carbon Calculator")

# user inpus
st.subheader(" 🌍 your country")
country=st.selectbox("Select",["India"])

col1, col2 =st.columns(2)

with col1:
    st.subheader(" 🚗 Daily commute distance (in km)")
    distance = 0.0  # Initialize distance to 0
    distance=st.slider("Distance",0.0,100.0,key="distance_input")

    st.subheader(" 💡Monthly electricity (in kwh)")
    electricity=st.slider("Elecricity",0.0,1000.0,key="electricity_input")

with col2:
    st.subheader("🗑️ Waste generated per week (in kg)")
    waste=st.slider("Waste",0.0,100.0,key="waste_input")

    st.subheader("🥗 Number of meals per day)")
    meals=st.number_input("Meals",0,key="meals_input")

# Normalise input
if distance > 0:
   distance=distance*365 # convert distance to yearly

if electricity > 0:
   electricity=electricity* 12

if meals > 0:
   meals=meals*365 # convert distance to yearly

if waste > 0:
   waste=waste* 52 # convert distance to yearly


#    calculate carbon emission
transportation_emissions=EMISSION_FACTORS[country]['Transportation']*distance
electricity_emissions=EMISSION_FACTORS[country]['Electricity']*electricity
diet_emissions=EMISSION_FACTORS[country]['Diet']*meals
waste_emissions=EMISSION_FACTORS[country]['Waste']*waste

transportation_emissions=round(transportation_emissions/1000, 2)
electricity_emissions=round(electricity_emissions/1000,2)
diet_emissions=round(diet_emissions/1000,2)
waste_emissions=round(waste_emissions/1000,2)

# convert emissions to tonnes and round off to 2 decimal places
total_emissions = round(
   transportation_emissions + electricity_emissions + diet_emissions+ waste_emissions, 2
)

if st.button("calculate CO2 Emissions"):
#    display result
    st.header("Results")
    col3, col4 = st.columns(2)

    with col3:
       st.subheader("crabon Emissions by category")
       st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
       st.info(f"💡Electricity: {electricity_emissions} tonnes CO2 per year")
       st.info(f"🥗 Diet: {diet_emissions} tonnes CO2 per year")
       st.info(f"🗑️Waste: {waste_emissions} tonnes CO2 per year")
    
    with col4:
        st.subheader("total carbon Footprint")
        st.info(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
        st.warning("Per capita carbon dioxide (CO₂) emissions in India have soared in recent decades, climbing from 0.39 metric tons in 1970 to a high of 1.91 metric tons in 2022. This was an increase of 5.5 percent in comparison to 2021 levels. Total CO₂ emissions in India also reached a record high in 2022.")
     
       