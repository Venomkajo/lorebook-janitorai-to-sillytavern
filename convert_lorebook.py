import json
import os

def convert_array_to_dict(lorebook_array, lorebook_name, description):

    entries = {}
    original_entries = []

    for i, entry in enumerate(lorebook_array):

        lorebook_entry = {
            "key": entry.get("key", []),
            "keysecondary": entry.get("keysecondary", []),
            "comment": entry.get("name", ""),
            "content": entry.get("content", ""),
            "vectorized": entry.get("vectorized", False),
            "selective": entry.get("selective", False),
            "selectiveLogic": entry.get("selectiveLogic", 0),
            "addMemo": entry.get("extensions", {}).get("addMemo", True),
            "order": entry.get("insertion_order", 100),
            "position": entry.get("position", 1),
            "disable": not entry.get("enabled", True),
            "ignoreBudget": entry.get("ignoreBudget", False),
            "excludeRecursion": entry.get("extensions", {}).get("excludeRecursion", False),
            "preventRecursion": False,
            "matchPersonaDescription": False,
            "matchCharacterDescription": False,
            "matchCharacterPersonality": False,
            "matchCharacterDepthPrompt": False,
            "matchScenario": False,
            "matchCreatorNotes": False,
            "delayUntilRecursion": False,
            "probability": entry.get("probability", 100),
            "useProbability": entry.get("extensions", {}).get("useProbability", False),
            "depth": entry.get("depth", 4),
            "outletName": "",
            "group": "",
            "groupOverride": False,
            "groupWeight": entry.get("groupWeight", 100),
            "scanDepth": None,
            "caseSensitive": None,
            "matchWholeWords": entry.get("matchWholeWords", None),
            "useGroupScoring": None,
            "automationId": "",
            "role": None,
            "sticky": None,
            "cooldown": None,
            "delay": None,
            "triggers": [],
            "uid": i + 1,
            "displayIndex": i,
            "extensions": {
                "depth": entry.get("extensions", {}).get("depth", 4),
                "linked": False,
                "weight": entry.get("extensions", {}).get("weight", 10),
                "addMemo": entry.get("extensions", {}).get("addMemo", True),
                "embedded": True,
                "probability": entry.get("extensions", {}).get("probability", 100),
                "displayIndex": i,
                "selectiveLogic": entry.get("extensions", {}).get("selectiveLogic", 0),
                "useProbability": entry.get("extensions", {}).get("useProbability", True),
                "characterFilter": entry.get("extensions", {}).get("characterFilter", None),
                "excludeRecursion": entry.get("extensions", {}).get("excludeRecursion", True)
            },
            "characterFilter": {
                "isExclude": False,
                "names": [],
                "tags": []
            }
        }

        original_entry = {
            "name": entry.get("name", f"Entry {i + 1}"),
            "keys": entry.get("key", []),
            "secondary_keys": entry.get("keysecondary", []),
            "content": entry.get("content", ""),
            "enabled": entry.get("enabled", True),
            "insertion_order": entry.get("insertion_order", 100),
            "case_sensitive": entry.get("case_sensitive", False),
            "priority": entry.get("priority", 100),
            "id": i + 1,
            "comment": entry.get("comment", ""),
            "selective": entry.get("selective", False),
            "constant": entry.get("constant", False),
            "position": "",
            "extensions": entry.get("extensions", {}),
            "probability": entry.get("probability", 100),
            "selectiveLogic": entry.get("selectiveLogic", 0)
        }

        entries[i + 1] = lorebook_entry
        original_entries.append(original_entry)

    result = {
        "entries": entries,
        "originalData": {
            "name": lorebook_name,
            "description": description,
            "scan_depth": 8,
            "token_budget": 1000,
            "recursive_scanning": True,
            "extensions": {},
            "entries": original_entries
        }
    }

    return result

def main():
    while True:
        lorebook_name = input("Enter the name of the lorebook: ")
        if not lorebook_name:
            lorebook_name = "Name not provided."

        description = input("Enter a description for the lorebook: ")
        if not description:
            description = "Description not provided."

        while True:
            lorebook_file = input("Enter the filename of the lorebook (e.g., janitor.json): ")

            if os.path.isfile(lorebook_file):
                break
            else:
                print("File not found. Please enter a valid filename. Ctrl + C to exit.")

        lorebook_data = {}

        with open(lorebook_file, "r") as f:
            lorebook_data = json.load(f)

        converted_lorebook = convert_array_to_dict(lorebook_data, lorebook_name, description)

        with open(f"{lorebook_name}.json", "w") as f:
            json.dump(converted_lorebook, f, indent=4)

        print(f"Lorebook converted and saved as {lorebook_name}.json")

        if input("Do you want to convert another lorebook? (y/n): ").lower() != "y":
            break

if __name__ == "__main__":
    main()