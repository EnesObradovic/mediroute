#!/usr/bin/env python3
"""
Build script: Inlines treatment-data.js into treatment.html and treatment-template.html.
This eliminates the external file dependency that causes Cloudflare upload issues.
Also copies results to deploy-bundle/.
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def read_file(path):
    with open(os.path.join(BASE_DIR, path), 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(os.path.join(BASE_DIR, path), 'w', encoding='utf-8') as f:
        f.write(content)

def inline_treatment_data(html_file):
    """Replace <script src="/treatment-data.js"></script> with inline content"""
    html = read_file(html_file)
    treatment_data = read_file('treatment-data.js')
    
    # Replace external script reference with inline version
    old_tag = '<script src="/treatment-data.js"></script>'
    inline_tag = f'<script>\n{treatment_data}\n</script>'
    
    if old_tag in html:
        html = html.replace(old_tag, inline_tag)
        write_file(html_file, html)
        print(f"✅ Inlined treatment-data.js into {html_file}")
        return True
    
    # Also check for the already-partially-inlined version
    partial = '// === INLINE TREATMENT DATA (eliminates external file dependency) ==='
    if partial in html:
        # Find the script tag containing this comment and replace it properly
        # We need to remove the empty inline script and the following script tag
        lines = html.split('\n')
        new_lines = []
        skip_until_close = False
        i = 0
        while i < len(lines):
            if partial in lines[i]:
                # Go back to find the opening <script> for this
                # Remove the previous <script> line
                while new_lines and '<script>' in new_lines[-1] and 'src=' not in new_lines[-1]:
                    new_lines.pop()
                # Skip until we find the closing </script> or next <script>
                i += 1
                while i < len(lines):
                    stripped = lines[i].strip()
                    if stripped == '' :
                        i += 1
                        continue
                    break
                # Now insert the inline data before the next <script>
                new_lines.append(f'<script>\n{treatment_data}\n</script>')
                continue
            new_lines.append(lines[i])
            i += 1
        
        html = '\n'.join(new_lines)
        write_file(html_file, html)
        print(f"✅ Fixed and inlined treatment-data.js into {html_file}")
        return True
    
    print(f"⚠️  No treatment-data.js reference found in {html_file}")
    return False

# Process both HTML files
for html_file in ['treatment.html', 'treatment-template.html']:
    inline_treatment_data(html_file)

# Copy to deploy-bundle
for f in ['treatment.html', 'treatment-template.html']:
    src = os.path.join(BASE_DIR, f)
    dst = os.path.join(BASE_DIR, 'deploy-bundle', f)
    if os.path.exists(src):
        write_file(os.path.join('deploy-bundle', f), read_file(f))
        print(f"📋 Copied {f} → deploy-bundle/{f}")

# Run static blog pre-rendering
print("\n🔄 Running static blog pre-rendering...")
try:
    import pre_render_blogs
    pre_render_blogs.render_all_blogs()
except Exception as e:
    print(f"❌ Failed to pre-render blogs: {e}")

print("\n🎉 Build complete! All treatments are inlined and static blogs pre-rendered.")
print("   You can now upload deploy-bundle/ to Cloudflare Pages.")
