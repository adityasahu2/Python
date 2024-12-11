# Mission 1: Clearing the Field
def clear_field_manual(cities):
    unique_cities = []
    for city in cities:
        if city not in unique_cities:  
            unique_cities.append(city)
    for i in range(len(unique_cities)):
        for j in range(0, len(unique_cities) - i - 1):
            if unique_cities[j] > unique_cities[j + 1]:
                unique_cities[j], unique_cities[j + 1] = unique_cities[j + 1], unique_cities[j]
    return unique_cities

cities = ["Kyiv", "Kharkiv", "Odessa", "Kyiv", "Lviv", "Kharkiv", "Dnipro"]
cleaned_cities = clear_field_manual(cities)
print("Cleaned Cities =",cleaned_cities)

# Mission 2: High Alert Identification
def high_alert_manual(cleaned_cities, previous_intel):
    all_cities = cleaned_cities[:]
    for city in previous_intel:
        if city not in all_cities:
            all_cities.append(city)
    
    unique_cities = []
    for city in all_cities:
        if (city in cleaned_cities and city not in previous_intel) or (city in previous_intel and city not in cleaned_cities):
            unique_cities.append(city)
    
    common_cities = []
    for city in cleaned_cities:
        if city in previous_intel:
            common_cities.append(city)
    
    return all_cities, unique_cities, common_cities

previous_intel = ["Kyiv", "Mariupol", "Lviv", "Donetsk"]

all_cities, unique_cities, high_alert_cities = high_alert_manual(cleaned_cities, previous_intel)
print("All Cities =", all_cities)
print("Unique Cities =",unique_cities)
print("High Alert Cities =",high_alert_cities)

# Mission 3: Detailed City Intel
def city_intel_manual(high_alert_cities, city_data):
    high_alert_info = {}
    total_population = 0
    total_requests = 0

    for city, population, requests in city_data:
        if city in high_alert_cities:
            high_alert_info[city] = (population, requests)
            total_population += population
            total_requests += requests

    return high_alert_info, total_population, total_requests

city_data = [("Kyiv", 2800000, 250), ("Kharkiv", 1431000, 180), ("Lviv", 721301, 90), ("Odessa", 1029049, 120)]

high_alert_info, total_population, total_requests = city_intel_manual(high_alert_cities, city_data)
print("High Alert Cities Info =", high_alert_info)
print("Total Population =",total_population)
print("Total Requests =",total_requests)

# Mission 4: Tracking Supply Distribution
def supply_distribution_manual(supplies):
    distribution = {}

    for city, supply_type, quantity in supplies:
        if city not in distribution:
            distribution[city] = {}
        distribution[city][supply_type] = quantity 

    return distribution

supplies = [("Kyiv", "Food", 500), ("Moscow", "Medicines", 200), ("Lviv", "Water", 300), 
            ("Saint Petersburg", "Blankets", 100), ("Kharkiv", "Food", 150)]

distribution = supply_distribution_manual(supplies)
print("Supply Distribution =", distribution)