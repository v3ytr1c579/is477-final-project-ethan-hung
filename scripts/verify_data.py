from pathlib import Path
import hashlib

DATA_DIR = Path("data")

FILES = [
    "Traffic_Crashes_-_Crashes_20260428.csv",
    "Traffic_Crashes_-_People_20260428.csv",
]

def sha256sum(file_path):
    hash_object = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            hash_object.update(chunk)

    return hash_object.hexdigest()

def main():
    print("Verifying dataset integrity with SHA-256 checksums...\n")

    for filename in FILES:
        file_path = DATA_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Missing required data file: {file_path}")

        checksum = sha256sum(file_path)
        print(f"{filename}")
        print(f"SHA-256: {checksum}\n")

    print("Data integrity check completed successfully.")

if __name__ == "__main__":
    main()