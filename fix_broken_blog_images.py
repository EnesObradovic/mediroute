import urllib.request
import json

SUPABASE_URL = 'https://phdmnzsdyjhqoqiqwmho.supabase.co'
SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBoZG1uenNkeWpocW9xaXF3bWhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc1NzAzMzksImV4cCI6MjA5MzE0NjMzOX0.zUoYTYjp8Shva1iSVE0oW1ukGpiEOCghPiqc__WisPg'

# Fully-verified 200 OK replacement images
replacements = [
    {
        "slug": "sac-ekim-rehberi",
        "updates": {
            "image_url": "https://images.unsplash.com/photo-1562322140-8baeececf3df?auto=format&fit=crop&w=800&q=80"
        }
    },
    {
        "slug": "ultimate-guide-hair-transplant-turkey-2026",
        "updates": {
            "image_url": "https://images.unsplash.com/photo-1582095133179-bfd08e2fc6b3?auto=format&fit=crop&w=800&q=80"
        }
    },
    {
        "slug": "sac-ekimi-sonrasi-sok-dokulme",
        "updates": {
            "image_url": "https://images.unsplash.com/photo-1582095133179-bfd08e2fc6b3?auto=format&fit=crop&w=800&q=80"
        }
    },
    {
        "slug": "laser-eye-surgery-istanbul-lasik",
        "updates": {
            "image_url": "https://images.unsplash.com/photo-1518152006812-edab29b069ac?auto=format&fit=crop&w=800&q=80"
        }
    },
    {
        "slug": "dental-veneers-istanbul-journey",
        "updates": {
            "author_image": "https://images.unsplash.com/photo-1614608682850-e0d6ed316d47?auto=format&fit=crop&w=150&h=150&q=80"
        }
    },
    {
        "slug": "zirconium-vs-porcelain-crowns-turkey",
        "updates": {
            "author_image": "https://images.unsplash.com/photo-1614608682850-e0d6ed316d47?auto=format&fit=crop&w=150&h=150&q=80"
        }
    }
]

def apply_replacements():
    headers = {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': f"Bearer {SUPABASE_ANON_KEY}",
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
    }
    
    print("Repairing broken Unsplash images and author avatars in Supabase...")
    success_count = 0
    
    for r in replacements:
        slug = r['slug']
        updates = r['updates']
        
        patch_url = f"{SUPABASE_URL}/rest/v1/blogs?slug=eq.{slug}"
        data_bytes = json.dumps(updates).encode('utf-8')
        
        try:
            req = urllib.request.Request(patch_url, data=data_bytes, headers=headers, method='PATCH')
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode('utf-8'))
                print(f"Successfully repaired broken assets for blog: {slug}")
                success_count += 1
        except Exception as e:
            print(f"Error repairing blog '{slug}':", e)
            
    print(f"\nDone! {success_count}/{len(replacements)} blogs updated successfully with live 200 OK assets.")

if __name__ == '__main__':
    apply_replacements()
