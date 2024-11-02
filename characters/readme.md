# Characters Folder

This folder contains character data used by the OS-tan Discord Bot. It consists of two main components: the `character_aliases.json` file which is used for storing every character and their alias and individual character JSON files. These files provide the necessary information for users to search and retrieve details about various OS-tan characters.

## character_aliases.json

The `character_aliases.json` file serves as a reference for searching characters within the bot. Each entry maps a primary character name to its various aliases and specifies the corresponding character JSON file. This is for accommodating different naming conventions used by the community.

### Example Structure

Here is a sample structure of the `character_aliases.json` file:

```json
{
    "OSC Windows 1.0": {
        "aliases": ["Windows 1.0", "OSC Windows 1.0", "Windows_1.0_OSC", "Windows 1.0-tan", "1.0-tan"],
        "character_file": "OSC_Windows_1.0.json"
    },
    "Futaba Windows 1.0": {
        "aliases": ["Windows 1.0", "Futaba Windows 1.0", "Oichi-san", "Windows 1.0 Futaba", "Futaba 1.0", "Windows 1.0-tan", "1.0-tan", "お壱さん"],
        "character_file": "Futaba_Windows_1.0.json"
    },
```
For OSes, software or hardware that have more than one character, the main alias **must** come first as shown in the example for Windows 1.0.

### Key Components

- **Primary Name**: The main identifier for the character (e.g., "OSC Windows 1.0"). This is for when the bot detects there is more than one character and has prompt the user to pick which one they want.
- **Aliases**: An array of alternative names that the character is known by (e.g., "Windows 1.0", "Windows 1.0-tan").
- **character_file**: The filename of the corresponding character JSON file (e.g., "OSC_Windows_1.0.json").

This structure allows users to search for characters who may go by different names and still brings up the right character json file. It must be used for when submitting a new character via a pull request.


## Character JSON Files

Each character has a dedicated JSON file that contains information about the character. This file is used for the embeds after a user searches for a character and must be used for when submitting a new character via a pull request.

### Example Structure

Here’s an example of what a character JSON file looks like:

```json
{
    "name": "Oichi-san",
    "common_names": "Oichi-san",
    "faction": "Windows Family",
    "lineage": "DOS/Win9x",
    "rivals": "Unknown",
    "height": "Not officially listed",
    "hair_color": "Brown",
    "eye_color": "Red or brown",
    "first_appearance": "Unknown",
    "character_details": "Oichi-san has short brown hair adorned with pink flowers, often depicted in traditional Japanese attire. She is characterized as reserved, slow, soft-spoken, and elegant, frequently appearing alongside oobaba-sama.",
    "page_link": "https://www.ostan-collections.net/wiki/index.php/Oichi-san"
}
```

### Key Components

- **name**: The name of the character. This will show up as a link in the embed to the character's page on the wiki.
- **common_names**: Alternate names used to refer to the character.
- **faction**: The character's faction or group association (e.g., "Windows Family").
- **lineage**: The lineage or historical context of the character (e.g., "DOS/Win9x").
- **rivals**: Notable rivals or adversaries of the character.
- **height**: The character's height (if available).
- **hair_color**: The color of the character's hair.
- **eye_color**: The color of the character's eyes.
- **first_appearance**: The character's first appearance in media or community. This is not always required.
- **character_details**: A brief description of the character's personality, traits, and notable features.
- **page_link**: A link to the character's wiki page for more detailed information. See "name" for an explanation.
