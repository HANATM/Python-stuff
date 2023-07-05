# A python script for Information gathering 
import socket
import requests

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_public_ip():
    response = requests.get('https://api.ipify.org').text
    return response

def get_user_agent():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get('https://httpbin.org/user-agent', headers=headers).json()
    user_agent = response['user-agent']
    return user_agent

def get_location(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    country = response['country_name']
    city = response['city']
    region = response['region']
    postal = response['postal']
    timezone = response['timezone']
    return country, city, region, postal, timezone

def main():
    ip_address = get_ip_address()
    public_ip = get_public_ip()
    user_agent = get_user_agent()
    country, city, region, postal, timezone = get_location(public_ip)

    print("Local IP Address:", ip_address)
    print("Public IP Address:", public_ip)
    print("User Agent:", user_agent)
    print("Location:")
    print("Country:", country)
    print("City:", city)
    print("Region:", region)
    print("Postal Code:", postal)
    print("Timezone:", timezone)

if __name__ == '__main__':
    main()
