#!/usr/bin/env python3
import urllib.request
import json
import os

SUPABASE_URL = 'https://phdmnzsdyjhqoqiqwmho.supabase.co'
SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBoZG1uenNkeWpocW9xaXF3bWhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc1NzAzMzksImV4cCI6MjA5MzE0NjMzOX0.zUoYTYjp8Shva1iSVE0oW1ukGpiEOCghPiqc__WisPg'

# Rich HTML formatted blog content with geo-targeting and case studies
blogs_to_add = [
    {
        "title": "Revision Rhinoplasty in Turkey: A Case Study of a London Patient",
        "slug": "revision-rhinoplasty-turkey-london-case-study",
        "category": "Aesthetic",
        "image_url": "https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?auto=format&fit=crop&w=800&q=80",
        "author": "Dr. Ahmet Yılmaz",
        "author_title": "Plastic Surgeon",
        "author_specialty": "Aesthetic & Reconstructive Surgery",
        "author_image": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=150&h=150&q=80",
        "status": "published",
        "content": """
        <p class="text-gray-600 mb-4 font-medium leading-relaxed">Revision rhinoplasty is widely considered one of the most complex procedures in plastic surgery. When a primary nose job fails to deliver the desired aesthetic result or compromises breathing, patients need a highly skilled reconstructive surgeon. At our Istanbul clinic, we frequently treat patients from the UK, particularly London, who are seeking expert revision work. In this case study, we examine how we restored both form and function for Sarah, a 28-year-old patient from London.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Patient Profile & Clinical Presentation</h2>
        <p class="text-gray-600 mb-4">Sarah travelled to Istanbul from her home in North London after undergoing a primary rhinoplasty in the UK two years prior. She presented with two major complaints:</p>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
          <li><strong>Severe breathing obstruction:</strong> The internal nasal valve had collapsed on the left side, making nasal breathing extremely difficult.</li>
          <li><strong>Aesthetic dissatisfaction:</strong> The tip of her nose had drooped (ptosis), creating a \"pollybeak\" deformity, and the bridge had an asymmetrical indentation.</li>
        </ul>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Why London Patients Choose Istanbul for Revision Work</h2>
        <p class="text-gray-600 mb-4">Undergoing revision rhinoplasty in London can cost between £9,000 and £15,000, often with long waiting times to see top reconstructive specialists. Through MediRoute, Sarah was able to connect with our board-certified surgeons and secure a comprehensive, all-inclusive treatment package (including surgery, 5-star hotel recovery, and private VIP transfers) at a fraction of the cost, without compromising on medical expertise or hospital safety standards.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">The Custom Reconstructive Plan</h2>
        <p class="text-gray-600 mb-4">Due to the lack of remaining septal cartilage from her first surgery, we prepared a customized plan using <strong>autologous costal (rib) cartilage harvesting</strong>. This technique provides the necessary structural support to rebuild the nasal framework. The procedure involved:</p>
        <ol class="list-decimal pl-5 mb-4 text-gray-600 space-y-2">
          <li>A micro-incision under the breast fold to harvest a small piece of rib cartilage.</li>
          <li>Open revision approach to expose the collapsed nasal structures.</li>
          <li>Placement of spreader grafts to open the collapsed nasal valves and restore breathing.</li>
          <li>Rebuilding the tip using a septal extension graft to secure the nose in a stable, natural position.</li>
        </ol>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">The Result and Recovery Journey</h2>
        <p class="text-gray-600 mb-4">The 4-hour surgery was performed under general anesthesia in our JCI-accredited partner hospital in Istanbul. Sarah spent 1 night in the hospital and 6 nights recovering at her hotel. On day 7, we removed the external splint and internal silicone plates. The immediate relief in Sarah's breathing was noticeable, and the structural symmetry of the nasal tip was beautifully restored. Six months post-op, Sarah reports full nasal breathing and a refined, balanced profile that complements her facial features.</p>
        """,
        "created_at": "2026-06-18T10:00:00Z"
    },
    {
        "title": "Restoring Norwood 5 Baldness: A Sapphire FUE Case Study from Dublin",
        "slug": "sapphire-fue-hair-transplant-dublin-patient-case-study",
        "category": "Hair",
        "image_url": "https://images.unsplash.com/photo-1566083042913-671534a759fc?auto=format&fit=crop&w=800&q=80",
        "author": "Dr. Serkan Aygın",
        "author_title": "Hair Restoration Specialist",
        "author_specialty": "Trichology Specialist & Surgeon",
        "author_image": "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=150&h=150&q=80",
        "status": "published",
        "content": """
        <p class="text-gray-600 mb-4 font-medium leading-relaxed">Norwood Scale 5 represents advanced hair loss, characterized by a receding hairline, significant thinning at the vertex (crown), and only a narrow bridge of hair separating the two zones. Restoring this degree of hair loss requires precise planning, high graft counts, and advanced implantation techniques. In this case study, we document the successful 4,800-graft hair transplant journey of David, a 34-year-old patient who travelled from Dublin to Istanbul.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">The Challenge: Dublin's High Costs vs. Advanced Turkish Techniques</h2>
        <p class="text-gray-600 mb-4">In Ireland, hair transplants are billed per graft, meaning a Norwood 5 restoration of nearly 5,000 grafts would cost upwards of €12,000 to €15,000. Additionally, many Irish clinics still utilize standard steel blades. In contrast, Turkey's leading clinics offer <strong>Sapphire FUE</strong>, utilizing blades made from gemstone sapphire to open micro-channels. This minimizes tissue trauma, reduces scab formation, and increases graft survival rates.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">David's Personalized Treatment Plan</h2>
        <p class="text-gray-600 mb-4">Upon reviewing David's case through MediRoute, we designed a two-stage density plan executed in a single, high-capacity session:</p>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
          <li><strong>Zone 1 (Frontal Hairline & Mid-Scalp):</strong> 3,200 grafts implanted using Sapphire FUE to create high density and a natural hairline angle.</li>
          <li><strong>Zone 2 (Vertex / Crown):</strong> 1,600 grafts placed in a whorl pattern matching David's natural hair growth direction.</li>
          <li><strong>Therapy:</strong> PRP (Platelet-Rich Plasma) therapy during the procedure to accelerate healing and stimulate growth.</li>
        </ul>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Case Analysis & 12-Month Results</h2>
        <p class="text-gray-600 mb-4">The extraction was performed using a micro-motor with punch diameters between 0.7mm and 0.8mm to preserve David's donor area. We harvested strong multi-hair grafts from the back of the head. Following his return to Dublin, David was monitored remotely via MediRoute's post-op follow-up protocol. He experienced normal shock loss between weeks 3 and 8, followed by steady regrowth. By month 12, David achieved complete coverage with a natural hairline, dramatically improving his confidence and youthfulness.</p>
        """,
        "created_at": "2026-06-18T10:05:00Z"
    },
    {
        "title": "Hollywood Smile with E-Max Veneers: A Manchester Patient Case Study",
        "slug": "emax-veneers-turkey-manchester-case-study",
        "category": "Dental",
        "image_url": "https://images.unsplash.com/photo-1606811971618-4486d14f3f99?auto=format&fit=crop&w=800&q=80",
        "author": "Dr. Canan Demirel",
        "author_title": "Cosmetic Dentist",
        "author_specialty": "Prosthodontist Specialist",
        "author_image": "https://images.unsplash.com/photo-1594824813573-246434de83fb?auto=format&fit=crop&w=150&h=150&q=80",
        "status": "published",
        "content": """
        <p class="text-gray-600 mb-4 font-medium leading-relaxed">A smile makeover is not just about whitening teeth; it is a comprehensive restoration of dental aesthetics, alignment, and facial harmony. For patients dealing with severe staining, enamel wear, or minor gaps, E-Max veneers offer a highly aesthetic, durable solution. This case study details the dental transformation of James, a 31-year-old marketing executive from Manchester, UK, who received a custom smile design in Turkey.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">The Clinical Challenge: Severe Fluorosis & Spacing</h2>
        <p class="text-gray-600 mb-4">James had suffered from severe dental fluorosis since childhood, leaving his teeth with unsightly brown blotches and an uneven, yellowish texture. He also had a diastema (gap) between his upper front teeth. After receiving quotes of over £18,000 from cosmetic dentists in Manchester, James searched for an affordable but clinically excellent alternative in Turkey through MediRoute.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">The Solution: 20 Premium E-Max Porcelain Veneers</h2>
        <p class="text-gray-600 mb-4">At our partner dental clinic, we selected **IPS e.max lithium disilicate** glass-ceramic. E-Max is renowned for its strength (400 MPa) and translucent qualities that mimic natural enamel. The treatment plan consisted of:</p>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
          <li>Digital smile design using 3D CAD/CAM software to match James's facial symmetry and jaw structure.</li>
          <li>Minimal preparation (shaving less than 0.5mm of enamel) to preserve healthy tooth structure.</li>
          <li>Bonding 10 upper and 10 lower E-Max veneers to achieve a complete, harmonious shade correction (select Bleach 3 shade for a bright but natural look).</li>
        </ul>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">The 6-Day Transformation</h2>
        <p class="text-gray-600 mb-4">James arrived in Antalya on a Sunday. By Friday afternoon, his custom veneers were milled, glazed, and permanently bonded. The gaps were closed, the shape of his teeth was corrected, and the discolored enamel was completely masked by the highly biocompatible E-Max porcelain. James returned to Manchester on Saturday with a radiant, confident smile, saving over 70% compared to UK prices while receiving state-of-the-art restorative care.</p>
        """,
        "created_at": "2026-06-18T10:10:00Z"
    },
    {
        "title": "Reversing Type 2 Diabetes: A Gastric Sleeve Case Study from Birmingham",
        "slug": "gastric-sleeve-turkey-birmingham-patient-case-study",
        "category": "Bariatric",
        "image_url": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=800&q=80",
        "author": "Dr. Mehmet Kaya",
        "author_title": "General Surgeon",
        "author_specialty": "Bariatric & Metabolic Surgery",
        "author_image": "https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&w=150&h=150&q=80",
        "status": "published",
        "content": """
        <p class="text-gray-600 mb-4 font-medium leading-relaxed">Obesity is not merely a cosmetic issue; it is a chronic metabolic disease closely linked with life-threatening comorbidities such as Type 2 diabetes, hypertension, and sleep apnea. Gastric sleeve surgery (Sleeve Gastrectomy) has proven to be a highly effective metabolic intervention, helping patients achieve massive weight loss and, in many cases, complete disease remission. In this study, we highlight the journey of Liam, a 42-year-old patient from Birmingham, UK.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Patient Profile: BMI 42 & Uncontrolled Diabetes</h2>
        <p class="text-gray-600 mb-4">Liam contacted MediRoute weighing 132kg with a BMI of 42. He had been taking metformin and insulin for Type 2 diabetes for five years but struggled to control his blood sugar levels. Facing a multi-year waiting list for bariatric surgery under the UK NHS, and private surgery costs starting at £11,000, Liam decided to travel to our accredited metabolic surgery center in Turkey.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">The Procedure: Laparoscopic Sleeve Gastrectomy</h2>
        <p class="text-gray-600 mb-4">After a rigorous 2-day pre-operative assessment in Istanbul—including cardiac clearance, endocrine workups, and pulmonary checks—Liam underwent a successful laparoscopic sleeve gastrectomy. We removed approximately 80% of his stomach, reducing its volume to about 150ml. This restricted food intake and significantly lowered levels of the hunger hormone ghrelin, resetting his metabolic baseline.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Metabolic Outcomes & 1-Year Follow-Up</h2>
        <p class="text-gray-600 mb-4">Within three months post-surgery, Liam had lost 25kg, and his HbA1c levels dropped to normal ranges, allowing his endocrinologist in Birmingham to safely discontinue his insulin therapy. By month 12, Liam had lost a total of 55kg, achieving a healthy BMI of 24.5. His Type 2 diabetes is in complete remission, and he reports a profound improvement in his daily mobility, energy levels, and overall quality of life.</p>
        """,
        "created_at": "2026-06-18T10:15:00Z"
    },
    {
        "title": "Trifocal Smart Lens Replacement: A Munich Patient's Istanbul Journey",
        "slug": "smart-lens-replacement-istanbul-munich-case-study",
        "category": "Eye",
        "image_url": "https://images.unsplash.com/photo-1579684389782-64d84b5e905d?auto=format&fit=crop&w=800&q=80",
        "author": "Dr. Elif Şahin",
        "author_title": "Ophthalmologist",
        "author_specialty": "Refractive Surgery Specialist",
        "author_image": "https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=150&h=150&q=80",
        "status": "published",
        "content": """
        <p class="text-gray-600 mb-4 font-medium leading-relaxed">As we age, the eye's natural lens gradually loses its flexibility, leading to presbyopia—the inability to focus on near objects. For active adults who want to eliminate the constant need for reading glasses, progressive glasses, or contact lenses, Refractive Lens Exchange (RLE) with Trifocal Smart Lenses is an exceptional, lifelong solution. Here, we outline the treatment of Hans, a 48-year-old professional from Munich, Germany.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">The Vision Deficit: Presbyopia Combined with High Myopia</h2>
        <p class="text-gray-600 mb-4">Hans was severely shortsighted (-6.50 diopters in both eyes) and had recently developed presbyopia, requiring him to constantly switch between distance glasses and reading glasses. In Germany, Trifocal Lens Replacement can cost up to €7,500 per eye. Hans used the MediRoute platform to compare accredited ophthalmology centers in Istanbul, choosing a clinic specializing in advanced Zeiss micro-incision technology.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">The Technology: Zeiss AT LISA Tri Lenses</h2>
        <p class="text-gray-600 mb-4">We selected premium **Zeiss AT LISA Tri** trifocal intraocular lenses (IOLs) for Hans. These advanced lenses provide excellent visual acuity at near, intermediate (computer distance), and far distances, with optimized light distribution to minimize night-time glare. The surgical steps included:</p>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
          <li>Topical anesthetic eye drops (no needles or general anesthesia required).</li>
          <li>A micro-incision of 1.8mm to gently liquefy and remove the aged natural lens using ultrasound (phacoemulsification).</li>
          <li>Implantation of the folded Trifocal Smart Lens into the natural capsule, where it unfolds and positions itself permanently.</li>
          <li>The entire procedure took just 10 minutes per eye, performed over two consecutive days.</li>
        </ul>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Clinical Result: Clear Vision at All Distances</h2>
        <p class="text-gray-600 mb-4">Twenty-four hours after the second eye surgery, Hans's vision was tested at 20/20 for distance and 1.0 (Jaeger 1) for reading. The micro-incisions healed self-sealing without stitches. Hans returned to Munich free from glasses, expressing his satisfaction with the efficiency, hygiene, and cutting-edge technology of our ophthalmic center in Istanbul.</p>
        """,
        "created_at": "2026-06-18T10:20:00Z"
    }
]

def insert_blog_to_supabase(blog):
    url = f"{SUPABASE_URL}/rest/v1/blogs"
    headers = {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': f"Bearer {SUPABASE_ANON_KEY}",
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
    }
    
    # Check if a blog with this slug already exists to prevent duplicate insertion error
    check_url = f"{SUPABASE_URL}/rest/v1/blogs?slug=eq.{blog['slug']}&select=id"
    try:
        check_req = urllib.request.Request(check_url, headers=headers)
        with urllib.request.urlopen(check_req) as response:
            existing = json.loads(response.read().decode('utf-8'))
            if existing:
                print(f"Blog with slug '{blog['slug']}' already exists. Skipping insertion.")
                return True
    except Exception as e:
        print(f"Checking slug '{blog['slug']}' failed, attempting insertion anyway...", e)

    # Insert row
    data_bytes = json.dumps(blog).encode('utf-8')
    try:
        req = urllib.request.Request(url, data=data_bytes, headers=headers, method='POST')
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(f"Successfully inserted blog: {blog['title']} (Slug: {blog['slug']})")
            return True
    except Exception as e:
        print(f"Error inserting blog '{blog['title']}':", e)
        if hasattr(e, 'read'):
            print("Response details:", e.read().decode('utf-8'))
        return False

def add_all_blogs():
    print(f"Starting insertion of {len(blogs_to_add)} geo case study articles...")
    success_count = 0
    for b in blogs_to_add:
        if insert_blog_to_supabase(b):
            success_count += 1
            
    print(f"Insertion complete. {success_count}/{len(blogs_to_add)} articles processed.")
    
    # Rebuild sitemap
    print("Rebuilding sitemap with new articles...")
    try:
        import generate_sitemap
        generate_sitemap.save_sitemaps()
        print("Sitemap successfully updated!")
    except Exception as e:
        print("Failed to run generate_sitemap.py automatic update:", e)

    # Pre-render static HTML pages
    print("Pre-rendering static HTML pages for new articles...")
    try:
        import pre_render_blogs
        pre_render_blogs.render_all_blogs()
        print("Static HTML pages successfully pre-rendered!")
    except Exception as e:
        print("Failed to run pre_render_blogs.py automatic update:", e)

if __name__ == '__main__':
    add_all_blogs()
