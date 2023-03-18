import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def get_links(url):
    """Returns a list of links on the given web page"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and not href.startswith('#'):
            links.append(href)
    return links

def tree_view(url, level=0):
    """Recursively generates a directory tree view of the given website"""
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    links = get_links(url)
    for link in links:
        full_url = urljoin(base_url, link)
        print("  " * level + "- " + link)
        if full_url.startswith(base_url):
            tree_view(full_url, level+1)

# Example usage:
tree_view("https://gazzettaproject.wordpress.com/")
