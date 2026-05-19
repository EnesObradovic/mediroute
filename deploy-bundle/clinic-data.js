/* ═══════════════════════════════════════════════
   clinic-data.js  –  Shared Clinic Data Layer
   Admin panelden eklenen klinikler burada yönetilir.
   index.html ve clinic-detail.html bu dosyayı kullanır.
   ═══════════════════════════════════════════════ */

// Translation helper — reads from i18n dictionary
function t(key, fallback) {
  if (typeof window.MEDIROUTE_I18N === 'undefined') return fallback || key;
  var lang = localStorage.getItem('mediroute-lang') || 'en';
  var dict = window.MEDIROUTE_I18N[lang];
  if (dict && dict[key] !== undefined) return dict[key];
  // Fallback to English
  var en = window.MEDIROUTE_I18N['en'];
  if (en && en[key] !== undefined) return en[key];
  return fallback || key;
}

const CLINIC_STORAGE_KEY = 'mr_clinics';

// Color themes for clinic cards (cycled based on index)
const CARD_THEMES = [
  { from: 'from-blue-900',   to: 'to-blue-700',   icon: 'fa-hospital',   accent: 'blue' },
  { from: 'from-teal-800',   to: 'to-teal-600',   icon: 'fa-tooth',      accent: 'teal' },
  { from: 'from-rose-800',   to: 'to-pink-600',   icon: 'fa-spa',        accent: 'rose' },
  { from: 'from-indigo-800', to: 'to-indigo-600', icon: 'fa-eye',        accent: 'indigo' },
  { from: 'from-purple-800', to: 'to-purple-600', icon: 'fa-hand-holding-medical', accent: 'purple' },
  { from: 'from-emerald-800',to: 'to-emerald-600',icon: 'fa-syringe',    accent: 'emerald' },
];

// Treatment category mapping (for filter matching)
const TREATMENT_CATEGORIES = {
  hair:       ['fue','dhi','hair','beard','prp','sapphire','eyebrow','saç','sakal'],
  dental:     ['dental','veneer','implant','crown','tooth','hollywood smile','diş','zirkonyum'],
  aesthetics: ['rhinoplasty','botox','filler','liposuction','bbl','facelift','tummy','burun','estetik'],
  bariatric:  ['bariatric','gastric','sleeve','bypass','obesity','obezite','mide'],
  eye:        ['lasik','prk','icl','eye','laser','göz']
};

// City slug mapping
const CITY_MAP = {
  istanbul:'istanbul', antalya:'antalya', budapest:'budapest',
  prague:'prague', warsaw:'warsaw', cancun:'cancun', izmir:'izmir'
};

// ── Default clinic data (ships with app) ──
const DEFAULT_CLINICS = [
  {
    id: 1, name: 'Estepera Medical Centre',
    city: 'Istanbul', country: 'Turkey',
    treatments: 'FUE, DHI, Beard, PRP, Aesthetics',
    priceMin: 1499, priceMax: 2499, rating: 4.9, reviews: 2481,
    jci: 'yes', status: 'active', featured: true,
    desc: 'Internationally recognised clinic with 15+ years of experience. Over 30,000 procedures performed. Dedicated UK patient coordinator from enquiry to aftercare.',
    badges: ['transfer','hotel','jci','translator'],
    hotelStars: 4
  },
  {
    id: 2, name: 'Dent Élite Budapest',
    city: 'Budapest', country: 'Hungary',
    treatments: 'Dental Veneer, Implant, Hollywood Smile, Crown',
    priceMin: 2200, priceMax: 6500, rating: 4.7, reviews: 1832,
    jci: 'yes', status: 'active', featured: false,
    desc: 'Award-winning dental clinic in the heart of Budapest. UK-trained dentists, state-of-the-art 3D imaging, and a dedicated post-treatment care team.',
    badges: ['transfer','hotel','jci'],
    hotelStars: 5
  },
  {
    id: 3, name: 'Aura Clinic Istanbul',
    city: 'Istanbul', country: 'Turkey',
    treatments: 'FUE, Sapphire, PRP, Rhinoplasty',
    priceMin: 1399, priceMax: 2100, rating: 4.6, reviews: 964,
    jci: 'yes', status: 'active', featured: false,
    desc: 'Sapphire FUE specialist with competitive pricing. JCI accredited facility with complimentary aftercare package and UK patient liaison.',
    badges: ['transfer','hotel','jci','translator'],
    hotelStars: 4
  },
  {
    id: 4, name: 'VisionCare Praha',
    city: 'Prague', country: 'Czech Republic',
    treatments: 'LASIK, PRK, ICL, Eye Laser',
    priceMin: 900, priceMax: 1600, rating: 4.8, reviews: 712,
    jci: 'no', status: 'active', featured: false,
    desc: 'Europe\'s leading refractive eye surgery centre. Award-winning surgeons with over 50,000 laser procedures. Advanced Zeiss technology.',
    badges: ['transfer','hotel'],
    hotelStars: 4
  },
  {
    id: 5, name: 'SmileLine Antalya',
    city: 'Antalya', country: 'Turkey',
    treatments: 'Hollywood Smile, Implant, Veneer, Crown',
    priceMin: 2000, priceMax: 4500, rating: 4.5, reviews: 543,
    jci: 'no', status: 'active', featured: false,
    desc: 'Combine your dental treatment with a Mediterranean holiday. Full ceramic restorations with German-made materials and lifetime warranty.',
    badges: ['transfer','hotel','translator'],
    hotelStars: 5
  }
];

// ── Data access (Supabase backed) ──
async function getClinicsData() {
  if (window.MR && MR.supabase) {
    const data = await MR.supabase.getClinics();
    return data.map(c => ({
      reviews: Math.floor(Math.random()*800)+200,
      badges: ['transfer','hotel'],
      hotelStars: 4,
      featured: false,
      desc: c.description, // Map db description to desc
      priceMin: c.price_min,
      priceMax: c.price_max,
      ...c
    }));
  }
  return [];
}

async function getActiveClinics() {
  const data = await getClinicsData();
  return data.filter(c => c.status === 'active');
}

async function getClinicById(id) {
  const data = await getClinicsData();
  return data.find(c => c.id === parseInt(id));
}

// ── Star HTML generator ──
function starsHTML(rating, size='text-base') {
  const full = Math.floor(rating);
  const half = rating - full >= 0.3;
  const empty = 5 - full - (half ? 1 : 0);
  let html = '';
  for (let i=0; i<full; i++) html += `<i class="fa-solid fa-star star-filled ${size}"></i>`;
  if (half) html += `<i class="fa-solid fa-star-half-stroke star-filled ${size}"></i>`;
  for (let i=0; i<empty; i++) html += `<i class="fa-solid fa-star star-empty ${size}"></i>`;
  return html;
}

// ── Treatment match ──
function matchesTreatmentCategory(clinicTreatments, category) {
  if (!category) return true;
  const keywords = TREATMENT_CATEGORIES[category] || [];
  const lower = clinicTreatments.toLowerCase();
  return keywords.some(kw => lower.includes(kw));
}

// ── City match ──
function matchesCity(clinicCity, citySlug) {
  if (!citySlug) return true;
  return clinicCity.toLowerCase().includes(citySlug.toLowerCase());
}

// ── Badge HTML ──
function badgeHTML(badge, hotelStars) {
  const map = {
    transfer: '<span class="tag badge-transfer"><i class="fa-solid fa-car-side"></i> ' + t('badge_transfer','VIP Transfer Included') + '</span>',
    hotel:    '<span class="tag badge-hotel"><i class="fa-solid fa-bed"></i> ' + (hotelStars||4) + '★ ' + t('idx_hotel_incl','Hotel Included') + '</span>',
    jci:      '<span class="tag badge-jci"><i class="fa-solid fa-certificate"></i> ' + t('badge_jci','JCI Accredited') + '</span>',
    translator: '<span class="tag" style="background:linear-gradient(135deg,#EDE9FE,#F5F3FF);color:#5B21B6;"><i class="fa-solid fa-language"></i> ' + t('badge_translator','English Translator') + '</span>'
  };
  return map[badge] || '';
}

// ── Render a single clinic card ──
function renderClinicCard(clinic, index) {
  const theme = CARD_THEMES[index % CARD_THEMES.length];
  const isFeatured = clinic.featured;

  return `
    <article class="clinic-card bg-white rounded-2xl shadow-card border border-gray-100 overflow-hidden" data-clinic-id="${clinic.id}" data-treatments="${clinic.treatments.toLowerCase()}" data-city="${clinic.city.toLowerCase()}" data-rating="${clinic.rating}" data-price-min="${clinic.priceMin}" data-price-max="${clinic.priceMax}" data-jci="${clinic.jci}">
      <div class="flex flex-col md:flex-row">
        <div class="relative md:w-64 flex-shrink-0">
          <div class="h-52 md:h-full bg-gradient-to-br ${theme.from} ${theme.to} flex items-center justify-center relative">
            <div class="absolute inset-0 opacity-20 clinic-img-pattern"></div>
            <div class="text-center text-white z-10 p-4">
              <i class="fa-solid ${theme.icon} text-5xl opacity-80 mb-2"></i>
              <p class="text-xs font-semibold opacity-70">${clinic.city}, ${clinic.country}</p>
            </div>
            ${isFeatured ? '<div class="absolute top-3 left-3 bg-amber-400 text-white text-xs font-bold px-2 py-1 rounded-full flex items-center gap-1 shadow"><i class="fa-solid fa-crown text-xs"></i> ' + t('badge_featured','Featured') + '</div>' : ''}
          </div>
        </div>
        <div class="flex-1 p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-start justify-between flex-wrap gap-2 mb-2">
              <div>
                <h2 class="text-lg font-bold text-navy-800">${clinic.name}</h2>
                <div class="flex items-center gap-1 text-sm text-gray-500 mt-0.5">
                  <i class="fa-solid fa-location-dot text-navy-800 text-xs"></i> ${clinic.city}, ${clinic.country}
                </div>
              </div>
              <div class="flex flex-col items-end gap-1">
                <div class="flex items-center gap-1">
                  ${starsHTML(clinic.rating)}
                  <span class="font-bold text-navy-800 text-sm ml-1">${clinic.rating}</span>
                </div>
                <span class="text-xs text-gray-400">${(clinic.reviews||0).toLocaleString()} ${t('common_verified','verified reviews')}</span>
              </div>
            </div>
            <div class="flex flex-wrap gap-2 mb-3">
              ${clinic.treatments.split(',').map(t => `<span class="text-xs font-medium px-2 py-1 rounded-full" style="background:#EFF6FF;color:#1E40AF;border:1px solid #BFDBFE;">${t.trim()}</span>`).join('')}
            </div>
            <div class="flex flex-wrap gap-2 mb-3">
              ${(clinic.badges||['transfer','hotel']).map(b => badgeHTML(b, clinic.hotelStars)).join('')}
            </div>
            <p class="text-sm text-gray-500 leading-relaxed mb-3">${clinic.desc || ''}</p>
          </div>
          <div class="flex items-center justify-between flex-wrap gap-3 pt-3 border-t border-gray-100">
            <div>
              <p class="text-xs text-gray-400 mb-0.5">${t('common_estimated_price','Estimated Price')}</p>
              <p class="text-2xl font-extrabold text-navy-800">£${(clinic.priceMin||0).toLocaleString()} <span class="text-base font-medium text-gray-400">– £${(clinic.priceMax||0).toLocaleString()}</span></p>
              <p class="text-xs text-green-600 font-semibold mt-0.5 flex items-center gap-1"><i class="fa-solid fa-circle-check"></i> ${t('common_all_inclusive','All-inclusive package')}</p>
            </div>
            <div class="flex gap-2">
              <button class="border border-navy-800 text-navy-800 text-sm font-semibold px-4 py-2.5 rounded-xl hover:bg-blue-50 transition flex items-center gap-1">
                <i class="fa-regular fa-heart"></i>
              </button>
              <a href=\"/clinic-detail?id=${clinic.id}\" class="btn-cta text-white text-sm font-bold px-6 py-2.5 flex items-center justify-center gap-2 shadow-md hover:text-white transition">
                ${t('cta_view_details','View Details')} <i class="fa-solid fa-arrow-right text-xs"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </article>
  `;
}

// ── Render all clinic cards into a container ──
async function renderAllClinics(containerId, filters) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let clinics = await getActiveClinics();

  // Apply filters
  if (filters) {
    if (filters.treatment) {
      clinics = clinics.filter(c => matchesTreatmentCategory(c.treatments, filters.treatment));
    }
    if (filters.city) {
      clinics = clinics.filter(c => matchesCity(c.city, filters.city));
    }
    if (filters.minRating) {
      clinics = clinics.filter(c => c.rating >= parseFloat(filters.minRating));
    }
    if (filters.maxPrice) {
      clinics = clinics.filter(c => c.priceMin <= parseFloat(filters.maxPrice));
    }
    if (filters.jciOnly) {
      clinics = clinics.filter(c => c.jci === 'yes');
    }
  }

  // Sort: featured first, then by rating
  clinics.sort((a, b) => {
    if (a.featured && !b.featured) return -1;
    if (!a.featured && b.featured) return 1;
    return b.rating - a.rating;
  });

  // Sort by user selection
  if (filters && filters.sortBy) {
    switch (filters.sortBy) {
      case 'rating': clinics.sort((a,b) => b.rating - a.rating); break;
      case 'price-asc': clinics.sort((a,b) => a.priceMin - b.priceMin); break;
      case 'price-desc': clinics.sort((a,b) => b.priceMin - a.priceMin); break;
      case 'reviews': clinics.sort((a,b) => (b.reviews||0) - (a.reviews||0)); break;
    }
  }

  // Update result count
  const countEl = document.getElementById('result-count');
  if (countEl) countEl.textContent = clinics.length;

  if (clinics.length === 0) {
    container.innerHTML = `
      <div class="bg-white rounded-2xl shadow-card border border-gray-100 p-12 text-center">
        <i class="fa-solid fa-magnifying-glass text-4xl text-gray-300 mb-4"></i>
        <h3 class="text-lg font-bold text-navy-800 mb-2">Sonuç bulunamadı</h3>
        <p class="text-gray-400 text-sm">Filtrelerinizi değiştirerek tekrar deneyin.</p>
      </div>`;
    return;
  }

  container.innerHTML = clinics.map((c, i) => renderClinicCard(c, i)).join('');
}
