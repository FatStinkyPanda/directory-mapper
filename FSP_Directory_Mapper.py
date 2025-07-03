#!/usr/bin/env python3
import os
import sys
import subprocess
import datetime

def check_and_install_dependencies():
    """Check if required packages are installed, and install them if needed."""
    # Currently using only built-in modules, but this function allows for
    # future expansion if external dependencies are added
    required_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing required package: {package}")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"Successfully installed {package}")
            except subprocess.CalledProcessError:
                print(f"Failed to install {package}. Please install it manually.")
                sys.exit(1)

def format_size(size):
    """Format size in a human-readable way."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0 or unit == 'TB':
            break
        size /= 1024.0
    return f"{size:.2f} {unit}"

def should_ignore(name, current_script, output_file):
    """Check if a file should be ignored."""
    # Only ignore the script itself and the output file
    return name == current_script or name == output_file

def get_file_icon_mapping():
    """Get a mapping of file extensions to icons."""
    return {
        '.py': '🐍',    # Python
        '.js': '📜',    # JavaScript
        '.html': '🌐',  # HTML
        '.css': '🎨',   # CSS
        '.json': '📋',  # JSON
        '.md': '📝',    # Markdown
        '.txt': '📄',   # Text
        '.pdf': '📑',   # PDF
        '.jpg': '🖼️',   # Image
        '.jpeg': '🖼️',  # Image
        '.png': '🖼️',   # Image
        '.gif': '🖼️',   # Image
        '.svg': '🖼️',   # Image
        '.mp3': '🎵',   # Audio
        '.mp4': '🎬',   # Video
        '.zip': '📦',   # Archive
        '.tar': '📦',   # Archive
        '.gz': '📦',    # Archive
        '.rar': '📦',   # Archive
        '.7z': '📦',    # Archive
        '.doc': '📃',   # Document
        '.docx': '📃',  # Document
        '.xls': '📊',   # Spreadsheet
        '.xlsx': '📊',  # Spreadsheet
        '.ppt': '📽️',   # Presentation
        '.pptx': '📽️',  # Presentation
        '.sh': '⚙️',    # Shell script
        '.bat': '⚙️',   # Batch script
        '.exe': '⚙️',   # Executable
        '.dll': '🔌',   # Library
        '.so': '🔌',    # Library
        '.h': '📚',     # Header
        '.c': '📚',     # C source
        '.cpp': '📚',   # C++ source
        '.java': '☕',  # Java
        '.class': '☕', # Java class
        '.rb': '💎',    # Ruby
        '.php': '🐘',   # PHP
        '.sql': '🗄️',   # SQL
        '.db': '🗄️',    # Database
        '.xml': '📰',   # XML
        '.yml': '📰',   # YAML
        '.yaml': '📰',  # YAML
        '.toml': '📰',  # TOML
        '.ini': '⚙️',   # INI configuration
        '.cfg': '⚙️',   # Configuration
        '.conf': '⚙️',  # Configuration
        '.log': '📜',   # Log
    }

def get_file_icon(filename):
    """Get an appropriate icon for the file based on its extension."""
    extension = os.path.splitext(filename)[1].lower()
    return get_file_icon_mapping().get(extension, '📄')  # Default to generic file icon

def generate_icon_legend():
    """Generate a legend for the file type icons."""
    icon_mapping = get_file_icon_mapping()
    
    # Group by icon
    icon_groups = {}
    for ext, icon in icon_mapping.items():
        if icon not in icon_groups:
            icon_groups[icon] = []
        icon_groups[icon].append(ext)
    
    # Create the legend
    legend = ["## Icon Legend", ""]
    
    # Add directory icon
    legend.append("📁 - Directory")
    
    # Add file icons
    for icon, extensions in sorted(icon_groups.items()):
        # Sort extensions and format them
        exts = sorted(extensions)
        if len(exts) > 5:
            # If there are many extensions, show a few and then "etc."
            ext_display = ", ".join(exts[:5]) + ", etc."
        else:
            ext_display = ", ".join(exts)
        
        legend.append(f"{icon} - {ext_display}")
    
    return legend

def generate_directory_tree(start_path, current_script, output_file):
    """Generate a nicely formatted directory tree."""
    lines = []
    start_path = os.path.abspath(start_path)
    root_name = os.path.basename(start_path)
    
    # Start with the root directory
    lines.append(f"📁 **{root_name}/**")
    
    # Store directory structure for easier processing
    structure = {}
    
    # Use os.walk to traverse the directory tree
    for root, dirs, files in os.walk(start_path):
        # Calculate relative path from start_path
        relative_path = os.path.relpath(root, start_path)
        if relative_path == '.':
            relative_path = ''
        
        # Filter files (only ignore the script itself and the output file)
        filtered_files = [f for f in files if not should_ignore(f, current_script, output_file)]
        
        # Store directories and files at this level
        structure[relative_path] = {
            'dirs': sorted(dirs),
            'files': sorted(filtered_files)
        }
    
    # Function to recursively print the tree
    def print_tree(path, prefix=""):
        data = structure.get(path, {'dirs': [], 'files': []})
        dirs = data['dirs']
        files = data['files']
        
        # Process all items (dirs first, then files)
        all_items = [(d, True) for d in dirs] + [(f, False) for f in files]
        
        for i, (name, is_dir) in enumerate(all_items):
            is_last = (i == len(all_items) - 1)
            
            # Determine the connector and next prefix
            if is_last:
                connector = "└── "
                next_prefix = prefix + "    "
            else:
                connector = "├── "
                next_prefix = prefix + "│   "
            
            # Create the full path for this item
            full_path = os.path.join(start_path, path, name)
            
            # Add the item to the tree
            if is_dir:
                lines.append(f"{prefix}{connector}📁 **{name}/**")
                
                # Recursively process this directory
                new_path = os.path.join(path, name) if path else name
                print_tree(new_path, next_prefix)
            else:
                # Get file information
                try:
                    stats = os.stat(full_path)
                    size = format_size(stats.st_size)
                    modified = datetime.datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
                    
                    # Get file extension
                    name_without_ext, ext = os.path.splitext(name)
                    if ext:
                        formatted_name = f"{name_without_ext}`{ext}`"
                    else:
                        formatted_name = name
                    
                    # Get icon for file type
                    icon = get_file_icon(name)
                    
                    lines.append(f"{prefix}{connector}{icon} {formatted_name} ({size}, {modified})")
                except (FileNotFoundError, PermissionError):
                    lines.append(f"{prefix}{connector}📄 {name} (unavailable)")
    
    # Start the recursive tree printing from the root
    print_tree('')
    
    return lines

def generate_directory_markdown(output_file="Project_Directory.md"):
    """Generate a markdown file with the directory structure."""
    current_dir = os.getcwd()
    parent_dir_name = os.path.basename(current_dir)
    
    # Get the actual script filename - handle potential naming discrepancies
    current_script = os.path.basename(sys.argv[0])
    print(f"Script filename detected as: {current_script}")
    
    # Start with a header
    content = f"# Project Directory: {parent_dir_name}\n\n"
    content += f"Directory structure generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    # Add some statistics
    file_count = 0
    dir_count = 0
    total_size = 0
    
    for root, dirs, files in os.walk(current_dir):
        # Count all files except the script itself and the output file
        file_count += sum(1 for f in files if not should_ignore(f, current_script, output_file))
        dir_count += len(dirs)
        
        for file in files:
            if not should_ignore(file, current_script, output_file):
                try:
                    total_size += os.path.getsize(os.path.join(root, file))
                except (FileNotFoundError, PermissionError):
                    pass
    
    content += f"* Total files: {file_count}\n"
    content += f"* Total directories: {dir_count}\n"
    content += f"* Total size: {format_size(total_size)}\n\n"
    
    content += "```\n"
    
    # Generate the tree structure
    tree = generate_directory_tree(current_dir, current_script, output_file)
    content += "\n".join(tree)
    
    content += "\n```\n\n"
    
    # Add icon legend
    content += "\n".join(generate_icon_legend())
    
    # Write the content to the output file - using UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Directory structure has been written to {output_file}")

def main():
    """Main function to run the script."""
    check_and_install_dependencies()
    generate_directory_markdown()

if __name__ == "__main__":
    main()