import requests

def get_country_info(country_name):
    base_url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            country = data[0]
            name = country.get('name', {}).get('common', 'Unknown')
            capital = country.get('capital', ['Unknown'])[0]
            population = country.get('population', 'Unknown')
            region = country.get('region', 'Unknown')
            print(f"Country: {name}")
            print(f"Capital: {capital}")
            print(f"Population: {population}")
            print(f"Region: {region}")
        else:
            print(f"Country '{country_name}' not found.")
    else:
        print("Error in the HTTP request")

if __name__ == "__main__":
    country_name = input("Enter the country name: ").lower()
    get_country_info(country_name)
