import requests
from bs4 import BeautifulSoup
import re
import json
import os

# Directory to store JSON files
output_dir = "D:/Code/ME-bot/To_add"
os.makedirs(output_dir, exist_ok=True)

# Optional file containing URLs
urls_file = "D:/Code/ME-bot/urls.txt"

def sanitize_filename(character_name):
    """Sanitize the character name to be a valid filename."""
    return re.sub(r'[<>:"/\\|?*]', '_', character_name)

def get_character_links_from_file():
    """Reads the character URLs from a file."""
    character_links = []
    if os.path.exists(urls_file):
        with open(urls_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:  # Ensure non-empty lines
                    character_name = line.split('/')[-1].replace('_', ' ').replace('-tan', '')
                    character_links.append((character_name, line))
    return character_links

def get_character_links_from_web():
    """Scrapes the 'View All' page to get links to each character's page."""
    url = "https://www.ostan-collections.net/wiki/index.php/Apple-tans"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    character_links = []
    for link in soup.select("a[href^='/wiki/']"):
        href = link.get('href')
        if "/wiki/" in href and "View_All" not in href:
            character_name = link.get_text()
            character_links.append((character_name, f"https://www.ostan-collections.net{href}"))
    return character_links

def construct_api_urls(character_name):
    query_with_tan = character_name.replace(' ', '_')
    query_without_tan = character_name.replace('-tan', '').replace(' ', '_')
    api_url_with_tan = f'https://www.ostan-collections.net/wiki/api.php?action=query&format=json&titles={query_with_tan}&prop=revisions&rvprop=content'
    api_url_without_tan = f'https://www.ostan-collections.net/wiki/api.php?action=query&format=json&titles={query_without_tan}&prop=revisions&rvprop=content'
    return api_url_with_tan, api_url_without_tan

def fetch_content(api_url_with_tan, api_url_without_tan):
    def request_content(url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    data = request_content(api_url_with_tan)
    if not data or 'query' not in data:
        data = request_content(api_url_without_tan)
        if not data or 'query' not in data:
            print(f"No data found for the page. It may not exist: {api_url_with_tan}")
            return None, None

    pages = data['query']['pages']
    page = next(iter(pages.values()), {})
    if 'revisions' in page:
        return page['title'], page['revisions'][0]['*']
    
    return None, None

def parse_infobox(content):
    infobox_match = re.search(r'{{OSinfobox(.*?)}}', content, re.DOTALL)
    infobox_dict = {}
    
    if infobox_match:
        infobox_content = infobox_match.group(1)
        infobox_lines = [line.strip() for line in infobox_content.split('|') if '=' in line]
        infobox_dict = {line.split('=')[0].strip(): line.split('=')[1].strip() for line in infobox_lines}
    
    return infobox_dict

def clean_text(text):
    """Remove unwanted bracketed text."""
    # Remove nested brackets and any remaining unclosed brackets
    while '[[' in text and ']]' in text:
        text = re.sub(r'\[\[.*?\]\]', '', text)
    text = re.sub(r'{{.*?}}', '', text)  # Remove template braces
    text = text.replace('[', '').replace(']', '')
    return text

def parse_character_details(content):
    character_section_match = re.search(r'==Character details==([\s\S]*?)(?=\n==|$)', content, re.DOTALL)
    character_details = ""
    
    if character_section_match:
        character_details = character_section_match.group(1).strip()
    else:
        character_description_match = re.search(r'(?<=}})([\s\S]*?)(?=\n==Technical details==|\n==See also==|\n\[Category:|\n?$)', content, re.DOTALL)
        if character_description_match:
            character_details = character_description_match.group(0).strip()
    
    if character_details:
        character_details = re.sub(r'{{.*?}}', '', character_details)
        character_details = character_details.replace('==', '').strip()
        character_details = re.sub(r'\n+', ' ', character_details)
        character_details = character_details.replace('  ', ' ').strip()
    
    return clean_text(character_details)

def save_character_data(character_name, infobox_dict, character_details, page_url):
    # Ensure faction is a single string, not a list
    faction = clean_text(infobox_dict.get('apfaction', 'Unknown')).replace('[', '').replace(']', '').replace('"', '').strip()

    character_data = {
        "name": character_name,
        "common_names": clean_text(infobox_dict.get('alias', 'Unknown')),
        "faction": faction,  # Ensure this is a string
        "lineage": clean_text(infobox_dict.get('lineage', 'Unknown')),
        "rivals": "Unknown",
        "height": clean_text(infobox_dict.get('height', 'Unknown')),
        "hair_color": clean_text(infobox_dict.get('haircolor', 'Unknown')),
        "eye_color": clean_text(infobox_dict.get('eyecolor', 'Unknown')),
        "first_appearance": clean_text(infobox_dict.get('debut', 'Unknown')),
        "character_details": character_details or 'No character details available.',
        "page_link": page_url  # Adding the page link to the saved data
    }
    
    # Sanitize the character name before using it as a filename
    filename = f"{sanitize_filename(character_name)}.json"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(character_data, f, ensure_ascii=False, indent=4)

def main():
    character_links = get_character_links_from_file() or get_character_links_from_web()
    
    print(f"Found {len(character_links)} characters. Starting data extraction...")
    
    for character_name, url in character_links:
        print(f"Fetching details for '{character_name}'...")
        api_url_with_tan, api_url_without_tan = construct_api_urls(character_name)
        title, content = fetch_content(api_url_with_tan, api_url_without_tan)
        
        if content:
            infobox_dict = parse_infobox(content)
            character_details = parse_character_details(content)
            page_url = f"https://www.ostan-collections.net/wiki/{character_name.replace(' ', '_')}"
            save_character_data(character_name, infobox_dict, character_details, page_url)
            print(f"Saved data for '{character_name}'")
        else:
            print(f"No data found for '{character_name}'")

if __name__ == "__main__":
    main()
