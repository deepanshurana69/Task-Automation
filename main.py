from pathlib import Path
import re
import shutil


def move_jpg_files():
    source = Path(input("Enter source folder: ").strip()).expanduser()
    destination = Path(input("Enter destination folder: ").strip()).expanduser()

    if not source.is_dir():
        print("Source folder does not exist.")
        return

    destination.mkdir(parents=True, exist_ok=True)
    moved = 0

    for file in source.iterdir():
        if file.is_file() and file.suffix.lower() == ".jpg":
            target = destination / file.name
            if target.exists():
                print(f"Skipped (already exists): {file.name}")
                continue
            shutil.move(str(file), str(target))
            moved += 1

    print(f"Moved {moved} JPG file(s).")


def extract_email_addresses():
    source = Path(input("Enter the input .txt file path: ").strip()).expanduser()
    destination = Path(input("Enter the output file path: ").strip()).expanduser()

    if not source.is_file():
        print("Input file does not exist.")
        return

    text = source.read_text(encoding="utf-8")
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)))

    destination.write_text("\n".join(emails), encoding="utf-8")
    print(f"Found {len(emails)} unique email address(es).")
    print(f"Saved to: {destination}")


def main():
    print("\n=== CodeAlpha Task Automation ===")
    print("1. Move JPG files")
    print("2. Extract email addresses")

    choice = input("Choose an automation (1/2): ").strip()

    if choice == "1":
        move_jpg_files()
    elif choice == "2":
        extract_email_addresses()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
