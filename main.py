import os
import hashlib
import logging
import json

# Configure logging
logging.basicConfig(filename='integrity_checker.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_hash(file_path):
    """Calculate the hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None

def store_hashes(directory, hash_file):
    """Store hashes of all files in a directory."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = calculate_hash(file_path)
    with open(hash_file, 'w') as f:
        json.dump(file_hashes, f)
    logging.info(f"Hashes stored in {hash_file}")

def check_integrity(hash_file):
    """Check the integrity of files based on stored hashes."""
    try:
        with open(hash_file, 'r') as f:
            stored_hashes = json.load(f)
        for file_path, stored_hash in stored_hashes.items():
            current_hash = calculate_hash(file_path)
            if current_hash != stored_hash:
                logging.warning(f"Integrity check failed: {file_path}")
    except FileNotFoundError:
        logging.error(f"Hash file not found: {hash_file}")

# Example usage
directory_to_monitor = 'path_to_directory'
hash_file = 'file_hashes.json'

# Step 1: Generate and store hashes
store_hashes(directory_to_monitor, hash_file)

# Step 2: Check integrity
check_integrity(hash_file)

    