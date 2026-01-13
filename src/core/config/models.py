from pydantic import BaseModel, Field

class GeneralConfig(BaseModel):
    projectdir: str = Field(..., description="Dir containing the project (default=/etc/pulsynk-core)")

class NetworkConfig(BaseModel):
    ipaddress: str
    port: int


class LogConfig(BaseModel):
    loglevel: str = Field(..., description="Logging Level")
    filename: str = Field(..., description="Path and Filename of logfile")


class ConfigModel(BaseModel):
    network: NetworkConfig
    log: LogConfig
