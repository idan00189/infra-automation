from pydantic import BaseModel, field_validator

class Machine(BaseModel):
    name: str
    os: str
    cpu: str
    ram: str

    @field_validator("os")
    def validate_os(cls, value):
        if value not in ["linux", "windows"]:
            raise ValueError("OS must be either 'linux' or 'windows'")
        return value

    @field_validator("cpu")
    def validate_cpu(cls, value):
        if not value.lower().endswith("vcpu"):
            raise ValueError("CPU must end with 'vCPU' (e.g., 2vCPU)")
        try:
            cpu_value = int(value.lower().replace("vcpu", "").strip())
            if cpu_value <= 0:
                raise ValueError("CPU must be a positive number")
        except Exception:
            raise ValueError("CPU must be a positive number ending with 'vCPU'")
        return value

    @field_validator("ram")
    def validate_ram(cls, value):
        if not value.lower().endswith("gb"):
            raise ValueError("RAM must end with 'GB' (e.g., 4GB)")
        try:
            ram_value = int(value.lower().replace("gb", "").strip())
            if ram_value <= 0:
                raise ValueError("RAM must be a positive number")
        except Exception:
            raise ValueError("RAM must be a positive number ending with 'GB'")
        return value

    def log_creation(self, logger):
        message = (
            f"Provisioning machine: {self.name} (OS: {self.os}, "
            f"CPU: {self.cpu}, RAM: {self.ram})"
        )
        logger.info(message)
        print(message)