# Ladywood Connect Dashboard

A community-focused platform designed to improve digital accessibility, access to local support, and community resources in Ladywood, Birmingham.

### Live application 
https://ladywood-connect.streamlit.app/

---
## Authors

**Group 11**
Multidisciplinary CBL (Engineering for People 2025/2026)  
Eindhoven University of Technology

---
## Overview 
Ladywood Connect was developed by Waypoint to support residents in improving digital literacy, taking opportunities, and accessing local services within the community. This platform brings together information about the Community Bus by Waypoint, workshops at the Community Bus, community announcements, and feedback channels. All of these features in one accessible interface. 

The key focus of the project is digital inclusion. The platform provides multilingual content, adjustable text sizes, and mobile-responsive layouts to support a diverse user base.

---

## Features
### Community Bus
- View the current location of the Community Bus
- Interactive map of where the Community Bus is
- View opening hours and location information 
- Quick navigation to available workshops

### Workshops
- Weekly workshop schedule
- Workshops of all three themes: Access, Opportunity, and Confidence
- Registration form for workshops
- Quick access to location and opening hours of Community Bus

### Announcements
- Local activities and events
- Relevant updates about Ladywood
- Updates about the dashboard 

### Feedback & Requests
- Submit feedback about the services Waypoint provides
- Request support, new workshops, additional features, etc.
- View contact information 
- Understand how feedback and requests are reviewed and processed

### Accessibility Features
- Multiple language options on every page (including right-to-left language support)
- Adjustable text sizes on every page
- The application works on both desktop and phone browsers 

---

## Project Structure
```text
Ladywood Connect Dashboard
│
├── app.py
├── translations.py
├── requirements.txt
├── README.md
│
├── assets/
│
└── pages/
    ├── announcements.py
    ├── bus.py
    ├── workshops.py
    └── feedback.py
```
---
## Installation
1. Extract the project ZIP file 
2. (Recommended) Create a virtual environment 

### Windows
```bash
python -m venv venv 
venv\Scripts\activate
``` 

### Mac / Linux 
```bash
python3 -m venv venv 
source venv/bin/activate
``` 
3. Open a terminal in the project folder
4. Install the requirements 
```bash
pip install -r requirements.txt
```
5. Run the application 
```bash
streamlit run app.py
```
6. The application will open automatically. If not, open the local URL that will be displayed in the terminal (http://localhost:8501)
---
## Deployment 
This platform was developed using Streamlit and deployed using Streamlit Community Cloud.
It can be accessed through the link provided above and contains the latest release of the application. 