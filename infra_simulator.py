import json
import subprocess
import os
from src.logger import logger
from src.machine import Machine  # Machine class includes Pydantic validation

CONFIG_FILE = "configs/instances.json"

def get_user_input():
    machines = []
    print("🛠️  Enter machine details (type 'done' to finish)...")
    
    while True:
        name = input("Enter machine name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        
        os_input = input("Enter OS (linux/windows): ").strip()
        cpu = input("Enter CPU (e.g., 2vCPU): ").strip()
        ram = input("Enter RAM (e.g., 4GB): ").strip()
        
        try:
            # Create a Machine instance using Pydantic validation
            machine = Machine(name=name, os=os_input, cpu=cpu, ram=ram)
            machines.append(machine)
            print(f"✅ Machine '{name}' added.\n")
        except Exception as e:
            print(f"[ERROR] {e}\n")
            continue

    return machines

def load_existing_instances():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                logger.warning("Invalid JSON detected in config file. Starting fresh.")
                return []
    return []

def save_configurations(machine_objects):
    # Convert each Machine object to a dict using model_dump() (or dict() if using Pydantic v1)
    new_instances = [machine.model_dump() for machine in machine_objects]
    all_instances = load_existing_instances() + new_instances
    # Ensure the configs directory exists
    os.makedirs("configs", exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(all_instances, f, indent=4)
    logger.info(f"Saved {len(new_instances)} new machine(s) to {CONFIG_FILE}")

def run_setup_script():
    try:
        subprocess.run(["bash", "scripts/setup_nginx.sh"], check=True)
        logger.info("Nginx installation simulated successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to run Bash script: {e}")

def main():
    logger.info("Provisioning session started.")
    
    machine_objects = get_user_input()
    if not machine_objects:
        logger.info("No machines provided. Exiting.")
        return

    save_configurations(machine_objects)

    # For each machine, log creation and run the Bash script individually
    for machine in machine_objects:
        machine.log_creation(logger)
        run_setup_script()  # Run the service installation script for each machine

    logger.info("Provisioning session completed.\n\n\n")

if __name__ == "__main__":
    main()