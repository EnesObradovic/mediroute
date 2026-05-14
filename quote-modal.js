/* ═══════════════════════════════════════════════
   quote-modal.js  –  Ücretsiz Teklif Talebi Modalı
   Navbar'daki "Get Free Quote" butonunu yakalar,
   modal form açar, talepleri localStorage'a kaydeder.
   Admin panelinde leads tablosunda görüntülenir.
   ═══════════════════════════════════════════════ */

(function() {
  'use strict';

  const LEADS_KEY = 'mr_leads';

  // ── Default leads (same as admin-logic.js) ──
  const DEFAULT_LEADS = [
    {id:1,name:'James T.',city:'London',treatment:'FUE Hair Transplant',clinic:'Estepera Medical',source:'organic',date:'12 Nis 2025',status:'completed'},
    {id:2,name:'Sarah M.',city:'Birmingham',treatment:'DHI + Eyebrow',clinic:'Estepera Medical',source:'paid',date:'11 Nis 2025',status:'confirmed'},
    {id:3,name:'Robert K.',city:'Edinburgh',treatment:'FUE Hair Transplant',clinic:'Aura Clinic',source:'referral',date:'10 Nis 2025',status:'completed'},
    {id:4,name:'Emily W.',city:'Manchester',treatment:'PRP Therapy',clinic:'Estepera Medical',source:'organic',date:'09 Nis 2025',status:'contacted'},
    {id:5,name:'Daniel P.',city:'Bristol',treatment:'Beard Transplant',clinic:'Aura Clinic',source:'paid',date:'08 Nis 2025',status:'new'},
    {id:6,name:'Olivia H.',city:'Leeds',treatment:'Dental Implant',clinic:'Dent Élite Budapest',source:'direct',date:'07 Nis 2025',status:'completed'},
    {id:7,name:'Thomas G.',city:'Liverpool',treatment:'DHI Hair Transplant',clinic:'Estepera Medical',source:'organic',date:'06 Nis 2025',status:'contacted'},
    {id:8,name:'Charlotte B.',city:'London',treatment:'LASIK Eye Surgery',clinic:'VisionCare Praha',source:'paid',date:'05 Nis 2025',status:'cancelled'},
    {id:9,name:'Jack N.',city:'Sheffield',treatment:'FUE Hair Transplant',clinic:'Aura Clinic',source:'referral',date:'04 Nis 2025',status:'confirmed'},
    {id:10,name:'Amelia F.',city:'Newcastle',treatment:'Hollywood Smile',clinic:'SmileLine Antalya',source:'organic',date:'03 Nis 2025',status:'new'}
  ];

  function getLeads() {
    const stored = localStorage.getItem(LEADS_KEY);
    if (stored) return JSON.parse(stored);
    localStorage.setItem(LEADS_KEY, JSON.stringify(DEFAULT_LEADS));
    return DEFAULT_LEADS;
  }
  function saveLeads(arr) { localStorage.setItem(LEADS_KEY, JSON.stringify(arr)); }

  // ── Inject modal HTML ──
  function injectQuoteModal() {
    const modal = document.createElement('div');
    modal.id = 'quote-modal';
    modal.className = 'quote-modal-overlay';
    modal.innerHTML = `
      <div class="quote-modal-box">
        <!-- Step indicator -->
        <div class="quote-steps" id="quote-steps">
          <div class="quote-step active" data-step="1"><span>1</span> Bilgileriniz</div>
          <div class="quote-step" data-step="2"><span>2</span> Tedavi Detayı</div>
          <div class="quote-step" data-step="3"><span>3</span> Tamamlandı</div>
        </div>

        <button onclick="closeQuoteModal()" class="quote-close"><i class="fa-solid fa-xmark"></i></button>
        
        <!-- STEP 1: Personal Info -->
        <div class="quote-panel active" id="qstep-1">
          <div class="quote-icon-row"><div class="quote-icon-circle"><i class="fa-solid fa-user"></i></div></div>
          <h2 class="quote-title">Ücretsiz Teklif Al</h2>
          <p class="quote-subtitle">Bilgilerinizi girin, en uygun klinikleri bulalım</p>
          <form onsubmit="quoteStep2(event)" novalidate>
            <div class="quote-grid">
              <div><label class="quote-label">Ad Soyad</label><input id="q-name" class="quote-input" placeholder="John Smith" required/></div>
              <div><label class="quote-label">E-posta</label><input id="q-email" type="email" class="quote-input" placeholder="john@email.com" required/></div>
            </div>
            <div class="quote-grid">
              <div><label class="quote-label">Telefon</label><input id="q-phone" class="quote-input" placeholder="+44 7700 900000"/></div>
              <div><label class="quote-label">Şehir / Ülke</label><input id="q-city" class="quote-input" placeholder="London, UK" required/></div>
            </div>
            <button type="submit" class="quote-btn">Devam Et <i class="fa-solid fa-arrow-right"></i></button>
          </form>
        </div>

        <!-- STEP 2: Treatment Details -->
        <div class="quote-panel" id="qstep-2">
          <div class="quote-icon-row"><div class="quote-icon-circle" style="background:linear-gradient(135deg,#059669,#10B981);"><i class="fa-solid fa-stethoscope"></i></div></div>
          <h2 class="quote-title">Tedavi Detayları</h2>
          <p class="quote-subtitle">İlgilendiğiniz tedavi türünü seçin</p>
          <form onsubmit="submitQuote(event)" novalidate>
            <div><label class="quote-label">Tedavi Türü</label>
              <select id="q-treatment" class="quote-input" required>
                <option value="">Seçiniz...</option>
                <option value="FUE Hair Transplant">FUE Saç Ekimi</option>
                <option value="DHI Hair Transplant">DHI Saç Ekimi</option>
                <option value="Beard Transplant">Sakal Ekimi</option>
                <option value="PRP Therapy">PRP Tedavisi</option>
                <option value="Dental Implant">Diş İmplant</option>
                <option value="Dental Veneer">Diş Kaplama (Veneer)</option>
                <option value="Hollywood Smile">Hollywood Smile</option>
                <option value="LASIK Eye Surgery">LASIK Lazer Göz</option>
                <option value="Rhinoplasty">Burun Estetiği</option>
                <option value="Gastric Sleeve">Tüp Mide</option>
                <option value="Other">Diğer</option>
              </select>
            </div>
            <div><label class="quote-label">Tercih Edilen Ülke</label>
              <select id="q-dest" class="quote-input">
                <option value="">Farketmez</option>
                <option value="Turkey">Türkiye</option>
                <option value="Hungary">Macaristan</option>
                <option value="Czech Republic">Çek Cumhuriyeti</option>
                <option value="Poland">Polonya</option>
                <option value="Mexico">Meksika</option>
              </select>
            </div>
            <div><label class="quote-label">Notlar (isteğe bağlı)</label>
              <textarea id="q-notes" class="quote-input" rows="2" placeholder="Özel istekleriniz veya sorularınız..."></textarea>
            </div>
            <div class="quote-btn-row">
              <button type="button" onclick="quoteBack1()" class="quote-btn-back"><i class="fa-solid fa-arrow-left"></i> Geri</button>
              <button type="submit" class="quote-btn" style="flex:1;">Teklifimi Gönder <i class="fa-solid fa-paper-plane"></i></button>
            </div>
          </form>
        </div>

        <!-- STEP 3: Success -->
        <div class="quote-panel" id="qstep-3">
          <div class="quote-icon-row"><div class="quote-icon-circle" style="background:linear-gradient(135deg,#059669,#10B981);"><i class="fa-solid fa-circle-check"></i></div></div>
          <h2 class="quote-title">Talebiniz Alındı! 🎉</h2>
          <p class="quote-subtitle">En kısa sürede size en uygun kliniklerden tekliflerle dönüş yapacağız.</p>
          <div class="quote-success-info">
            <div class="quote-info-item"><i class="fa-solid fa-clock"></i><span>Ortalama yanıt süresi: <strong>2-4 saat</strong></span></div>
            <div class="quote-info-item"><i class="fa-solid fa-shield-halved"></i><span>Verileriniz <strong>güvenli</strong> şekilde saklanır</span></div>
            <div class="quote-info-item"><i class="fa-solid fa-phone"></i><span>UK destek hattı: <strong>24/7</strong> aktif</span></div>
          </div>
          <button onclick="closeQuoteModal()" class="quote-btn" style="background:linear-gradient(135deg,#059669,#10B981);">Tamam <i class="fa-solid fa-check"></i></button>
        </div>
      </div>
    `;
    document.body.appendChild(modal);

    // Close on backdrop
    modal.addEventListener('click', function(e) { if (e.target === modal) closeQuoteModal(); });
    document.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeQuoteModal(); });
  }

  // ── Step navigation ──
  function showStep(n) {
    document.querySelectorAll('.quote-panel').forEach(p => p.classList.remove('active'));
    document.getElementById('qstep-' + n).classList.add('active');
    document.querySelectorAll('.quote-step').forEach(s => {
      const sn = parseInt(s.dataset.step);
      s.classList.toggle('active', sn <= n);
      s.classList.toggle('completed', sn < n);
    });
  }

  // ── Inline error helpers for quote modal ──
  function qError(el, msg) {
    el.style.borderColor = '#EF4444';
    el.style.boxShadow = '0 0 0 3px rgba(239,68,68,.12)';
    // Add error message below input
    let errEl = el.parentElement.querySelector('.q-field-error');
    if (!errEl) {
      errEl = document.createElement('div');
      errEl.className = 'q-field-error';
      errEl.style.cssText = 'font-size:11px;color:#EF4444;margin-top:4px;display:flex;align-items:center;gap:4px;font-weight:500;animation:mrFadeIn .25s ease;';
      el.parentElement.appendChild(errEl);
    }
    errEl.innerHTML = '<i class="fa-solid fa-circle-exclamation" style="font-size:10px"></i> ' + msg;
    errEl.style.display = 'flex';
    // Shake
    el.classList.remove('mr-shake');
    void el.offsetWidth;
    el.classList.add('mr-shake');
  }

  function qClear(el) {
    el.style.borderColor = '#22C55E';
    el.style.boxShadow = '0 0 0 3px rgba(34,197,94,.1)';
    const errEl = el.parentElement.querySelector('.q-field-error');
    if (errEl) errEl.style.display = 'none';
  }

  function qReset(el) {
    el.style.borderColor = '';
    el.style.boxShadow = '';
    const errEl = el.parentElement.querySelector('.q-field-error');
    if (errEl) errEl.style.display = 'none';
  }

  // ── Localized error messages ──
  function qMsg(key) {
    const lang = (localStorage.getItem('mr_lang') || 'en');
    const msgs = {
      required:  { en:'This field is required', tr:'Bu alan zorunludur', ar:'هذا الحقل مطلوب', de:'Pflichtfeld', fr:'Champ requis' },
      name:      { en:'Name must be at least 2 characters', tr:'İsim en az 2 karakter olmalı', ar:'الاسم قصير جداً', de:'Mind. 2 Zeichen', fr:'Min 2 caractères' },
      email:     { en:'Please enter a valid email', tr:'Geçerli bir e-posta girin', ar:'بريد إلكتروني غير صالح', de:'Ungültige E-Mail', fr:'E-mail invalide' },
      phone:     { en:'Invalid phone number', tr:'Geçersiz telefon numarası', ar:'رقم هاتف غير صالح', de:'Ungültige Nummer', fr:'Numéro invalide' },
    };
    return (msgs[key] && msgs[key][lang]) || msgs[key].en;
  }

  window.quoteStep2 = function(e) {
    e.preventDefault();
    const name = document.getElementById('q-name');
    const email = document.getElementById('q-email');
    const phone = document.getElementById('q-phone');
    const city = document.getElementById('q-city');
    let valid = true;

    // Name
    if (!name.value.trim()) { qError(name, qMsg('required')); valid = false; }
    else if (name.value.trim().length < 2) { qError(name, qMsg('name')); valid = false; }
    else { qClear(name); }

    // Email
    if (!email.value.trim()) { qError(email, qMsg('required')); valid = false; }
    else if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email.value.trim())) { qError(email, qMsg('email')); valid = false; }
    else { qClear(email); }

    // Phone (optional)
    if (phone.value && !/^[+]?[\d\s\-().]{7,20}$/.test(phone.value.trim())) { qError(phone, qMsg('phone')); valid = false; }
    else { phone.value ? qClear(phone) : qReset(phone); }

    // City
    if (!city.value.trim()) { qError(city, qMsg('required')); valid = false; }
    else { qClear(city); }

    // Live validation listeners (attach once)
    [name, email, phone, city].forEach(el => {
      if (!el.dataset.qLive) {
        el.dataset.qLive = '1';
        el.addEventListener('input', () => qReset(el));
      }
    });

    if (valid) showStep(2);
  };

  window.quoteBack1 = function() { showStep(1); };

  window.submitQuote = async function(e) {
    e.preventDefault();
    const name = document.getElementById('q-name').value;
    const email = document.getElementById('q-email').value;
    const phone = document.getElementById('q-phone').value;
    const city = document.getElementById('q-city').value;
    const treatment = document.getElementById('q-treatment').value;
    const dest = document.getElementById('q-dest').value;
    const notes = document.getElementById('q-notes').value;

    // Determine best clinic match based on treatment
    let clinic = 'Estepera Medical';
    const lower = treatment.toLowerCase();
    if (lower.includes('dental') || lower.includes('veneer') || lower.includes('smile') || lower.includes('implant')) {
      clinic = dest === 'Hungary' ? 'Dent Élite Budapest' : 'SmileLine Antalya';
    } else if (lower.includes('lasik') || lower.includes('eye')) {
      clinic = 'VisionCare Praha';
    } else if (lower.includes('gastric') || lower.includes('sleeve')) {
      clinic = 'Slim & Health Antalya';
    }

    const newLead = {
      name: name,
      email: email,
      phone: phone,
      city: city.split(',')[0].trim(),
      treatment: treatment,
      clinic: clinic,
      source: 'direct',
      status: 'new',
      notes: notes
    };

    const btn = e.target.querySelector('button[type="submit"]') || e.target;
    const ogText = btn.innerHTML;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Gönderiliyor...';
    btn.disabled = true;

    try {
      if (window.MR && MR.supabase) {
        await MR.supabase.createLead(newLead);
      } else {
        const months = ['Oca','Şub','Mar','Nis','May','Haz','Tem','Ağu','Eyl','Eki','Kas','Ara'];
        const now = new Date();
        const dateStr = now.getDate() + ' ' + months[now.getMonth()] + ' ' + now.getFullYear();
        newLead.id = Date.now();
        newLead.date = dateStr;
        newLead.name = name.split(' ').map((w,i) => i === 0 ? w : w[0] + '.').join(' ');
        const leads = getLeads();
        leads.unshift(newLead);
        saveLeads(leads);
      }
      showStep(3);
    } catch(err) {
      alert('Gönderim hatası: ' + err.message);
    }

    btn.innerHTML = ogText;
    btn.disabled = false;
  };

  // ── Open / Close ──
  window.openQuoteModal = function(preselectedTreatment) {
    // Reset form
    showStep(1);
    ['q-name','q-email','q-phone','q-city','q-treatment','q-dest','q-notes'].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.value = '';
    });
    if (preselectedTreatment) {
      document.getElementById('q-treatment').value = preselectedTreatment;
    }
    document.getElementById('quote-modal').classList.add('show');
    document.body.style.overflow = 'hidden';
  };

  window.closeQuoteModal = function() {
    document.getElementById('quote-modal').classList.remove('show');
    document.body.style.overflow = '';
  };

  // ── Auto-bind quote buttons ──
  function bindQuoteButtons() {
    // All "Get Free Quote" links/buttons
    document.querySelectorAll('a[href=\"/auth\"][data-i18n="cta_free_quote"], a[data-quote-trigger]').forEach(el => {
      el.addEventListener('click', function(e) {
        e.preventDefault();
        openQuoteModal();
      });
      el.href = 'javascript:void(0)';
    });
  }

  // ── Init ──
  function initQuoteModal() {
    injectQuoteModal();
    bindQuoteButtons();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initQuoteModal);
  } else {
    initQuoteModal();
  }

})();
