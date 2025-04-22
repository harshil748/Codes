import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
import time

def extract_emails_from_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return []
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        # Extract all email addresses from the page
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
        return list(set(emails))
    except:
        return []

def find_company_info(company_name):
    try:
        query = f"{company_name} contact OR career OR HR email"
        for url in search(query, num_results=3):
            emails = extract_emails_from_url(url)
            if emails:
                return url, ', '.join(emails)
        return "Not found", "No email found"
    except:
        return "Error", "Error"

def main():
    input_file = "companiescopy.csv"  # Your file
    output_file = "companies_with_contact_info.csv"

    df = pd.read_csv(input_file)
    df['Website'] = ""
    df['Email(s)'] = ""

    for i, row in df.iterrows():
        company_name = row['Company Name']
        print(f"🔍 Searching: {company_name}")
        website, emails = find_company_info(company_name)
        df.at[i, 'Website'] = website
        df.at[i, 'Email(s)'] = emails
        time.sleep(2)  # Prevent getting blocked by Google

    df.to_csv(output_file, index=False)
    print(f"\n✅ All done! Results saved to: {output_file}")

if __name__ == "__main__":
    main()