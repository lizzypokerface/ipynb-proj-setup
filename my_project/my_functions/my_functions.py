import logging

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def add(number_one, number_two):
    logger.debug(f"Called add({number_one}, {number_two})")
    if not (isinstance(number_one, int) and isinstance(number_two, int)):
        logger.error("TypeError: Both arguments must be integers")
        raise TypeError("Both arguments must be integers")
    result = number_one + number_two
    logger.debug(f"Result of add: {result}")
    return result


def divide(number_one, number_two):
    logger.debug(f"Called divide({number_one}, {number_two})")
    if number_two == 0:
        logger.error("ValueError: The divisor cannot be zero")
        raise ValueError("The divisor cannot be zero")
    result = number_one / number_two
    logger.debug(f"Result of divide: {result}")
    return result


def multiply(number_one, number_two):
    logger.debug(f"Called multiply({number_one}, {number_two})")
    result = number_one * number_two
    logger.debug(f"Result of multiply: {result}")
    return result
