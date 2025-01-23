# Database Exporter

This application allows users to connect to a MySQL database, view its tables, and select tables for export (WIP). It provides a simple graphical user interface (GUI) built with wxPython.

## Features
- Reads database configuration from a `config.ini` file.
- Connects to a MySQL database and lists all available tables.
- Displays tables in a grid with checkboxes for selection.

## Requirements
- Python 3.8 or higher
- MySQL database

## Installation and Setup

1. **Clone the repository:**
git clone https://github.com/HaniSalt/Database-converter-in-wxPython.git
cd <location of database-exporter>

2. Set up a virtual environment:
python -m venv venv

3. Install dependencies:
pip install -r requirements.txt

4. Configure the database:
Create/use the config.ini file in the project.
Replace the placeholders with your database credentials.

5. Run the application: 
python -m src.database_exporter.app