import urllib.request
import json

SUPABASE_URL = 'https://phdmnzsdyjhqoqiqwmho.supabase.co'
SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBoZG1uenNkeWpocW9xaXF3bWhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc1NzAzMzksImV4cCI6MjA5MzE0NjMzOX0.zUoYTYjp8Shva1iSVE0oW1ukGpiEOCghPiqc__WisPg'

# Ultra-rich, authoritative medical tourism copy for "sac-ekim-rehberi"
rich_content = """
<p class="text-gray-600 mb-6 font-medium leading-relaxed">Türkiye, özellikle de İstanbul, her yıl 1 milyondan fazla hastanın tercih ettiği <strong>dünya saç ekimi başkenti</strong> haline gelmiştir. Batı ülkelerine kıyasla sunduğu %70'e varan fiyat avantajının yanı sıra, en son safir FUE ve DHI teknolojilerini kullanan dünyaca ünlü cerrahlarıyla bu liderliği elinde tutmaktadır. Bu kapsamlı rehberde; en iyi teknikleri, 3 günlük tedavi takvimini, gerçek maliyet karşılaştırmalarını ve iyileşme sürecine dair tüm detayları bulacaksınız.</p>

<h2 class="text-2xl font-bold text-navy-900 mt-8 mb-4">FUE mi, DHI mi? Doğru Saç Ekimi Tekniğini Seçmek</h2>
<p class="text-gray-600 mb-4">Saç ekiminde başarı oranını belirleyen en önemli unsur, saç dökülme tipinize en uygun tekniğin seçilmesidir. Günümüzde uygulanan en gelişmiş iki yöntem şunlardır:</p>

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-6">
  <div class="bg-blue-50/50 p-5 rounded-2xl border border-blue-100">
    <h3 class="text-lg font-bold text-navy-950 mb-2 flex items-center gap-2">
      <i class="fa-solid fa-gem text-blue-600"></i> Safir FUE (Foliküler Ünite Ekstraksiyonu)
    </h3>
    <p class="text-sm text-gray-600 leading-relaxed">Geleneksel metal bıçaklar yerine, doğal değerli safir kristalinden üretilen ultra ince bıçakların kullanıldığı yöntemdir. Safir uçlar sayesinde açılan kanallar çok daha küçük ve pürüzsüz olur. Bu da kabuklanmayı minimuma indirir, iyileşme sürecini hızlandırır ve maksimum sıklıkta saç ekilmesine olanak tanır. Geniş açıklıklara sahip hastalar için idealdir.</p>
  </div>
  
  <div class="bg-emerald-50/50 p-5 rounded-2xl border border-emerald-100">
    <h3 class="text-lg font-bold text-emerald-950 mb-2 flex items-center gap-2">
      <i class="fa-solid fa-pen-nib text-emerald-600"></i> DHI (Direct Hair Implantation)
    </h3>
    <p class="text-sm text-gray-600 leading-relaxed">Bu yöntemde, özel bir medikal kalem olan <strong>Choi Implanter</strong> kullanılır. Donör bölgeden toplanan saç kökleri, kanal açma ve ekme işlemleri aynı anda olacak şekilde tek bir adımda kafa derisine yerleştirilir. DHI tekniğinin en büyük avantajı, saçların tıraş edilmeden ekilebilmesi ve mevcut saçların arasına zarar vermeden sıklaştırma yapılabilmesidir.</p>
  </div>
</div>

<h2 class="text-2xl font-bold text-navy-900 mt-8 mb-4">İstanbul'da 3 Günlük Tedavi ve Seyahat Programı</h2>
<p class="text-gray-600 mb-4">Türkiye'de saç ekimi operasyonları son derece organize ve konforlu paketler halinde sunulur. İşte İstanbul'daki 3 günlük VIP planınız:</p>

<ul class="list-none pl-0 my-6 space-y-4">
  <li class="flex gap-4 items-start">
    <div class="w-8 h-8 rounded-full bg-navy-950 text-white font-bold flex items-center justify-center shrink-0">1</div>
    <div>
      <h4 class="font-bold text-navy-950 text-base">1. Gün: VIP Karşılama & Konsültasyon</h4>
      <p class="text-sm text-gray-600">Havalimanında sizi karşılayan VIP Mercedes transfer aracınız ile 5 yıldızlı otelinize geçiş yaparsınız. Aynı gün klinikte kan tahlilleri, saç analizi ve doktorunuzla birlikte ekim yapılacak sınırların belirlendiği saç çizgisi tasarımı gerçekleştirilir.</p>
    </div>
  </li>
  <li class="flex gap-4 items-start">
    <div class="w-8 h-8 rounded-full bg-navy-950 text-white font-bold flex items-center justify-center shrink-0">2</div>
    <div>
      <h4 class="font-bold text-navy-950 text-base">2. Gün: Operasyon Günü (6-8 Saat)</h4>
      <p class="text-sm text-gray-600">Ağrısız lokal anestezi (iğnesiz basınçlı anestezi cihazları ile) uygulanır. Uzman ekip tarafından köklerin toplanması, kanalların açılması ve ekim aşamaları titizlikle yürütülür. Operasyon sırasında veya sonrasında saç köklerini beslemek için PRP (Trombositten Zengin Plazma) tedavisi de uygulanır.</p>
    </div>
  </li>
  <li class="flex gap-4 items-start">
    <div class="w-8 h-8 rounded-full bg-navy-950 text-white font-bold flex items-center justify-center shrink-0">3</div>
    <div>
      <h4 class="font-bold text-navy-950 text-base">3. Gün: İlk Yıkama & Medikal Bakım</h4>
      <p class="text-sm text-gray-600">Klinikte ilk pansuman sökülür, özel şampuanlarla ilk saç yıkaması uzmanlar eşliğinde yapılır. Köklerin hızlı tutunması için soğuk lazer tedavisi uygulanır. Bakım şampuanları, ilaç kiti ve boyun yastığınız teslim edilerek havalimanına VIP transferiniz sağlanır.</p>
    </div>
  </li>
</ul>

<h2 class="text-2xl font-bold text-navy-900 mt-8 mb-4">Saç Ekimi Fiyat Karşılaştırması: Türkiye Neden Avantajlı?</h2>
<p class="text-gray-600 mb-4">Türkiye'deki saç ekim merkezleri, yüksek döviz kuru avantajı ve devletin sağlık turizmine sunduğu teşvikler sayesinde operasyon maliyetlerini çok daha rekabetçi seviyelerde tutabilmektedir. İşte ortalama 4500 greft ekim paket fiyatları karşılaştırması:</p>

<div class="overflow-x-auto my-6 rounded-xl border border-blue-50 shadow-sm">
  <table class="min-w-full divide-y divide-gray-200 text-sm text-left text-gray-500">
    <thead class="bg-navy-950 text-white font-semibold">
      <tr>
        <th class="px-4 py-3">Ülke</th>
        <th class="px-4 py-3">Ortalama Fiyat (All-Inclusive Paket)</th>
        <th class="px-4 py-3">Klinik Standartları</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-150 bg-white">
      <tr>
        <td class="px-4 py-3 font-semibold text-navy-900">Türkiye (MediRoute Onaylı)</td>
        <td class="px-4 py-3 text-emerald-600 font-bold">1,800 € - 3,200 €</td>
        <td class="px-4 py-3 text-navy-800">JCI Belgeli Hastane, VIP Transfer, 5* Otel, 1 Yıllık Takip</td>
      </tr>
      <tr>
        <td class="px-4 py-3 font-semibold text-navy-900">İngiltere (UK)</td>
        <td class="px-4 py-3 text-red-600 font-medium">8,000 £ - 14,000 £</td>
        <td class="px-4 py-3">Sadece operasyon (Otel ve transferler dahil değil)</td>
      </tr>
      <tr>
        <td class="px-4 py-3 font-semibold text-navy-900">Almanya</td>
        <td class="px-4 py-3 text-red-600 font-medium">6,000 € - 10,000 €</td>
        <td class="px-4 py-3">Sadece operasyon ve sınırlı post-op destek</td>
      </tr>
      <tr>
        <td class="px-4 py-3 font-semibold text-navy-900">İspanya</td>
        <td class="px-4 py-3 text-red-600 font-medium">5,000 € - 8,500 €</td>
        <td class="px-4 py-3">Standart klinikler (Ek hizmetler ücretlidir)</td>
      </tr>
    </tbody>
  </table>
</div>

<h2 class="text-2xl font-bold text-navy-900 mt-8 mb-4">Saç Ekimi Sonrası Altın Kurallar (İlk 10 Gün)</h2>
<p class="text-gray-600 mb-4">Ekilen saç köklerinin zarar görmemesi ve ilk 10 günlük kritik tutunma sürecinin sağlıklı tamamlanması için şu kurallara kesinlikle uymalısınız:</p>
<ul class="list-disc pl-5 mb-6 text-gray-600 space-y-2">
  <li><strong>Uyku Pozisyonu</strong>: İlk 7 gece, başınız 45 derece yukarıda olacak şekilde size verilen medikal seyahat yastığı ile sırt üstü uyumalısınız. Kafa derinizin yastığa sürtünmesini engelleyin.</li>
  <li><strong>İlk Yıkama</strong>: İlk 10 gün boyunca kafa derisine asla tazyikli su tutmayın. Yıkamayı size öğretildiği şekilde, hafif dokunuşlarla ve medikal köpük şampuanıyla yapın.</li>
  <li><strong>Fiziksel Aktiviteler</strong>: İlk 1 ay boyunca ağır sporlardan, fitness ve ağırlık antrenmanlarından, sauna ve hamam gibi aşırı sıcak ortamlardan kesinlikle uzak durun.</li>
  <li><strong>Güneş ve Yağmur Koruması</strong>: İlk 15 gün kafa derinizi doğrudan güneş ışığından veya sert yağmur damlalarından koruyun. Dışarı çıkarken doktorunuzun onayladığı gevşek şapkaları tercih edin.</li>
</ul>
"""

def update_sac_ekim_rehberi():
    headers = {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': f"Bearer {SUPABASE_ANON_KEY}",
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
    }
    
    # Define fields to update for the premium sac-ekim-rehberi
    payload = {
        "title": "Türkiye'de Saç Ekimi: Fiyatlar, Teknikler (FUE & DHI) ve İyileşme Rehberi",
        "category": "Guide",
        "image_url": "https://images.unsplash.com/photo-1622335088251-89c09c9b58ad?auto=format&fit=crop&w=800&q=80",
        "author": "Dr. Serkan Aygın",
        "author_title": "Hair Restoration Specialist",
        "author_specialty": "Trikoloji Uzmanı & Cerrah",
        "author_image": "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=150&h=150&q=80",
        "status": "published",
        "content": rich_content
    }
    
    patch_url = f"{SUPABASE_URL}/rest/v1/blogs?slug=eq.sac-ekim-rehberi"
    data_bytes = json.dumps(payload).encode('utf-8')
    
    try:
        print("Updating sac-ekim-rehberi article in Supabase...")
        req = urllib.request.Request(patch_url, data=data_bytes, headers=headers, method='PATCH')
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            print("Successfully updated sac-ekim-rehberi with authoritative, premium medical tourism content!")
            
            # Rebuild sitemap
            print("Rebuilding sitemap to ensure the new content is registered...")
            import generate_sitemap
            generate_sitemap.save_sitemaps()
            print("Sitemap update complete!")
            return True
    except Exception as e:
        print("Error updating sac-ekim-rehberi:", e)
        return False

if __name__ == '__main__':
    update_sac_ekim_rehberi()
