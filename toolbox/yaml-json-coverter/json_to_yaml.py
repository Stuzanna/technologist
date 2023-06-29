import yaml
import json

def json2yaml(current_json, new_yaml):
    """
    Takes a json file, converts it to a yaml, dumps in a directory.
    Requires pyyaml library.

    Args:
        json_file_location (string): path (relative?) to the json.
        output_dir (string): path (relative?) of destination where yaml should go.

    Returns:
        string: the output path to where to find the yaml.
    """
    with open(current_json, 'r') as f:
        data = json.load(f)
    
    with open(new_yaml, 'w') as f:
        yaml.dump(data, f)
    
    # print(new_yaml)
    # return 1

current_json = 'exampleInput.json'
new_yaml='exampleOutput.yaml'

json2yaml(current_json, new_yaml)