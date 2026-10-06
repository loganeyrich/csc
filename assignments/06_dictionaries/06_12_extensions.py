'''
Logan Eyrich
Chapter 6
Extensions
'''

# Creates a dictionary of rivers and the countries they flow through.
# This version extends the original example by adding more entries and improving output formatting.
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Mississippi': 'United States',
    'Yangtze': 'China',
    'Danube': 'Germany'
}

print("River and Country Overview")
print("=" * 28)

# Prints a clear sentence for each river-country pair.
for river, country in rivers.items():
    print(f"- The {river} flows through {country}.")

print("\nRiver names:")
for river in sorted(rivers.keys()):
    print(f"  * {river}")

print("\nCountries represented:")
for country in sorted(set(rivers.values())):
    print(f"  * {country}")
