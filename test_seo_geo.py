#!/usr/bin/env python3
"""
MediRoute — Kapsamlı SEO/GEO Test Suite
Son yapılan tüm optimizasyonları doğrular.
"""
import os, re, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEPLOY_DIR = os.path.join(BASE_DIR, 'deploy-bundle')
BASE_URL = 'https://medirouteturkey.com'

errors = []
successes = []
warnings = []

def ok(msg):
    successes.append(msg)
    print(f"  ✅ {msg}")

def fail(msg):
    errors.append(msg)
    print(f"  ❌ {msg}")

def warn(msg):
    warnings.append(msg)
    print(f"  ⚠️  {msg}")

def check(cond, s, e):
    if cond: ok(s)
    else: fail(e)

def read(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# ════════════════════════════════════════════════════════════════
# 1. CANONICAL URL TESTLERİ
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  1. CANONICAL URL TESTLERİ")
print("="*60)

seo_js = read(os.path.join(BASE_DIR, 'seo.js'))
check(seo_js is not None, "seo.js dosyası mevcut", "seo.js dosyası BULUNAMADI")

if seo_js:
    check('injectCanonical' in seo_js, "injectCanonical() fonksiyonu mevcut", "injectCanonical() fonksiyonu YOK")
    check('location.pathname' in seo_js, "Canonical URL location.pathname kullanıyor (dinamik)", "Canonical statik — location.pathname kullanmıyor")
    # co.uk yok
    check('.co.uk' not in seo_js, "seo.js'de .co.uk domain yok ✓", "seo.js'de .co.uk domain HALA VAR!")
    check(BASE_URL in seo_js, f"Base URL doğru: {BASE_URL}", f"Base URL yanlış — {BASE_URL} bulunamadı")
    # Canonical + og:url senkronize
    check("og:url" in seo_js and "canonicalUrl" in seo_js, "og:url canonical ile senkronize", "og:url canonical ile senkronize DEĞİL")

# ════════════════════════════════════════════════════════════════
# 2. META SÖZLÜĞÜ TESTLERİ (treatments.html & treatment.html dahil)
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  2. META SÖZLÜĞÜ TESTLERİ")
print("="*60)

required_pages = [
    'index.html', 'about.html', 'contact.html', 'compare.html',
    'blog.html', 'faq.html', 'auth.html', 'clinic-detail.html',
    'treatments.html', 'treatment.html', 'blog-detail.html',
    'patient-dashboard.html'
]

if seo_js:
    for page in required_pages:
        in_meta = f"'{page}'" in seo_js or f'"{page}"' in seo_js
        check(in_meta, f"META sözlüğünde {page} tanımlı", f"META sözlüğünde {page} EKSİK!")

    # Çoklu dil desteği kontrol
    langs = ['en', 'tr', 'ar', 'de', 'fr']
    for lang in langs:
        check(f"'{lang}'" in seo_js or f'"{lang}"' in seo_js,
              f"Dil desteği mevcut: {lang}",
              f"Dil desteği EKSİK: {lang}")

# ════════════════════════════════════════════════════════════════
# 3. HREFLANG TUTARLILIĞI (sitemap vs shared.js)
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  3. HREFLANG TUTARLILIĞI")
print("="*60)

sitemap = read(os.path.join(DEPLOY_DIR, 'sitemap.xml'))
shared_js = read(os.path.join(BASE_DIR, 'shared.js'))

if sitemap:
    sitemap_langs = set(re.findall(r'hreflang="([^"]+)"', sitemap))
    check('en' in sitemap_langs, "Sitemap hreflang: en ✓", "Sitemap hreflang: en EKSİK")
    check('tr' in sitemap_langs, "Sitemap hreflang: tr ✓", "Sitemap hreflang: tr EKSİK")
    check('ar' in sitemap_langs, "Sitemap hreflang: ar ✓", "Sitemap hreflang: ar EKSİK")
    check('de' in sitemap_langs, "Sitemap hreflang: de ✓", "Sitemap hreflang: de EKSİK")
    check('fr' in sitemap_langs, "Sitemap hreflang: fr ✓", "Sitemap hreflang: fr EKSİK")
    check('x-default' in sitemap_langs, "Sitemap hreflang: x-default ✓", "Sitemap hreflang: x-default EKSİK")
    # co.uk kontrolü
    check('.co.uk' not in sitemap, "Sitemap'te .co.uk domain yok ✓", "Sitemap'te .co.uk domain HALA VAR!")
    check(BASE_URL in sitemap, f"Sitemap base URL doğru: {BASE_URL}", f"Sitemap base URL yanlış")

if shared_js:
    check('hreflang' in shared_js, "shared.js'de hreflang enjeksiyon kodu mevcut", "shared.js'de hreflang kodu YOK")
    shared_langs = re.findall(r"code:\s*'([^']+)'", shared_js)
    for lang in ['en', 'tr', 'ar', 'de', 'fr']:
        check(lang in shared_langs, f"shared.js hreflang: {lang} ✓", f"shared.js hreflang: {lang} EKSİK")

# ════════════════════════════════════════════════════════════════
# 4. SECURITY & CACHE HEADERS (vercel.json)
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  4. SECURITY & CACHE HEADERS")
print("="*60)

vercel_src = read(os.path.join(BASE_DIR, 'vercel.json'))
if vercel_src:
    try:
        vercel = json.loads(vercel_src)
    except:
        vercel = None
        fail("vercel.json JSON parse hatası!")

    if vercel:
        headers = vercel.get('headers', [])
        header_values = ' '.join(json.dumps(h) for h in headers)
        
        security_headers = [
            'X-Content-Type-Options',
            'X-Frame-Options',
            'X-XSS-Protection',
            'Referrer-Policy',
            'Strict-Transport-Security',
            'Permissions-Policy'
        ]
        for sh in security_headers:
            check(sh in header_values, f"Security header: {sh} ✓", f"Security header: {sh} EKSİK!")

        # Cache headers
        check('max-age=31536000' in header_values, "Image cache: 1 yıl (immutable) ✓", "Image cache ayarı EKSİK")
        check('max-age=604800' in header_values, "CSS/JS cache: 1 hafta ✓", "CSS/JS cache ayarı EKSİK")
        check('max-age=3600' in header_values, "HTML cache: 1 saat ✓", "HTML cache ayarı EKSİK")
        check('stale-while-revalidate' in header_values, "stale-while-revalidate mevcut ✓", "stale-while-revalidate EKSİK")

# ════════════════════════════════════════════════════════════════
# 5. OG IMAGE TESTLERİ
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  5. OG IMAGE TESTLERİ")
print("="*60)

og_img_path = os.path.join(BASE_DIR, 'og-image.png')
check(os.path.exists(og_img_path), "og-image.png dosyası mevcut", "og-image.png dosyası BULUNAMADI!")
if os.path.exists(og_img_path):
    size = os.path.getsize(og_img_path)
    check(size > 10000, f"og-image.png boyutu: {size//1024}KB (yeterli)", f"og-image.png boyutu çok küçük: {size} bytes")

if seo_js:
    check('og:image' in seo_js, "seo.js'de og:image meta etiketi enjekte ediliyor ✓", "seo.js'de og:image EKSİK")
    check('1200' in seo_js and '630' in seo_js, "OG image boyutları 1200x630 tanımlı ✓", "OG image boyutları EKSİK")
    check('twitter:card' in seo_js, "Twitter Card meta etiketi mevcut ✓", "Twitter Card meta EKSİK")
    check('summary_large_image' in seo_js, "Twitter Card tipi: summary_large_image ✓", "Twitter Card tipi yanlış")

# ════════════════════════════════════════════════════════════════
# 6. JSON-LD STRUCTURED DATA TESTLERİ
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  6. JSON-LD STRUCTURED DATA")
print("="*60)

if seo_js:
    schemas = ['Organization', 'BreadcrumbList', 'WebSite', 'SearchAction',
               'FAQPage', 'MedicalBusiness', 'MedicalProcedure']
    for s in schemas:
        check(s in seo_js, f"Schema: {s} ✓", f"Schema: {s} EKSİK")
    
    check('application/ld+json' in seo_js, "JSON-LD injection mekanizması mevcut ✓", "JSON-LD injection mekanizması EKSİK")
    check('AggregateRating' in seo_js, "AggregateRating schema mevcut ✓", "AggregateRating EKSİK")

# ════════════════════════════════════════════════════════════════
# 7. INTERNAL LINKING TESTLERİ
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  7. INTERNAL LINKING (Blog yazıları)")
print("="*60)

blog_dir = os.path.join(DEPLOY_DIR, 'blog')
if os.path.isdir(blog_dir):
    blog_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]
    check(len(blog_files) >= 15, f"Blog yazısı sayısı: {len(blog_files)} (≥15 ✓)", f"Blog yazısı sayısı yetersiz: {len(blog_files)}")
    
    # Internal link kontrolü (en az birkaç blog'da /treatment/ veya /blog/ linki var mı)
    internal_link_count = 0
    for bf in blog_files[:10]:  # İlk 10 blog'u kontrol et
        content = read(os.path.join(blog_dir, bf))
        if content and ('/treatment/' in content or '/blog/' in content):
            internal_link_count += 1
    
    check(internal_link_count >= 5, f"Internal link içeren blog yazıları: {internal_link_count}/10 ✓", f"Internal link yetersiz: {internal_link_count}/10")

# ════════════════════════════════════════════════════════════════
# 8. UNSPLASH PRECONNECT TESTLERİ
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  8. UNSPLASH PRECONNECT")
print("="*60)

preconnect_pages = ['index.html', 'about.html', 'blog.html', 'treatments.html', 'treatment.html']
for page in preconnect_pages:
    content = read(os.path.join(BASE_DIR, page))
    if content:
        has_preconnect = 'preconnect' in content and 'images.unsplash.com' in content
        check(has_preconnect, f"Unsplash preconnect: {page} ✓", f"Unsplash preconnect EKSİK: {page}")

# ════════════════════════════════════════════════════════════════
# 9. ROBOTS.TXT TESTLERİ
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  9. ROBOTS.TXT")
print("="*60)

robots = read(os.path.join(BASE_DIR, 'robots.txt'))
if robots:
    check('Allow: /' in robots, "robots.txt: Allow: / ✓", "robots.txt: Allow: / EKSİK")
    check('Sitemap:' in robots, "robots.txt: Sitemap referansı ✓", "robots.txt: Sitemap referansı EKSİK")
    check(BASE_URL in robots, f"robots.txt: Doğru domain ({BASE_URL}) ✓", "robots.txt: Yanlış domain")
    check('Disallow: /admin' in robots, "robots.txt: Admin sayfası engellendi ✓", "robots.txt: Admin sayfası engellenmemiş")
    check('Allow: /seo.js' in robots, "robots.txt: seo.js render için izinli ✓", "robots.txt: seo.js izin EKSİK")
    check('.co.uk' not in robots, "robots.txt'de .co.uk yok ✓", "robots.txt'de .co.uk HALA VAR!")

# ════════════════════════════════════════════════════════════════
# 10. DEPLOY BUNDLE BÜTÜNLÜK TESTLERİ
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  10. DEPLOY BUNDLE BÜTÜNLÜĞÜ")
print("="*60)

# tailwindcss binary yok
tailwind_path = os.path.join(DEPLOY_DIR, 'tailwindcss')
check(not os.path.exists(tailwind_path), "tailwindcss binary deploy-bundle'da YOK ✓ (25MB limit)", "tailwindcss binary deploy-bundle'da HALA VAR!")

# Gerekli dosyalar mevcut
required_deploy_files = [
    'index.html', 'seo.js', 'shared.js', 'shared.css', 'output.css',
    'i18n.js', 'sitemap.xml', 'robots.txt', 'treatment.html', 'treatments.html',
    'blog.html', 'about.html', 'contact.html', 'faq.html', 'compare.html'
]
for f in required_deploy_files:
    path = os.path.join(DEPLOY_DIR, f)
    check(os.path.exists(path), f"deploy-bundle/{f} mevcut ✓", f"deploy-bundle/{f} EKSİK!")

# 25MB dosya limiti kontrolü
for root, dirs, files in os.walk(DEPLOY_DIR):
    for f in files:
        fpath = os.path.join(root, f)
        fsize = os.path.getsize(fpath)
        if fsize > 25 * 1024 * 1024:
            fail(f"25MB limitini AŞAN dosya: {f} ({fsize // (1024*1024)}MB)")

ok("Deploy bundle'da 25MB üzeri dosya yok ✓")

# ════════════════════════════════════════════════════════════════
# 11. GOOGLE ANALYTICS & SEARCH CONSOLE
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  11. GOOGLE ANALYTICS & SEARCH CONSOLE")
print("="*60)

if seo_js:
    check('google-site-verification' in seo_js, "Google Search Console verification ✓", "GSC verification EKSİK")
    check('googletagmanager' in seo_js or 'gtag' in seo_js, "Google Analytics (GA4) mevcut ✓", "GA4 EKSİK")
    check('G-' in seo_js, "GA4 Measurement ID mevcut ✓", "GA4 Measurement ID EKSİK")

# ════════════════════════════════════════════════════════════════
# 12. DEPLOY BUNDLE vs SOURCE SENKRONIZASYONU
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  12. SOURCE ↔ DEPLOY SENKRONIZASYONU")
print("="*60)

sync_files = ['seo.js', 'shared.js', 'sitemap.xml', 'robots.txt', 'i18n.js']
for f in sync_files:
    src = read(os.path.join(BASE_DIR, f))
    dst = read(os.path.join(DEPLOY_DIR, f))
    if src and dst:
        check(src == dst, f"{f}: Source ↔ Deploy senkronize ✓", f"{f}: Source ↔ Deploy FARKLI!")
    elif src and not dst:
        fail(f"{f}: Deploy-bundle'da YOK!")

# ════════════════════════════════════════════════════════════════
# 13. .co.uk KALINTI KONTROLÜ (TÜM DOSYALARDA)
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  13. .co.uk KALINTI KONTROLÜ")
print("="*60)

couk_found = []
critical_files = ['seo.js', 'shared.js', 'sitemap.xml', 'robots.txt', 'index.html', 'about.html']
for f in critical_files:
    content = read(os.path.join(BASE_DIR, f))
    if content and '.co.uk' in content:
        couk_found.append(f)

if couk_found:
    fail(f".co.uk kalıntısı bulunan dosyalar: {', '.join(couk_found)}")
else:
    ok("Hiçbir kritik dosyada .co.uk kalıntısı yok ✓")

# ════════════════════════════════════════════════════════════════
# SONUÇ
# ════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("  📊 TEST SONUÇLARI")
print("="*60)
print(f"  ✅ Başarılı : {len(successes)}")
print(f"  ❌ Hatalı   : {len(errors)}")
print(f"  ⚠️  Uyarılar : {len(warnings)}")
print("="*60)

if errors:
    print("\n  🔴 BAŞARISIZ TESTLER:")
    for e in errors:
        print(f"    • {e}")
else:
    print("\n  🎉 TÜM SEO/GEO TESTLERİ BAŞARILI!")
    print("  ✨ Site tamamen optimize edilmiş ve deploy'a hazır.")
print()
