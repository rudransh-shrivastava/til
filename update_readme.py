import os

# List of directory names.
# Why? because otherwise python includes hidden directories.
whitelisted_dir = ["Vim"]
whitelisted_dir.sort()

# Initialize the README content and add some info.
readme_content = """\
# Today I Learned (TIL)

This repo is a collection of short articles about the things I learn everyday.
TILs are short Markdown notes that contain a few sentences + example code, they're too short for a blog.
I stole this idea from [jwworth/til/](https://github.com/jwworth/til/), who stole that idea from [jbranchaud/til](https://github.com/jbranchaud/til/), who shamelessly stole that idea from [thoughtbot/til](https://github.com/thoughtbot/til).

---

## Categories
"""

# Function that returns headings by replacing spaces with "-".


def space_to_hyphen(name):
    return f"* [{name}](#{name.lower().replace(' ', '-')})\n"

# Function that returns the [Directory Name](Directory%20Name/File%20Name.md) format.


def generate_link(category, name):
    clean_name = name.replace('.md', '').replace('-', ' ')
    directory_url = category.replace(' ', '%20')
    file_url = name.replace(' ', '%20')
    return f"  * [{clean_name}]({directory_url}/{file_url})\n"

# Function that returns the headings in ### Heading format.


def generate_heading(name):
    return f"### {name}\n"


# Traverse through folders and gather TILs
for root, dirs, files in os.walk("."):
    dirs.sort()
    for dir_name in dirs:
        if dir_name in whitelisted_dir:
            heading_entry = space_to_hyphen(dir_name)
            readme_content += heading_entry

# Add a line break
readme_content += "\n---\n\n"

# Append category headings and TIL file entries
for category_name in whitelisted_dir:
    readme_content += generate_heading(category_name)
    directory_path = os.path.join(".", category_name)
    file_list = os.listdir(directory_path)
    file_list.sort()
    for file_name in file_list:
        if file_name.endswith(".md"):
            til_entry = generate_link(category_name, file_name)
            readme_content += til_entry

# Add a line break
readme_content += "\n---\n"

# Add the License information
readme_content += """
### License

This repository is licensed under the [MIT License](http://www.opensource.org/licenses/MIT).
"""

# Write the updated README content to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
