from pathlib import Path
import urllib.request

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

FILES = {
    "Traffic_Crashes_-_People_20260428.csv":
    "https://uofi.box.com/shared/static/bksbuwoh1lm8ynk0uphus87dpeqguvtw.csv",

    "Traffic_Crashes_-_Crashes_20260428.csv":
    "https://uofi.box.com/shared/static/hg4teekmboyne215qad782ls2jlxagrl.csv"
}

def download_file(filename, url):
    output_path = DATA_DIR / filename

    if output_path.exists():
        print(f"{filename} already exists. Skipping download.")
        return

    print(f"Downloading {filename}...")
    urllib.request.urlretrieve(url, output_path)
    print(f"Saved to {output_path}\n")

def main():
    for filename, url in FILES.items():
        download_file(filename, url)

    print("Data acquisition completed successfully.")

if __name__ == "__main__":
    main()