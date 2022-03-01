import yaml
import pkgutil


data = pkgutil.get_data(__name__, "config.yaml")
if data is not None:
    config = yaml.load(data, Loader=yaml.FullLoader)
else:
    raise Exception("Couldn't load config")


def get(key_looked):
    global config
    return config[key_looked]
