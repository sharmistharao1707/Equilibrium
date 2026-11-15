markdown
# Project Summary: Mood → Productivity Tracker

## Overview
The **Mood → Productivity Tracker** is a single-file Python desktop application designed to track and evaluate the relationship between a user's daily mood and their study duration.

## Architecture & Components

### 1. Data Storage (`mood_data.csv`)
- On startup, the script checks if `mood_data.csv` exists in the working directory.
- If absent, it initializes the file with three headers: `Date`, `Mood`, and `Hours`.

### 2. Core Functions
- **`save_data()`**:
  - Retrieves the selected mood and entered hours from the UI.
  - Validates that the hours input can be cast to a `float`.
  - Appends `[date.today(), mood, hours_float]` to `mood_data.csv`, displays a confirmation dialog, and clears the input field.
- **`analyze_data()`**:
  - Reads `mood_data.csv` using `csv.DictReader`.
  - Aggregates total hours (`mood_totals`) and entry counts (`mood_counts`) per mood category.
  - Computes the mean hours per mood ($\text{Average} = \frac{\text{Total Hours}}{\text{Entry Count}}$) formatted to two decimal places and updates the UI label.

### 3. Graphical User Interface (Tkinter)
- **Window:** Fixed `350x350` window titled *"Mood → Productivity Tracker"*.
- **Controls:**
  - `OptionMenu` dropdown defaulting to `"Happy"`.
  - `Entry` text box for numeric study hours.
  - Action `Button` widgets bound to `save_data` and `analyze_data`.
  - Dynamic `Label` widget to render analytical output.
