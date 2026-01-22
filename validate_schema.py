import re
import json

def validate_schema(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'{% schema %}(.*?){% endschema %}', content, re.DOTALL)
    if match:
        json_str = match.group(1)
        try:
            json.loads(json_str)
            print("Schema is VALID JSON.")
        except json.JSONDecodeError as e:
            print(f"Schema is INVALID JSON: {e}")
    else:
        print("No schema found.")

validate_schema('theme/sections/mobile-nav.liquid')
