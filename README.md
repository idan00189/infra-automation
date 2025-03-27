# 🖥️ Infrastructure Simulator

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Pydantic](https://img.shields.io/badge/pydantic-2.0+-orange.svg)](https://pydantic-docs.helpmanual.io/)

A lightweight infrastructure simulator I built to help developers test and prototype virtual machine configurations. Perfect for learning infrastructure concepts or planning deployments without cloud costs.

## 🎯 Why I Built This

I created this project to:
- Simplify the process of planning infrastructure deployments
- Practice infrastructure-as-code concepts
- Provide a risk-free environment for learning VM configuration
- Demonstrate Python best practices with Pydantic validation

## ✨ Key Features

- 🖥️ Simple CLI interface for quick VM definitions
- ✅ Smart validation to catch configuration errors early
- 💾 Persistent JSON storage for your machine configs
- 🚀 Nginx installation simulation
- 📝 Detailed logging for tracking actions

## 🚀 Quick Start

1. Clone this repo:
```bash
git clone https://github.com/yourusername/infrastructure-simulator
cd infrastructure-simulator
```

2. Install the only dependency (Pydantic):
```bash
pip install -r requirements.txt
```

3. Run the simulator:
```bash
python infra_simulator.py
```

## 💡 How to Use

Just follow the interactive prompts to create your virtual machines:

```bash
🛠️  Enter machine details (type 'done' to finish)...
Enter machine name (or 'done' to finish): web-server
Enter OS (linux/windows): linux
Enter CPU (e.g., 2vCPU): 2vCPU
Enter RAM (e.g., 4GB): 4GB
✅ Machine 'web-server' added.
```

### Valid Inputs:
- **OS**: `linux` or `windows`
- **CPU**: Any number followed by `vCPU` (e.g., `2vCPU`, `4vCPU`)
- **RAM**: Any number followed by `GB` (e.g., `4GB`, `8GB`)

## 📁 Project Structure

```
infrastructure-simulator/
├── configs/                 # Where your VM configs are stored
├── logs/                   # Detailed operation logs
├── scripts/                # Simulation scripts (like Nginx setup)
├── src/                    # Core functionality
└── infra_simulator.py      # Main entry point
```

## 📝 Configuration Example

Your machines are saved in `configs/instances.json` like this:

```json
{
    "name": "web-server",
    "os": "linux",
    "cpu": "2vCPU",
    "ram": "4GB"
}
```

## 🔍 Logging

All actions are logged to `logs/provisioning.log` for easy debugging and audit trails.

## 🛠️ Technical Details

Built with:
- **Python 3.7+**: For modern language features
- **Pydantic**: For rock-solid data validation
- **Standard Library**: json, subprocess, logging, os

## 🤝 Want to Contribute?

Feel free to:
- Open issues for bugs or suggestions
- Submit PRs for improvements
- Fork and adapt for your own use

## 📫 Get in Touch

- GitHub: [Your GitHub Profile]
- LinkedIn: [Your LinkedIn]
- Email: [Your Email]

---

<p align="center">
  Built with 💻 by [Your Name] - A passionate infrastructure enthusiast
</p>

## Configuration Format

Machines are configured with the following specifications:
- **name**: Unique identifier for the machine
- **os**: Operating system (linux/windows)
- **cpu**: CPU allocation (must end with 'vCPU')
- **ram**: RAM allocation (must end with 'GB')

Example configuration:
```json
{
    "name": "web-server",
    "os": "linux",
    "cpu": "2vCPU",
    "ram": "4GB"
}
```

## Project Structure

```
infrastructure-simulator/
├── configs/
│   └── instances.json       # Stored machine configurations
├── logs/
│   └── provisioning.log     # Application logs
├── scripts/
│   └── setup_nginx.sh       # Service installation simulation
├── src/
│   ├── __init__.py
│   ├── logger.py           # Logging configuration
│   └── machine.py          # Machine model and validation
├── infra_simulator.py      # Main application
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Logging

The application maintains detailed logs in `logs/provisioning.log`, including:
- Machine provisioning details
- Service installation status
- Error messages and warnings

## Dependencies

- pydantic >= 2.0: Data validation using Python type annotations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

