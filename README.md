# Lorebook Format Converter

A simple Python utility for converting lorebook JSON files between different formats used by various AI roleplay frontends. Mainly designed to convert from JanitorAI format to SillyTavern format.

## Features

- Converts array-based lorebook format to a dictionary-based format with preserved original data
- Interactive CLI with validation
- Batch processing support via continuous operation

## Requirements

- Python

## Usage

Run the script:

```bash
python convert_lorebook.py
```

Follow the prompts:

1. Enter a name for your lorebook (or press Enter for default)
2. Enter a description (or press Enter for default)
3. Enter the filename of the lorebook to convert (must exist in current directory)
4. The converted file will be saved as`{lorebook_name}.json`