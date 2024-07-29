# Shodan-Subdomain-Finder

## Introduction
To fetch sub-domains for a given list of domains and output the sub-domains as a CSV file

## Requirements
- Make sure you install the below dependencies using pip - `pip install <dependency>`
```
shodan
argparse
csv
```
- You will need a Shodan API key, which you can fetch by logging into your [Shodan Account](https://developer.shodan.io/api/)

## How to Run
- Save the script as **subdomain_finder.py**
- Save the list of domains that you want to run in a text file. Example, **input_domains.txt**
- Run the script as below, passing two arguments, the first being the input domains file and the second one being the CSV file, to capture the output.
```
python subdomain_finder.py input_domains.txt output.csv
```

## Interpreting the Output
- The output file `output.csv` contains two columns
- The first column has the parent domain that was searched and the second column has the corresponding sub-domain
