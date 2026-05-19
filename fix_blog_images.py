import urllib.request
import json

SUPABASE_URL = 'https://phdmnzsdyjhqoqiqwmho.supabase.co'
SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBoZG1uenNkeWpocW9xaXF3bWhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc1NzAzMzksImV4cCI6MjA5MzE0NjMzOX0.zUoYTYjp8Shva1iSVE0oW1ukGpiEOCghPiqc__WisPg'

updates = [
    {
        "slug": "sac-ekim-rehberi",
        "updates": {
            "image_url": "https://images.unsplash.com/photo-1622335088251-89c09c9b58ad?auto=format&fit=crop&w=800&q=80",
            "author": "Dr. Serkan Aygın",
            "author_title": "Hair Restoration Specialist",
            "author_specialty": "Trikoloji Uzmanı & Cerrah",
            "author_image": "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=150&h=150&q=80"
        }
    },
    {
        "slug": "ultimate-guide-hair-transplant-turkey-2026",
        "updates": {
            # Replace dental/teeth cover with a highly relevant hair clinic/examination cover
            "image_url": "https://images.unsplash.com/photo-1566083042913-671534a759fc?auto=format&fit=crop&w=800&q=80"
        }
    },
    {
        "slug": "dental-veneers-istanbul-journey",
        "updates": {
            "author": "Dr. Canan Demirel",
            "author_title": "Cosmetic Dentist",
            "author_specialty": "Prosthodontist Specialist",
            "author_image": "https://images.unsplash.com/photo-1594824813573-246434de83fb?auto=format&fit=crop&w=150&h=150&q=80"
        }
    },
    {
        "slug": "recovering-abroad-medical-holiday-tips",
        "updates": {
            # Replace medical clinical image with a relaxing premium travel wellness cover
            "image_url": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=800&q=80",
            "author": "MediRoute Medical Board",
            "author_title": "Editorial Team",
            "author_specialty": "Health Tourism Advisory",
            "author_image": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=150&h=150&q=80"
        }
    }
]

def apply_blog_updates():
    headers = {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': f"Bearer {SUPABASE_ANON_KEY}",
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
    }
    
    print("Starting blog image and author metadata repair in Supabase...")
    success_count = 0
    
    for u in updates:
        slug = u['slug']
        blog_updates = u['updates']
        
        # In Supabase REST API, patch endpoint is f"{SUPABASE_URL}/rest/v1/blogs?slug=eq.{slug}"
        patch_url = f"{SUPABASE_URL}/rest/v1/blogs?slug=eq.{slug}"
        data_bytes = json.dumps(blog_updates).encode('utf-8')
        
        try:
            req = urllib.request.Request(patch_url, data=data_bytes, headers=headers, method='PATCH')
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode('utf-8'))
                print(f"Successfully repaired blog: {slug}")
                success_count += 1
        except Exception as e:
            print(f"Error repairing blog '{slug}':", e)
            
    print(f"Repair complete. {success_count}/{len(updates)} blogs updated successfully.")

if __name__ == '__main__':
    apply_blog_updates()
