
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
    # Step 1: Check if inputs are valid
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
    
    # Step 2: Handle empty cases
    if template == "":
        print("Template is empty, no output files generated.")
        return
    
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    
    # Step 3: Process each person
    for item in attendees:
        
    
    # Step 4: Write files
