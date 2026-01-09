from modules.email_sender import send_real_email

def send_follow_up_email(contact):
    body = f"""
Hi {contact['name']},

Just following up on my previous email regarding the internship opportunity.
I would really appreciate hearing back from you.

Regards,
Jahnvi
"""
    send_real_email(contact["email"], "Follow-up: " + contact["subject"], body)
    contact["status"] = "FOLLOW_UP_SENT"
    print("Follow-up email sent.")

def check_and_send_follow_up(contact, current_day):
    if contact["status"] == "REPLIED":
        print("User already replied. No follow-up.")
        return

    if contact["status"] == "FOLLOW_UP_SENT":
        print("Follow-up already sent.")
        return

    if contact["status"] == "SENT":
        days_passed = current_day - contact["last_sent_day"]
        if days_passed >= 3:
            send_follow_up_email(contact)
        else:
            print("Waiting before sending follow-up.")