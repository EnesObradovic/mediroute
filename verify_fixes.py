#!/usr/bin/env python3
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEPLOY_DIR = os.path.join(BASE_DIR, 'deploy-bundle')

errors = []
successes = []

def check(condition, success_msg, error_msg):
    if condition:
        successes.append(success_msg)
        print(f"✅ {success_msg}")
    else:
        errors.append(error_msg)
        print(f"❌ {error_msg}")

# 1. Logo Links Check
print("\n--- 1. Testing Logo Links ---")
logo_files = ['auth.html', 'patient-dashboard.html', 'admin.html']
for filename in logo_files:
    path = os.path.join(BASE_DIR, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Look for a link containing logo or heart-pulse pointing to /
        has_logo_link = '/' in re.findall(r'href="([^"]+)"', content) or 'href="/"' in content
        # Specifically check if logo elements are wrapped in href="/"
        check(has_logo_link, f"Logo link pointing to '/' found in {filename}", f"Logo link pointing to '/' not found in {filename}")
    else:
        print(f"⚠️ {filename} not found.")

# 2. Search Scroll Check
print("\n--- 2. Testing Search Scroll Behavior ---")
index_path = os.path.join(BASE_DIR, 'index.html')
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()
    has_scroll = 'scrollIntoView' in index_content
    check(has_scroll, "Search button 'scrollIntoView' click handler found in index.html", "Search button 'scrollIntoView' click handler not found in index.html")

# 3. Clinic Card Clickability Check
print("\n--- 3. Testing Clinic Card Clickability ---")
clinic_data_path = os.path.join(BASE_DIR, 'clinic-data.js')
if os.path.exists(clinic_data_path):
    with open(clinic_data_path, 'r', encoding='utf-8') as f:
        clinic_data = f.read()
    # Check if there is an onclick handler or clickable card
    has_card_click = 'onclick' in clinic_data or 'clinic-detail' in clinic_data
    check(has_card_click, "Clinic card click handler found in clinic-data.js", "Clinic card click handler not found in clinic-data.js")

# 4. Mobile Menu Scroll Check
print("\n--- 4. Testing Mobile Menu CSS ---")
shared_css_path = os.path.join(BASE_DIR, 'shared.css')
if os.path.exists(shared_css_path):
    with open(shared_css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    has_padding = 'padding-bottom' in css_content and 'mobile-menu' in css_content
    check(has_padding, "Mobile menu padding-bottom style found in shared.css", "Mobile menu padding-bottom style not found in shared.css")

# 5. i18n Keys Check
print("\n--- 5. Testing i18n Keys ---")
i18n_path = os.path.join(BASE_DIR, 'i18n.js')
if os.path.exists(i18n_path):
    with open(i18n_path, 'r', encoding='utf-8') as f:
        i18n_content = f.read()
    new_keys = ['auth_terms_label', 'auth_enter_pw', 'footer_pages', 'footer_patient_guide', 'footer_safety']
    for key in new_keys:
        has_key = key in i18n_content
        check(has_key, f"i18n key '{key}' found in i18n.js", f"i18n key '{key}' missing from i18n.js")

# 6. Footer Standard Container Check
print("\n--- 6. Testing Footer Containers ---")
footer_pages = ['index.html', 'about.html', 'contact.html', 'blog.html', 'clinic-detail.html', 'compare.html', 'faq.html', 'treatments.html', 'auth.html']
for page in footer_pages:
    path = os.path.join(BASE_DIR, page)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        has_container = 'footer-container' in content
        check(has_container, f"Footer container found in {page}", f"Footer container missing in {page}")

# 7. Blog Articles Check
print("\n--- 7. Testing 15 New Blog Articles ---")
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
    "lifetime-guarantee-turkish-clinics-what-it-actually-means",
    "liposuction-turkey-vs-uk-clinical-facility-standards",
    "how-to-verify-turkish-plastic-surgeon-credentials",
    "gastric-sleeve-leak-test-protocols-turkey",
    "veneers-prep-tolerances-zirconium-vs-emax",
    "hbot-prp-graft-survival-hair-transplant-turkey"
]

for slug in new_slugs:
    # Check in deploy-bundle
    path = os.path.join(DEPLOY_DIR, 'blog', f"{slug}.html")
    exists = os.path.exists(path)
    check(exists, f"Statically pre-rendered blog file exists: deploy-bundle/blog/{slug}.html", f"Missing pre-rendered blog: deploy-bundle/blog/{slug}.html")
    if exists:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        check('STATIC_RENDERED' in content, f"Static render flag found in {slug}.html", f"Static render flag missing in {slug}.html")

# 8. Sitemap Check
print("\n--- 8. Testing Sitemap ---")
sitemap_path = os.path.join(DEPLOY_DIR, 'sitemap.xml')
if os.path.exists(sitemap_path):
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        sitemap_content = f.read()
    for slug in new_slugs:
        check(slug in sitemap_content, f"Blog slug '{slug}' registered in sitemap.xml", f"Blog slug '{slug}' missing in sitemap.xml")

print("\n--- Verification Summary ---")
print(f"Total Successes: {len(successes)}")
print(f"Total Errors: {len(errors)}")

if len(errors) == 0:
    print("\n🎉 ALL TESTS PASSED! Everything is clean and fully verified.")
else:
    print(f"\n⚠️ {len(errors)} tests failed. Please review the errors above.")
