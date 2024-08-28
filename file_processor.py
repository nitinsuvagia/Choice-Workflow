# file_processor.py
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_file(file_path):
    """Reads content from a file."""
    with open(file_path, 'r') as file:
        return file.read()

def process_data(data):
    """Processes the data (e.g., Add Timestamp)."""

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    process_data = f"{timestamp}\n----------------------\n{data}\n\n"
    return process_data


def write_file(file_path, data):
    """Writes processed data to a file."""
    with open(file_path, 'w') as file:
        file.write(data)

def main():
    input_path = 'mnt\data\input.txt'
    output_path = 'mnt\data\output.txt'

    # Log when processing starts
    logging.info(f"Processing started. Reading from {input_file} and writing to {output_file}")

    try:

        # Step 1: Read from input file
        data = read_file(input_path)
        print(f"Original Data:\n{data}")

        # Step 2: Process the data
        processed_data = process_data(data)

        # Step 3: Write to output file
        write_file(output_path, processed_data)

        print(f"\nProcessed Data written to {output_path}"
    except Exception as e:
        # Log any errors
        logging.error(f"Error during processing: {str(e)}")

if __name__ == "__main__":
    main()
