from bs4 import BeautifulSoup
import re


def analyze_terminal():
    try:
        # 1. Read the HTML file
        with open("Cyber Games Terminal.html", "r", encoding="utf-8") as f:
            content = f.read()

        # 2. Extract the script
        soup = BeautifulSoup(content, "html.parser")
        scripts = soup.find_all("script")

        print(f"Found {len(scripts)} script(s).\n")

        for i, script in enumerate(scripts):
            print(f"--- Script {i+1} Content ---")
            if script.string:
                script_content = script.string.strip()
                print(script_content)

                # 3. Simple Check for Password Logic (Optional Helper)
                # Looks for standard comparisons like 'if (password == "XYZ")'
                match = re.search(r'==\s*["\'](.*?)["\']', script_content)
                if match:
                    print(f"\n[POTENTIAL PASSWORD FOUND]: {match.group(1)}")
            else:
                print("(This script tag is empty or links to an external file.)")
            print("------------------------\n")

    except FileNotFoundError:
        print(
            "Error: Could not find 'Cyber Games Terminal.html'. Make sure the file is in the correct folder."
        )


if __name__ == "__main__":
    analyze_terminal()
