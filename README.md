# Jarvis: Your Personal AI Assistant

---

## Overview

Jarvis is a Python-based desktop voice assistant designed to help you automate various tasks and provide information through simple voice commands. Inspired by the iconic AI from Iron Man, Jarvis aims to be a helpful and interactive companion for your daily computer usage.

## Features

Jarvis comes packed with a variety of functionalities to make your life easier:

* **Time & Date:** Get the current time and date instantly.
* **Personal Information:** Ask Jarvis about itself (who it is, its version, etc.).
* **Wikipedia Search:** Query Wikipedia for information on any topic.
* **Web Browse:** Open popular websites like YouTube, Google, Stack Overflow, and Flipkart with a voice command.
* **System Control:**
    * **Logout/Restart/Shutdown:** Safely log out, restart, or shut down your system.
    * **Open Applications:** Launch specific applications (e.g., VS Code).
* **Music Playback:** Play music from a designated local music directory.
* **Reminders:**
    * **Add Reminders:** Create and store voice-activated reminders.
    * **Recall Reminders:** Have Jarvis read back your saved reminders.
* **System Information:** Check CPU usage and battery percentage.
* **Weather Updates:** Get current weather conditions for any city worldwide (requires an API key).
* **Voice Customization:** Change Jarvis's voice between male and female.
* **Greetings:** Jarvis offers personalized greetings based on the time of day.

---

## Getting Started

Follow these steps to set up and run Jarvis on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.x:** If you don't have Python, download it from [python.org](https://www.python.org/).
* **`pip`:** Python's package installer (usually comes with Python).

### Installation

1.  **Clone the Repository (or download the code):**
    ```bash
    git clone [https://github.com/YourGitHubUsername/Jarvis-AI-Assistant.git](https://github.com/YourGitHubUsername/Jarvis-AI-Assistant.git)
    cd Jarvis-AI-Assistant
    ```
    *(Replace `YourGitHubUsername` with your actual GitHub username and `Jarvis-AI-Assistant` with your repository name)*

2.  **Install Required Libraries:**
    Open your terminal or command prompt in the project directory and run:
    ```bash
    pip install pyttsx3 SpeechRecognition wikipedia smtplib pyautogui psutil pyjokes requests
    ```

### API Keys Configuration

* **OpenWeatherMap API (for Weather feature):**
    1.  Go to [OpenWeatherMap](https://openweathermap.org/api) and sign up for a free account.
    2.  Generate an **API key**.
    3.  Open the `jarvis.py` (or your main script file) and locate the `weather()` function.
    4.  Replace `"YOUR-API_KEY"` with your actual OpenWeatherMap API key:
        ```python
        api_key = "YOUR-API_KEY" # Replace this line
        ```

* **Email Functionality (Optional):**
    The `sendEmail` function is currently commented out in the provided code. If you wish to enable it, you'll need to:
    1.  **Uncomment** the `sendEmail` function and the corresponding `elif ("send email" in query):` block in your `if __name__ == "__main__":` section.
    2.  **Enable "Less secure app access"** in your Gmail account settings (or use an App Password if 2-factor authentication is enabled). **Be aware of the security implications when enabling less secure app access.**
    3.  Replace `"user-name@xyz.com"` and `"pwd"` with your **Gmail address** and **App Password (or regular password if less secure app access is enabled)** in the `sendEmail` function.

### Paths Configuration

You'll need to update a few paths in the code to match your system:

* **Music Folder:**
    Locate `music_dir = r'path to your music folder'` in the `main` block and replace it with the actual path to your music directory. For example:
    ```python
    music_dir = r'C:\Users\YourUser\Music' # Windows example
    # Or '/home/YourUser/Music' # Linux example
    ```
* **VS Code Path:**
    If you use a different path for VS Code or a different editor, update `codePath` in the `elif 'changes' in query:` block.
    ```python
    codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # Update if different
    ```
* **Screenshot Save Path (if enabled):**
    The `screenshot()` function is commented out. If you enable it, remember to update the `img.save()` path:
    ```python
    # img.save(r'path to folder in which you would like to save screenshot')
    ```
* **Reminder File Path:**
    Update the paths for reading and writing the reminder file:
    ```python
    # Example:
    # reminder_file = open(r"C:\Users\YourUser\Documents\reminders.txt", 'a')
    # reminder_file = open(r"C:\Users\YourUser\Documents\reminders.txt", 'r')
    ```
    Choose a suitable folder on your system for storing reminders.

---

## How to Use

Simply run the Python script, and Jarvis will greet you. Then, speak your commands clearly into your microphone.

```bash
python your_main_script_name.py
