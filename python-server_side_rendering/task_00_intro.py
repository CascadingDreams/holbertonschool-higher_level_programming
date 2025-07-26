
'''Generates text in template'''

def generate_invitations(template, attendees):
    '''
        Fills in template with data
        Args:
            template: string
            attendees: list, dictionary
        Returns:
                template with data filled in
    '''
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Each attendee must be a dictionary")
            return

    #print("All input validations passed!")    

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    out_files = 1
    for item in attendees:
        safe_item = {}
        for key in ["name", "event_title", "event_date", "event_location"]:
            if key in item and item[key] is not None:
                safe_item[key] = item[key]
            else:
                safe_item[key] = "N/A"

        personal_invite = template.format(**safe_item)
        filename = f"output_{out_files}.txt"
        with open(filename, "w") as file:
            file.write(personal_invite)
        print(f"Created {filename}")
        out_files += 1