# NariBot USSD Session Handler (v1.12)
# Replicates Firebase Cloud Function Logic for Public Documentation

def handle_request(session_id, phone, text):
    # Split USSD input by '*' to determine menu depth
    levels = text.split('*')
    
    if text == "":
        # Initial greeting for Women Job Seekers & Entrepreneurs
        # Onboarding Check: If new, start language -> name -> district
        return "CON Welcome to NariBot.\n1. Yojana (Schemes)\n2. Local Work\n3. Ghar se Kaam\n4. AI Mentor"
    
    # Path Routing Logic (v1.12 Section: USSD Flow Diagram):
    # Path 1: Yojana (Static + AI hybrid)
    # Path 2: Local Work (Static tips)
    # Path 3: Home Gigs (Static tips)
    # Path 4: AI Mentor (Gemini 2.5 Flash Logic)
    
    return "CON Please select an option to continue."
