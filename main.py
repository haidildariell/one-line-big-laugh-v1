"""One Line, Big Laugh — writes the entry line to /output/entry.txt."""

import os

ENTRY_TEXT = "The warranty covers water damage, so the technician poured a glass of water over my laptop to check if it was really broken."

DEFAULT_OUTPUT = "/output/entry.txt"


def resolve_output_path():
    return os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)


def validate_entry(text):
    cleaned = text.strip()
    if not 1 <= len(cleaned) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in cleaned:
        raise ValueError("entry must be a single line")
    return cleaned


def write_entry(path, text):
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    return len(text.encode("utf-8"))


def main():
    text = validate_entry(ENTRY_TEXT)
    path = resolve_output_path()
    byte_count = write_entry(path, text)
    print(f"wrote {len(text)} chars ({byte_count} bytes) to {path}")


if __name__ == "__main__":
    main()
