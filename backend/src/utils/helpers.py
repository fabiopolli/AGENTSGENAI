import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def validate_input(input_text):
    if not input_text or not isinstance(input_text, str):
        raise ValueError("A entrada precisa ser uma string válida.")
    return input_text.strip()
