import os
import sys
import argparse
from fnmatch import fnmatch

def replace_text(root, search_text, replace_text):
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, "index.html") or fnmatch(name, "thankyou.html"):
                file_path = os.path.join(path, name)
                with open(file_path, 'r+') as file:
                    content = file.read()
                    content = content.replace(search_text, replace_text)
                    file.seek(0)
                    file.write(content)
                    file.truncate()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="Directory to search")
    parser.add_argument("search_text", help="Text to search for")
    parser.add_argument("replace_text", help="Text to replace with")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print("Directory does not exist")
        sys.exit(1)
    else:
        replace_text(args.directory, args.search_text, args.replace_text)
        print("Replacement done.")


def main_loop():
    # create a list of  search strings paired with their replacement strings
    search_replace_list = [
            {
            "directory": "honestabebrunswick",
            "replacement_list": [
                ("904-574-4249", "(912) 333-3512"),
                ("9045744249", "9123333512"),
                ("123-456-7890", "(912) 333-3512"),
                ("1234567890", "9123333512"),
            ]
        },
       {
            "directory": "honestabedaytona",
            "replacement_list": [
                ("904-574-4249", "(386) 387-5665"),
                ("9045744249", "3863875665"),
                ("123-456-7890", "(386) 387-5665"),
                ("1234567890", "3863875665"),
            ]
        }, 
        {
            "directory": "honestabemacon",
            "replacement_list": [
                ("904-574-4249", "(478) 292-2316"),
                ("9045744249", "4782922316"),
                ("123-456-7890", "(478) 292-2316"),
                ("1234567890", "4782922316"),
            ]
        },
        {
            "directory": "honestabevaldosta",
            "replacement_list": [
                ("904-574-4249", "(229) 999-2065"),
                ("9045744249", "2299992065"),
                ("123-456-7890", "(229) 999-2065"),
                ("1234567890", "2299992065"),
            ]
        },
        {
            "directory": "honestabewestpalm",
            "replacement_list": [
                ("904-574-4249", "(561) 677-2921"),
                ("9045744249", "5616772921"),
                ("123-456-7890", "(561) 677-2921"),
                ("1234567890", "5616772921"),
            ]
        },
    ]

    for item in search_replace_list:
        directory = item["directory"]
        for search_text, replacement_text in item["replacement_list"]:
            print("Replacing {} with {} in {}".format(search_text, replacement_text, directory))
            replace_text(directory, search_text, replacement_text)


if __name__ == "__main__":
    main_loop()
