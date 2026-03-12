# NariBot USSD
**Session Orchestration and Menu-Tree Logic**

This repository manages the session state and routing for NariBot's USSD and IVR channels.

### Architecture
* **`/server`**: Generic handler for incoming USSD strings (v1.12 flow).
* **`/menus`**: JSON-based navigation trees for Paths 1, 2, and 3.
* **`/prompts`**: Multi-lingual interface text for onboarding and navigation.

### Features
* **Path 1:** Government Scheme Discovery (Yojana).
* **Path 2 & 3:** Local and Home-based Livelihood tips.
* **Path 4:** Integration point for the AI Navigator.

---
*Built for DPG (Digital Public Good) scalability.*
