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

    # Create a more visually appealing progress badge URL
    badge_url = f"![Progress Badge](https://img.shields.io/static/v1?label=Challenge&message={progress}%25%20Complete&color=4c1&style=for-the-badge&logo=github&logoColor=white)"

    # Insert the progress badge
    readme = readme.replace('<progress-placeholder>', badge_url)

    with open('README.md', 'w') as file:
        file.write(readme)

if __name__ == "__main__":
    progress = calculate_progress()
    update_readme(progress)



# import requests
# from pybadges import badge
# import matplotlib.pyplot as plt

# def calculate_progress(owner, token):
#     # Example: Fetch progress data (modify as needed for your repo logic)
#     url = f"https://api.github.com/repos/{owner}/YOUR_REPO_NAME"
#     headers = {"Authorization": f"token {token}"}
#     response = requests.get(url, headers=headers).json()
    
#     total_tasks = 100  # Replace with actual logic
#     completed_tasks = response.get("open_issues", 0)  # Example metric

#     progress = (completed_tasks / total_tasks) * 100
#     return progress

# def generate_badge(progress, output_path):
#     # Generate a stylish SVG badge
#     color = "red" if progress < 50 else "orange" if progress < 75 else "green"
#     badge_svg = badge(left_text="Progress", right_text=f"{progress:.2f}%", right_color=color)
    
#     with open(output_path, "w") as f:
#         f.write(badge_svg)

# def generate_graph(progress, output_path):
#     # Create a simple progress chart
#     plt.figure(figsize=(6, 1))
#     plt.barh(["Progress"], [progress], color="skyblue", height=0.5)
#     plt.xlim(0, 100)
#     plt.xlabel("Percentage")
#     plt.title("Project Progress")
#     plt.tight_layout()
#     plt.savefig(output_path)

# if __name__ == "__main__":
#     import argparse
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--owner", required=True)
#     parser.add_argument("--token", required=True)
#     parser.add_argument("--readme-path", required=True)
#     parser.add_argument("--badge-path", required=True)
#     args = parser.parse_args()

#     progress = calculate_progress(args.owner, args.token)
#     generate_badge(progress, args.badge_path)
#     generate_graph(progress, "progress_graph.png")

#     # Update the README with badge and graph
#     with open(args.readme_path, "r+") as f:
#         readme = f.read()
#         f.seek(0)
#         badge_md = f'![Progress](progress.svg)\n![Graph](progress_graph.png)\n'
#         updated_readme = badge_md + readme
#         f.write(updated_readme)
#         f.truncate()
