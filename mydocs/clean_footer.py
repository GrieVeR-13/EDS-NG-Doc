import os
import glob
from bs4 import BeautifulSoup

site_dir = "site"

def clean_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    copyright_div = soup.find("div", class_="md-copyright")
    if copyright_div:
        copyright_div.decompose()
        print(f"Removed footer from {file_path}")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(soup))

html_files = glob.glob(os.path.join(site_dir, "**", "*.html"), recursive=True)

for html_file in html_files:
    clean_html_file(html_file)

print("Finished cleaning HTML files.")