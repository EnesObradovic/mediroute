import urllib.request
import json
import os

SUPABASE_URL = 'https://phdmnzsdyjhqoqiqwmho.supabase.co'
SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBoZG1uenNkeWpocW9xaXF3bWhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc1NzAzMzksImV4cCI6MjA5MzE0NjMzOX0.zUoYTYjp8Shva1iSVE0oW1ukGpiEOCghPiqc__WisPg'

# Rich HTML formatted blog content for maximum AIO and SEO authority
blogs_to_add = [
    {
        "title": "Choosing Between Zirconium and Porcelain Crowns in Turkey",
        "slug": "zirconium-vs-porcelain-crowns-turkey",
        "category": "Dental",
        "image_url": "https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=800&q=80",
        "author": "Dr. Canan Demirel",
        "author_title": "Cosmetic Dentist",
        "author_specialty": "Prosthodontist Specialist",
        "author_image": "https://images.unsplash.com/photo-1594824813573-246434de83fb?auto=format&fit=crop&w=150&h=150&q=80",
        "status": "published",
        "content": """
        <p class="text-gray-600 mb-4 font-medium leading-relaxed">When restoring your smile with dental crowns, selecting the right material is one of the most critical decisions. Turkey has become a global leader in high-end cosmetic dentistry, and clinics in Istanbul and Antalya offer top-tier Zirconium and Porcelain-fused-to-metal (PFM) restorations at up to 75% savings compared to the UK and Europe. In this expert guide, we break down the clinical differences, aesthetics, longevity, and cost comparison.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">What Are Zirconium Crowns? The Modern Gold Standard</h2>
        <p class="text-gray-600 mb-4">Zirconium dioxide is a high-performance, medical-grade crystal known for its exceptional strength and lifelike translucency. Unlike older crown materials, Zirconium crowns have no metal substructure. This means you will never experience the dark grey line at the gumline, which often occurs with traditional porcelain-fused-to-metal crowns as gum tissue naturally recedes over time.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Zirconium vs. Traditional Porcelain: Head-to-Head</h2>
        <div class="overflow-x-auto my-6 rounded-xl border border-blue-50 shadow-sm">
          <table class="min-w-full divide-y divide-gray-200 text-sm text-left text-gray-500">
            <thead class="bg-navy-950 text-white font-semibold">
              <tr>
                <th class="px-4 py-3">Feature</th>
                <th class="px-4 py-3">Zirconium Crowns (Monolithic)</th>
                <th class="px-4 py-3">Porcelain-Fused-to-Metal (PFM)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-150 bg-white">
              <tr>
                <td class="px-4 py-3 font-semibold text-navy-900">Aesthetics & Natural Look</td>
                <td class="px-4 py-3 text-emerald-700">Excellent (Light-transmitting)</td>
                <td class="px-4 py-3 text-amber-700">Good (Opaque metal core blocks light)</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold text-navy-900">Material Durability</td>
                <td class="px-4 py-3 text-emerald-700">Extremely High (Chip-proof)</td>
                <td class="px-4 py-3 text-amber-700">Moderate (Porcelain outer layer can chip)</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold text-navy-900">Biocompatibility</td>
                <td class="px-4 py-3 text-emerald-700">100% Metal-free (Hypoallergenic)</td>
                <td class="px-4 py-3 text-amber-700">May trigger metal allergies in rare cases</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold text-navy-900">Average Lifespan</td>
                <td class="px-4 py-3 text-emerald-700">15 - 20+ Years</td>
                <td class="px-4 py-3 text-amber-700">10 - 15 Years</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Treatment Timeline in Turkey: Just 5 Days</h2>
        <p class="text-gray-600 mb-4">Thanks to advanced in-house dental laboratories equipped with 3D CAD/CAM milling technology, Turkey's top dental clinics can design and bond your custom Zirconium crowns in a single 5-day visit:</p>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
          <li><strong>Day 1</strong>: Comprehensive examination, panoramic X-rays, 3D CT scan, tooth preparation, digital scanning, and fitting of high-quality temporary crowns.</li>
          <li><strong>Day 2 & 3</strong>: The CAD/CAM digital design process in the clinic's state-of-the-art lab. You can enjoy sightseeing or shopping.</li>
          <li><strong>Day 4</strong>: A trial fitting (mock-up) to test occlusion, fit, and color, followed by glazes and characterization by the dental technicians.</li>
          <li><strong>Day 5</strong>: Permanent adhesive bonding and final polishing. You walk away with a perfect, healthy smile!</li>
        </ul>
        """
    },
    {
        "title": "Türkiye'de BBL (Brazilian Butt Lift) Ameliyatı Rehberi",
        "slug": "turkiyede-bbl-ameliyati-rehberi",
        "category": "Aesthetic",
        "image_url": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=800&q=80",
        "author": "Dr. Ahmet Yılmaz",
        "author_title": "Plastic Surgeon",
        "author_specialty": "Aesthetic & Reconstructive Surgery",
        "author_image": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=150&h=150&q=80",
        "status": "published",
        "content": """
        <p class="text-gray-600 mb-4 font-medium leading-relaxed">Brazilian Butt Lift (BBL), son yıllarda dünyada en çok talep gören vücut şekillendirme operasyonlarından biri haline gelmiştir. Türkiye, uluslararası akreditasyona (JCI) sahip hastaneleri ve ISAPS üyesi deneyimli cerrahlarıyla BBL operasyonlarında en çok tercih edilen ülke konumundadır. Bu kapsamlı rehberde ameliyat süreci, güvenli tıp uygulamaları ve iyileşme dönemine dair bilmeniz gereken her şeyi derledik.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">BBL Ameliyatı Nedir? Vücut Şekillendirmede İki Aşamalı Mucize</h2>
        <p class="text-gray-600 mb-4">BBL, vücudunuzun fazla yağ olan bölgelerinden (karın, bel, sırt veya uyluk) liposuction yöntemiyle yağ alınması ve bu yağların özel işlemlerden geçirilerek popo bölgesine transfer edilmesi işlemidir. Sentetik silikon implantlar yerine hastanın kendi doğal dokusu kullanıldığı için vücut yabancı madde reaksiyonu göstermez ve son derece doğal, kıvrımlı bir silüet elde edilir.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Neden Türkiye'de BBL? Güvenlik ve Uzmanlık</h2>
        <p class="text-gray-600 mb-4">Türkiye'deki plastik cerrahlar, dünya standartlarında vaka deneyimine sahiptir. MediRoute onaylı kliniklerimizde hastaların güvenliğini en üst düzeyde tutmak amacıyla şu altın kurallara kesinlikle uyulur:</p>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
          <li><strong>Güvenli Kanül Teknikleri</strong>: Yağ enjeksiyonu kesinlikle kas içine değil, sadece cilt altındaki yağ dokusuna (subkutan) yapılır. Bu, yağ embolisi riskini sıfıra indirir.</li>
          <li><strong>Tam Teşekküllü Hastane Şartları</strong>: Operasyonlar klinik odalarında değil, mutlaka yoğun bakım ünitesi olan tam donanımlı A-grubu hastanelerde gerçekleştirilir.</li>
          <li><strong>Vaser Liposuction Teknolojisi</strong>: Dokuya zarar vermeyen ultrasonik Vaser Liposuction kullanılarak, çekilen yağ hücrelerinin maksimum canlılıkta kalması sağlanır.</li>
        </ul>

        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">BBL İyileşme Takvimi ve Altın Tavsiyeler</h2>
        <p class="text-gray-600 mb-4">Başarılı bir BBL sonucunun %50'si ameliyata, diğer %50'si ise ameliyat sonrası bakıma bağlıdır:</p>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
          <li><strong>İlk 2-3 Hafta</strong>: Popo üzerine doğrudan oturmak kesinlikle yasaktır. Özel BBL yastığı (BBL pillow) kullanılarak bacak arkasından destek alınarak oturulmalıdır.</li>
          <li><strong>Medikal Korse Kullanımı</strong>: Yağ alınan bölgelerin düzgün şekillenmesi ve ödemin atılması için 6-8 hafta boyunca cerrahi korse takılmalıdır.</li>
          <li><strong>Nihai Sonuç</strong>: Enjekte edilen yağların yaklaşık %60-70'i kalıcı olarak vücutta tutunur. Ödemlerin tamamen inmesi ve poponun son şeklini alması 6 ayı bulmaktadır.</li>
        </ul>
        """
    },
    {
        "title": "Gastric Sleeve Surgery in Turkey: Recovery, Cost & Success Rates",
        "slug": "gastric-sleeve-turkey-guide-2026",
        "category": "Bariatric",
        "image_url": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=800&q=80",
        "author": "Dr. Mehmet Kaya",
        "author_title": "General Surgeon",
        "author_specialty": "Bariatric & Metabolic Surgery",
        "author_image": "https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&w=150&h=150&q=80",
        "status": "published",
        "content": """
        <p class="text-gray-600 mb-4 font-medium leading-relaxed">Obesity is a complex medical condition that affects millions worldwide. Gastric Sleeve Surgery (Sleeve Gastrectomy) has emerged as one of the most effective long-term weight-loss solutions. In Turkey, advanced bariatric centers offer state-of-the-art laparoscopic procedures, expert multidisciplinary care, and comprehensive nutritional support at a fraction of the cost found in private UK or European hospitals.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">What is Gastric Sleeve Surgery? How It Works</h2>
        <p class="text-gray-600 mb-4">Laparoscopic Sleeve Gastrectomy involves removing approximately 75-80% of the stomach, leaving a narrow tube or "sleeve" roughly the size and shape of a banana. This restricts the amount of food you can consume in one sitting. Additionally, the procedure removes the portion of the stomach that produces <strong>Ghrelin</strong> (the primary hunger hormone), significantly reducing appetite and cravings.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Cost Comparison: Turkey vs. UK & Europe</h2>
        <p class="text-gray-600 mb-4">Bariatric surgery in private UK clinics is extremely expensive, often excluding mandatory pre-op and post-op care. Turkey offers all-inclusive medical packages that save you up to 70%:</p>
        <div class="overflow-x-auto my-6 rounded-xl border border-blue-50 shadow-sm">
          <table class="min-w-full divide-y divide-gray-200 text-sm text-left text-gray-500">
            <thead class="bg-navy-950 text-white font-semibold">
              <tr>
                <th class="px-4 py-3">Feature</th>
                <th class="px-4 py-3">United Kingdom (Private)</th>
                <th class="px-4 py-3">Turkey (MediRoute Vetted)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-150 bg-white">
              <tr>
                <td class="px-4 py-3 font-semibold text-navy-900">Average Cost</td>
                <td class="px-4 py-3 text-red-600 font-medium">£9,500 - £12,000</td>
                <td class="px-4 py-3 text-emerald-600 font-bold">£2,800 - £3,900</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold text-navy-900">Hospital Stay</td>
                <td class="px-4 py-3">1 Night (Standard)</td>
                <td class="px-4 py-3 text-navy-800">3 Nights in Hospital + 2 Nights in VIP Hotel</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-semibold text-navy-900">Support Included</td>
                <td class="px-4 py-3">Extra charges apply</td>
                <td class="px-4 py-3 text-navy-800">12 Months Dietician & Post-Op Coordinator Support</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Post-Op Liquid & Solid Diet Timeline</h2>
        <p class="text-gray-600 mb-4">Adapting to your new stomach requires a careful, 4-stage dietary transition over 4-6 weeks to allow the staple lines to heal perfectly:</p>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
          <li><strong>Weeks 1 - 2 (Clear Liquids Only)</strong>: Water, clear broths, herbal teas, and high-protein sugar-free shakes. Sip extremely slowly.</li>
          <li><strong>Weeks 3 - 4 (Pureed Foods)</strong>: Low-fat high-protein foods blended to baby food consistency (pureed salmon, scrambled eggs, yogurt).</li>
          <li><strong>Weeks 5 - 6 (Soft Solids)</strong>: Ground turkey, well-cooked soft vegetables, bananas, and soft fish. Avoid tough meats or fibrous vegetables.</li>
          <li><strong>Week 7 onwards (Regular Healthy Foods)</strong>: Balanced high-protein solid foods. Focus on protein first, chew thoroughly, and never drink liquids during meals.</li>
        </ul>
        """
    },
    {
        "title": "Saç Ekimi Sonrası Şok Dökülme Nedir ve Nasıl Yönetilir?",
        "slug": "sac-ekimi-sonrasi-sok-dokulme",
        "category": "Hair",
        "image_url": "https://images.unsplash.com/photo-1566083042913-671534a759fc?auto=format&fit=crop&w=800&q=80",
        "author": "Dr. Serkan Aygın",
        "author_title": "Hair Restoration Specialist",
        "author_specialty": "Trichology Specialist & Surgeon",
        "author_image": "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=150&h=150&q=80",
        "status": "published",
        "content": """
        <p class="text-gray-600 mb-4 font-medium leading-relaxed">Saç ekimi yaptıran neredeyse her hastanın yaşadığı en endişe verici süreçlerden biri **"Şok Dökülme" (Shock Loss)** aşamasıdır. Operasyonun hemen ardından büyük bir hevesle yeni saçlarını bekleyen hastalar, ekilen saçların aniden döküldüğünü gördüklerinde paniğe kapılabilir. Ancak trikoloji uzmanı olarak belirtmek isterim ki bu dökülme, saç foliküllerinin fizyolojik döngüsünün tamamen normal ve sağlıklı bir parçasıdır.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Şok Dökülme Nedir ve Neden Olur?</h2>
        <p class="text-gray-600 mb-4">Saç kökleri donör bölgeden (başın arkası) alınıp saçsız bölgelere nakledilirken geçici bir süre oksijensiz ve besinsiz kalırlar. Nakil sonrasında kafa derisine yerleşen foliküller kendilerini korumak amacıyla dinlenme (telojen) fazına geçerler. Bu geçiş sürecinde saç telleri dökülür, ancak saç kökü (folikül) deri altında canlı ve sağlıklı kalmaya devam eder. Şok dökülme, yeni ve güçlü saç tellerinin çıkması için eski tellerin atılması işlemidir.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Şok Dökülme Zaman Çizelgesi</h2>
        <p class="text-gray-600 mb-4">Dökülme süreci ve sonrasındaki gelişim genellikle şu kronolojik sırayı takip eder:</p>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
          <li><strong>2. - 4. Hafta (Başlangıç)</strong>: Şok dökülme başlar. Ekilen saçların %70 ila %90'ı bu dönemde tamamen dökülebilir.</li>
          <li><strong>2. - 3. Ay (Durgun Dönem)</strong>: Dökülme durur. Saçlı deride geçici bir seyrelme veya kelleşme görüntüsü oluşur. Bu dönem sabır gerektiren aşamadır.</li>
          <li><strong>3. - 4. Ay (Yeniden Doğuş)</strong>: Deri altındaki foliküllerden yeni, ince ve bebeksi saçlar çıkmaya başlar.</li>
          <li><strong>6. Ay (Belirgin Değişim)</strong>: Çıkan saçlar kalınlaşır ve hacim kazanır. Nihai sonucun yaklaşık %50-60'ı net şekilde gözlemlenir.</li>
        </ul>

        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Şok Dökülme Sürecinde Dikkat Edilmesi Gerekenler</h2>
        <p class="text-gray-600 mb-4">Foliküllerin en iyi şekilde beslenmesi ve güçlü uzaması için şu tavsiyelere uymanız iyileşmeyi hızlandıracaktır:</p>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
          <li><strong>Kafa Derisine Nazik Davranın</strong>: İlk 1 ay kafa derisini tırnaklamaktan, sert masajlardan veya kimyasal jöle/sprey kullanımından kaçının.</li>
          <li><strong>Doğru Şampuan Tercih Edin</strong>: Hekiminizin önerdiği pH 5.5 değerli, kimyasal içermeyen bitkisel veya tıbbi şampuanları kullanın.</li>
          <li><strong>Beslenmenizi Destekleyin</strong>: Saçın ana maddesi olan keratin ve protein üretimini artırmak için Biotin (B7 vitamini), Çinko, Demir ve B kompleks vitaminleri yönünden zengin beslenin.</li>
        </ul>
        """
    },
    {
        "title": "Laser Eye Surgery (LASIK/PRK) in Istanbul: What to Expect",
        "slug": "laser-eye-surgery-istanbul-lasik",
        "category": "Eye",
        "image_url": "https://images.unsplash.com/photo-1579684389782-64d84b5e905d?auto=format&fit=crop&w=800&q=80",
        "author": "Dr. Elif Şahin",
        "author_title": "Ophthalmologist",
        "author_specialty": "Refractive Surgery Specialist",
        "author_image": "https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=150&h=150&q=80",
        "status": "published",
        "content": """
        <p class="text-gray-600 mb-4 font-medium leading-relaxed">Are you tired of relying on glasses or contact lenses for everyday tasks? Laser eye surgery offers a life-changing correction for refractive errors such as myopia (nearsightedness), hyperopia (farsightedness), and astigmatism. Istanbul has become a premier global hub for advanced laser vision correction, offering internationally accredited eye hospitals, elite surgeons, and the latest wavefront laser technologies at an affordable cost.</p>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">LASIK vs. PRK: Understanding the Methods</h2>
        <p class="text-gray-600 mb-4">The two most common methods of laser vision correction are highly effective but differ in how the corneal surface is prepared:</p>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
          <li><strong>LASIK (Laser-Assisted In Situ Keratomileusis)</strong>: The surgeon uses a femtosecond laser to create a micro-thin protective flap on the cornea. The flap is gently folded back, and an excimer laser reshapes the underlying corneal tissue to correct the prescription. The flap is then repositioned, bonding naturally without stitches. Recovery is extremely fast, with most patients achieving 20/20 vision within 24 hours.</li>
          <li><strong>PRK (Photorefractive Keratectomy)</strong>: Instead of creating a flap, the surgeon gently removes the ultra-thin outer layer of the cornea (epithelium). The laser then reshapes the surface. PRK is the preferred solution for patients with thin or irregular corneas. Healing takes slightly longer (3-5 days for the outer cells to fully regenerate), but the long-term visual outcomes are identical to LASIK.</li>
        </ul>
        
        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Why Istanbul is a Top Choice for Refractive Surgery</h2>
        <p class="text-gray-600 mb-4">Ophthalmic centers in Istanbul are equipped with state-of-the-art Diagnostic Wavefront scanners and advanced laser platforms (e.g., Zeiss Mel 90, Schwind Amaris). Vetted MediRoute clinic clinics offer complete packages including VIP hotel stay, medication kits, and standard post-op checkups starting from just **£1,100** for both eyes.</p>

        <h2 class="text-2xl font-bold text-navy-900 mt-6 mb-4">Preparation and Post-Op Success Rules</h2>
        <p class="text-gray-600 mb-4">To ensure a safe procedure and optimal visual outcome, patients must strictly adhere to these ophthalmic rules:</p>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
          <li><strong>Stop Contact Lenses</strong>: Stop wearing soft contact lenses at least 7 days (and hard lenses 3 weeks) before your examination, as lenses temporarily alter the natural shape of your cornea.</li>
          <li><strong>Keep Eyes Hydrated</strong>: Use the prescribed preservative-free lubricating eye drops frequently to prevent dry eye sensations, which are normal and temporary during the initial 3 months of recovery.</li>
          <li><strong>Avoid Water and Rubbing</strong>: Never rub your eyes during the first 2 weeks. Avoid getting shower water, soap, or swimming pool chlorine in your eyes during recovery.</li>
        </ul>
        """
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
        return False

def add_all_blogs():
    print(f"Starting insertion of {len(blogs_to_add)} medical tourism articles...")
    success_count = 0
    for b in blogs_to_add:
        if insert_blog_to_supabase(b):
            success_count += 1
            
    print(f"Insertion complete. {success_count}/{len(blogs_to_add)} articles processed.")
    
    # Automatically execute generate_sitemap.py to rebuild sitemap with these new articles!
    print("Rebuilding sitemap with new articles...")
    try:
        import generate_sitemap
        generate_sitemap.save_sitemaps()
        print("Sitemap successfully updated with new blogs!")
    except Exception as e:
        print("Failed to run generate_sitemap.py automatic update:", e)

    # Automatically execute pre_render_blogs.py to pre-render static HTML pages
    print("Pre-rendering static HTML pages for new articles...")
    try:
        import pre_render_blogs
        pre_render_blogs.render_all_blogs()
        print("Static HTML pages successfully pre-rendered!")
    except Exception as e:
        print("Failed to run pre_render_blogs.py automatic update:", e)

if __name__ == '__main__':
    add_all_blogs()
