# EchoVerse

A short description of your project: what it does and its purpose.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.11.x  
- Virtual environment (recommended)  
- Dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/project-name.git
cd project-name

# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt

# For running the project
streamlit run app.py

# Configuration your hugginface Api Key in .env file
API_KEY = "your_api_key_here"
