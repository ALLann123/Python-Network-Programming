import requests
from bs4 import BeautifulSoup
import whois
import argparse
import socket
from datetime import datetime

class OSINTFramework:
    def __init__(self, target):
        self.target = target

    def google_search(self, query, num_results=10):
        """
        Perform a Google search and return the results.
        """
        url = f"https://www.google.com/search?q={query}&num={num_results}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            results = []
            for g in soup.find_all('div', class_='tF2Cxc'):
                anchor = g.find('a')
                if anchor:
                    link = anchor['href']
                    title = g.find('h3').text
                    item = {
                        "title": title,
                        "link": link
                    }
                    results.append(item)
            return results
        except requests.exceptions.RequestException as e:
            print(f"Google search failed: {e}")
            return []

    def check_social_media(self, username):
        """
        Check if a username exists on popular social media platforms.
        """
        social_media_sites = {
            "Twitter": f"https://twitter.com/{username}",
            "Instagram": f"https://instagram.com/{username}",
            "Facebook": f"https://facebook.com/{username}",
            "LinkedIn": f"https://linkedin.com/in/{username}"
        }
        results = {}
        for site, url in social_media_sites.items():
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    results[site] = "Exists"
                else:
                    results[site] = "Does not exist"
            except requests.exceptions.RequestException as e:
                results[site] = f"Error: {e}"
        return results

    def whois_lookup(self, domain):
        """
        Perform a WHOIS lookup on a domain.
        """
        try:
            domain_info = whois.whois(domain)
            return domain_info
        except Exception as e:
            return f"WHOIS lookup failed: {e}"

    def run(self):
        """
        Run all OSINT modules.
        """
        print(f"Running OSINT on target: {self.target}\n")

        # Google Search
        print("Performing Google search...")
        google_results = self.google_search(self.target)
        for result in google_results:
            print(f"Title: {result['title']}")
            print(f"Link: {result['link']}\n")

        # Social Media Check
        print("Checking social media profiles...")
        social_media_results = self.check_social_media(self.target)
        for site, status in social_media_results.items():
            print(f"{site}: {status}")

        # WHOIS Lookup
        if "." in self.target:  # Simple check to see if it's a domain
            print("\nPerforming WHOIS lookup...")
            whois_info = self.whois_lookup(self.target)
            print(whois_info)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OSINT Framework")
    parser.add_argument("target", help="Target to investigate (e.g., username, domain, or search query)")
    args = parser.parse_args()

    osint = OSINTFramework(args.target)
    osint.run()