import pandas as pd
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import json

# Load config
with open('config.json') as f:
    config = json.load(f)

one_month_ago = datetime.now() - timedelta(days=config['threshold_days'])

df = pd.read_excel('sample.xlsx')

with smtplib.SMTP(config['smtp_server'], config['smtp_port']) as server:
    server.starttls()
    server.login(config['username'], config['password'])
    
    for index, row in df.iterrows():
        last_date = pd.to_datetime(row['Last Date'])
        
        # Skip rows with empty/malformed email
        if not isinstance(row['Client Email'], str) or '@' not in row['Client Email']:
            print(f"Skipping invalid email for {row['Client Name']}")
            continue
        
        if last_date < one_month_ago:
            msg = MIMEText(
                f"Hi {row['Client Name']},\n\n"
                f"It's been over {config['threshold_days']} days since our last interaction on {last_date.date()}.\n"
                "Please get in touch.\n\nBest regards."
            )
            msg['Subject'] = "Reminder: Time to follow up"
            msg['From'] = config['sender']
            msg['To'] = row['Client Email']
            
            try:
                server.sendmail(config['sender'], row['Client Email'], msg.as_string())
                print(f"Email sent to {row['Client Email']}")
            except Exception as e:
                print(f"Failed to send to {row['Client Email']}: {e}")
            
            # Update last date using proper datetime
            df.at[index, 'Last Date'] = pd.Timestamp.now()
        
# Save the updated Excel file
df.to_excel('sample.xlsx', index=False)

print("Demo run complete.")
