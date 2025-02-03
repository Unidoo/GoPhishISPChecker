
IP WHOIS Lookup with False-Positive Detection

This Python script processes a CSV file containing details about IP addresses, extracts those IPs, performs WHOIS lookups, and flags potential "false-positives" related to Microsoft (MSFT). It features a progress bar for monitoring the processing status, and the results are saved in a new CSV file with an additional "notes" column indicating whether the IP was identified as a false-positive.
Features:

    CSV Input/Output: The script reads from a CSV file with columns like email, message, and details, and writes to a new CSV file with an additional notes column.
    WHOIS Lookup: For each IP address, a WHOIS query is made asynchronously, and it checks three fields (NetName, OrgName, OrgId) to flag any IPs associated with Microsoft.
    False-Positive Detection: If the WHOIS data contains:
        NetName: MSFT
        OrgName: Microsoft Corporation
        OrgId: MSFT The script flags the entry as a "false-positive" in the notes column.
    Progress Bar: A dynamic progress bar (via tqdm) tracks the number of processed IPs, providing a real-time status update every second.

Requirements:

    Python 3
    tqdm library for progress tracking. You can install it using:

    pip install tqdm

    whois command-line tool must be installed on your system.

How to Use:

    Place your input CSV file (e.g., input.csv) in the same directory as the script.
    Run the script:

    python ip_whois_lookup.py

    The script will prompt you to enter the input and output CSV file names.
    The processed data with the "false-positive" flags will be saved in the specified output CSV file.

Example:

Input CSV (input.csv):
email	message	details
example1@test.com	Hello	{"address":"8.8.8.8", "message":"test"}
example2@test.com	Hi	{"address":"40.76.4.10", "message":"test"}

Output CSV (output.csv):
email	message	IP Address	notes
example1@test.com	Hello	8.8.8.8	
example2@test.com	Hi	40.76.4.10	false-positive



![image](https://github.com/user-attachments/assets/2b15d6b0-f073-48ed-906a-7b024a33e4e9)

