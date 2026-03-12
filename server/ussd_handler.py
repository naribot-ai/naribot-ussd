# NariBot USSD Session Handler
# Generic Routing Logic for Livelihood Navigation

def handle_request(session_id, phone, text):
    """
    Handles incoming USSD strings.
    Logic: Onboarding -> Main Menu -> Paths 1-4
    """
    if not text or text == "":
        # Initial greeting for women job seekers & entrepreneurs
        return "CON Welcome to NariBot.\n1. Yojana\n2. Local Work\n3. Ghar se Kaam\n4. AI Mentor"
    
    # Logic for routing to specific paths
    return "CON Please select an option to continue."
