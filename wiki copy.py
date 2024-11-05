import requests
from discord import Embed
import re

def clean_text(text):
    """Convert bracketed wiki links to plain text and clean up extra spaces."""
    text = re.sub(r'\[\[(.*?)\|(.*?)\]\]', r'\2', text) 
    text = re.sub(r'\[\[(.*?)\]\]', r'\1', text)
    text = re.sub(r'{{.*?}}', '', text)  
    text = re.sub(r'http[^ ]*', '', text)  
    text = text.replace('==', '').strip() 
    text = ' '.join(text.split())  
    return text

async def execute(client, message):
    command_prefix = '&wiki'  
    command_pattern = rf'{re.escape(command_prefix)} "(.+?)"'
    
    if not re.search(command_pattern, message.content):
        await message.channel.send('Please use quotation marks around the character\'s name, e.g., `!wiki "Windows 95-tan"`')
        return
    
    query = re.search(command_pattern, message.content).group(1)
    query_with_tan = query.replace(' ', '_')
    query_without_tan = query.replace('-tan', '').replace(' ', '_')
    
    print(f'Query with -tan: {query_with_tan}') 
    await message.channel.send(f'Fetching details for "{query_with_tan}"...')  
    
    api_url_with_tan = f'https://www.ostan-collections.net/wiki/api.php?action=query&format=json&titles={query_with_tan}&prop=revisions&rvprop=content'
    api_url_without_tan = f'https://www.ostan-collections.net/wiki/api.php?action=query&format=json&titles={query_without_tan}&prop=revisions&rvprop=content'
    
    print(f'API URL (with -tan): {api_url_with_tan}')
    print(f'API URL (without -tan): {api_url_without_tan}')
    
    response = requests.get(api_url_with_tan)
    print(f'Response status (with -tan): {response.status_code}')  
    data = response.json()
    print(f'Response data (with -tan): {data}') 
    
    pages = data['query']['pages']
    page = next(iter(pages.values()))
    
    if 'revisions' in page:
        title = page['title']
        content = page['revisions'][0]['*']
    else:
        response = requests.get(api_url_without_tan)
        print(f'Response status (without -tan): {response.status_code}')  
        data = response.json()
        print(f'Response data (without -tan): {data}')  
        
        pages = data['query']['pages']
        page = next(iter(pages.values()))
        
        if 'revisions' in page:
            title = page['title']
            content = page['revisions'][0]['*']
        else:
            await message.channel.send(f"No results found for '{query}'.")
            return
    
    page_url = f'https://www.ostan-collections.net/wiki/index.php/{title.replace(" ", "_")}'
    
    infobox_match = re.search(r'{{OSinfobox(.*?)}}', content, re.DOTALL)
    if infobox_match:
        infobox_content = infobox_match.group(1)
        infobox_lines = [line.strip() for line in infobox_content.split('|') if '=' in line]
        infobox_dict = {line.split('=')[0].strip(): line.split('=')[1].strip() for line in infobox_lines}
    else:
        infobox_dict = {}
    
    character_details = None
    character_section_match = re.search(r'==Character details==([\s\S]*?)(?=\n==|$)', content, re.DOTALL)
    if character_section_match:
        character_details = character_section_match.group(1).strip()
    else:
        character_description_match = re.search(r'(?<=}})([\s\S]*?)(?=\n==Technical details==|\n==See also==|\n\[\[Category:|\n?$)', content, re.DOTALL)
        if character_description_match:
            character_details = character_description_match.group(0).strip()
        else:
            old_infobox_match = re.search(r'\{\|(.*?)\|\}', content, re.DOTALL)
            if old_infobox_match:
                old_infobox_content = old_infobox_match.group(1)
                character_details = old_infobox_content.strip()
    
    if character_details:
        character_details = clean_text(character_details)
    
    character_data = {
        "name": title,
        "debut": clean_text(infobox_dict.get('debut', 'Unknown')),
        "hair_color": clean_text(infobox_dict.get('haircolor', 'Unknown')),
        "eye_color": clean_text(infobox_dict.get('eyecolor', 'Unknown')),
        "character_details": character_details or 'No character details available.'
    }
    
    embed = Embed(
        title=character_data["name"],
        url=page_url,
        description=(
            f"**Debut:** {character_data['debut']}\n"
            f"**Hair color:** {character_data['hair_color']}\n"
            f"**Eye color:** {character_data['eye_color']}\n"
        ),
        color=0x0099FF
    )
    
    if "image" in infobox_dict:
        avatar_url = f'https://www.ostan-collections.net/wiki/images/{infobox_dict["image"]}'
        embed.set_thumbnail(url=avatar_url)
    
    if character_data["character_details"]:
        embed.add_field(name='Character Details', value=character_data["character_details"], inline=False)
    else:
        embed.add_field(name='Character Details', value="No character details available.", inline=False)
    
    embed.set_footer(text='Fetched from OS-tan Collections')
    await message.channel.send(embed=embed)
