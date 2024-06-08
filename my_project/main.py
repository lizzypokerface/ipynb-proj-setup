import logging
import yaml
import csv
import os
from my_functions.my_functions import add, multiply, divide
from shapes.shapes import Square, Circle, Rectangle


# Function to read YAML file
def read_yaml(file_path):
    logger = logging.getLogger(__name__)
    logger.info(f"Reading YAML file from {file_path}")
    try:
        with open(file_path) as file:
            data = yaml.safe_load(file)
            logger.debug(f"YAML data: {data}")
            return data
    except Exception as e:
        logger.error(f"Failed to read YAML file: {e}")
        raise


def run():
    # Creating a logger
    logger = logging.getLogger(__name__)

    # Configuring the logging system
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Read the YAML configuration file
    try:
        config = read_yaml("config.yaml")
    except Exception as e:
        logger.critical(f"Failed to read configuration: {e}")
        return

    # Extract values into variables
    try:
        project_name = config["project"]["name"]
        project_version = config["project"]["version"]
        python_kernel_path = config["paths"]["python_kernel"]
        data_directory = config["paths"]["data_dir"]
        debug_mode = config["settings"]["debug"]
        max_retries = config["settings"]["max_retries"]

        logger.info(f"Project Name: {project_name}")
        logger.info(f"Project Version: {project_version}")
        logger.info(f"Python Kernel Path: {python_kernel_path}")
        logger.info(f"Data Directory: {data_directory}")
        logger.info(f"Debug Mode: {debug_mode}")
        logger.info(f"Max Retries: {max_retries}")
    except KeyError as e:
        logger.error(f"Missing configuration key: {e}")
        return

    # Ensure the 'tmp' directory exists
    try:
        os.makedirs("tmp", exist_ok=True)
        logger.info("'tmp' directory is ensured to exist")
    except Exception as e:
        logger.error(f"Failed to create 'tmp' directory: {e}")
        return

    # Define the CSV file path
    csv_file_path = os.path.join("tmp", "data.csv")

    # Create some made-up data
    data = [
        ["Name", "Age", "City"],
        ["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"],
        ["Charlie", 35, "Chicago"],
        ["David", 40, "Houston"],
        ["Eve", 22, "Phoenix"],
    ]

    # Write the data to the CSV file
    try:
        with open(csv_file_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)
        logger.info(f"Data has been written to {csv_file_path}")
    except Exception as e:
        logger.error(f"Failed to write data to CSV file: {e}")
        return

    # Test module level logging with detailed debug
    try:
        logger.debug("Testing add function")
        add_result = add(2, 3)
        logger.info(f"add(2, 3) = {add_result}")

        logger.debug("Testing multiply function")
        multiply_result = multiply(2, 3)
        logger.info(f"multiply(2, 3) = {multiply_result}")

        logger.debug("Testing divide function")
        divide_result = divide(2, 3)
        logger.info(f"divide(2, 3) = {divide_result}")
    except Exception as e:
        logger.error(f"Error in arithmetic operations: {e}")

    try:
        logger.debug("Testing Square class")
        sq = Square(5)
        sq_area = sq.area()
        logger.info(f"Square(5).area() = {sq_area}")

        logger.debug("Testing Circle class")
        ci = Circle(5)
        ci_area = ci.area()
        logger.info(f"Circle(5).area() = {ci_area}")

        logger.debug("Testing Rectangle class")
        re = Rectangle(5, 10)
        re_area = re.area()
        logger.info(f"Rectangle(5, 10).area() = {re_area}")
    except Exception as e:
        logger.error(f"Error in shape calculations: {e}")


if __name__ == "__main__":
    run()
