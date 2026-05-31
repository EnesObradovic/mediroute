import urllib.request
import json
import os
from datetime import datetime

import re

SUPABASE_URL = 'https://phdmnzsdyjhqoqiqwmho.supabase.co'
SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBoZG1uenNkeWpocW9xaXF3bWhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc1NzAzMzksImV4cCI6MjA5MzE0NjMzOX0.zUoYTYjp8Shva1iSVE0oW1ukGpiEOCghPiqc__WisPg'

def strip_html(html_str):
    if not html_str:
        return ""
    clean = re.compile('<.*?>')
    text = re.sub(clean, '', html_str)
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    return text.strip()

def detect_lang(title, content):
    turkish_words = [' ve ', ' bir ', ' için ', ' bu ', ' da ', ' de ', ' ama ', ' veya ', ' rehber', ' ameliyat', ' sonras']
    clean_text = strip_html(content).lower()
    
    tr_count = sum(1 for w in turkish_words if w in clean_text or w in title.lower())
    if tr_count >= 2:
        return 'tr'
    return 'en'

def fetch_supabase_blogs():
    print("Fetching active blog posts from Supabase...")
    url = f"{SUPABASE_URL}/rest/v1/blogs?select=slug,created_at,title,content&status=eq.published"
    # Fallback to query all if no status column filter is needed
    url_all = f"{SUPABASE_URL}/rest/v1/blogs?select=slug,created_at,title,content"
    
    headers = {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': f"Bearer {SUPABASE_ANON_KEY}"
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print("Status filter failed or returned error, trying all blogs...", e)
        try:
            req = urllib.request.Request(url_all, headers=headers)
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode('utf-8'))
        except Exception as ex:
            print("Failed to fetch blogs from Supabase REST API:", ex)
            return []

def generate_xml():
    blogs = fetch_supabase_blogs()
    print(f"Discovered {len(blogs)} blog articles.")

    today = datetime.today().strftime('%Y-%m-%d')
    
    # Base URLs with alternate languages
    base_urls = [
        {
            "loc": "https://medirouteturkey.com",
            "priority": "1.0",
            "changefreq": "weekly",
            "lastmod": "2026-05-19",
            "multilingual": True
        },
        {
            "loc": "https://medirouteturkey.com/treatments",
            "priority": "0.85",
            "changefreq": "weekly",
            "lastmod": "2026-05-19",
            "multilingual": True
        },
        {
            "loc": "https://medirouteturkey.com/about",
            "priority": "0.7",
            "changefreq": "monthly",
            "lastmod": "2026-05-19",
            "multilingual": True
        },
        {
            "loc": "https://medirouteturkey.com/compare",
            "priority": "0.8",
            "changefreq": "weekly",
            "lastmod": "2026-05-19",
            "multilingual": True
        },
        {
            "loc": "https://medirouteturkey.com/blog",
            "priority": "0.7",
            "changefreq": "weekly",
            "lastmod": "2026-05-19",
            "multilingual": True
        },
        {
            "loc": "https://medirouteturkey.com/contact",
            "priority": "0.6",
            "changefreq": "monthly",
            "lastmod": "2026-05-19",
            "multilingual": True
        },
        {
            "loc": "https://medirouteturkey.com/faq",
            "priority": "0.6",
            "changefreq": "monthly",
            "lastmod": "2026-05-19",
            "multilingual": True
        },
        {
            "loc": "https://medirouteturkey.com/auth",
            "priority": "0.5",
            "changefreq": "monthly",
            "lastmod": "2026-05-19",
            "multilingual": False
        },
        {
            "loc": "https://medirouteturkey.com/treatment/hair-transplant",
            "priority": "0.9",
            "changefreq": "weekly",
            "lastmod": "2026-05-19",
            "multilingual": True
        },
        {
            "loc": "https://medirouteturkey.com/treatment/dental",
            "priority": "0.9",
            "changefreq": "weekly",
            "lastmod": "2026-05-19",
            "multilingual": True
        },
        {
            "loc": "https://medirouteturkey.com/treatment/aesthetics",
            "priority": "0.9",
            "changefreq": "weekly",
            "lastmod": "2026-05-19",
            "multilingual": True
        },
        {
            "loc": "https://medirouteturkey.com/treatment/bariatric",
            "priority": "0.9",
            "changefreq": "weekly",
            "lastmod": "2026-05-19",
            "multilingual": True
        },
        {
            "loc": "https://medirouteturkey.com/treatment/eye-surgery",
            "priority": "0.9",
            "changefreq": "weekly",
            "lastmod": "2026-05-19",
            "multilingual": True
        }
    ]

    xml = '<?xml version="1.0" ?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'

    # 1. Append Base URLs
    for url in base_urls:
        xml += '  <url>\n'
        xml += f'    <loc>{url["loc"]}</loc>\n'
        xml += f'    <lastmod>{url["lastmod"]}</lastmod>\n'
        xml += f'    <changefreq>{url["changefreq"]}</changefreq>\n'
        xml += f'    <priority>{url["priority"]}</priority>\n'
        
        if url["multilingual"]:
            xml += f'    <xhtml:link rel="alternate" hreflang="en" href="{url["loc"]}?lang=en"/>\n'
            xml += f'    <xhtml:link rel="alternate" hreflang="tr" href="{url["loc"]}?lang=tr"/>\n'
            xml += f'    <xhtml:link rel="alternate" hreflang="ar" href="{url["loc"]}?lang=ar"/>\n'
            xml += f'    <xhtml:link rel="alternate" hreflang="de" href="{url["loc"]}?lang=de"/>\n'
            xml += f'    <xhtml:link rel="alternate" hreflang="fr" href="{url["loc"]}?lang=fr"/>\n'
            xml += f'    <xhtml:link rel="alternate" hreflang="x-default" href="{url["loc"]}"/>\n'
            
        xml += '  </url>\n'

    # 2. Append Dynamic Blog URLs
    for b in blogs:
        slug = b['slug']
        created_at_raw = b.get('created_at', today)
        try:
            # Extract date part (YYYY-MM-DD)
            lastmod = created_at_raw.split('T')[0]
        except:
            lastmod = today
            
        xml += '  <url>\n'
        xml += f'    <loc>https://medirouteturkey.com/blog/{slug}</loc>\n'
        xml += f'    <lastmod>{lastmod}</lastmod>\n'
        xml += '    <changefreq>monthly</changefreq>\n'
        xml += '    <priority>0.7</priority>\n'
        
        # Detect language of the blog post
        blog_lang = detect_lang(b.get('title', ''), b.get('content', ''))

        # Only output native language and x-default to prevent search engine indexing duplicate content penalties
        xml += f'    <xhtml:link rel="alternate" hreflang="{blog_lang}" href="https://medirouteturkey.com/blog/{slug}"/>\n'
        xml += f'    <xhtml:link rel="alternate" hreflang="x-default" href="https://medirouteturkey.com/blog/{slug}"/>\n'
        
        xml += '  </url>\n'

    xml += '</urlset>\n'
    return xml

def save_sitemaps():
    xml_content = generate_xml()
    
    # Save to root
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)
    print("Successfully wrote sitemap.xml to root directory.")
    
    # Save to deploy-bundle
    deploy_path = 'deploy-bundle/sitemap.xml'
    if os.path.exists('deploy-bundle'):
        with open(deploy_path, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        print("Successfully wrote sitemap.xml to deploy-bundle directory.")

if __name__ == '__main__':
    save_sitemaps()
