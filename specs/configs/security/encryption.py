import pydantic
import pydantic_settings


class JWTConfig(pydantic_settings.BaseSettings):
    jwt_secret: pydantic.SecretStr = pydantic.Field(..., env="encryption_jwt_secret")

    @property
    def jwt_secret_value(self):
        return self.jwt_secret.get_secret_value()

    class Config:
        case_sensitive = False
        secrets_dir = "/run/secrets"
        env_prefix = "encryption_"
