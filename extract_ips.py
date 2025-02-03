import csv
import re
import subprocess
import time
import threading
from tqdm import tqdm  # Import tqdm for progress bar

def extract_ip(details):
    match = re.search(r'"address":"([0-9\.]+)"', details)
    return match.group(1) if match else "No IP Found"

def run_whois(ip):
    # Start the whois process asynchronously
    process = subprocess.Popen(['whois', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        # Set a timeout to immediately cancel after getting the output
        stdout, stderr = process.communicate(timeout=15)  # 15 seconds timeout to get the data
        return stdout
    except subprocess.TimeoutExpired:
        process.kill()  # Kill the process after the timeout
        return process.stdout.read()  # Read available output

def get_netname_org(whois_data):
    # Check for 'NetName', 'OrgName', and 'OrgId' in the whois data
    netname_match = re.search(r'NetName:\s*(\S+)', whois_data)
    orgname_match = re.search(r'OrgName:\s*"(.*?)"', whois_data)
    orgid_match = re.search(r'OrgId:\s*(\S+)', whois_data)
    
    netname = netname_match.group(1) if netname_match else None
    orgname = orgname_match.group(1) if orgname_match else None
    orgid = orgid_match.group(1) if orgid_match else None
    
    return netname, orgname, orgid

def process_csv(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = ['email', 'message', 'IP Address', 'notes']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        # Convert the reader to a list to get the total number of IPs
        rows = list(reader)
        total_rows = len(rows)
        
        # Create a progress bar with tqdm
        with tqdm(total=total_rows, desc="Processing IPs", ncols=100, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} IPs") as pbar:
            for row in rows:
                ip_address = extract_ip(row['details'])
                whois_data = run_whois(ip_address)
                netname, orgname, orgid = get_netname_org(whois_data)
                
                # If any of the fields match the Microsoft-related terms, mark as 'false-positive'
                if netname == 'MSFT' or orgname == 'Microsoft Corporation' or orgid == 'MSFT':
                    notes = 'false-positive'
                else:
                    notes = ''
                
                writer.writerow({'email': row['email'], 'message': row['message'], 'IP Address': ip_address, 'notes': notes})
                
                # Update the progress bar
                pbar.update(1)

if __name__ == "__main__":
    input_csv = input("Please enter the name of the input CSV file: ")  # Ask for input file
    output_csv = input("Please enter the name of the output CSV file: ")  # Ask for output file
    process_csv(input_csv, output_csv)
    print(f"Processed data saved to {output_csv}")
