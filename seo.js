/* ═══════════════════════════════════════════════════════════════
   MediRoute SEO Module — Structured Data, OG Tags & Dynamic Meta
   ═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  const BASE = 'https://www.mediroute.co.uk';
  const SITE = 'MediRoute';
  const LOGO = BASE + '/assets/logo.png';
  const OG_IMG = BASE + '/assets/og-cover.jpg';

  /* ── Page meta dictionary (per-lang) ── */
  const META = {
    'index.html': {
      en: { title: 'MediRoute – Find Your Perfect Clinic Abroad', desc: 'Search and compare top-rated clinics for hair transplant, dental, and aesthetic treatments. Trusted by 12,000+ UK patients.' },
      tr: { title: 'MediRoute – Yurtdışında Mükemmel Kliniğinizi Bulun', desc: 'Saç ekimi, diş ve estetik tedaviler için en iyi klinikleri arayın ve karşılaştırın. 12.000+ İngiliz hasta tarafından güveniliyor.' },
      ar: { title: 'MediRoute – اعثر على عيادتك المثالية في الخارج', desc: 'ابحث وقارن بين أفضل العيادات لزراعة الشعر والأسنان والتجميل.' },
      de: { title: 'MediRoute – Finden Sie Ihre perfekte Klinik im Ausland', desc: 'Vergleichen Sie Top-Kliniken für Haartransplantation, Zahnbehandlung und Ästhetik.' },
      fr: { title: 'MediRoute – Trouvez votre clinique idéale à l\'étranger', desc: 'Comparez les meilleures cliniques pour greffe de cheveux, soins dentaires et esthétiques.' }
    },
    'about.html': {
      en: { title: 'About Us | MediRoute', desc: 'MediRoute is an independent UK-registered marketplace connecting patients with verified, JCI-accredited clinics across Europe and Turkey.' },
      tr: { title: 'Hakkımızda | MediRoute', desc: 'MediRoute, hastaları Avrupa ve Türkiye\'deki doğrulanmış, JCI akrediteli kliniklerle buluşturan bağımsız bir İngiltere kayıtlı platformdur.' },
      ar: { title: 'من نحن | MediRoute', desc: 'منصة بريطانية مستقلة تربط المرضى بالعيادات المعتمدة في أوروبا وتركيا.' },
      de: { title: 'Über uns | MediRoute', desc: 'Unabhängiger britischer Marktplatz für verifizierte, JCI-akkreditierte Kliniken.' },
      fr: { title: 'À propos | MediRoute', desc: 'Place de marché britannique indépendante reliant les patients à des cliniques vérifiées.' }
    },
    'contact.html': {
      en: { title: 'Contact Us | MediRoute', desc: 'Get in touch with the MediRoute team. UK helpline, email, WhatsApp support for medical travel enquiries.' },
      tr: { title: 'İletişim | MediRoute', desc: 'MediRoute ekibiyle iletişime geçin. İngiltere yardım hattı, e-posta ve WhatsApp desteği.' },
      ar: { title: 'اتصل بنا | MediRoute', desc: 'تواصل مع فريق MediRoute. خط مساعدة بريطاني ودعم واتساب.' },
      de: { title: 'Kontakt | MediRoute', desc: 'Kontaktieren Sie das MediRoute-Team. UK-Helpline, E-Mail, WhatsApp-Support.' },
      fr: { title: 'Contact | MediRoute', desc: 'Contactez l\'équipe MediRoute. Ligne d\'aide UK, e-mail, WhatsApp.' }
    },
    'compare.html': {
      en: { title: 'Compare Clinics | MediRoute', desc: 'Compare top hair transplant and aesthetic clinics side by side. Prices, reviews, inclusions and accreditations.' },
      tr: { title: 'Klinikleri Karşılaştır | MediRoute', desc: 'En iyi saç ekimi ve estetik kliniklerini yan yana karşılaştırın. Fiyatlar, yorumlar ve akreditasyonlar.' },
      ar: { title: 'قارن العيادات | MediRoute', desc: 'قارن أفضل عيادات زراعة الشعر والتجميل جنباً إلى جنب.' },
      de: { title: 'Kliniken vergleichen | MediRoute', desc: 'Vergleichen Sie Kliniken für Haartransplantation und Ästhetik.' },
      fr: { title: 'Comparer les cliniques | MediRoute', desc: 'Comparez les meilleures cliniques côte à côte.' }
    },
    'blog.html': {
      en: { title: 'Guides & Resources | MediRoute', desc: 'Expert advice and guides for your medical travel journey. Hair transplant, dental and aesthetic treatment tips.' },
      tr: { title: 'Rehberler & Kaynaklar | MediRoute', desc: 'Tıbbi seyahatiniz için uzman tavsiyeleri ve rehberler.' },
      ar: { title: 'أدلة وموارد | MediRoute', desc: 'نصائح الخبراء لرحلتك الطبية.' },
      de: { title: 'Ratgeber & Ressourcen | MediRoute', desc: 'Expertenrat für Ihre medizinische Reise.' },
      fr: { title: 'Guides & Ressources | MediRoute', desc: 'Conseils d\'experts pour votre voyage médical.' }
    },
    'faq.html': {
      en: { title: 'FAQ | MediRoute', desc: 'Answers to the most common questions about medical travel, clinic safety, pricing, and what to expect.' },
      tr: { title: 'SSS | MediRoute', desc: 'Tıbbi seyahat, klinik güvenliği ve fiyatlandırma hakkında sık sorulan sorular.' },
      ar: { title: 'الأسئلة الشائعة | MediRoute', desc: 'إجابات عن أكثر الأسئلة شيوعاً حول السفر الطبي.' },
      de: { title: 'FAQ | MediRoute', desc: 'Antworten auf häufige Fragen zu medizinischen Reisen.' },
      fr: { title: 'FAQ | MediRoute', desc: 'Réponses aux questions fréquentes sur le tourisme médical.' }
    },
    'auth.html': {
      en: { title: 'Sign In / Register | MediRoute', desc: 'Join MediRoute to compare verified clinics, track your quotes and manage your medical travel journey.' },
      tr: { title: 'Giriş / Kayıt | MediRoute', desc: 'MediRoute\'a katılın, doğrulanmış klinikleri karşılaştırın ve tıbbi seyahatinizi yönetin.' },
      ar: { title: 'تسجيل الدخول | MediRoute', desc: 'انضم إلى MediRoute لمقارنة العيادات وتتبع عروضك.' },
      de: { title: 'Anmelden / Registrieren | MediRoute', desc: 'Treten Sie MediRoute bei, um Kliniken zu vergleichen.' },
      fr: { title: 'Connexion / Inscription | MediRoute', desc: 'Rejoignez MediRoute pour comparer les cliniques vérifiées.' }
    },
    'clinic-detail.html': {
      en: { title: 'Clinic Details | MediRoute', desc: 'Detailed clinic profile with doctors, reviews, before & after results and free quote request.' },
      tr: { title: 'Klinik Detayı | MediRoute', desc: 'Doktorlar, yorumlar, öncesi-sonrası sonuçlar ve ücretsiz teklif talebi ile detaylı klinik profili.' },
      ar: { title: 'تفاصيل العيادة | MediRoute', desc: 'ملف تعريف مفصل للعيادة مع الأطباء والمراجعات.' },
      de: { title: 'Klinikdetails | MediRoute', desc: 'Detailliertes Klinikprofil mit Ärzten und Bewertungen.' },
      fr: { title: 'Détails de la clinique | MediRoute', desc: 'Profil détaillé avec médecins, avis et devis gratuit.' }
    }
  };

  /* ── Detect current page ── */
  const path = location.pathname.split('/').pop() || 'index.html';
  const lang = localStorage.getItem('mediroute-lang') || 'en';

  /* ── 1. Update <title> and <meta description> ── */
  function updateMeta(l) {
    const pm = META[path];
    if (!pm) return;
    const m = pm[l] || pm.en;
    document.title = m.title;
    let desc = document.querySelector('meta[name="description"]');
    if (desc) desc.setAttribute('content', m.desc);
  }

  /* ── 2. Inject Open Graph + Twitter Card ── */
  function injectOG() {
    const pm = META[path];
    if (!pm) return;
    const m = pm[lang] || pm.en;
    const pageUrl = BASE + '/' + path;
    const tags = [
      // Open Graph
      { p: 'og:type', c: 'website' },
      { p: 'og:site_name', c: SITE },
      { p: 'og:title', c: m.title },
      { p: 'og:description', c: m.desc },
      { p: 'og:url', c: pageUrl },
      { p: 'og:image', c: OG_IMG },
      { p: 'og:image:width', c: '1200' },
      { p: 'og:image:height', c: '630' },
      { p: 'og:locale', c: lang === 'tr' ? 'tr_TR' : lang === 'ar' ? 'ar_SA' : lang === 'de' ? 'de_DE' : lang === 'fr' ? 'fr_FR' : 'en_GB' },
      // Twitter Card
      { n: 'twitter:card', c: 'summary_large_image' },
      { n: 'twitter:title', c: m.title },
      { n: 'twitter:description', c: m.desc },
      { n: 'twitter:image', c: OG_IMG }
    ];
    const head = document.head;
    tags.forEach(t => {
      let el;
      if (t.p) {
        el = head.querySelector('meta[property="' + t.p + '"]');
        if (!el) { el = document.createElement('meta'); el.setAttribute('property', t.p); head.appendChild(el); }
      } else {
        el = head.querySelector('meta[name="' + t.n + '"]');
        if (!el) { el = document.createElement('meta'); el.setAttribute('name', t.n); head.appendChild(el); }
      }
      el.setAttribute('content', t.c);
    });

    // Canonical URL
    let canon = head.querySelector('link[rel="canonical"]');
    if (!canon) { canon = document.createElement('link'); canon.setAttribute('rel', 'canonical'); head.appendChild(canon); }
    canon.setAttribute('href', pageUrl);
  }

  /* ── 3. JSON-LD Structured Data ── */
  function injectJSONLD() {
    const schemas = [];

    // Organization (on every page)
    schemas.push({
      '@context': 'https://schema.org',
      '@type': 'Organization',
      name: 'MediRoute',
      url: BASE,
      logo: LOGO,
      description: 'UK-registered marketplace connecting patients with verified, JCI-accredited clinics across Europe and Turkey.',
      address: {
        '@type': 'PostalAddress',
        streetAddress: '71-75 Shelton Street',
        addressLocality: 'London',
        addressRegion: 'Covent Garden',
        postalCode: 'WC2H 9JQ',
        addressCountry: 'GB'
      },
      contactPoint: {
        '@type': 'ContactPoint',
        telephone: '+44-800-123-4567',
        contactType: 'customer service',
        availableLanguage: ['English', 'Turkish', 'Arabic', 'German', 'French']
      },
      sameAs: [
        'https://www.facebook.com/mediroute',
        'https://www.instagram.com/mediroute',
        'https://twitter.com/mediroute'
      ]
    });

    // BreadcrumbList
    const crumbs = [{ name: 'Home', url: BASE + '/index.html' }];
    const pageTitles = {
      'about.html': 'About Us', 'contact.html': 'Contact', 'compare.html': 'Compare Clinics',
      'blog.html': 'Guides & Resources', 'faq.html': 'FAQ', 'auth.html': 'Sign In',
      'clinic-detail.html': 'Clinic Details'
    };
    if (pageTitles[path]) {
      crumbs.push({ name: pageTitles[path], url: BASE + '/' + path });
    }
    if (crumbs.length > 1) {
      schemas.push({
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        itemListElement: crumbs.map((c, i) => ({
          '@type': 'ListItem',
          position: i + 1,
          name: c.name,
          item: c.url
        }))
      });
    }

    // WebSite with SearchAction (homepage only)
    if (path === 'index.html' || path === '') {
      schemas.push({
        '@context': 'https://schema.org',
        '@type': 'WebSite',
        name: 'MediRoute',
        url: BASE,
        potentialAction: {
          '@type': 'SearchAction',
          target: BASE + '/index.html?q={search_term_string}',
          'query-input': 'required name=search_term_string'
        }
      });
    }

    // MedicalBusiness (clinic detail page)
    if (path === 'clinic-detail.html') {
      schemas.push({
        '@context': 'https://schema.org',
        '@type': 'MedicalBusiness',
        name: document.querySelector('h1')?.textContent || 'Medical Clinic',
        description: document.querySelector('meta[name="description"]')?.content || '',
        url: BASE + '/clinic-detail.html',
        image: LOGO,
        address: { '@type': 'PostalAddress', addressCountry: 'TR', addressLocality: 'Istanbul' },
        aggregateRating: {
          '@type': 'AggregateRating',
          ratingValue: '4.9',
          reviewCount: '847',
          bestRating: '5'
        },
        priceRange: '£1,499 – £2,499'
      });
    }

    // Inject all schemas
    schemas.forEach(s => {
      const script = document.createElement('script');
      script.type = 'application/ld+json';
      script.textContent = JSON.stringify(s);
      document.head.appendChild(script);
    });
  }

  /* ── 4. Listen for language changes ── */
  function onLangChange() {
    // Monitor mediroute-lang changes (used by shared.js)
    const origSetItem = localStorage.setItem;
    localStorage.setItem = function (key, val) {
      origSetItem.call(this, key, val);
      if (key === 'mediroute-lang') {
        updateMeta(val);
      }
    };
  }

  /* ── Init ── */
  updateMeta(lang);
  injectOG();
  injectJSONLD();
  onLangChange();

  // Expose hook for shared.js language switcher
  window.__MR_SEO_UPDATE = updateMeta;

})();
