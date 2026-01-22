import json
import re

def check_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract schema
        match = re.search(r'{% schema %}(.*?){% endschema %}', content, re.DOTALL)
        if not match:
            print(f"ERROR: No schema tags found in {path}")
            return
            
        json_str = match.group(1).strip()
        try:
            data = json.loads(json_str)
            print(f"SUCCESS: Schema in {path} is valid JSON.")
            # Check for required properties
            if 'name' not in data:
                print("WARNING: 'name' property missing in schema")
        except json.JSONDecodeError as e:
            print(f"CRITICAL ERROR: Invalid JSON in {path}")
            print(e)
            # Print context
            lines = json_str.split('\n')
            if e.lineno <= len(lines):
                 print(f"Error around line {e.lineno}: {lines[e.lineno-1]}")

    except Exception as e:
        print(f"System Error: {e}")

check_file('sections/mobile-bar.liquid')
