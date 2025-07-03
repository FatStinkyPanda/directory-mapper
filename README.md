# FSP Directory Mapper

A high-quality Python utility that generates beautiful Markdown documentation of your project's directory structure.

[GitHub](https://img.shields.io/github/license/fatstinkypanda/FSP-directory-mapper)
[Python](https://img.shields.io/badge/python-3.6+-blue.svg)

## Overview

FSP Directory Mapper creates a comprehensive visual representation of your project's file structure in a well-formatted Markdown document. It's perfect for project documentation, READMEs, wikis, and giving collaborators a quick overview of your codebase organization.

Developed by [FatStinkyPanda](https://github.com/fatstinkypanda)

## Features

- 📂 Creates a beautiful directory tree visualization in Markdown
- 🔍 Automatically detects file types with appropriate icons
- 📊 Includes file sizes and modification timestamps
- 📝 Generates project statistics (file count, directory count, total size)
- 🧩 Includes a comprehensive icon legend for file types
- 🛠️ Simple to use - just run and get instant documentation
- 🔄 Automatically updates - overwrites previous versions
- 🚀 No external dependencies - uses only Python standard library

## Installation

Simply download the `FSP_Directory_Mapper.py` file to your project directory:

```bash
# Clone the repository
git clone https://github.com/fatstinkypanda/FSP-directory-mapper.git

# Or download just the script file
curl -O https://raw.githubusercontent.com/fatstinkypanda/FSP-directory-mapper/main/FSP_Directory_Mapper.py
```

## Usage

1. Place the script in the root directory of your project
2. Run the script:

```bash
python FSP_Directory_Mapper.py
```

3. Find the generated `Project_Directory.md` file in the same directory

That's it! The script will create a comprehensive Markdown document of your project structure.

## Example Output

The generated Markdown file will look something like this:

```
# Project Directory: my-awesome-project

Directory structure generated on 2025-07-03 14:30:21

* Total files: 42
* Total directories: 15
* Total size: 4.35 MB

```
📁 **my-awesome-project/**
├── 📁 **assets/**
│   ├── 🖼️ sample`.png` (145.23 KB, 2025-06-28 09:45:32)
│   └── 🎨 styles`.css` (12.45 KB, 2025-06-29 16:22:15)
├── 📁 **src/**
│   ├── 📁 **components/**
│   │   ├── 🐍 button`.py` (4.56 KB, 2025-07-01 12:34:56)
│   │   └── 🐍 input`.py` (3.21 KB, 2025-07-01 14:23:45)
│   └── 🐍 main`.py` (8.76 KB, 2025-07-02 10:11:22)
├── 📝 README`.md` (2.34 KB, 2025-06-25 08:00:12)
└── 📋 config`.json` (1.23 KB, 2025-06-30 11:22:33)
```

## Icon Legend

📁 - Directory
🐍 - .py
🎨 - .css
🖼️ - .jpg, .jpeg, .png, .gif, .svg
📝 - .md
📋 - .json
...
```

## How It Works

FSP Directory Mapper:

1. Walks through your project directory recursively
2. Collects information about files and directories
3. Formats this information into a hierarchical tree structure
4. Adds file details (size, modified date) and appropriate icons
5. Generates project statistics
6. Creates a comprehensive Markdown document

The script is self-contained and only ignores itself and the output file it generates.

## Customization

You can easily customize the script by modifying:

- Output filename: Change the default `"Project_Directory.md"` in the `generate_directory_markdown()` function
- File icons: Add or modify file extension icons in the `get_file_icon_mapping()` function
- Tree formatting: Adjust the tree appearance in the `generate_directory_tree()` function

## Requirements

- Python 3.6+
- No external dependencies

## License

MIT License

## Support

For issues, suggestions, or contributions:

- GitHub: [github.com/fatstinkypanda](https://github.com/fatstinkypanda)
- Email: [support@fatstinkypanda.com](mailto:support@fatstinkypanda.com)

---

Created with ❤️ by [FatStinkyPanda](https://github.com/fatstinkypanda)
