# DevOps Infrastructure Provisioning & Configuration Automation

## Overview
This project simulates infrastructure provisioning and configuration automation. It is designed as a modular Python application that:
- Accepts user inputs for virtual machine (VM) definitions.
- Validates and stores configuration data in a JSON file.
- Uses a `Machine` class for representing VM instances.
- Calls a Bash script to simulate service installation (e.g., installing Nginx).
- Implements logging and error handling throughout the process.

## Setup & Execution
1. **Clone the repository & set up the environment:**
   ```bash
   git clone <repository_url>
   cd infra-automation
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt  # (if additional packages are added later)