#!/usr/bin/env python3
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEPLOY_DIR = os.path.join(BASE_DIR, 'deploy-bundle')

# Files to sync from root to deploy-bundle
files_to_sync = [
    '404.html',
    '_redirects',
    'about.html',
    'admin-logic.js',
    'admin.html',
    'auth.html',
    'blog-detail.html',
    'blog-static-backup.html',
    'blog-template.html',
    'blog.html',
    'clinic-data.js',
    'clinic-detail.html',
    'compare.html',
    'contact.html',
    'faq.html',
    'favicon.png',
    'form-validation.js',
    'i18n.js',
    'index.html',
    'input.css',
    'output.css',
    'patient-dashboard.html',
    'performance.js',
    'provider.html',
    'quote-modal.js',
    'robots.txt',
    'seed_clinics.js',
    'seo.js',
    'shared.css',
    'shared.js',
    'sitemap.xml',
    'supabase-client.js',
    'test_supabase.js',
    'test_tab.html',
    'treatment-data.js',
    'treatment-template.html',
    'treatment.html',
    'treatments.html'
]

def sync():
    print("Starting sync to deploy-bundle...")
    os.makedirs(DEPLOY_DIR, exist_ok=True)
    count = 0
    for filename in files_to_sync:
        src = os.path.join(BASE_DIR, filename)
        dst = os.path.join(DEPLOY_DIR, filename)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            count += 1
    print(f"Successfully synced {count} files to deploy-bundle.")

if __name__ == '__main__':
    sync()
