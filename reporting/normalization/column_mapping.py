# File for column naming conventions

column_map = {
    'race': 'Race',
    'ethnicity': 'Ethnicity',
    'gender': 'Gender',
    'language': 'Language',
    'household_size': 'Household_Size',
    'in your household':'Household_Size',
    'part of your household':'Household_Size',
    'Household Size?':'Household_Size',
    'numhhmembers':'Household_Size',
    'county':'County',
    'zip':'Zip Code',
    'postal':'Zip Code',
    'review stage':'Review Stage',
    'birth':'Date of birth',
    'Case Id':'Case_Id',
    "Open Date":"Open Date",
    "Close Date":"Close Date",
    'Date entered':'Date entered',
    'Date entered "HC - 09- Post Session, Notes & Finalize Client Action Pan (Housing Counseling Pipeline)" - Daily':'Date entered',
    'Date entered "16BE - Initial Application Approved (General Benefit Enrollment)"':'Date entered',
    'Date entered "13 VA - Exit Processing - Doc Collection (Voucher Administration )" - Daily':'Date entered',
    'Date entered "19CM- Case Management Closed (Case Management)" - Monthly':'Date entered',
    'Date entered stage "RA 17- Ops Approved, Ready for Payment" - Monthly':'Date entered',
    'Date entered "10-Invoices/Payments (Peer Support)" - Monthly':'Date entered',
    'Date entered "19 - Exit/Graduated (Rural RRH/EHP (Primary))" - Monthly':'Date entered',
    'Date entered "11 (TSS) Move in/Ongoing CM services (Tenancy Support Services)" - Monthly':'Date entered'
}

phone_patterns = {
    'primary': 'Phone_Primary',
    'alternate': 'Phone_Alternate',
    'alternative': 'Phone_Alternate'
}

email_patterns = {
    'primary': 'Email_Primary',
    'alternate': 'Email_Alternate',
    'alternative': 'Email_Alternate'
}