/* ═══════════════════════════════════════════════════
   form-validation.js  — MediRoute Shared Form Validation
   Premium inline validation with animated feedback.
   ═══════════════════════════════════════════════════ */

(function() {
  'use strict';

  // ── Validation rules ──
  const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  const PHONE_RE = /^[+]?[\d\s\-().]{7,20}$/;

  const RULES = {
    email:   { test: v => EMAIL_RE.test(v.trim()),       msg: { en:'Please enter a valid email address', tr:'Geçerli bir e-posta adresi girin', ar:'أدخل بريدًا إلكترونيًا صالحًا', de:'Bitte geben Sie eine gültige E-Mail ein', fr:'Veuillez entrer un e-mail valide' }},
    password:{ test: v => v.length >= 8,                  msg: { en:'Password must be at least 8 characters', tr:'Şifre en az 8 karakter olmalı', ar:'يجب أن تكون كلمة المرور 8 أحرف على الأقل', de:'Passwort muss mindestens 8 Zeichen haben', fr:'Le mot de passe doit contenir au moins 8 caractères' }},
    name:    { test: v => v.trim().length >= 2,           msg: { en:'Name must be at least 2 characters', tr:'İsim en az 2 karakter olmalı', ar:'يجب أن يكون الاسم حرفين على الأقل', de:'Name muss mindestens 2 Zeichen haben', fr:'Le nom doit contenir au moins 2 caractères' }},
    phone:   { test: v => !v || PHONE_RE.test(v.trim()),  msg: { en:'Please enter a valid phone number', tr:'Geçerli bir telefon numarası girin', ar:'أدخل رقم هاتف صالحًا', de:'Bitte geben Sie eine gültige Telefonnummer ein', fr:'Veuillez entrer un numéro valide' }},
    required:{ test: v => v.trim().length > 0,            msg: { en:'This field is required', tr:'Bu alan zorunludur', ar:'هذا الحقل مطلوب', de:'Dieses Feld ist erforderlich', fr:'Ce champ est requis' }},
    message: { test: v => v.trim().length >= 10,          msg: { en:'Message must be at least 10 characters', tr:'Mesaj en az 10 karakter olmalı', ar:'يجب أن تكون الرسالة 10 أحرف على الأقل', de:'Nachricht muss mindestens 10 Zeichen haben', fr:'Le message doit contenir au moins 10 caractères' }},
    terms:   { test: v => v === true,                     msg: { en:'You must agree to the terms', tr:'Kullanım şartlarını kabul etmelisiniz', ar:'يجب الموافقة على الشروط', de:'Sie müssen den Bedingungen zustimmen', fr:'Vous devez accepter les conditions' }},
  };

  // ── CSS injection ──
  const style = document.createElement('style');
  style.textContent = `
    .mr-field-error{
      display:none;font-size:11px;color:#EF4444;margin-top:4px;
      align-items:center;gap:4px;font-weight:500;
      animation: mrFadeIn .25s ease;
    }
    .mr-field-error.show{display:flex;}
    .mr-field-error i{font-size:10px;}
    .mr-input-error{border-color:#EF4444 !important;box-shadow:0 0 0 3px rgba(239,68,68,.12) !important;}
    .mr-shake{animation:mrShake .4s ease;}
    @keyframes mrShake{
      0%,100%{transform:translateX(0);}
      20%,60%{transform:translateX(-6px);}
      40%,80%{transform:translateX(6px);}
    }
    @keyframes mrFadeIn{from{opacity:0;transform:translateY(-4px);}to{opacity:1;transform:translateY(0);}}
    .mr-input-success{border-color:#22C55E !important;box-shadow:0 0 0 3px rgba(34,197,94,.1) !important;}
    .mr-check-icon{position:absolute;right:12px;top:50%;transform:translateY(-50%);color:#22C55E;font-size:12px;pointer-events:none;animation:mrFadeIn .25s ease;}
  `;
  document.head.appendChild(style);

  // ── Helpers ──
  function getLang() {
    try { return localStorage.getItem('mr_lang') || 'en'; } catch { return 'en'; }
  }

  function getMsg(rule) {
    const lang = getLang();
    return rule.msg[lang] || rule.msg.en;
  }

  function addError(input, errorEl) {
    input.classList.add('mr-input-error');
    input.classList.remove('mr-input-success');
    removeCheck(input);
    errorEl.classList.add('show');
    // Shake
    input.classList.remove('mr-shake');
    void input.offsetWidth; // force reflow
    input.classList.add('mr-shake');
    setTimeout(() => input.classList.remove('mr-shake'), 400);
  }

  function clearError(input, errorEl) {
    input.classList.remove('mr-input-error', 'mr-shake');
    errorEl.classList.remove('show');
  }

  function showSuccess(input) {
    input.classList.add('mr-input-success');
    input.classList.remove('mr-input-error');
    // Add check icon if relative parent
    removeCheck(input);
    const parent = input.parentElement;
    if (parent && getComputedStyle(parent).position !== 'static') {
      const check = document.createElement('i');
      check.className = 'fa-solid fa-circle-check mr-check-icon';
      check.setAttribute('data-mr-check', '1');
      parent.appendChild(check);
    }
  }

  function removeCheck(input) {
    const parent = input.parentElement;
    if (parent) {
      parent.querySelectorAll('[data-mr-check]').forEach(c => c.remove());
    }
  }

  function createErrorEl(input, ruleKey) {
    // Check if error el already exists
    let errorEl = input.parentElement.querySelector('.mr-field-error[data-rule="' + ruleKey + '"]');
    if (errorEl) return errorEl;
    errorEl = document.createElement('div');
    errorEl.className = 'mr-field-error';
    errorEl.setAttribute('data-rule', ruleKey);
    errorEl.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i><span></span>';
    // Insert after input (or after parent if it's a relative wrapper)
    const container = input.closest('.relative') || input.parentElement;
    container.appendChild(errorEl);
    return errorEl;
  }

  // ── Field validator ──
  function validateField(input, ruleKey) {
    const rule = RULES[ruleKey];
    if (!rule) return true;

    const errorEl = createErrorEl(input, ruleKey);
    const msgSpan = errorEl.querySelector('span');
    msgSpan.textContent = getMsg(rule);

    let value;
    if (input.type === 'checkbox') {
      value = input.checked;
    } else {
      value = input.value || '';
    }

    if (!rule.test(value)) {
      addError(input, errorEl);
      return false;
    } else {
      clearError(input, errorEl);
      if (input.type !== 'checkbox' && value.trim()) {
        showSuccess(input);
      }
      return true;
    }
  }

  // ── Attach live validation ──
  function attachLiveValidation(input, ruleKey) {
    const events = input.type === 'checkbox' ? ['change'] : ['blur', 'input'];
    let touched = false;

    events.forEach(evt => {
      input.addEventListener(evt, () => {
        if (evt === 'blur') touched = true;
        if (touched || evt === 'change') {
          validateField(input, ruleKey);
        }
      });
    });
  }

  // ── Form validation API ──
  /**
   * Register validation on a form.
   * @param {HTMLFormElement|string} form
   * @param {Array} fields - [{id: 'el-id', rules: ['email','required']}, ...]
   * @param {Function} onSuccess - called if all fields valid
   */
  window.MRValidation = {
    register: function(form, fields, onSuccess) {
      if (typeof form === 'string') form = document.getElementById(form);
      if (!form) return;

      // Disable native browser validation
      form.setAttribute('novalidate', '');

      // Attach live validators
      fields.forEach(({ id, rules }) => {
        const input = document.getElementById(id) || form.querySelector('[name="' + id + '"]');
        if (!input) return;
        rules.forEach(ruleKey => attachLiveValidation(input, ruleKey));
      });

      // Override submit
      form.addEventListener('submit', function(e) {
        e.preventDefault();
        let allValid = true;
        let firstInvalid = null;

        fields.forEach(({ id, rules }) => {
          const input = document.getElementById(id) || form.querySelector('[name="' + id + '"]');
          if (!input) return;
          rules.forEach(ruleKey => {
            if (!validateField(input, ruleKey)) {
              allValid = false;
              if (!firstInvalid) firstInvalid = input;
            }
          });
        });

        if (!allValid && firstInvalid) {
          firstInvalid.focus();
          firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
          return;
        }

        if (onSuccess) onSuccess(e);
      });
    }
  };

})();
