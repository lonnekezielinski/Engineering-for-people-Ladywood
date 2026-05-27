# Ladywood Connect Dashboard

Community-focused dashboard prototype designed to improve digital accessibility and reduce reliance on informal support networks in Ladywood.

---

# Clone the Repository (VS Code Method)

## 1. Copy the Repository Link

Go to the GitHub repository and click the green **Code** button.

Copy the HTTPS link.

---

## 2. Open VS Code

Open Visual Studio Code.

Press:

```bash
Ctrl + Shift + P
```

(Mac: `Cmd + Shift + P`)

---

## 3. Clone the Repository

Type:

```bash
Git: Clone
```

Click:

```bash
Git: Clone
```

Paste the repository URL when prompted.

---

## 4. Choose a Folder Location

Select where you want the project folder to be saved on your computer.

---

## 5. Open the Repository

After cloning, VS Code will ask:

```bash
Open cloned repository?
```

Click:

```bash
Open
```

---

# Set Up the Virtual Environment

## 1. Open a New Terminal

In VS Code:

```bash
Terminal > New Terminal
```
---

## 2. Create the Virtual Environment

Run:

```bash
python -m venv venv
```

This creates a local virtual environment called:

```bash
venv
```

---

## 3. Activate the Virtual Environment

### Windows

In terminal run the following:

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

If successful, you should now see:

```bash
(venv)
```

at the beginning of your terminal line. When working on the code always check in your terminal if the environment is activated. If not run the above line in your terminal. 

---

# Install Required Packages

Run:

```bash
pip install -r requirements.txt
```

This installs all required project dependencies automatically.

---

# Run the Dashboard

Start the Streamlit app by running the following in your terminal:

```bash
streamlit run app.py
```

The dashboard should automatically open in your browser.

---

# Project Structure

## `app.py`

Main dashboard homepage.

Contains:
- homepage layout
- navigation buttons
- accessibility settings
- dashboard styling
- links to other pages

---

## `pages/`

Contains all additional dashboard pages.

Current pages:
- `bus.py`
- `workshops.py`
- `announcements.py`
- `feedback.py`

---

## `assets/`

Contains all visual assets used in the dashboard. 

Currently stores:
- PNG icons

---

## `requirements.txt`

Contains all required Python packages for the project.

Used to install dependencies with:

```bash
pip install -r requirements.txt
```

---

# Git Workflow

## Pull latest changes

Before you start coding ALWAYS pull changes first! 
To do so, go to Source Control in VS code and pull the changes.

---

## Save and upload changes

To save and upload your changes: first save your changes (ctrl + S or cmd + S), then describe your changes and push them. 

---
Have fun coding!