from pydantic import BaseModel, Field


class NetworkConfig(BaseModel):
    ipaddress: str
    port: int


class LogConfig(BaseModel):
    loglevel: str = Field(..., description="Logging Level")


class ConfigModel(BaseModel):
    network: NetworkConfig
    log: LogConfig
