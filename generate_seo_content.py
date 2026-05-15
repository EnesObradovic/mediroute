import json

data = {
  'hair-transplant': {
    'slug': 'hair-transplant',
    'icon': 'fa-solid fa-scissors',
    'title': { 'en': 'Hair Transplant in Turkey', 'tr': 'Türkiye\'de Saç Ekimi' },
    'heroSub': { 'en': 'World-class FUE & DHI hair restoration starting from £1,499 all-inclusive', 'tr': 'Dünya standartlarında FUE & DHI saç restorasyonu, her şey dahil £1.499\'dan başlayan fiyatlarla' },
    'metaDesc': { 'en': 'Compare top-rated hair transplant clinics in Turkey. FUE & DHI techniques, all-inclusive packages with hotel & transfer.', 'tr': 'Türkiye\'nin en iyi saç ekimi kliniklerini karşılaştırın. FUE & DHI teknikleri, otel & transfer dahil paketler.' },
    'stats': [
      { 'val': '30,000+', 'en': 'Procedures/Year', 'tr': 'Yıllık İşlem' },
      { 'val': '£1,499', 'en': 'Starting Price', 'tr': 'Başlangıç Fiyatı' },
      { 'val': '98%', 'en': 'Success Rate', 'tr': 'Başarı Oranı' },
      { 'val': '3-5', 'en': 'Days Recovery', 'tr': 'Gün İyileşme' }
    ],
    'techniques': [
      { 'name': 'FUE', 'en': 'Follicular Unit Extraction — individual grafts harvested with micro-punch tool. Minimal scarring.', 'tr': 'Foliküler Ünite Ekstraksiyonu — mikro punch aletiyle tek tek greft alımı. Minimum iz.' },
      { 'name': 'DHI', 'en': 'Direct Hair Implantation — implanted directly with Choi pen. No canal opening needed.', 'tr': 'Doğrudan Saç İmplantasyonu — Choi kalemiyle doğrudan ekim. Kanal açma gerektirmez.' },
      { 'name': 'Sapphire FUE', 'en': 'Premium FUE with sapphire blades for finer incisions and faster healing.', 'tr': 'Safir bıçaklarla premium FUE, daha ince kesiler ve hızlı iyileşme.' }
    ],
    'faq': [
      { 'q': { 'en': 'How many grafts do I need?', 'tr': 'Kaç grefte ihtiyacım var?' }, 'a': { 'en': 'Typically 2,000-5,000 grafts depending on hair loss level.', 'tr': 'Saç dökülme seviyesine bağlı olarak genellikle 2.000-5.000 greft.' } },
      { 'q': { 'en': 'When will I see results?', 'tr': 'Sonuçları ne zaman göreceğim?' }, 'a': { 'en': 'Initial growth at 3-4 months, full results at 12-18 months.', 'tr': 'İlk büyüme 3-4 ay, tam sonuçlar 12-18 ay.' } }
    ],
    'filterValue': 'hair',
    'seoContent': {
      'en': '''
        <h2 class="text-2xl font-bold text-navy-900 mb-4">The Ultimate Guide to Hair Transplants in Turkey</h2>
        <p class="text-gray-600 mb-4">Turkey, particularly Istanbul, has firmly established itself as the global capital for hair transplantation. Combining world-renowned surgeons, state-of-the-art medical facilities, and highly competitive pricing, over a million patients travel to Turkey annually to restore their hair.</p>
        <h3 class="text-xl font-semibold text-navy-800 mt-6 mb-3">Why Choose Turkey for Hair Restoration?</h3>
        <p class="text-gray-600 mb-4">The cost of a hair transplant in the UK, US, or Western Europe can easily exceed £10,000. In contrast, <strong>top-tier clinics in Turkey offer all-inclusive packages</strong> starting around £1,499. These packages typically include:</p>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
            <li>Maximum grafts required (no hidden per-graft fees)</li>
            <li>3 nights accommodation in a 4 or 5-star hotel</li>
            <li>VIP airport transfers and clinic transportation</li>
            <li>Pre-operative blood tests and post-operative medications</li>
            <li>12 months of dedicated aftercare and follow-up</li>
        </ul>
        <h3 class="text-xl font-semibold text-navy-800 mt-6 mb-3">Advanced Techniques: FUE vs DHI</h3>
        <p class="text-gray-600 mb-4">Modern clinics in Turkey utilize cutting-edge techniques. <strong>FUE (Follicular Unit Extraction)</strong> is ideal for covering large areas of baldness, utilizing micro-punches to extract and implant grafts without linear scarring. <strong>DHI (Direct Hair Implantation)</strong> uses a specialized Choi Implanter Pen, allowing for maximum density and the ability to implant without fully shaving the head.</p>
        <p class="text-gray-600">By booking through MediRoute, you are guaranteed access to strictly vetted, JCI-accredited clinics and board-certified surgeons, ensuring the highest standards of safety and aesthetic excellence.</p>
      ''',
      'tr': '''
        <h2 class="text-2xl font-bold text-navy-900 mb-4">Türkiye\'de Saç Ekimi: Kapsamlı Rehber</h2>
        <p class="text-gray-600 mb-4">Türkiye ve özellikle İstanbul, saç ekimi konusunda dünyanın başkenti haline gelmiştir. Dünyaca ünlü cerrahlar, son teknoloji tesisler ve rekabetçi fiyatlar sayesinde her yıl bir milyondan fazla hasta saçlarını geri kazanmak için Türkiye\'yi tercih ediyor.</p>
        <h3 class="text-xl font-semibold text-navy-800 mt-6 mb-3">Neden Saç Ekimi İçin Türkiye\'yi Seçmelisiniz?</h3>
        <p class="text-gray-600 mb-4">Avrupa veya Amerika\'da saç ekimi maliyetleri 10.000£\'u aşabilirken, <strong>Türkiye\'deki en iyi klinikler her şey dahil paketleri</strong> ortalama 1.499£\'dan başlayan fiyatlarla sunmaktadır. Bu paketler genellikle şunları içerir:</p>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
            <li>Gerekli olan maksimum greft (greft başına gizli ücret yok)</li>
            <li>4 veya 5 yıldızlı lüks otellerde konaklama</li>
            <li>VIP havalimanı ve klinik transferleri</li>
            <li>Operasyon öncesi testler ve sonrası ilaçlar</li>
            <li>12 aylık özel hasta takibi</li>
        </ul>
        <h3 class="text-xl font-semibold text-navy-800 mt-6 mb-3">Gelişmiş Teknikler: FUE ve DHI</h3>
        <p class="text-gray-600 mb-4">Türkiye\'deki modern klinikler en son teknolojileri kullanır. <strong>FUE</strong> geniş açıklıkları kapatmak için idealken, <strong>DHI</strong> (Choi kalemi) tıraşsız ekim ve maksimum yoğunluk sağlar.</p>
        <p class="text-gray-600">MediRoute üzerinden rezervasyon yaparak, güvenlik ve estetik mükemmellik standartlarını karşılayan, sıkı denetimden geçmiş JCI akreditasyonlu kliniklere ulaşırsınız.</p>
      '''
    }
  },
  'dental': {
    'slug': 'dental',
    'icon': 'fa-solid fa-tooth',
    'title': { 'en': 'Dental Treatment in Turkey', 'tr': 'Türkiye\'de Diş Tedavisi' },
    'heroSub': { 'en': 'Hollywood smile, veneers, implants & crowns — save up to 70% vs UK prices', 'tr': 'Hollywood gülüşü, kaplama, implant & kron — İngiltere fiyatlarına göre %70\'e kadar tasarruf' },
    'metaDesc': { 'en': 'Top dental clinics in Turkey for veneers, implants and smile makeovers. All-inclusive packages.', 'tr': 'Kaplama, implant ve gülüş tasarımı için Türkiye\'nin en iyi diş klinikleri.' },
    'stats': [
      { 'val': '50,000+', 'en': 'Smiles Created', 'tr': 'Oluşturulan Gülüş' },
      { 'val': '£199', 'en': 'Per Veneer', 'tr': 'Kaplama Başına' },
      { 'val': '99%', 'en': 'Satisfaction', 'tr': 'Memnuniyet' },
      { 'val': '5-7', 'en': 'Days Treatment', 'tr': 'Gün Tedavi' }
    ],
    'techniques': [
      { 'name': 'E-Max Veneers', 'en': 'Ultra-thin porcelain shells for a natural, bright smile. Minimal tooth preparation.', 'tr': 'Doğal, parlak gülüş için ultra ince porselen kaplamalar. Minimum diş hazırlığı.' },
      { 'name': 'Dental Implants', 'en': 'Titanium root replacement with ceramic crown. Lifetime solution for missing teeth.', 'tr': 'Seramik kronlu titanyum kök değişimi. Eksik dişler için ömür boyu çözüm.' }
    ],
    'faq': [
      { 'q': { 'en': 'How long do veneers last?', 'tr': 'Kaplamalar ne kadar sürer?' }, 'a': { 'en': 'E-Max veneers typically last 15-20 years with proper care.', 'tr': 'E-Max kaplamalar uygun bakımla genellikle 15-20 yıl sürer.' } }
    ],
    'filterValue': 'dental',
    'seoContent': {
      'en': '''
        <h2 class="text-2xl font-bold text-navy-900 mb-4">Complete Guide to Dental Treatments in Turkey</h2>
        <p class="text-gray-600 mb-4">Dental tourism in Turkey has exploded in popularity, offering patients the chance to achieve a perfect "Hollywood Smile" while saving up to 70% compared to UK, US, or Western European prices. Cities like Istanbul, Antalya, and Izmir are home to state-of-the-art dental centers equipped with 3D CAD/CAM technology.</p>
        <h3 class="text-xl font-semibold text-navy-800 mt-6 mb-3">Popular Dental Procedures</h3>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
            <li><strong>E-Max Veneers:</strong> Known for their durability and natural translucency, E-Max veneers require minimal tooth shaving and provide a flawless, bright smile.</li>
            <li><strong>Dental Implants:</strong> Using premium global brands like Straumann or Nobel Biocare, Turkish clinics offer permanent solutions for missing teeth, including All-on-4 and All-on-6 full arch restorations.</li>
            <li><strong>Zirconium Crowns:</strong> Exceptionally strong and aesthetically pleasing, ideal for both front and back teeth restorations.</li>
        </ul>
        <h3 class="text-xl font-semibold text-navy-800 mt-6 mb-3">The Dental Holiday Experience</h3>
        <p class="text-gray-600">A typical veneer procedure takes about 5 to 7 days. During the downtime between fittings, patients can enjoy a luxury holiday. MediRoute ensures your treatment plan is handled by certified cosmetic dentists, complete with VIP transfers and hotel accommodations.</p>
      ''',
      'tr': '''
        <h2 class="text-2xl font-bold text-navy-900 mb-4">Türkiye\'de Diş Tedavisi: Kusursuz Gülüşler</h2>
        <p class="text-gray-600 mb-4">Türkiye\'de sağlık turizmi, özellikle diş alanında son yıllarda inanılmaz bir büyüme göstermiştir. Hastalar, Avrupa fiyatlarına kıyasla %70\'e varan tasarruflarla mükemmel bir "Hollywood Gülüşüne" sahip olabiliyorlar.</p>
        <h3 class="text-xl font-semibold text-navy-800 mt-6 mb-3">En Çok Tercih Edilen İşlemler</h3>
        <ul class="list-disc pl-5 mb-4 text-gray-600 space-y-2">
            <li><strong>E-Max Zirkonyum:</strong> Doğal görünümü ve dayanıklılığı ile bilinen E-Max kaplamalar, minimum diş kesimi ile uygulanır.</li>
            <li><strong>Diş İmplantları:</strong> Straumann gibi birinci sınıf markalar kullanılarak, eksik dişler için ömür boyu kalıcı çözümler (All-on-4, All-on-6) sunulur.</li>
        </ul>
        <p class="text-gray-600">Tedavi süreci genellikle 5-7 gün sürer. MediRoute, süreci tamamen planlayarak VIP transfer, lüks konaklama ve sertifikalı hekim garantisi sunar.</p>
      '''
    }
  },
  'aesthetics': {
    'slug': 'aesthetics',
    'icon': 'fa-solid fa-spa',
    'title': { 'en': 'Aesthetic Surgery in Turkey', 'tr': 'Türkiye\'de Estetik Cerrahi' },
    'heroSub': { 'en': 'Rhinoplasty, BBL, liposuction & more — board-certified surgeons', 'tr': 'Burun estetiği, BBL, liposuction ve daha fazlası — sertifikalı cerrahlar' },
    'metaDesc': { 'en': 'Aesthetic surgery in Turkey: rhinoplasty, tummy tuck, BBL. JCI-accredited clinics.', 'tr': 'Türkiye\'de estetik cerrahi: burun estetiği, karın germe, BBL. JCI akredite klinikler.' },
    'stats': [
      { 'val': '20,000+', 'en': 'Surgeries/Year', 'tr': 'Yıllık Ameliyat' },
      { 'val': '£2,499', 'en': 'Starting Price', 'tr': 'Başlangıç Fiyatı' },
      { 'val': '97%', 'en': 'Satisfaction', 'tr': 'Memnuniyet' },
      { 'val': '7-14', 'en': 'Days Recovery', 'tr': 'Gün İyileşme' }
    ],
    'techniques': [
      { 'name': 'Rhinoplasty', 'en': 'Nose reshaping for aesthetic or functional improvement.', 'tr': 'Estetik veya fonksiyonel iyileştirme için burun şekillendirme.' },
      { 'name': 'Liposuction', 'en': 'Fat removal with VASER or laser-assisted technology.', 'tr': 'VASER veya lazer teknolojisi ile bölgesel yağ alma.' }
    ],
    'faq': [
      { 'q': { 'en': 'How long is recovery?', 'tr': 'İyileşme ne kadar sürer?' }, 'a': { 'en': 'Rhinoplasty: 7-10 days. Full results in 6 months.', 'tr': 'Burun estetiği: 7-10 gün. Tam sonuçlar 6 ayda.' } }
    ],
    'filterValue': 'aesthetics',
    'seoContent': {
      'en': '''
        <h2 class="text-2xl font-bold text-navy-900 mb-4">Transformative Aesthetic Surgery in Turkey</h2>
        <p class="text-gray-600 mb-4">Turkey has emerged as a premier destination for cosmetic and plastic surgery. Renowned for highly skilled, board-certified surgeons and luxurious recovery facilities, patients travel from across the globe for procedures like Rhinoplasty, Brazilian Butt Lifts (BBL), Mommy Makeovers, and VASER Liposuction.</p>
        <h3 class="text-xl font-semibold text-navy-800 mt-6 mb-3">Why Undergo Surgery in Istanbul or Antalya?</h3>
        <p class="text-gray-600 mb-4">The level of surgical expertise in Turkey is world-class. Many surgeons are members of international societies like ISAPS. Furthermore, the all-inclusive model means that your surgery, hospital stay, hotel accommodation, and private transfers are bundled into one affordable price—often 50-60% less than in the UK or US.</p>
        <h3 class="text-xl font-semibold text-navy-800 mt-6 mb-3">Safety and Accreditation</h3>
        <p class="text-gray-600">Patient safety is paramount. MediRoute partners exclusively with JCI-accredited hospitals equipped with modern ICUs and strict hygiene protocols. From your initial online consultation to your final post-op check, every step is rigorously monitored.</p>
      ''',
      'tr': '''
        <h2 class="text-2xl font-bold text-navy-900 mb-4">Türkiye\'de Estetik ve Plastik Cerrahi</h2>
        <p class="text-gray-600 mb-4">Türkiye, plastik cerrahi alanında küresel bir merkezdir. Burun estetiği (Rinoplasti), BBL, Karın Germe ve Liposuction gibi işlemlerde uzmanlaşmış Türk cerrahlar, dünya çapında haklı bir üne sahiptir.</p>
        <h3 class="text-xl font-semibold text-navy-800 mt-6 mb-3">Güvenlik ve Konfor</h3>
        <p class="text-gray-600 mb-4">Estetik ameliyatlar, JCI akreditasyonuna sahip tam teşekküllü uluslararası hastanelerde gerçekleştirilir. Avrupa ve Amerika\'ya kıyasla çok daha uygun maliyetlerle, birinci sınıf sağlık hizmeti alırsınız.</p>
        <p class="text-gray-600">MediRoute, yalnızca deneyimli hekimlerle çalışarak iyileşme sürecinizin 5 yıldızlı otellerde, VIP transfer güvencesiyle konforlu geçmesini sağlar.</p>
      '''
    }
  },
  'bariatric': {
    'slug': 'bariatric',
    'icon': 'fa-solid fa-weight-scale',
    'title': { 'en': 'Bariatric Surgery in Turkey', 'tr': 'Türkiye\'de Obezite Cerrahisi' },
    'heroSub': { 'en': 'Gastric sleeve, bypass & balloon — transform your life', 'tr': 'Tüp mide, bypass & balon — hayatınızı dönüştürün' },
    'metaDesc': { 'en': 'Bariatric surgery in Turkey: gastric sleeve, bypass. Accredited hospitals.', 'tr': 'Türkiye\'de obezite cerrahisi: tüp mide, bypass. Akredite hastaneler.' },
    'stats': [
      { 'val': '15,000+', 'en': 'Surgeries Done', 'tr': 'Yapılan Ameliyat' },
      { 'val': '£3,499', 'en': 'Starting Price', 'tr': 'Başlangıç Fiyatı' },
      { 'val': '96%', 'en': 'Success Rate', 'tr': 'Başarı Oranı' },
      { 'val': '5-7', 'en': 'Days Recovery', 'tr': 'Gün İyileşme' }
    ],
    'techniques': [
      { 'name': 'Gastric Sleeve', 'en': '80% of stomach removed. Most popular weight loss surgery.', 'tr': 'Midenin %80\'i alınır. En popüler kilo verme ameliyatı.' }
    ],
    'faq': [
      { 'q': { 'en': 'What BMI do I need?', 'tr': 'Hangi BMI gerekli?' }, 'a': { 'en': 'Generally BMI 30+ for sleeve, BMI 35+ for bypass.', 'tr': 'Genel olarak tüp mide için BMI 30+, bypass için BMI 35+.' } }
    ],
    'filterValue': 'bariatric',
    'seoContent': {
      'en': '''
        <h2 class="text-2xl font-bold text-navy-900 mb-4">Weight Loss Surgery: Start Your New Life in Turkey</h2>
        <p class="text-gray-600 mb-4">Bariatric surgery is a life-changing step towards better health. Turkey offers highly experienced bariatric surgeons and advanced laparoscopic technology, making procedures like the Gastric Sleeve and Gastric Bypass safe, affordable, and effective.</p>
        <h3 class="text-xl font-semibold text-navy-800 mt-6 mb-3">Comprehensive Care Packages</h3>
        <p class="text-gray-600 mb-4">Undergoing bariatric surgery abroad requires meticulous planning. MediRoute partner clinics provide comprehensive packages that include extensive pre-operative cardio and metabolic testing, nutritional counseling, the surgery itself, and a minimum of 3 to 4 nights in the hospital under close monitoring.</p>
        <p class="text-gray-600">Aftercare is crucial for weight loss surgery. You will receive a detailed dietary plan and long-term remote follow-ups with dietitians to ensure you achieve your weight goals safely.</p>
      ''',
      'tr': '''
        <h2 class="text-2xl font-bold text-navy-900 mb-4">Obezite Cerrahisi ile Yeni Bir Hayat</h2>
        <p class="text-gray-600 mb-4">Kilo verme ameliyatları (Tüp Mide, Mide Bypass vb.), sağlığınıza kavuşmanız için kritik bir adımdır. Türkiye, deneyimli obezite cerrahları ve gelişmiş laparoskopik teknolojileriyle güvenli ve uygun fiyatlı çözümler sunar.</p>
        <h3 class="text-xl font-semibold text-navy-800 mt-6 mb-3">Kapsamlı Değerlendirme ve Bakım</h3>
        <p class="text-gray-600">Ameliyat öncesinde detaylı kardiyolojik ve metabolik testler yapılır. Ameliyat sonrası dönemde ise diyetisyen takibi ve uzun vadeli beslenme planlaması, başarılı kilo kaybının anahtarıdır. MediRoute, bu kritik sürecin her aşamasında yanınızdadır.</p>
      '''
    }
  },
  'eye-surgery': {
    'slug': 'eye-surgery',
    'icon': 'fa-solid fa-eye',
    'title': { 'en': 'Eye Surgery in Turkey', 'tr': 'Türkiye\'de Göz Cerrahisi' },
    'heroSub': { 'en': 'LASIK, lens replacement & cataract surgery — see clearly', 'tr': 'LASIK, lens değişimi & katarakt ameliyatı — net görün' },
    'metaDesc': { 'en': 'Eye surgery in Turkey: LASIK, lens replacement. Save up to 60%.', 'tr': 'Türkiye\'de göz cerrahisi: LASIK, lens değişimi. %60 tasarruf.' },
    'stats': [
      { 'val': '25,000+', 'en': 'Eyes Treated', 'tr': 'Tedavi Edilen Göz' },
      { 'val': '£899', 'en': 'Starting Price', 'tr': 'Başlangıç Fiyatı' },
      { 'val': '99%', 'en': 'Success Rate', 'tr': 'Başarı Oranı' },
      { 'val': '1-2', 'en': 'Days Recovery', 'tr': 'Gün İyileşme' }
    ],
    'techniques': [
      { 'name': 'LASIK', 'en': 'Laser vision correction for myopia, hyperopia and astigmatism.', 'tr': 'Miyopi, hipermetropi ve astigmat için lazer görme düzeltme.' }
    ],
    'faq': [
      { 'q': { 'en': 'Am I a candidate for LASIK?', 'tr': 'LASIK için aday mıyım?' }, 'a': { 'en': 'Most people 18+ with stable prescription are candidates.', 'tr': '18+ yaş ve stabil reçetesi olan çoğu kişi adaydır.' } }
    ],
    'filterValue': 'eye',
    'seoContent': {
      'en': '''
        <h2 class="text-2xl font-bold text-navy-900 mb-4">Advanced Laser Eye Surgery in Turkey</h2>
        <p class="text-gray-600 mb-4">Say goodbye to glasses and contact lenses. Turkey\'s specialized eye hospitals use the exact same FDA-approved laser technologies (like Zeiss and Alcon) found in top European and American clinics, but at a fraction of the cost.</p>
        <h3 class="text-xl font-semibold text-navy-800 mt-6 mb-3">Popular Treatments</h3>
        <p class="text-gray-600 mb-4">Whether you need <strong>LASIK, SMILE, or Smart Lens Replacement</strong> (multifocal IOLs for patients over 40), Turkish ophthalmologists are globally recognized for their precision and high success rates.</p>
        <p class="text-gray-600">The procedure is incredibly fast—often taking less than 15 minutes per eye—and recovery is rapid. Most patients can see clearly and enjoy the vibrant city of Istanbul the very next day.</p>
      ''',
      'tr': '''
        <h2 class="text-2xl font-bold text-navy-900 mb-4">Türkiye\'de İleri Lazer Göz Cerrahisi</h2>
        <p class="text-gray-600 mb-4">Gözlük ve lenslere veda edin. Türkiye\'deki tam donanımlı göz hastaneleri, Avrupa ve Amerika\'daki en iyi kliniklerde bulunan FDA onaylı lazer teknolojilerinin (Zeiss, Alcon vb.) aynısını çok daha uygun fiyatlarla sunmaktadır.</p>
        <h3 class="text-xl font-semibold text-navy-800 mt-6 mb-3">Hızlı ve Kesin Sonuçlar</h3>
        <p class="text-gray-600">İşlem genellikle göz başına 15 dakikadan az sürer ve iyileşme inanılmaz derecede hızlıdır. Birçok hasta ertesi gün net bir görüşe kavuşur. Kapsamlı göz muayeneleri ve ömür boyu garanti sunan kliniklerimiz, maksimum memnuniyet sağlar.</p>
      '''
    }
  }
}

with open("treatment-data.js", "w") as f:
    f.write(f"window.TREATMENTS = {json.dumps(data, indent=2)};\n")
