# File watch
A lightweight tool to ensure the integrity of files and directories by monitoring and detecting unauthorized modifications. This project uses cryptographic hashing to verify that files remain unchanged, providing a reliable way to safeguard against tampering

## **Features**

- **Hash Generation:** Calculate cryptographic hashes (SHA-256) for files.
- **Integrity Monitoring:** Detect unauthorized changes by comparing current hashes to stored ones.
- **Logging:** Record changes and integrity violations with detailed logs.
- **User-Friendly:** Easy to set up and run for any directory.
- **Extensible:** Can be enhanced with real-time monitoring, notifications, or GUI

## **Use Cases**

- **System Security:** Monitor critical system files for unauthorized changes.
- **Backup Validation:** Ensure backup files are not corrupted.
- **Compliance:** Maintain file integrity for audit requirements.

## **Installation**

### Prerequisites

- Python 3.x
- Required Python libraries (install with pip):
```
pip install -r requirements.txt
```
### Clone the Repository

```
git clone https://github.com/CyOwl-V/Integrity-Checker
``` 

## **Usage** ***

### 1. Generate and Store File Hashes

Run the following command to generate SHA-256 hashes for all files in a directory and store them in a JSON file:
```
python integrity_checker.py --store --directory /path/to/monitor --output hashes.json
```
### 2. Verify File Integrity

To check if any files have been modified, run:


```
python integrity_checker.py --check --hashfile hashes.json
```

### Example Commands

- Store hashes:
``` 
python integrity_checker.py --store --directory /path/to/directory --output file_hashes.json  
```

- Check integrity:
```
python integrity_checker.py --check --hashfile file_hashes.json
```

## **Project Structure**

```
├── integrity_checker.py  # Main script 
├── requirements.txt      # Dependencies 
├── README.md             # Documentation 
└── integrity_checker.log # Log file (auto-generated)
```

## **Configuration**

You can modify the following parameters in the script:

- Directory to monitor
- Hashing algorithm (default: SHA-256)
- Log file location

## **Contributing**

Contributions are welcome! Here’s how you can help:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.
## **Future Enhancements**

- Real-time file monitoring with the `watchdog` library.
- GUI for ease of use.
- Notification system for integrity violations.
- Scheduler
- Timestamp Verification
- File Metadata Monitoring
- Encryption-Based Verification "OpenSSL"
- Add Fail-Safe Measures "Backup"
- Database for Integrity Data
- Testing and Validation " checking if it work or not"

## **Acknowledgements**

Special thanks to the open-source community for libraries like `hashlib` and `logging` that make projects like this possible.

