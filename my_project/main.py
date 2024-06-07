import logging
import yaml
import csv
import os
from my_functions.my_functions import add, multiply, divide
from shapes.shapes import Square, Circle, Rectangle


# Function to read YAML file
def read_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def run():

    # Creating a logger
    logger = logging.getLogger(__name__)

    # Configuring the logging system
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Logging messages at different levels
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    # Read the YAML configuration file
    config = read_yaml("config.yaml")

    # Extract values into variables
    project_name = config["project"]["name"]
    project_version = config["project"]["version"]

    python_kernel_path = config["paths"]["python_kernel"]
    data_directory = config["paths"]["data_dir"]

    debug_mode = config["settings"]["debug"]
    max_retries = config["settings"]["max_retries"]

    # Print variables to verify
    logger.debug(f"Project Name: {project_name}")
    logger.debug(f"Project Version: {project_version}")
    logger.debug(f"Python Kernel Path: {python_kernel_path}")
    logger.debug(f"Data Directory: {data_directory}")
    logger.debug(f"Debug Mode: {debug_mode}")
    logger.debug(f"Max Retries: {max_retries}")

    # Ensure the 'tmp' directory exists
    os.makedirs("tmp", exist_ok=True)

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
    with open(csv_file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

    logger.info(f"Data has been written to {csv_file_path}")

    # Test module level logging
    add(2, 3)
    multiply(2, 3)
    divide(2, 3)

    sq = Square(5)
    sq.area()

    ci = Circle(5)
    ci.area()

    re = Rectangle(5, 10)
    re.area()


if __name__ == "__main__":
    run()
