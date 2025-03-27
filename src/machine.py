# src/schemas.py

from pydantic import BaseModel, validator

class MachineModel(BaseModel):
    name: str
    os: str
    cpu: str
    ram: str

    @validator("os")
    def validate_os(cls, value):
        if value not in ["Ubuntu", "CentOS"]:
            raise ValueError("OS must be either 'Ubuntu' or 'CentOS'")
        return value

    @validator("cpu")
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

    @validator("ram")
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