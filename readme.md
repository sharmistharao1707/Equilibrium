# Mood → Productivity Tracker

A lightweight desktop GUI application built with Python and Tkinter to log daily moods alongside study hours, helping you analyze how your emotional state correlates with your productivity.

## Features
- **Daily Logging:** Record your current mood (`Happy`, `Neutral`, `Stressed`, `Tired`) and study hours with automatic date stamping.
- **Persistent Storage:** Automatically creates and appends entries to a local `mood_data.csv` file.
- **Input Validation:** Ensures only valid numeric entries are accepted for study hours.
- **Productivity Analytics:** Calculates and displays the average study hours per mood directly within the interface.

## Prerequisites
- Python 3.x (uses only built-in standard libraries: `tkinter`, `csv`, `os`, and `datetime`—no external packages required).

## How to Run
1. Save the Python script as `tracker.py`.
2. Open your terminal or command prompt and navigate to the project directory.
3. Run the application:
   ```bash
   python tracker.py
