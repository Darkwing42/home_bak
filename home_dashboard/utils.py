import os

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

# the values of those depend on your setup
POSTGRES_URL = get_env_variable("POSTGRES_URL") or "172.17.0.2"
POSTGRES_USER = get_env_variable("POSTGRES_USER") or "postgres"
POSTGRES_PW = get_env_variable("POSTGRES_PW") or "mysecretpassword"
POSTGRES_DB = get_env_variable("POSTGRES_DB") or "test"
