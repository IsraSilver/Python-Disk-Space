import subprocess

def send_alert(email_recipient):
    subject = "Disk Space Alert"
    message = "Free disk space is below 85%."
    sender = "your_email@example.com"

    # Form the command to send the email using ssmtp
    command = f"echo 'Subject:{subject}\n\n{message}' | ssmtp {email_recipient} -f {sender}"

    # Execute the command in the shell
    subprocess.run(command, shell=True)

def check_disk_space():
    # Replace the path with the location you want to check
    disk_path = "/"

    # Execute the command to retrieve disk information
    command = ["df", "-h", disk_path]
    output = subprocess.check_output(command).decode("utf-8")

    # Split the output into lines and extract the available space percentage
    lines = output.strip().split("\n")
    disk_info = lines[1].split()
    available_space_percentage = disk_info[3]

    # Convert the available space percentage to a number
    available_space_percentage = int(available_space_percentage.strip("%"))

    # If the available space is less than 85%, send an alert via email
    if available_space_percentage < 85:
        email_recipient = "recipient@example.com"
        send_alert(email_recipient)

check_disk_space()
