#######################################################

# Usage - python sd_finder.py domains.txt output.csv

#######################################################

import shodan
import argparse
import csv
from shodan import Shodan
from shodan.cli.helpers import get_api_key

# Secure way to fetch the Shodan API key. Ensure that the Shodan CLI is installed and that you had run <shodan init "API_KEY"> before running this script
api = Shodan(get_api_key())

# Function to extract subdomains from a domain
def get_subdomains(domain):
    try:
        # Search Shodan for the domain
        results = api.search(f'hostname:{domain}')
        subdomains = set()

        # Iterate through the results and extract subdomains
        for result in results['matches']:
            hostnames = result.get('hostnames', [])
            for hostname in hostnames:
                if domain in hostname:
                    subdomains.add(hostname)

        return list(subdomains)
    except shodan.APIError as e:
        print(f'Error: {e}')
        return []

# Function to read domains from a text file
def read_domains_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Set up argument parsing
parser = argparse.ArgumentParser(description='Extract subdomains from a list of domains using Shodan.')
parser.add_argument('filename', type=str, help='The filename containing the list of domains')
parser.add_argument('output', type=str, help='Output CSV file')

args = parser.parse_args()

# Read the list of domains from the provided text file
domains = read_domains_from_file(args.filename)

# Dictionary to store the subdomains for each domain
domain_subdomains = {}

# Extract subdomains for each domain in the list
for domain in domains:
    print("Processing: " + domain)
    subdomains = get_subdomains(domain)
    domain_subdomains[domain] = subdomains

# Write the results to a CSV file
with open(args.output, 'w', newline='') as csvfile:
    fieldnames = ['Domain', 'Subdomain']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for domain, subdomains in domain_subdomains.items():
        for subdomain in subdomains:
            writer.writerow({'Domain': domain, 'Subdomain': subdomain})

print(f'Results saved to {args.output}')
