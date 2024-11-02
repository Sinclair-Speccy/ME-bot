import json
import os

# Define the directory to save JSON files
output_directory = r"D:\Code\ME-bot\characters"

# List of Windows character names and their page links
characters = [
    {"name": "Windows 1.0-tan", "page_link": "https://www.ostan-collections.net/wiki/index.php/OSC_Windows_1.0"},
    {"name": "Windows 1.0 Futaba", "page_link": "https://www.ostan-collections.net/wiki/index.php/Oichi-san"},  # Updated link
    {"name": "Windows 2.0", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_2.0"},
    {"name": "Windows 3.1", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_3.1"},
    {"name": "Windows 3.2", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_3.2"},
    {"name": "Windows NT", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_NT"},
    {"name": "Windows 95", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_95"},
    {"name": "Windows 95 OSR 2.1", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_95_OSR_2.1"},
    {"name": "Windows 95 OSR 2.5", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_95_OSR_2.5"},
    {"name": "Windows CE", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_CE"},
    {"name": "Windows NT Workstation", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_NT_Workstation"},
    {"name": "Windows 97", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_97"},
    {"name": "Windows 98", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_98"},
    {"name": "Windows 98SE", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_98SE"},
    {"name": "Windows Neptune", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_Neptune"},
    {"name": "Windows Odyssey", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_Odyssey"},
    {"name": "Windows ME", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_ME"},
    {"name": "Windows 2000", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_2000"},
    {"name": "Nyaake", "page_link": "https://www.ostan-collections.net/wiki/index.php/Nyaake"},
    {"name": "Windows XP Pro", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_XP_Pro"},
    {"name": "Windows XP Homeko", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_XP_Homeko"},
    {"name": "Windows XP Media Center Edition", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_XP_Media_Center_Edition"},
    {"name": "Windows 2003 Server", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_2003_Server"},
    {"name": "Windows Vista", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_Vista"},
    {"name": "Windows 2008 Server", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_2008_Server"},
    {"name": "Windows 7", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_7"},
    {"name": "Windows 8", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_8"},
    {"name": "Windows 10", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_10"},
    {"name": "Microsoft Silverlight", "page_link": "https://www.ostan-collections.net/wiki/index.php/Microsoft_Silverlight"},
    {"name": "Windows Azure", "page_link": "https://www.ostan-collections.net/wiki/index.php/Windows_Azure"},
]

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Generate JSON files
for character in characters:
    character_data = {
        "name": character["name"],
        "common_names": character["name"],
        "faction": "Unknown",  # Placeholder, update as necessary
        "lineage": "Unknown",  # Placeholder, update as necessary
        "rivals": "Unknown",  # Placeholder, update as necessary
        "height": "Unknown",  # Placeholder, update as necessary
        "hair_color": "Unknown",  # Placeholder, update as necessary
        "eye_color": "Unknown",  # Placeholder, update as necessary
        "first_appearance": "Unknown",  # Placeholder, update as necessary
        "character_details": "No character details available.",
        "page_link": character["page_link"]
    }

    # Create the file name
    file_name = f"{character['name'].replace(' ', '_')}.json"
    file_path = os.path.join(output_directory, file_name)

    # Write the JSON data to a file
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(character_data, json_file, ensure_ascii=False, indent=4)

    print(f"Created: {file_path}")