import subprocess

subprocess.run(
    ["python", "scripts/generate_tags.py"]
)

subprocess.run(
    ["python", "scripts/generate_books.py"]
)

subprocess.run(
    ["python", "scripts/generate_home.py"]
)

subprocess.run(
    ["python", "scripts/generate_stats.py"]
)

print("Afriknomics Build OK")