import sys
import logging
from vault import decrypt_password

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

ENV_FILE = "hcv.env"
logging.info(f"Reading environment variables from {ENV_FILE}")

env = {}
with open(ENV_FILE, 'r') as f:
    for line in f:
        if line.strip() and not line.startswith('#'):
            key, value = line.strip().split(':', 1)
            env[key.strip()] = value.strip()

try:
    LOGIN_USERNAME = env.get('username')
    logging.info(f"Login username: {LOGIN_USERNAME}")
    LOGIN_PASSWORD = decrypt_password(env.get('password'))['decrypted_password']   
    logger.info(f"Decrypted password: {LOGIN_PASSWORD}")
except Exception as e:
    logger.error(f"Error decrypting password: {e}")
    sys.exit(1)


JSON_ENV = "hcv.json"
logging.info(f"Reading environment variables from {JSON_ENV}")
with open(JSON_ENV, 'r') as f:
    import json
    json_env = json.load(f)
    LOGIN_USERNAME_JSON = json_env.get('username')
    logging.info(f"Login username from JSON: {LOGIN_USERNAME_JSON}")
    LOGIN_PASSWORD_JSON = decrypt_password(json_env.get('password'))['decrypted_password']
    logger.info(f"Login password from JSON: {LOGIN_PASSWORD_JSON}")

ENV_FILE2 = "hcv2.env"

logging.info(f"Reading environment variables from {ENV_FILE2}")
with open(ENV_FILE2, 'r') as f:
    env2 = {}
    for line in f:
        if line.strip() and not line.startswith('#'):
            key, value = line.strip().split('=', 1)
            env2[key.strip().strip('"')] = value.strip().strip('"')
    LOGIN_USERNAME2 = env2.get('username')
    logging.info(f"Login username from hcv2.env: {LOGIN_USERNAME2}")
    LOGIN_PASSWORD2 = decrypt_password(env2.get('password'))['decrypted_password']  
    logger.info(f"Login password from hcv2.env: {LOGIN_PASSWORD2}")

    