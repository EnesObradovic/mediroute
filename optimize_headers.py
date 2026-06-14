#!/usr/bin/env python3
import os
import re
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Files to optimize in base directory
html_files = [
    'index.html',
    'about.html',
    'contact.html',
    'blog.html',
    'compare.html',
    'faq.html',
    'treatments.html',
    'treatment.html',
    'blog-template.html',
    'treatment-template.html',
    'auth.html',
    'admin.html',
    'patient-dashboard.html',
    '404.html'
]

preconnect_tags = """  <link rel="preconnect" href="https://images.unsplash.com" crossorigin />
  <link rel="dns-prefetch" href="https://images.unsplash.com" />"""

def optimize_file(filename):
    path = os.path.join(BASE_DIR, filename)
    if not os.path.exists(path):
        return False
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if already preconnected to unsplash
    if 'images.unsplash.com' in content:
        return False
        
    # Find </head> tag and insert preconnect tags right before it
    if '</head>' in content:
        updated = content.replace('</head>', f'{preconnect_tags}\n</head>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Optimized headers in {filename}")
        return True
    return False

def main():
    optimized_count = 0
    for filename in html_files:
        if optimize_file(filename):
            optimized_count += 1
            
    print(f"Header optimization complete. {optimized_count} files updated.")
    
    # Sync with deploy bundle
    if optimized_count > 0:
        print("Running sync_deploy_bundle.py...")
        subprocess.run(["python3", "sync_deploy_bundle.py"], check=True)

if __name__ == '__main__':
    main()
