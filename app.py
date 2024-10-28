from flask import Flask, render_template, request

app = Flask(__name__)

EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,      # kgCO2/kWh
        "Diet": 1.25,              # kgCO2/meal
        "Waste": 0.1               # kgCO2/kg
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs
        country = request.form['country']
        distance = float(request.form['distance']) * 365  # yearly
        electricity = float(request.form['electricity']) * 12  # yearly
        waste = float(request.form['waste']) * 52  # yearly
        meals = int(request.form['meals']) * 365  # yearly

        # Calculate emissions
        transportation_emissions = EMISSION_FACTORS[country]['Transportation'] * distance / 1000
        electricity_emissions = EMISSION_FACTORS[country]['Electricity'] * electricity / 1000
        diet_emissions = EMISSION_FACTORS[country]['Diet'] * meals / 1000
        waste_emissions = EMISSION_FACTORS[country]['Waste'] * waste / 1000

        total_emissions = round(
            transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
        )

        return render_template('results.html', 
                               transportation=round(transportation_emissions, 2),
                               electricity=round(electricity_emissions, 2),
                               diet=round(diet_emissions, 2),
                               waste=round(waste_emissions, 2),
                               total=total_emissions)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
