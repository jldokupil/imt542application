
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys

def is_valid_wikipedia_url(url):
    parsed = urlparse(url)
    return parsed.netloc.endswith("wikipedia.org") and "/wiki/" in parsed.path

def get_references_from_wikipedia(url):
    if not is_valid_wikipedia_url(url):
        raise ValueError("Please enter a valid Wikipedia article URL.")

    response = requests.get(url)
    if response.status_code != 200:
        raise ConnectionError("Failed to fetch the page.")

    soup = BeautifulSoup(response.text, "html.parser")
    references = soup.find_all("ol", class_="references")

    all_sources = []
    for ref_list in references:
        for li in ref_list.find_all("li"):
            source_text = li.get_text(strip=True, separator=" ")
            all_sources.append(source_text)

    return all_sources

def display_sources(sources):
    print("\n📚 References:\n" + "-"*60)
    if not sources:
        print("No references found.")
    for i, source in enumerate(sources, 1):
        print(f"{i}. {source}\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python wiki_sources.py <Wikipedia Article URL>")
        return

    url = sys.argv[1]
    try:
        sources = get_references_from_wikipedia(url)
        display_sources(sources)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
