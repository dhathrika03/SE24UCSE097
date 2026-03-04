# AQI Simple Reflex Agent
# Input sensor: sensor_data.txt

def read_sensor_data(filename):
    sensor_data = {}
    with open(filename, 'r') as file:
        for line in file:
            gas, value = line.strip().split('=')
            sensor_data[gas] = float(value)
    return sensor_data


def get_sub_index(gas, value):

    if gas == "PM2.5":
        if value <= 50:
            return 50
        elif value <= 100:
            return 100
        else:
            return 160

    elif gas == "PM10":
        if value <= 50:
            return 50
        elif value <= 100:
            return 100
        else:
            return 140

    elif gas == "CO":
        if value <= 1:
            return 50
        elif value <= 2:
            return 100
        else:
            return 150

    elif gas == "NO2":
        if value <= 40:
            return 50
        elif value <= 80:
            return 100
        else:
            return 150

    elif gas == "SO2":
        if value <= 40:
            return 50
        elif value <= 80:
            return 100
        else:
            return 150

    elif gas == "O3":
        if value <= 50:
            return 50
        elif value <= 100:
            return 100
        else:
            return 150

    elif gas == "NH3":
        if value <= 200:
            return 50
        elif value <= 400:
            return 100
        else:
            return 150

    else:
        return 0


def reflex_agent():
    sensor_file = "sensor_data.txt"
    sensor_data = read_sensor_data(sensor_file)
    sub_indices = []

    print("Sensor Readings:")
    for gas, value in sensor_data.items():
        print(f"{gas} = {value}")
        sub_indices.append(get_sub_index(gas, value))

    final_aqi = max(sub_indices)

    print("\nFinal AQI:", final_aqi)

    if final_aqi <= 50:
        print("AQI Category: Good")
    elif final_aqi <= 100:
        print("AQI Category: Moderate")
    elif final_aqi <= 200:
        print("AQI Category: Poor")
    else:
        print("AQI Category: Very Poor")


# Run the agent
reflex_agent()