import json
import os
import logging

logger = logging.getLogger(__name__)

def read_config(file_path='config.json'):
    """
    Reads a configuration file and returns its contents as a dictionary.

    :param file_path: The path to the configuration file (default: 'config.json').
    :return: A dictionary containing the configuration.
    :raises: FileNotFoundError if the file is not found.
             json.JSONDecodeError if the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"Configuration file not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON in the configuration file: {e}")
        raise
