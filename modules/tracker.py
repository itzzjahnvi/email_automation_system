def update_contact_status(contact, status, day=None):
    contact["status"] = status
    if day is not None:
        contact["last_sent_day"] = day
