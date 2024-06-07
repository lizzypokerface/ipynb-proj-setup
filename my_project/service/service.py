import logging
import requests

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

database = {1: "Alice", 2: "Bob", 3: "Charlie"}


def get_user_from_db(user_id):
    logger.debug(f"Fetching user with ID: {user_id}")
    user = database.get(user_id)
    if user:
        logger.info(f"User found: {user}")
    else:
        logger.warning(f"User with ID {user_id} not found in the database")
    return user


def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    logger.debug(f"Fetching users from URL: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    raise requests.HTTPError
