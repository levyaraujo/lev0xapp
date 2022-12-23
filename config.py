from dynaconf import Dynaconf, FlaskDynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml', '.secrets.toml'],
    env_switcher='APP_ENV',
    environments=['default', 'development', 'docker', 'testing', 'production'],
    load_dotenv=True
)

def init_app(app):
    FlaskDynaconf(app=app)
