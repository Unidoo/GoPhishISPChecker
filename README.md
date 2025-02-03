Phishing Data Processor

This Python script processes a CSV file containing GoPhish-related data, extracts IP addresses, checks them against Microsoft IPs using curl, and filters out false positives. It also ensures that if an email appears twice (once for a "clicked link" and once for "submitted data"), only the "submitted data" row is kept.
Features

✅ Extracts IP addresses from a "details" column.
✅ Checks IP ownership using curl -s https://ipinfo.io/<IP>/org.
✅ Identifies Microsoft IPs (AS8075 Microsoft Corporation) and marks "clicked link" rows as false positives.
✅ Filters duplicate emails, keeping "submitted data" rows and removing corresponding "clicked link" rows.
✅ Displays a progress bar while processing IP lookups.

Installation


    git clone https://github.com/unidoo/GoPhishISPChecker.git

    
cd phishing-data-processor

Install dependencies

    pip install tqdm

Usage

Run the script and enter the input/output CSV file names:

    python extract_ips.py

You will be prompted to enter the filenames, for example:

Please enter the name of the input CSV file: input.csv
Please enter the name of the output CSV file: output.csv


How It Works

    Extracts the IP address from the "details" column.
    Runs curl to check the IP’s organization.
    If "AS8075 Microsoft Corporation" appears, marks the "clicked link" row as a false positive.
    If an email appears with both "clicked link" and "submitted data" rows, keeps only the "submitted data" row.
    Writes the cleaned data to the output CSV file.

Notes

    "Submitted data" rows are not marked as false positives, even if they contain a Microsoft IP.
    The script uses a 10-second timeout for curl to avoid long waits.
    The progress bar updates as IPs are checked.

License

MIT License – Feel free to modify and use!



![image](https://github.com/user-attachments/assets/2b15d6b0-f073-48ed-906a-7b024a33e4e9)

