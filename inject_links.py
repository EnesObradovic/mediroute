#!/usr/bin/env python3
"""
MediRoute Blog Internal Link Injector
Analyzes blog content in Supabase, injects contextually relevant internal links
for SEO/GEO (avoiding self-links and duplicate links), updates Supabase,
and runs pre-rendering.
"""
import json
import os
import re
import urllib.request
import urllib.parse
import subprocess

SUPABASE_URL = 'https://phdmnzsdyjhqoqiqwmho.supabase.co'
SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBoZG1uenNkeWpocW9xaXF3bWhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc1NzAzMzksImV4cCI6MjA5MzE0NjMzOX0.zUoYTYjp8Shva1iSVE0oW1ukGpiEOCghPiqc__WisPg'

headers = {
    'apikey': SUPABASE_ANON_KEY,
    'Authorization': f"Bearer {SUPABASE_ANON_KEY}",
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

# Link mappings
# Priority order: specific blogs, specific treatments, generic pages
LINK_RULES_EN = [
    # Blogs
    {"terms": ["General Medical Commission", "GMC", "verify Turkish plastic surgeon credentials", "TTB registration"], "slug": "how-to-verify-turkish-plastic-surgeon-credentials"},
    {"terms": ["flying home after surgery", "flying home", "flight after surgery", "fit-to-fly"], "slug": "flying-home-after-surgery-turkey-medical-protocol"},
    {"terms": ["shock loss", "FUE hair transplant shock loss", "shock loss timeline"], "slug": "fue-hair-transplant-shock-loss-week-by-week-timeline"},
    {"terms": ["gastric sleeve leak", "leak test", "leak check"], "slug": "gastric-sleeve-leak-test-protocols-turkey"},
    {"terms": ["gastric sleeve in Turkey vs NHS", "NHS waiting list", "waiting list reality"], "slug": "gastric-sleeve-turkey-vs-nhs-waiting-list-guide"},
    {"terms": ["hyperbaric oxygen", "HBOT", "follicular graft survival"], "slug": "hbot-prp-graft-survival-hair-transplant-turkey"},
    {"terms": ["hidden costs", "medical tourism Turkey cost", "real budget", "extra nights", "revision consultations"], "slug": "hidden-costs-medical-tourism-turkey-real-budget"},
    {"terms": ["LASIK in Istanbul", "lasik eye surgery", "lasik vs london"], "slug": "lasik-eye-surgery-istanbul-vs-london-complete-guide"},
    {"terms": ["lifetime guarantee", "lifetime guarantees", "clinic guarantees"], "slug": "lifetime-guarantee-turkish-clinics-what-it-actually-means"},
    {"terms": ["liposuction standards", "clinical facility standards", "A-Group hospitals"], "slug": "liposuction-turkey-vs-uk-clinical-facility-standards"},
    {"terms": ["BBL safety regulations", "BBL safety", "BBL regulations"], "slug": "turkey-bbl-safety-regulations-2026-what-changed"},
    {"terms": ["E-Max vs Zirconium", "flexural strength", "enamel prep"], "slug": "veneers-prep-tolerances-zirconium-vs-emax"},
    {"terms": ["zirconium vs porcelain", "porcelain crowns"], "slug": "zirconium-vs-porcelain-crowns-turkey"},
    {"terms": ["recovery tips", "medical holiday", "recovering abroad"], "slug": "recovering-abroad-medical-holiday-tips"},
    {"terms": ["rhinoplasty cost", "rhinoplasty turkey vs uk", "nose job cost"], "slug": "rhinoplasty-turkey-vs-uk-real-cost-comparison-2026"},
    {"terms": ["Istanbul aesthetic surgery districts", "districts", "Nişantaşı", "Kadıköy"], "slug": "istanbul-aesthetic-surgery-districts-insider-guide"},
    
    # Treatments
    {"terms": ["hair transplant", "hair restoration"], "url": "/treatment/hair-transplant"},
    {"terms": ["dental veneers", "veneers"], "url": "/treatment/dental-veneers"},
    {"terms": ["rhinoplasty", "nose job"], "url": "/treatment/rhinoplasty"},
    {"terms": ["gastric sleeve", "bariatric surgery"], "url": "/treatment/gastric-sleeve"},
    {"terms": ["BBL", "Brazilian Butt Lift"], "url": "/treatment/bbl"},
    {"terms": ["liposuction", "lipo"], "url": "/treatment/liposuction"},
    {"terms": ["laser eye surgery", "SMILE"], "url": "/treatment/lasik"},
    
    # Generic
    {"terms": ["free comparison tool", "compare clinics"], "url": "/compare"},
    {"terms": ["frequently asked questions", "FAQ section"], "url": "/faq"},
    {"terms": ["all treatments", "treatment options"], "url": "/treatments"}
]

LINK_RULES_TR = [
    # Blogs
    {"terms": ["şok dökülme", "şok dökülme süreci"], "slug": "sac-ekimi-sonrasi-sok-dokulme"},
    {"terms": ["saç ekimi", "saç ekimi fiyatları", "saç ekimi teknikleri"], "slug": "sac-ekim-rehberi"},
    {"terms": ["BBL", "BBL ameliyatı", "bbl ameliyatı rehberi"], "slug": "turkiyede-bbl-ameliyati-rehberi"},
    
    # Treatments
    {"terms": ["saç ekimi tedavisi"], "url": "/treatment/hair-transplant"},
    {"terms": ["diş kaplama", "lamina kaplama"], "url": "/treatment/dental-veneers"},
    {"terms": ["burun estetiği"], "url": "/treatment/rhinoplasty"},
    {"terms": ["tüp mide"], "url": "/treatment/gastric-sleeve"},
    
    # Generic
    {"terms": ["karşılaştır", "klinik karşılaştırma"], "url": "/compare"},
    {"terms": ["sıkça sorulan sorular", "SSS"], "url": "/faq"},
    {"terms": ["tedavilerimiz", "tüm tedaviler"], "url": "/treatments"}
]

def fetch_all_blogs():
    print("Fetching blogs from Supabase...")
    url = f"{SUPABASE_URL}/rest/v1/blogs?select=*"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching blogs: {e}")
        return []

def update_blog_content(blog_id, content):
    url = f"{SUPABASE_URL}/rest/v1/blogs?id=eq.{blog_id}"
    data_bytes = json.dumps({"content": content}).encode('utf-8')
    req = urllib.request.Request(url, data=data_bytes, headers=headers, method='PATCH')
    try:
        with urllib.request.urlopen(req) as response:
            return True
    except Exception as e:
        print(f"Error patching blog {blog_id}: {e}")
        if hasattr(e, 'read'):
            print("Response:", e.read().decode('utf-8'))
        return False

def detect_language(content, title):
    turkish_words = [' ve ', ' bir ', ' için ', ' bu ', ' da ', ' de ', ' ama ', ' veya ', ' rehber', ' ameliyat', ' sonras']
    clean_text = content.lower()
    tr_count = sum(1 for w in turkish_words if w in clean_text or w in title.lower())
    return 'tr' if tr_count >= 2 else 'en'

def inject_links_into_html(html_content, rules, current_slug):
    # Split the HTML by tags to avoid changing text inside tags or already inside links
    tokens = re.split(r'(<[^>]+>)', html_content)
    
    # Pre-compile the regexes for all terms to avoid repeating it
    compiled_rules = []
    for r in rules:
        target_url = r.get('url')
        if not target_url:
            target_slug = r.get('slug')
            # If the link points to the current blog post, skip it to avoid self-linking
            if target_slug == current_slug:
                continue
            target_url = f"/blog/{target_slug}"
            
        for term in r['terms']:
            # Use negative lookahead/lookbehind to ensure we match whole words and not parts of words
            pattern = re.compile(r'\b(' + re.escape(term) + r')\b', re.IGNORECASE)
            compiled_rules.append((pattern, target_url))

    # We track which URLs have been injected to avoid multiple links to the same page
    injected_urls = set()
    
    in_link = False
    
    for i in range(len(tokens)):
        token = tokens[i]
        if not token:
            continue
            
        # Check tag type
        if token.startswith('<'):
            tag_name_match = re.match(r'^<(/?[a-zA-Z0-9]+)', token)
            if tag_name_match:
                tag_name = tag_name_match.group(1).lower()
                if tag_name == 'a':
                    in_link = True
                elif tag_name == '/a':
                    in_link = False
            continue
            
        # If we are inside an <a> tag, do not modify
        if in_link:
            continue
            
        # We are in text content! Apply the rules
        # To avoid replacing a term multiple times or nested replacements, we perform them one by one
        # but only if the URL hasn't been injected yet in this article.
        for pattern, url in compiled_rules:
            if url in injected_urls:
                continue
                
            match = pattern.search(token)
            if match:
                # Replace the first occurrence of the term in this text token
                matched_text = match.group(1)
                replacement = f'<a href="{url}">{matched_text}</a>'
                tokens[i] = pattern.sub(replacement, token, count=1)
                injected_urls.add(url)
                # Re-fetch token after replacement
                token = tokens[i]
                
    return "".join(tokens)

def main():
    blogs = fetch_all_blogs()
    if not blogs:
        print("No blogs found.")
        return
        
    print(f"Loaded {len(blogs)} blogs from database.")
    
    updated_count = 0
    for blog in blogs:
        slug = blog.get('slug')
        title = blog.get('title')
        content = blog.get('content', '')
        blog_id = blog.get('id')
        
        lang = detect_language(content, title)
        rules = LINK_RULES_TR if lang == 'tr' else LINK_RULES_EN
        
        # Strip existing identical links if any (optional/not needed since we avoid re-linking if already linked)
        updated_content = inject_links_into_html(content, rules, slug)
        
        if updated_content != content:
            print(f"Injecting links into '{slug}' ({lang})...")
            if update_blog_content(blog_id, updated_content):
                print(f"✅ Updated content for '{slug}' in Supabase.")
                updated_count += 1
            else:
                print(f"❌ Failed to update content for '{slug}'.")
        else:
            print(f"No new links to inject for '{slug}'.")
            
    print(f"Successfully updated {updated_count} blogs in Supabase.")
    
    # 5. Run pre-renderer to update all local files
    print("Running pre_render_blogs.py to update local files...")
    subprocess.run(["python3", "pre_render_blogs.py"], check=True)
    
    # 6. Run verify script
    print("Running verify_fixes.py...")
    subprocess.run(["python3", "verify_fixes.py"], check=True)
    
if __name__ == '__main__':
    main()
