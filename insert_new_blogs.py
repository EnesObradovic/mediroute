#!/usr/bin/env python3
import os
import re
import json
import urllib.request

SUPABASE_URL = 'https://phdmnzsdyjhqoqiqwmho.supabase.co'
SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBoZG1uenNkeWpocW9xaXF3bWhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc1NzAzMzksImV4cCI6MjA5MzE0NjMzOX0.zUoYTYjp8Shva1iSVE0oW1ukGpiEOCghPiqc__WisPg'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BLOG_DIR = os.path.join(BASE_DIR, 'blog')

headers = {
    'apikey': SUPABASE_ANON_KEY,
    'Authorization': f"Bearer {SUPABASE_ANON_KEY}",
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

def parse_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    slug = os.path.splitext(os.path.basename(file_path))[0]
    
    # Extract Title
    title_match = re.search(r'<title>(.*?) \| MediRoute</title>', html)
    title = title_match.group(1) if title_match else ""
    
    # Extract Category
    cat_match = re.search(r'<span class="tag-pill.*?>(.*?)</span>', html)
    category = cat_match.group(1) if cat_match else "Guide"
    
    # Extract Image URL
    img_match = re.search(r'<meta property="og:image" content="(.*?)"/>', html)
    image_url = img_match.group(1) if img_match else ""
    
    # Extract Author Name & Title/Specialty from JSON-LD schema
    schema_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    author = "MediRoute Team"
    author_specialty = ""
    if schema_match:
        try:
            schema = json.loads(schema_match.group(1).strip())
            author_data = schema.get('author', {})
            if isinstance(author_data, dict):
                author = author_data.get('name', author)
                author_specialty = author_data.get('jobTitle', author_specialty)
        except Exception as e:
            print(f"Failed to parse JSON-LD schema for {slug}: {e}")
            
    # Extract Author Image
    author_img_match = re.search(r'<div class="author-avatar">\s*<img.*?src="(.*?)"', html, re.DOTALL)
    author_image = author_img_match.group(1) if author_img_match else ""
    
    # Extract Content Body (the inside of <article class="article-body fade-up">)
    content_match = re.search(r'<article class="article-body fade-up">(.*?)</article>', html, re.DOTALL)
    content = content_match.group(1).strip() if content_match else ""
    
    # Clean content of comments or extra whitespace if any, but keep HTML formatting
    
    return {
        "title": title,
        "slug": slug,
        "category": category,
        "image_url": image_url,
        "author": author,
        "author_title": author_specialty,
        "author_specialty": author_specialty,
        "author_image": author_image,
        "status": "published",
        "content": content,
        "created_at": "2026-06-05T10:00:00Z"
    }

def check_blog_exists(slug):
    url = f"{SUPABASE_URL}/rest/v1/blogs?slug=eq.{slug}&select=id"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            existing = json.loads(response.read().decode('utf-8'))
            return len(existing) > 0
    except Exception as e:
        print(f"Error checking if {slug} exists: {e}")
        return False

def insert_blog(blog_data):
    url = f"{SUPABASE_URL}/rest/v1/blogs"
    data_bytes = json.dumps(blog_data).encode('utf-8')
    req = urllib.request.Request(url, data=data_bytes, headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(f"Successfully inserted blog: {blog_data['title']} (Slug: {blog_data['slug']})")
            return True
    except Exception as e:
        print(f"Error inserting blog {blog_data['slug']}: {e}")
        if hasattr(e, 'read'):
            print("Response:", e.read().decode('utf-8'))
        return False

def run():
    print("Scanning blog directory...")
    new_slugs = [
        "rhinoplasty-turkey-vs-uk-real-cost-comparison-2026",
        "fue-hair-transplant-shock-loss-week-by-week-timeline",
        "istanbul-aesthetic-surgery-districts-insider-guide",
        "flying-home-after-surgery-turkey-medical-protocol",
        "turkey-bbl-safety-regulations-2025-what-changed",
        "dental-veneers-turkey-5-year-longevity-data",
        "hidden-costs-medical-tourism-turkey-real-budget",
        "gastric-sleeve-turkey-vs-nhs-waiting-list-guide",
        "lasik-eye-surgery-istanbul-vs-london-complete-guide",
        "lifetime-guarantee-turkish-clinics-what-it-actually-means"
    ]
    
    success_count = 0
    for slug in new_slugs:
        file_path = os.path.join(BLOG_DIR, f"{slug}.html")
        if not os.path.exists(file_path):
            print(f"File {file_path} not found! Skipping.")
            continue
            
        print(f"Processing {slug}...")
        try:
            blog_data = parse_html_file(file_path)
            
            if check_blog_exists(slug):
                print(f"Blog '{slug}' already exists in Supabase. Skipping.")
                continue
                
            if insert_blog(blog_data):
                success_count += 1
        except Exception as e:
            print(f"Failed to process or insert {slug}: {e}")
            
    print(f"Insertion process completed. {success_count} new blogs inserted.")

if __name__ == '__main__':
    run()
