from __future__ import annotation

from dataclasses import dataclass
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ClickHouseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_predix = "CLICKHOUSE_",
        env_file = ".env",
        env_file_encoding= "utf-8",
        extra="ignore",
        case_sensitive=False,
    )
    
    host: str = Field(default='localhost', description='хост')
    port: str = Field(default='8123', ge=1, le=65535, description='порт')
    database: str = Field(default='shop', description='база данных')
    user: str = Field(default='default', description='пользователь')
    password: str = Field(default='', description='пароль')


class GeneratorSettings:
    model_config = SettingsConfigDict(
        env_prefix="GENERATOR_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )
    
    batch_size: int = Field(default=1000, ge=1, description="Записи в одном батче")
    interval_seconds: float = Field(
        default=1.0, ge=0.0, description="Пауза между батчами, секунды"
    )
    seed: int = Field(default=42, description="Seed для воспроизводимости генерации")
    
    anomaly_probability: float = Field(
        default=0.02, ge=0.0, le=1.0, description="Вероятность аномалии на запись"
    )
    anomaly_strength: float = Field(
        default=3.0, ge=0.0, description="Множитель силы аномалии"
    )

    # --- Справочник станций -------------------------------------------------
    cities: str = Field(
        default="Vladivostok,Moscow,Kazan,Sochi,Irkutsk",
        description="Города станций через запятую",
    )

    # --- Логирование ---------------------------------------------------------
    log_level: str = Field(default="INFO", description="Уровень логирования")

    # --- Retry: устойчивость к отказам БД --------------------------------------
    retry_max_attempts: int = Field(default=5, ge=1)
    retry_base_delay_seconds: float = Field(default=0.5, ge=0.0)
    retry_max_delay_seconds: float = Field(default=30.0, ge=0.0)
    retry_backoff_factor: float = Field(default=2.0, ge=1.0)

    @property
    def city_list(self) -> list[str]:
        """Города как список (env хранит их строкой через запятую)."""
        return [c.strip() for c in self.cities.split(",") if c.strip()]

    
@dataclass(frozen=True, slots=True)
class Settings:
    generator: GeneratorSettings
    cliclhouse: ClickHouseSettings


@lru_cache
def get_settings() -> Settings:
    return Settings(generator=GeneratorSettings(), cliclhouse=ClickHouseSettings())