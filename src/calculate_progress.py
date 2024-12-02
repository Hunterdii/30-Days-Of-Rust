import json
import sys

def calculate_progress():
    # Read the progress data (adjust path as needed)
    with open("progress.json", "r") as f:
        data = json.load(f)

    total_days = data.get('total_days', 30)  # Default to 30 if missing
    completed_days = data.get('completed_days', 0)

    # Calculate progress
    progress = (completed_days * 100) // total_days
    return progress

def update_readme(progress):
    with open('README.md', 'r') as file:
        readme = file.read()

    # Create the progress badge URL
    badge_url = f"![Progress Badge](https://img.shields.io/static/v1?label=Challenge&message={progress}%25%20Complete&color=brightgreen&style=flat-square)"

    # Insert the progress badge
    readme = readme.replace('<progress-placeholder>', badge_url)

    with open('README.md', 'w') as file:
        file.write(readme)

if __name__ == "__main__":
    progress = calculate_progress()
    update_readme(progress)
