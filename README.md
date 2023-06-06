# Python-Disk-Space
Write a script that checks the disk status and sends an alert email if the free space is less than 85%. You can use the ssmtp client to send emails directly from the console.

# Disk Space Monitoring Script

This script is designed to monitor the disk space of a specific location and send an email alert if the available space falls below 85%. It utilizes the ssmtp client to send emails directly from the console.

## Prerequisites

Before using this script, ensure that you have the following prerequisites:

- Python (version 3 or above) installed on your system.
- The ssmtp client properly installed and configured to send emails from the console.
- An active email account to use as the sender for the alerts.

## Usage

1. Clone this repository or download the script `disk_space_monitor.py` to your local machine.

2. Open the script in a text editor and configure the following variables:
   - `disk_path`: Set the path to the location you want to monitor.
   - `sender`: Set the email address of the sender (your email address).
   - `email_recipient`: Set the email address of the recipient for the alerts.

3. Save the changes to the script.

4. Open a terminal or command prompt and navigate to the directory where the script is located.

5. Run the script using the following command:  python disk_space_monitor.py

6. The script will execute and check the disk space at the specified location. If the free space is below 85%, an email alert will be sent to the specified recipient.

7. You can schedule the script to run at regular intervals using task scheduling tools or cron jobs for continuous monitoring.




