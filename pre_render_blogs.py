#!/usr/bin/env python3
"""
MediRoute Blog Pre-renderer
Fetches published blogs from Supabase, processes blog-template.html,
and generates highly optimized static HTML pages under blog/ and deploy-bundle/blog/
"""
import os
import urllib.request
import json
import re
from datetime import datetime

# Supabase Credentials
SUPABASE_URL = 'https://phdmnzsdyjhqoqiqwmho.supabase.co'
SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBoZG1uenNkeWpocW9xaXF3bWhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc1NzAzMzksImV4cCI6MjA5MzE0NjMzOX0.zUoYTYjp8Shva1iSVE0oW1ukGpiEOCghPiqc__WisPg'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def fetch_blogs():
    print("[MR] Fetching published blogs from Supabase...")
    url = f"{SUPABASE_URL}/rest/v1/blogs?select=*&status=eq.published"
    headers = {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': f"Bearer {SUPABASE_ANON_KEY}"
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print("[MR] Error fetching blogs with status filter, trying to fetch all and filter in Python:", e)
        url_all = f"{SUPABASE_URL}/rest/v1/blogs?select=*"
        try:
            req = urllib.request.Request(url_all, headers=headers)
            with urllib.request.urlopen(req) as response:
                all_blogs = json.loads(response.read().decode('utf-8'))
                return [b for b in all_blogs if b.get('status') == 'published']
        except Exception as ex:
            print("[MR] Failed to fetch blogs from Supabase REST API:", ex)
            return []

def strip_html(html_str):
    if not html_str:
        return ""
    # Remove HTML tags
    clean = re.compile('<.*?>')
    text = re.sub(clean, '', html_str)
    # Decode basic HTML entities
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    return text.strip()

def get_excerpt(html_str, max_len=155):
    text = strip_html(html_str)
    if len(text) > max_len:
        return text[:max_len-3] + "..."
    return text

def format_turkish_date(date_str):
    if not date_str:
        return "31 Mayıs 2026"
    try:
        date_part = date_str.split('T')[0]
        dt = datetime.strptime(date_part, '%Y-%m-%d')
        months = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
        return f"{dt.day} {months[dt.month - 1]} {dt.year}"
    except Exception as e:
        return "Mayıs 2026"

def get_cat_class(cat):
    c = (cat or '').lower()
    if c in ['guide', 'rehber']:
        return 'bg-blue-900/60 border border-blue-400/30 text-blue-200'
    if c in ['tips', 'ipuçları', 'ipucu']:
        return 'bg-emerald-900/50 border border-emerald-400/30 text-emerald-200'
    if c in ['news', 'haber', 'haberler']:
        return 'bg-amber-900/50 border border-amber-400/30 text-amber-200'
    return 'bg-white/10 border border-white/20 text-blue-200'

def get_cat_pill_class(cat):
    c = (cat or '').lower()
    if c in ['guide', 'rehber']:
        return 'cat-guide'
    if c in ['tips', 'ipuçları', 'ipucu']:
        return 'cat-tips'
    if c in ['news', 'haber', 'haberler']:
        return 'cat-news'
    return 'cat-default'

def generate_related_html(blogs, current_id):
    related = [b for b in blogs if b.get('id') != current_id][:3]
    if not related:
        return ""
    
    html = ""
    for b in related:
        date_str = format_turkish_date(b.get('created_at'))
        excerpt = get_excerpt(b.get('content'), 80)
        img_html = ""
        if b.get('image_url'):
            img_html = f'<img loading="lazy" src="{b.get("image_url")}" alt="{b.get("title")}" style="width:100%;height:100%;object-fit:cover;">'
        else:
            img_html = '<i class="fa-solid fa-image text-3xl text-blue-200"></i>'
            
        html += f"""
          <a href="/blog/{b.get('slug')}" class="related-card">
            <div style="height:140px;background:linear-gradient(135deg,#E1E8FF,#C3D1FF);display:flex;align-items:center;justify-content:center;overflow:hidden;">
              {img_html}
            </div>
            <div style="padding:1rem;">
              <p style="font-size:.68rem;font-weight:700;color:#3B5FDD;margin-bottom:.4rem;">{b.get('category')}</p>
              <h3 style="font-size:.9rem;font-weight:700;color:#0A1F6B;line-height:1.3;margin-bottom:.3rem;">{b.get('title')}</h3>
              <p style="font-size:.78rem;color:#6B7280;line-height:1.5;">{excerpt}</p>
              <p style="font-size:.68rem;color:#94A3B8;margin-top:.5rem;">{date_str}</p>
            </div>
          </a>
        """
    return html

def render_all_blogs():
    print("[MR] Starting static blog pre-rendering...")
    
    # Ensure output directories exist
    os.makedirs(os.path.join(BASE_DIR, 'blog'), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, 'deploy-bundle', 'blog'), exist_ok=True)
    
    # Load template
    template_path = os.path.join(BASE_DIR, 'blog-template.html')
    if not os.path.exists(template_path):
        print(f"[MR] Error: Template file {template_path} not found!")
        return
        
    with open(template_path, 'r', encoding='utf-8') as f:
        template_html = f.read()
        
    blogs = fetch_blogs()
    if not blogs:
        print("[MR] No published blogs found or failed to fetch.")
        return
        
    print(f"[MR] Found {len(blogs)} published blogs to pre-render.")
    
    success_count = 0
    for blog in blogs:
        slug = blog.get('slug')
        title = blog.get('title')
        content = blog.get('content', '')
        category = blog.get('category', 'Guide')
        image_url = blog.get('image_url', 'https://images.unsplash.com/photo-1579684389782-64d84b5e905d?auto=format&fit=crop&w=800&q=80')
        author = blog.get('author', 'MediRoute Team')
        author_title = blog.get('author_title', '')
        author_specialty = blog.get('author_specialty', '')
        author_image = blog.get('author_image', '')
        created_at = blog.get('created_at')
        updated_at = blog.get('updated_at', created_at)
        
        excerpt = get_excerpt(content, 155)
        formatted_date = format_turkish_date(created_at)
        
        # Word count & Read time
        word_count = len(strip_html(content).split())
        read_time = max(1, int(word_count / 200) + 1)
        
        # 1. Update Title and Meta Description
        html = template_html
        html = html.replace('<title>Blog | MediRoute</title>', f'<title>{title} | MediRoute</title>')
        html = html.replace('<meta name="description" content="MediRoute blog article — expert health tourism advice."/>', f'<meta name="description" content="{excerpt}"/>')
        
        # 2. Add dynamic variables and pre-render marker in Script
        static_render_js = f'<script>window.STATIC_RENDERED = true; window.STATIC_BLOG_DATA = {json.dumps(blog)};</script>'
        html = html.replace('<body>', f'<body>\n{static_render_js}')
        
        # 3. Inject Open Graph and Twitter Card tags
        og_tags = f"""
  <meta property="og:title" content="{title} | MediRoute"/>
  <meta property="og:description" content="{excerpt}"/>
  <meta property="og:image" content="{image_url}"/>
  <meta property="og:url" content="https://medirouteturkey.com/blog/{slug}"/>
  <meta property="og:type" content="article"/>
  <meta name="twitter:card" content="summary_large_image"/>
  <meta name="twitter:title" content="{title} | MediRoute"/>
  <meta name="twitter:description" content="{excerpt}"/>
  <meta name="twitter:image" content="{image_url}"/>
  <!-- schema.org JSON-LD for Search Engines -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "{title}",
    "description": "{excerpt}",
    "image": "{image_url}",
    "datePublished": "{created_at}",
    "dateModified": "{updated_at}",
    "author": {{
      "@type": "Person",
      "name": "{author}",
      "jobTitle": "{author_specialty or 'Medical Writer'}"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "MediRoute",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://medirouteturkey.com/favicon.png"
      }}
    }},
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://medirouteturkey.com/blog/{slug}"
    }}
  }}
  </script>
        """
        html = html.replace('</head>', f'{og_tags}\n</head>')
        
        # 4. Fill Breadcrumb
        html = html.replace('<span class="text-blue-200" id="breadcrumb-title">Loading…</span>', f'<span class="text-blue-200" id="breadcrumb-title">{title}</span>')
        
        # 5. Fill Hero Tags
        hero_tags_placeholder = '<div id="hero-tags" class="flex flex-wrap gap-2 mb-4"></div>'
        hero_tags_content = f'<div id="hero-tags" class="flex flex-wrap gap-2 mb-4"><span class="tag-pill {get_cat_class(category)}">{category}</span></div>'
        html = html.replace(hero_tags_placeholder, hero_tags_content)
        
        # 6. Fill Hero Title (remove skeletons)
        hero_title_placeholder = """<h1 class="text-3xl md:text-4xl font-extrabold text-white leading-tight mb-4" id="hero-title">
      <div class="skeleton" style="height:38px;width:80%;margin-bottom:8px;"></div>
      <div class="skeleton" style="height:38px;width:55%;"></div>
    </h1>"""
        hero_title_content = f'<h1 class="text-3xl md:text-4xl font-extrabold text-white leading-tight mb-4" id="hero-title">{title}</h1>'
        html = html.replace(hero_title_placeholder, hero_title_content)
        
        # 7. Fill Hero Meta (Author, Date, Read Time)
        hero_meta_placeholder = '<div class="flex flex-wrap items-center gap-4 text-xs text-blue-300" id="hero-meta"></div>'
        hero_meta_content = f"""<div class="flex flex-wrap items-center gap-4 text-xs text-blue-300" id="hero-meta">
        <span class="flex items-center gap-1"><i class="fa-solid fa-user-pen"></i> {author}</span>
        <span class="flex items-center gap-1"><i class="fa-solid fa-calendar"></i> {formatted_date}</span>
        <span class="flex items-center gap-1"><i class="fa-solid fa-clock"></i> {read_time} dk okuma</span>
      </div>"""
        html = html.replace(hero_meta_placeholder, hero_meta_content)
        
        # 8. Cover Image
        cover_placeholder = """  <!-- Cover image -->
  <div id="cover-image-wrapper" class="mb-8 rounded-2xl overflow-hidden shadow-lg" style="display:none;">
    <img id="cover-image" src="" alt="" class="w-full" style="max-height:420px;object-fit:cover;">
  </div>"""
        cover_content = f"""  <!-- Cover image -->
  <div id="cover-image-wrapper" class="mb-8 rounded-2xl overflow-hidden shadow-lg" style="display:block;">
    <img id="cover-image" src="{image_url}" alt="{title}" class="w-full" style="max-height:420px;object-fit:cover;">
  </div>"""
        html = html.replace(cover_placeholder, cover_content)
        
        # 9. Article Body
        body_placeholder = """  <!-- Article body -->
  <article class="article-body fade-up" id="article-body">
    <!-- Skeleton -->
    <div class="skeleton" style="height:18px;width:100%;margin-bottom:12px"></div>
    <div class="skeleton" style="height:18px;width:92%;margin-bottom:12px"></div>
    <div class="skeleton" style="height:18px;width:85%;margin-bottom:20px"></div>
    <div class="skeleton" style="height:24px;width:60%;margin-bottom:14px"></div>
    <div class="skeleton" style="height:18px;width:100%;margin-bottom:12px"></div>
    <div class="skeleton" style="height:18px;width:95%;margin-bottom:12px"></div>
    <div class="skeleton" style="height:18px;width:78%;margin-bottom:20px"></div>
    <div class="skeleton" style="height:18px;width:88%;margin-bottom:12px"></div>
    <div class="skeleton" style="height:18px;width:100%;margin-bottom:12px"></div>
  </article>"""
        body_content = f"""  <!-- Article body -->
  <article class="article-body fade-up" id="article-body">
    {content}
  </article>"""
        html = html.replace(body_placeholder, body_content)
        
        # 10. Author Card
        author_placeholder = """  <!-- Author Profile Card -->
  <div id="author-card" class="author-card fade-up" style="display:none;">
    <div class="author-avatar" id="author-avatar">
      <i class="fa-solid fa-user-doctor"></i>
    </div>
    <div>
      <div class="flex items-center gap-2 flex-wrap mb-1">
        <h3 class="font-extrabold text-navy-900 text-base" id="author-name"></h3>
        <span class="author-badge"><i class="fa-solid fa-circle-check text-[9px]"></i> Doğrulanmış Uzman</span>
      </div>
      <p class="text-sm font-semibold text-navy-700" id="author-title-text"></p>
      <p class="text-xs text-gray-500 mt-0.5" id="author-specialty"></p>
    </div>
  </div>"""
        
        # Build author content
        full_author_name = f"{author_title} {author}".strip()
        avatar_content = f'<img loading="lazy" src="{author_image}" alt="{full_author_name}">' if author_image else '<i class="fa-solid fa-user-doctor"></i>'
        specialty_sub = "Medikal İçerik Danışmanı" if author_specialty else ""
        
        author_content = f"""  <!-- Author Profile Card -->
  <div id="author-card" class="author-card fade-up" style="display:flex;">
    <div class="author-avatar" id="author-avatar">
      {avatar_content}
    </div>
    <div>
      <div class="flex items-center gap-2 flex-wrap mb-1">
        <h3 class="font-extrabold text-navy-900 text-base" id="author-name">{full_author_name}</h3>
        <span class="author-badge"><i class="fa-solid fa-circle-check text-[9px]"></i> Doğrulanmış Uzman</span>
      </div>
      <p class="text-sm font-semibold text-navy-700" id="author-title-text">{author_specialty}</p>
      <p class="text-xs text-gray-500 mt-0.5" id="author-specialty">{specialty_sub}</p>
    </div>
  </div>"""
        html = html.replace(author_placeholder, author_content)
        
        # 11. Related Section
        related_placeholder = """  <!-- Related posts -->
  <div class="mt-12" id="related-section" style="display:none;">
    <h2 class="text-xl font-extrabold text-navy-900 mb-5"><i class="fa-solid fa-book-open text-navy-700 mr-2"></i>Diğer Yazılar</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" id="related-grid"></div>
  </div>"""
        
        related_cards = generate_related_html(blogs, blog.get('id'))
        related_content = f"""  <!-- Related posts -->
  <div class="mt-12" id="related-section" style="display:block;">
    <h2 class="text-xl font-extrabold text-navy-900 mb-5"><i class="fa-solid fa-book-open text-navy-700 mr-2"></i>Diğer Yazılar</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" id="related-grid">
      {related_cards}
    </div>
  </div>"""
        html = html.replace(related_placeholder, related_content)
        
        # 12. Save statically pre-rendered file to blog/ and deploy-bundle/blog/
        out_filename = f"{slug}.html"
        
        # Save to blog/
        blog_out_path = os.path.join(BASE_DIR, 'blog', out_filename)
        with open(blog_out_path, 'w', encoding='utf-8') as out_f:
            out_f.write(html)
            
        # Save to deploy-bundle/blog/
        deploy_out_path = os.path.join(BASE_DIR, 'deploy-bundle', 'blog', out_filename)
        with open(deploy_out_path, 'w', encoding='utf-8') as out_f:
            out_f.write(html)
            
        print(f"[MR] ✅ Pre-rendered static HTML for slug '{slug}' successfully.")
        success_count += 1
        
    print(f"[MR] Pre-render complete: {success_count}/{len(blogs)} articles statically generated.")

if __name__ == '__main__':
    render_all_blogs()
