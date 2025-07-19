# Maintenance Log App

## Project Description
This project is a simple Flask application for recording maintenance logs. Users can add entries about parts, mileage, and notes which are stored in a SQLite database. A basic web interface lets you view and create logs.

## Requirements
- Python 3
- Flask
- Flask-SQLAlchemy

## Installation
Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## How to Run
Start the development server with:

```bash
python app.py
```

The application will run on `http://localhost:5000/` by default.

## Basic Usage
1. Open the application in your browser.
2. Click **เพิ่มรายการ** to add a maintenance log.
3. Fill in the part, mileage, and any notes, then submit the form.
4. The log will appear on the main page where all entries are listed.

