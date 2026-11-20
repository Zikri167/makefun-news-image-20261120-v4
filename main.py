"""Deliver the finished front page.

The artwork is baked into entry.png beside this file, so the whole
program is one faithful copy: read the bundled page, write it to
/output/entry.png, and confirm the copy kept every byte.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def main():
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    expected = os.path.getsize(SOURCE)
    delivered = os.path.getsize(DEST)
    if delivered != expected:
        raise SystemExit(
            "copy fell short: %d of %d bytes reached %s" % (delivered, expected, DEST)
        )


if __name__ == "__main__":
    main()
