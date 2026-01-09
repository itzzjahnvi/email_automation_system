# main.py
from modules.email_sender import send_real_email
from modules.follow_up_logic import check_and_send_follow_up
from modules.tracker import update_contact_status

# Sample contact
contacts = [
    {
        "name": "Test User",
        "email": "jahnvigoel25@gmail.com", 
        "subject": "Internship Opportunity",
        "status": "SENT",
        "last_sent_day": 0
    }
]

# Current day simulation
current_day = 4

# Check each contact for follow-up
for contact in contacts:
    check_and_send_follow_up(contact, current_day)
