import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
original_css_path = os.path.join(BASE_DIR, 'static', 'css', 'style.css')
missing_css_path = os.path.join(BASE_DIR, 'missing_style.css')

if not os.path.exists(missing_css_path):
    print(f"Source file not found: {missing_css_path}")
else:
    with open(missing_css_path, 'r', encoding='utf-8') as f_missing:
        missing_content = f_missing.read()
    with open(original_css_path, 'a', encoding='utf-8') as f_orig:
        f_orig.write('\n' + missing_content)
    print("Successfully appended missing CSS to style.css")
