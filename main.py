"""One-letter entry for the make.fun 'One Letter: Coffee or Tea' bounty.

Writes exactly one letter to /output/entry.txt: "A" for coffee.
The gate requires 1 to 1 characters, so there is no newline,
no punctuation and no explanation -- just the letter.
"""

import os

# "A" = coffee. Coffee is the bolder, more vivid stance: the first
# thing most people reach for in the morning, and the louder half
# of the coffee-against-tea argument.
LETTER = "A"


def main():
    # Guard the sealed gate: the entry must be exactly one letter,
    # "A" for coffee or "B" for tea, and nothing else.
    assert len(LETTER) == 1 and LETTER in ("A", "B"), LETTER
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
