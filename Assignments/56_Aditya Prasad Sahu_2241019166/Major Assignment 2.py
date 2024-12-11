# Mission 1: Clearing the Field
def clear_field_manual(cities):
    return sorted(set(cities))

cities = ["Kyiv", "Kharkiv", "Odessa", "Kyiv", "Lviv", "Kharkiv", "Dnipro"]
cleaned_cities = clear_field_manual(cities)
print("Cleaned Cities :", cleaned_cities)

# Mission 2: High Alert Identification
def high_alert_manual(cleaned_cities, previous_intel):
    all_cities = list(set(cleaned_cities + previous_intel))
    unique_cities = [city for city in all_cities if city not in cleaned_cities or city not in previous_intel]
    common_cities = [city for city in cleaned_cities if city in previous_intel]
    return all_cities, unique_cities, common_cities

previous_intel = ["Kyiv", "Mariupol", "Lviv", "Donetsk"]
all_cities, unique_cities, high_alert_cities = high_alert_manual(cleaned_cities, previous_intel)
print("All Cities :", all_cities)
print("Unique Cities :", unique_cities)
print("High Alert Cities :", high_alert_cities)

# Mission 3: Detailed City Intel
def city_intel_manual(high_alert_cities, city_data):
    high_alert_info = {city: (pop, req) for city, pop, req in city_data if city in high_alert_cities}
    total_population = sum(pop for city, pop, req in city_data if city in high_alert_cities)
    total_requests = sum(req for city, pop, req in city_data if city in high_alert_cities)
    return high_alert_info, total_population, total_requests

city_data = [("Kyiv", 2800000, 250), ("Kharkiv", 1431000, 180), ("Lviv", 721301, 90), ("Odessa", 1029049, 120)]
high_alert_info, total_population, total_requests = city_intel_manual(high_alert_cities, city_data)
print("High Alert Cities Info :", high_alert_info)
print("Total Population :", total_population)
print("Total Requests :", total_requests)

# Mission 4: Tracking Supply Distribution
def supply_distribution_manual(supplies):
    distribution = {}
    for city, supply, qty in supplies:
        distribution.setdefault(city, {})[supply] = qty
    return distribution

supplies = [("Kyiv", "Food", 500), ("Moscow", "Medicines", 200), ("Lviv", "Water", 300), 
            ("Saint Petersburg", "Blankets", 100), ("Kharkiv", "Food", 150)]
distribution = supply_distribution_manual(supplies)
print("Supply Distribution :", distribution)
