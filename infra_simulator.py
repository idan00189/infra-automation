# infra_simulator.py

import json
import subprocess
import os
from src.machine import Machine
from src.logger import logger

# Ensure necessary directories exist
os.makedirs("configs", exist_ok=True)

def validate_instance_input(instance):
    """Basic validation for machine input."""
    valid_os = ["Ubuntu", "CentOS"]
    if instance["os"] not in valid_os:
        logger.error(f"Invalid OS for machine '{instance['name']}': {instance['os']}")
        return False

    if not instance["cpu"].lower().endswith("vcpu"):
        logger.error(f"Invalid CPU format for machine '{instance['name']}': {instance['cpu']}")
        return False

    if not instance["ram"].lower().endswith("gb"):
        logger.error(f"Invalid RAM format for machine '{instance['name']}': {instance['ram']}")
        return False

    return True

def get_user_input():
    """Collects user input for machine provisioning."""
    machines = []
    while True:
        name = input("Enter machine name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        os_input = input("Enter OS (Ubuntu/CentOS): ")
        cpu = input("Enter CPU (e.g., 2vCPU): ")
        ram = input("Enter RAM (e.g., 4GB): ")

        instance_data = {"name": name, "os": os_input, "cpu": cpu, "ram": ram}

        if not validate_instance_input(instance_data):
            print("Invalid input. Please try again.")
            continue

        machines.append(instance_data)
    return machines

def save_configurations(instances):
    """Save the machine instances to a JSON configuration file."""
    config_file = "configs/instances.json"
    with open(config_file, "w") as f:
        json.dump(instances, f, indent=4)
    logger.info(f"Saved configurations to {config_file}")

def run_setup_script():
    """Runs the Bash script to simulate service installation."""
    try:
        # Ensure the scripts directory is correctly referenced
        subprocess.run(["bash", "scripts/setup_nginx.sh"], check=True)
        logger.info("Nginx installation simulated successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to install Nginx: {e}")

def main():
    logger.info("Provisioning started.")

    # Get user inputs and validate
    instances = get_user_input()
    if not instances:
        logger.info("No machines defined. Exiting.")
        return

    # Save configurations to JSON
    save_configurations(instances)

    # Create Machine objects and log each creation
    machine_objects = []
    for instance in instances:
        machine = Machine(instance["name"], instance["os"], instance["cpu"], instance["ram"])
        machine.log_creation(logger)
        machine_objects.append(machine)

    # Simulate service installation via Bash script
    run_setup_script()

    logger.info("Provisioning completed.")

if __name__ == "__main__":
    main()