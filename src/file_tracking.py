import hashlib
import json
from pathlib import Path


TRACKING_FILE = Path("artifacts/file_hashes.json")


def file_hash(filepath):
    """Compute SHA256 hash of a file."""

    sha = hashlib.sha256()

    with open(filepath, "rb") as f:

        while True:

            data = f.read(8192)

            if not data:
                break

            sha.update(data)

    return sha.hexdigest()


def load_hashes():

    if TRACKING_FILE.exists():

        with open(TRACKING_FILE, "r") as f:

            return json.load(f)

    return {}


def save_hashes(hashes):

    TRACKING_FILE.parent.mkdir(exist_ok=True)

    with open(TRACKING_FILE, "w") as f:

        json.dump(hashes, f, indent=4)