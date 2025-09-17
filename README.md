# Client Email Automation

Automate follow-ups with clients using Excel + SMTP.  
This script checks your client list and sends emails to those who haven’t been contacted within a configurable number of days, then updates the Excel sheet automatically.


## Features

- Reads clients from an Excel file (`sample.xlsx`)
- Checks `Last Date` column against a threshold
- Sends reminder emails automatically via SMTP
- Updates `Last Date` to prevent duplicate emails
- Configurable via `config.json`

## Demo
- Open demo.mp4

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Turytl/client-email-project.git
cd client-email-project
````

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure SMTP and settings

Edit `config.json`:

```json
{
    "smtp_server": "smtp-relay.brevo.com",
    "smtp_port": 587,
    "username": "your-smtp-username",
    "password": "your-smtp-password",
    "sender": "youremail@example.com",
    "threshold_days": 30
}
```

**Notes:**

* `smtp_server` / `smtp_port` should match your email provider (Brevo, Gmail SMTP, etc.)
* `username` / `password` are for the SMTP login
* `sender` is the email address displayed as “From”
* `threshold_days` defines how many days since the last contact to trigger an email

### 5. Prepare Excel

Your `sample.xlsx` should have columns:

| Client Name | Client Email                                | Client Phone | Last Date  |
| ----------- | ------------------------------------------- | ------------ | ---------- |
| John        | [john@example.com](mailto:john@example.com) | +1234567890  | 01-08-2025 |

Only `Client Name`, `Client Email`, and `Last Date` are required for the script.

## Running the script

```bash
python app.py
```

* The script will send emails to clients who haven’t been contacted in the last `threshold_days`.

* `Last Date` in the Excel file will be updated automatically to prevent duplicate emails.

## Notes

* Ensure your SMTP credentials allow sending emails from scripts (some providers require app passwords or special settings).
* Handle emails responsibly—don’t spam.
* Works on macOS, Linux, Windows.
* A Sample Excel File is included for testing purposes.

## Dependencies

* `pandas>=2.0`
* `openpyxl>=3.1`