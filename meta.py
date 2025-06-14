from tflite_support import metadata as _metadata
import os

# Path to the model
model_path = "./model/model_full.tflite"

try:
    # Check if the model file exists
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    # Load and display metadata
    print("Loading metadata...")
    displayer = _metadata.MetadataDisplayer.with_model_file(model_path)

    # Print metadata as JSON
    print("Metadata as JSON:")
    print(displayer.get_metadata_json())

    # Print associated files (e.g., labels.txt)
    associated_files = displayer.get_packed_associated_file_list()
    print("\nAssociated Files:")
    print(associated_files)

    # Print content of associated files
    if associated_files:
        for file_name in associated_files:
            file_content = displayer.get_associated_file(file_name)
            print(f"\nContent of {file_name}:")
            print(file_content.decode('utf-8'))

except ValueError as e:
    print(f"Error: No metadata found in the model. Details: {e}")
except Exception as e:
    print(f"Error reading metadata: {e}")
