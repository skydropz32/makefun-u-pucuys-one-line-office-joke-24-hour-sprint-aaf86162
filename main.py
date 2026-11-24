"""One-Line Office Joke: 24-Hour Sprint.

Writes a single original office joke to /output/entry.txt.
"""

import os

JOKE = "The intern asked where the fire exit is; I pointed at the door marked 'Exit Interview'."


def main() -> None:
    # The gate: 1 to 200 characters of UTF-8 text, not only whitespace.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError("joke must be 1-200 characters of non-blank text")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
