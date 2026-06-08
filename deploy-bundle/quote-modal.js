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

  // ── Built-in quote modal translations ──
  function qT(key) {
    const lang = localStorage.getItem('mediroute-lang') || 'en';
    const t = {
      step1_label:    { en:'Your Info',            tr:'Bilgileriniz',        ar:'معلوماتك',           de:'Ihre Daten',          fr:'Vos Infos' },
      step2_label:    { en:'Treatment',            tr:'Tedavi Detayı',       ar:'تفاصيل العلاج',      de:'Behandlung',          fr:'Traitement' },
      step3_label:    { en:'Complete',              tr:'Tamamlandı',          ar:'مكتمل',              de:'Fertig',              fr:'Terminé' },
      title:          { en:'Get a Free Quote',      tr:'Ücretsiz Teklif Al',  ar:'احصل على عرض مجاني',  de:'Kostenloses Angebot', fr:'Devis Gratuit' },
      subtitle:       { en:'Enter your details, we\'ll find the best clinics for you', tr:'Bilgilerinizi girin, en uygun klinikleri bulalım', ar:'أدخل بياناتك وسنجد لك أفضل العيادات', de:'Geben Sie Ihre Daten ein, wir finden die besten Kliniken', fr:'Entrez vos coordonnées, nous trouverons les meilleures cliniques' },
      fullname:       { en:'Full Name',             tr:'Ad Soyad',            ar:'الاسم الكامل',        de:'Vollständiger Name',  fr:'Nom Complet' },
      email:          { en:'Email',                 tr:'E-posta',             ar:'البريد الإلكتروني',   de:'E-Mail',              fr:'E-mail' },
      phone:          { en:'Phone',                 tr:'Telefon',             ar:'الهاتف',             de:'Telefon',             fr:'Téléphone' },
      city:           { en:'City / Country',        tr:'Şehir / Ülke',        ar:'المدينة / البلد',     de:'Stadt / Land',        fr:'Ville / Pays' },
      continue:       { en:'Continue',              tr:'Devam Et',            ar:'متابعة',             de:'Weiter',              fr:'Continuer' },
      treat_title:    { en:'Treatment Details',     tr:'Tedavi Detayları',    ar:'تفاصيل العلاج',      de:'Behandlungsdetails',  fr:'Détails du Traitement' },
      treat_sub:      { en:'Select the treatment you\'re interested in', tr:'İlgilendiğiniz tedavi türünü seçin', ar:'اختر نوع العلاج الذي يهمك', de:'Wählen Sie die gewünschte Behandlung', fr:'Sélectionnez le traitement souhaité' },
      treat_type:     { en:'Treatment Type',        tr:'Tedavi Türü',         ar:'نوع العلاج',          de:'Behandlungsart',      fr:'Type de Traitement' },
      select:         { en:'Select...',             tr:'Seçiniz...',          ar:'اختر...',            de:'Auswählen...',        fr:'Sélectionner...' },
      fue:            { en:'FUE Hair Transplant',   tr:'FUE Saç Ekimi',       ar:'زراعة شعر FUE',      de:'FUE Haartransplantation', fr:'Greffe de Cheveux FUE' },
      dhi:            { en:'DHI Hair Transplant',   tr:'DHI Saç Ekimi',       ar:'زراعة شعر DHI',      de:'DHI Haartransplantation', fr:'Greffe de Cheveux DHI' },
      beard:          { en:'Beard Transplant',      tr:'Sakal Ekimi',         ar:'زراعة اللحية',       de:'Barttransplantation', fr:'Greffe de Barbe' },
      prp:            { en:'PRP Therapy',           tr:'PRP Tedavisi',        ar:'علاج PRP',           de:'PRP-Therapie',        fr:'Thérapie PRP' },
      implant:        { en:'Dental Implant',        tr:'Diş İmplant',         ar:'زراعة الأسنان',      de:'Zahnimplantat',       fr:'Implant Dentaire' },
      veneer:         { en:'Dental Veneer',         tr:'Diş Kaplama (Veneer)',ar:'قشور الأسنان',       de:'Zahnveneer',          fr:'Facette Dentaire' },
      hollywood:      { en:'Hollywood Smile',       tr:'Hollywood Smile',     ar:'ابتسامة هوليوود',    de:'Hollywood Smile',     fr:'Hollywood Smile' },
      lasik:          { en:'LASIK Eye Surgery',     tr:'LASIK Lazer Göz',     ar:'جراحة العيون بالليزك', de:'LASIK Augenoperation', fr:'Chirurgie LASIK' },
      rhino:          { en:'Rhinoplasty',           tr:'Burun Estetiği',      ar:'تجميل الأنف',        de:'Nasenkorrektur',      fr:'Rhinoplastie' },
      gastric:        { en:'Gastric Sleeve',        tr:'Tüp Mide',            ar:'تكميم المعدة',       de:'Schlauchmagen',       fr:'Sleeve Gastrique' },
      other:          { en:'Other',                 tr:'Diğer',               ar:'أخرى',               de:'Andere',              fr:'Autre' },
      pref_country:   { en:'Preferred Country',     tr:'Tercih Edilen Ülke',  ar:'الدولة المفضلة',     de:'Bevorzugtes Land',    fr:'Pays Préféré' },
      any:            { en:'No preference',         tr:'Farketmez',           ar:'لا تفضيل',           de:'Egal',                fr:'Peu importe' },
      turkey:         { en:'Turkey',                tr:'Türkiye',             ar:'تركيا',              de:'Türkei',              fr:'Turquie' },
      hungary:        { en:'Hungary',               tr:'Macaristan',          ar:'المجر',              de:'Ungarn',              fr:'Hongrie' },
      czech:          { en:'Czech Republic',        tr:'Çek Cumhuriyeti',     ar:'التشيك',             de:'Tschechien',          fr:'Rép. Tchèque' },
      poland:         { en:'Poland',                tr:'Polonya',             ar:'بولندا',             de:'Polen',               fr:'Pologne' },
      mexico:         { en:'Mexico',                tr:'Meksika',             ar:'المكسيك',            de:'Mexiko',              fr:'Mexique' },
      notes:          { en:'Notes (optional)',       tr:'Notlar (isteğe bağlı)', ar:'ملاحظات (اختياري)',  de:'Notizen (optional)',  fr:'Notes (facultatif)' },
      notes_ph:       { en:'Any special requests or questions...', tr:'Özel istekleriniz veya sorularınız...', ar:'أي طلبات أو أسئلة خاصة...', de:'Besondere Wünsche oder Fragen...', fr:'Demandes spéciales ou questions...' },
      back:           { en:'Back',                  tr:'Geri',                ar:'رجوع',               de:'Zurück',              fr:'Retour' },
      submit:         { en:'Send My Quote',         tr:'Teklifimi Gönder',    ar:'إرسال طلبي',         de:'Angebot senden',      fr:'Envoyer mon Devis' },
      success_title:  { en:'Request Received! 🎉',  tr:'Talebiniz Alındı! 🎉', ar:'تم استلام طلبك! 🎉', de:'Anfrage erhalten! 🎉', fr:'Demande Reçue ! 🎉' },
      success_sub:    { en:'We\'ll get back to you shortly with quotes from the best clinics.', tr:'En kısa sürede size en uygun kliniklerden tekliflerle dönüş yapacağız.', ar:'سنعود إليك قريباً بعروض من أفضل العيادات.', de:'Wir melden uns in Kürze mit Angeboten der besten Kliniken.', fr:'Nous vous recontacterons rapidement avec des devis des meilleures cliniques.' },
      resp_time:      { en:'Average response time: <strong>2-4 hours</strong>', tr:'Ortalama yanıt süresi: <strong>2-4 saat</strong>', ar:'متوسط وقت الرد: <strong>2-4 ساعات</strong>', de:'Durchschnittliche Antwortzeit: <strong>2-4 Stunden</strong>', fr:'Temps de réponse moyen : <strong>2-4 heures</strong>' },
      data_safe:      { en:'Your data is stored <strong>securely</strong>', tr:'Verileriniz <strong>güvenli</strong> şekilde saklanır', ar:'بياناتك مخزنة <strong>بأمان</strong>', de:'Ihre Daten werden <strong>sicher</strong> gespeichert', fr:'Vos données sont stockées <strong>en sécurité</strong>' },
      uk_support:     { en:'UK support line: <strong>24/7</strong> active', tr:'UK destek hattı: <strong>24/7</strong> aktif', ar:'خط الدعم البريطاني: نشط <strong>24/7</strong>', de:'UK-Hotline: <strong>24/7</strong> aktiv', fr:'Ligne UK : <strong>24/7</strong> active' },
      ok:             { en:'OK',                    tr:'Tamam',               ar:'حسناً',              de:'OK',                  fr:'OK' },
      sending:        { en:'Sending...',             tr:'Gönderiliyor...',     ar:'جارٍ الإرسال...',     de:'Wird gesendet...',    fr:'Envoi en cours...' },
      send_error:     { en:'Submission error: ',     tr:'Gönderim hatası: ',   ar:'خطأ في الإرسال: ',    de:'Fehler beim Senden: ', fr:'Erreur d\'envoi : ' },
    };
    return (t[key] && t[key][lang]) || (t[key] && t[key].en) || key;
  }

  // ── Inject modal HTML ──
  function injectQuoteModal() {
    const modal = document.createElement('div');
    modal.id = 'quote-modal';
    modal.className = 'quote-modal-overlay';
    modal.innerHTML = `
      <div class="quote-modal-box">
        <!-- Step indicator -->
        <div class="quote-steps" id="quote-steps">
          <div class="quote-step active" data-step="1"><span>1</span> ${qT('step1_label')}</div>
          <div class="quote-step" data-step="2"><span>2</span> ${qT('step2_label')}</div>
          <div class="quote-step" data-step="3"><span>3</span> ${qT('step3_label')}</div>
        </div>

        <button onclick="closeQuoteModal()" class="quote-close"><i class="fa-solid fa-xmark"></i></button>
        
        <!-- STEP 1: Personal Info -->
        <div class="quote-panel active" id="qstep-1">
          <div class="quote-icon-row"><div class="quote-icon-circle"><i class="fa-solid fa-user"></i></div></div>
          <h2 class="quote-title">${qT('title')}</h2>
          <p class="quote-subtitle">${qT('subtitle')}</p>
          <form onsubmit="quoteStep2(event)" novalidate>
            <div class="quote-grid">
              <div><label class="quote-label">${qT('fullname')}</label><input id="q-name" class="quote-input" placeholder="John Smith" required/></div>
              <div><label class="quote-label">${qT('email')}</label><input id="q-email" type="email" class="quote-input" placeholder="john@email.com" required/></div>
            </div>
            <div class="quote-grid">
              <div><label class="quote-label">${qT('phone')}</label><input id="q-phone" class="quote-input" placeholder="+44 7700 900000"/></div>
              <div><label class="quote-label">${qT('city')}</label><input id="q-city" class="quote-input" placeholder="London, UK" required/></div>
            </div>
            <button type="submit" class="quote-btn">${qT('continue')} <i class="fa-solid fa-arrow-right"></i></button>
          </form>
        </div>

        <!-- STEP 2: Treatment Details -->
        <div class="quote-panel" id="qstep-2">
          <div class="quote-icon-row"><div class="quote-icon-circle" style="background:linear-gradient(135deg,#059669,#10B981);"><i class="fa-solid fa-stethoscope"></i></div></div>
          <h2 class="quote-title">${qT('treat_title')}</h2>
          <p class="quote-subtitle">${qT('treat_sub')}</p>
          <form onsubmit="submitQuote(event)" novalidate>
            <div><label class="quote-label">${qT('treat_type')}</label>
              <select id="q-treatment" class="quote-input" required>
                <option value="">${qT('select')}</option>
                <option value="FUE Hair Transplant">${qT('fue')}</option>
                <option value="DHI Hair Transplant">${qT('dhi')}</option>
                <option value="Beard Transplant">${qT('beard')}</option>
                <option value="PRP Therapy">${qT('prp')}</option>
                <option value="Dental Implant">${qT('implant')}</option>
                <option value="Dental Veneer">${qT('veneer')}</option>
                <option value="Hollywood Smile">${qT('hollywood')}</option>
                <option value="LASIK Eye Surgery">${qT('lasik')}</option>
                <option value="Rhinoplasty">${qT('rhino')}</option>
                <option value="Gastric Sleeve">${qT('gastric')}</option>
                <option value="Other">${qT('other')}</option>
              </select>
            </div>
            <div><label class="quote-label">${qT('pref_country')}</label>
              <select id="q-dest" class="quote-input">
                <option value="">${qT('any')}</option>
                <option value="Turkey">${qT('turkey')}</option>
                <option value="Hungary">${qT('hungary')}</option>
                <option value="Czech Republic">${qT('czech')}</option>
                <option value="Poland">${qT('poland')}</option>
                <option value="Mexico">${qT('mexico')}</option>
              </select>
            </div>
            <div><label class="quote-label">${qT('notes')}</label>
              <textarea id="q-notes" class="quote-input" rows="2" placeholder="${qT('notes_ph')}"></textarea>
            </div>
            <div class="quote-btn-row">
              <button type="button" onclick="quoteBack1()" class="quote-btn-back"><i class="fa-solid fa-arrow-left"></i> ${qT('back')}</button>
              <button type="submit" class="quote-btn" style="flex:1;">${qT('submit')} <i class="fa-solid fa-paper-plane"></i></button>
            </div>
          </form>
        </div>

        <!-- STEP 3: Success -->
        <div class="quote-panel" id="qstep-3">
          <div class="quote-icon-row"><div class="quote-icon-circle" style="background:linear-gradient(135deg,#059669,#10B981);"><i class="fa-solid fa-circle-check"></i></div></div>
          <h2 class="quote-title">${qT('success_title')}</h2>
          <p class="quote-subtitle">${qT('success_sub')}</p>
          <div class="quote-success-info">
            <div class="quote-info-item"><i class="fa-solid fa-clock"></i><span>${qT('resp_time')}</span></div>
            <div class="quote-info-item"><i class="fa-solid fa-shield-halved"></i><span>${qT('data_safe')}</span></div>
            <div class="quote-info-item"><i class="fa-solid fa-phone"></i><span>${qT('uk_support')}</span></div>
          </div>
          <button onclick="closeQuoteModal()" class="quote-btn" style="background:linear-gradient(135deg,#059669,#10B981);">${qT('ok')} <i class="fa-solid fa-check"></i></button>
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
    const lang = (localStorage.getItem('mediroute-lang') || 'en');
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

  function loadScript(src) {
    return new Promise((resolve, reject) => {
      const s = document.createElement('script');
      s.src = src;
      s.onload = resolve;
      s.onerror = reject;
      document.body.appendChild(s);
    });
  }

  async function ensureSupabaseLoaded() {
    if (window.MR && window.MR.supabase) return;
    
    try {
      if (typeof window.supabase === 'undefined') {
        await loadScript('https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2');
      }
      if (typeof window.MR === 'undefined' || !window.MR.supabase) {
        await loadScript('/supabase-client.js');
      }
    } catch(e) {
      console.warn('[MR] Failed to load Supabase dynamically:', e);
    }
  }

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
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> ' + qT('sending');
    btn.disabled = true;

    // Dynamic self-healing: Load Supabase SDK if page doesn't have it
    await ensureSupabaseLoaded();

    try {
      if (window.MR && MR.supabase) {
        await MR.supabase.createLead(newLead);
      } else {
        const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
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
      alert(qT('send_error') + err.message);
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
