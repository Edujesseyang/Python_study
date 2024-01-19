# ===========================================================
# Fremont: 59
# Sunnyvale: 60
# Saratoga: 56
# San Jose: 61
# Campbell: 59
# Los Altos: 58
# Put these into a dictionary and print out the city with the highest and lowest temperatures. If there's a tie, just pick one city
# Solution: --------------------------------------------------
city_temps = {
    'Fremont': 59,
    'Sunnyvale': 60,
    'Saratoga': 56,
    'San Jose': 61,
    'Campbell': 59,
    'Los Altos': 58,
}
hightest = 0
hi_city = ""
for name in city_temps:
    if city_temps[name] > hightest:
        hightest = city_temps[name]
        hi_city = name
lowest = hightest
lo_city = ""
for name in city_temps:
    if city_temps[name] < lowest:
        lowest = city_temps[name]
        lo_city = name
print(f'The hottest city is {hi_city}, the temperature is {hightest}.')
print(f'The coldest city is {lo_city}, the temperature is {lowest}.')
# ====================================================================================
