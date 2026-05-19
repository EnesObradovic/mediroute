import urllib.request
import json

SUPABASE_URL = 'https://phdmnzsdyjhqoqiqwmho.supabase.co'
SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBoZG1uenNkeWpocW9xaXF3bWhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc1NzAzMzksImV4cCI6MjA5MzE0NjMzOX0.zUoYTYjp8Shva1iSVE0oW1ukGpiEOCghPiqc__WisPg'

def check_image(url):
    if not url:
        return "Empty"
    try:
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as res:
            return res.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return f"Error: {e}"

def test_all_images():
    headers = {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': f"Bearer {SUPABASE_ANON_KEY}"
    }
    
    req = urllib.request.Request(f"{SUPABASE_URL}/rest/v1/blogs?select=slug,title,image_url,author_image", headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            blogs = json.loads(response.read().decode('utf-8'))
            print(f"Testing {len(blogs)} blogs for broken images...\n")
            for b in blogs:
                cover_status = check_image(b.get('image_url'))
                author_status = check_image(b.get('author_image'))
                print(f"Blog: {b['slug']}")
                print(f"  - Cover:  {cover_status} | {b.get('image_url')}")
                print(f"  - Author: {author_status} | {b.get('author_image')}")
                print("-" * 50)
    except Exception as e:
        print("Error checking Supabase blogs:", e)

if __name__ == '__main__':
    test_all_images()
