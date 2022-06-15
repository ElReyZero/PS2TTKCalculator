from configparser import ConfigParser, ParsingError
import os
import pathlib

class ConfigError(Exception):
    """
    Raised when an error occur while reading the config file.

    :param msg: Error message.
    """
    def __init__(self, msg: str):
        self.message = "Error in config file: " + msg
        super().__init__(self.message)

class MissingConfig(Exception):
    """
    Raised when a config value is missing.

    :param msg: Error message.
    """
    def __init__(self, msg: str):
        self.message = "Missing config value: " + msg
        super().__init__(self.message)


## DYNAMIC PARAMETERS:
# (pulled from the config file)

service_id = "s:"
django_key = None

#: Contains database parameters.
database = {
    "host": "",
    "name": "",
    "user": "",
    "password": ""
}

def get_config():
    """
    Populate the config data from the config file.
    """
    file = f"{pathlib.Path(__file__).parent.absolute()}/../config.cfg"

    try:
        global service_id
        service_id += os.environ["SERVICE_ID"]

        global django_key
        django_key = os.environ["DJANGO_KEY"]

        global database
        database["host"] = os.environ["DB_HOST"]
        database["user"] = os.environ["DB_USER"]
        database["password"] = os.environ["DB_PASSWORD"]
        database["name"] = os.environ["DB_NAME"]

    except KeyError:
        if not os.path.isfile(file):
            raise ConfigError(f"{file} not found! "+file)

        config = ConfigParser(inline_comment_prefixes="#")
        try:
            config.read(file)
        except ParsingError as e:
            raise ConfigError(f"Parsing Error in '{file}'\n{e}")

        _check_section(config, "General", file)

        try:
            service_id += config["General"]["service_id"]
        except KeyError:
            _error_missing(service_id, 'General', file)
        except ValueError:
            _error_incorrect(service_id, 'General', file)

        _check_section(config, "Django", file)
        try:
            django_key = config["Django"]["django_key"]
        except KeyError:
            _error_missing(django_key, 'Django', file)
        except ValueError:
            _error_incorrect(django_key, 'Django', file)

        _check_section(config, "Database", file)

        for key in database:
            try:
                database[key] = config["Database"][key]
            except KeyError:
                _error_missing(key, 'Database', file)
            except ValueError:
                _error_incorrect(key, 'Database', file)


def _check_section(config, section, file):
    if section not in config:
        raise ConfigError(f"Missing section '{section}' in '{file}'")


def _error_missing(field, section, file):
    raise ConfigError(f"Missing field '{field}' in '{section}' in '{file}'")


def _error_incorrect(field, section, file):
    raise ConfigError(f"Incorrect field '{field}' in '{section}' in '{file}'")