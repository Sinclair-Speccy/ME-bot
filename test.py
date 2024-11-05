import json
import os

# Define file paths
character_dir = r'D:\Code\ME-bot\characters'
aliases_file = os.path.join(character_dir, 'character_aliases.json')
fixed_aliases_file = os.path.join(character_dir, 'fixed_character_aliases.json')

def load_aliases(file_path):
    """Load character aliases from the JSON file with UTF-8 encoding."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def test_aliases(aliases_data):
    """Test each alias to ensure it maps to the correct character file."""
    results = {
        "passed": [],
        "failed": [],
        "fixed": {}
    }

    # Go through each character and its aliases
    for character_name, character_info in aliases_data.items():
        expected_file = character_info['character_file']
        for alias in character_info['aliases']:
            # Check if alias maps to the correct file
            matching_entry = next(
                (entry for entry, info in aliases_data.items() if alias in info['aliases']),
                None
            )
            
            # Verify that the alias returns the correct character file
            if matching_entry and aliases_data[matching_entry]['character_file'] == expected_file:
                results["passed"].append((alias, expected_file))
            else:
                results["failed"].append((alias, expected_file))
                # Record the alias under the correct character for fixing
                results["fixed"].setdefault(character_name, {
                    "aliases": [],
                    "character_file": expected_file
                })
                results["fixed"][character_name]["aliases"].append(alias)

    return results

def save_fixed_aliases(fixed_data, file_path):
    """Save fixed aliases to a JSON file with UTF-8 encoding, ensuring non-ASCII characters are preserved."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(fixed_data, f, indent=4, ensure_ascii=False)
    print(f"Fixed aliases saved to {file_path}")

def print_test_results(results):
    """Print the results of the alias test."""
    print("\n=== Test Results ===")
    print(f"Passed tests: {len(results['passed'])}")
    for alias, file in results['passed']:
        print(f"✔️ Alias '{alias}' correctly maps to '{file}'")
    
    print(f"\nFailed tests: {len(results['failed'])}")
    for alias, file in results['failed']:
        print(f"❌ Alias '{alias}' did NOT map to '{file}'")

if __name__ == "__main__":
    # Load the character aliases data
    aliases_data = load_aliases(aliases_file)

    # Run the tests
    results = test_aliases(aliases_data)

    # Print results
    print_test_results(results)

    # Save fixed aliases if there are any failed cases
    if results["failed"]:
        save_fixed_aliases(results["fixed"], fixed_aliases_file)
