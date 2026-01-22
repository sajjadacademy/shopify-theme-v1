import zipfile
import os

def create_shopify_zip(source_dir, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Calculate relative path from the source_dir
                # If source_dir is "theme", we want "theme/layout/theme.liquid" -> "layout/theme.liquid"
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
    print(f"Created {output_filename} successfully.")

if __name__ == "__main__":
    create_shopify_zip('theme', 'theme_fixed.zip')
