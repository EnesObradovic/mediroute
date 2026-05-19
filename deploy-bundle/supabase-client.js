/* ═══════════════════════════════════════════════════════════════
   MediRoute — Supabase Client Module
   Merkezi Supabase bağlantı ve veri katmanı.
   Tüm auth, clinic, lead işlemleri buradan yönetilir.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  const SUPABASE_URL = 'https://phdmnzsdyjhqoqiqwmho.supabase.co';
  const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBoZG1uenNkeWpocW9xaXF3bWhvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc1NzAzMzksImV4cCI6MjA5MzE0NjMzOX0.zUoYTYjp8Shva1iSVE0oW1ukGpiEOCghPiqc__WisPg';

  // Wait for Supabase SDK to load
  let _supabase = null;

  function getClient() {
    if (_supabase) return _supabase;
    if (typeof window.supabase !== 'undefined' && window.supabase.createClient) {
      _supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
      return _supabase;
    }
    console.warn('[MR] Supabase SDK not loaded yet');
    return null;
  }

  /* ═══════════════════════════════════
     AUTH — Kimlik Doğrulama
     ═══════════════════════════════════ */

  /** E-posta + şifre ile kayıt */
  async function signUp(email, password, firstName, lastName) {
    const sb = getClient();
    if (!sb) throw new Error('Supabase not available');

    const { data, error } = await sb.auth.signUp({
      email: email,
      password: password,
      options: {
        data: { first_name: firstName, last_name: lastName }
      }
    });

    if (error) throw error;

    // Profil bilgilerini güncelle
    if (data.user) {
      await sb.from('profiles').upsert({
        id: data.user.id,
        first_name: firstName,
        last_name: lastName
      });
    }

    return data;
  }

  /** E-posta + şifre ile giriş */
  async function signIn(email, password) {
    const sb = getClient();
    if (!sb) throw new Error('Supabase not available');

    const { data, error } = await sb.auth.signInWithPassword({
      email: email,
      password: password
    });

    if (error) throw error;
    return data;
  }

  /** Google OAuth ile giriş */
  async function signInWithGoogle() {
    const sb = getClient();
    if (!sb) throw new Error('Supabase not available');

    const { data, error } = await sb.auth.signInWithOAuth({
      provider: 'google',
      options: {
        redirectTo: window.location.origin + '/patient-dashboard.html'
      }
    });

    if (error) throw error;
    return data;
  }

  /** Çıkış */
  async function signOut() {
    const sb = getClient();
    if (!sb) return;

    // Eski localStorage session'ı da temizle (geçiş dönemi)
    localStorage.removeItem('mr_session');

    const { error } = await sb.auth.signOut();
    if (error) console.error('[MR] Sign out error:', error);
  }

  /** Mevcut oturum bilgisi */
  async function getSession() {
    const sb = getClient();
    if (!sb) return null;

    const { data: { session } } = await sb.auth.getSession();
    return session;
  }

  /** Mevcut kullanıcı */
  async function getUser() {
    const session = await getSession();
    if (!session) return null;
    return session.user;
  }

  /** Kullanıcı profil bilgileri (profiles tablosundan) */
  async function getProfile() {
    const sb = getClient();
    const user = await getUser();
    if (!sb || !user) return null;

    const { data, error } = await sb
      .from('profiles')
      .select('*')
      .eq('id', user.id)
      .single();

    if (error) { console.error('[MR] Profile fetch error:', error); return null; }
    return data;
  }

  /** Auth state değişikliklerini dinle */
  function onAuthStateChange(callback) {
    const sb = getClient();
    if (!sb) return null;
    return sb.auth.onAuthStateChange(callback);
  }

  /* ═══════════════════════════════════
     CLINICS — Klinik Verileri
     ═══════════════════════════════════ */

  /** Tüm klinikleri getir */
  async function getClinics(filters) {
    const sb = getClient();
    if (!sb) return _fallbackClinics();

    let query = sb.from('clinics').select('*');

    if (filters) {
      if (filters.status) query = query.eq('status', filters.status);
      if (filters.city) query = query.eq('city', filters.city);
      if (filters.jci === 'yes') query = query.eq('jci', 'yes');
    }

    query = query.order('rating', { ascending: false });

    const { data, error } = await query;

    if (error) {
      console.error('[MR] Clinics fetch error:', error);
      return _fallbackClinics();
    }

    // localStorage cache'i güncelle
    localStorage.setItem('mr_clinics_cache', JSON.stringify(data));
    return data;
  }

  /** Tek klinik getir */
  async function getClinic(id) {
    const sb = getClient();
    if (!sb) return null;

    const { data, error } = await sb
      .from('clinics')
      .select('*')
      .eq('id', id)
      .single();

    if (error) { console.error('[MR] Clinic fetch error:', error); return null; }
    return data;
  }

  /** Klinik ekle */
  async function createClinic(clinic) {
    const sb = getClient();
    if (!sb) throw new Error('Supabase not available');

    const { data, error } = await sb
      .from('clinics')
      .insert(clinic)
      .select()
      .single();

    if (error) throw error;
    return data;
  }

  /** Klinik güncelle */
  async function updateClinic(id, updates) {
    const sb = getClient();
    if (!sb) throw new Error('Supabase not available');

    const { data, error } = await sb
      .from('clinics')
      .update(updates)
      .eq('id', id)
      .select()
      .single();

    if (error) throw error;
    return data;
  }

  /** Klinik sil */
  async function deleteClinic(id) {
    const sb = getClient();
    if (!sb) throw new Error('Supabase not available');

    const { error } = await sb
      .from('clinics')
      .delete()
      .eq('id', id);

    if (error) throw error;
  }

  /** Offline fallback — cache'den oku */
  function _fallbackClinics() {
    try {
      const cached = localStorage.getItem('mr_clinics_cache');
      if (cached) return JSON.parse(cached);
    } catch (e) {}
    return [];
  }

  /* ═══════════════════════════════════
     LEADS — Hasta Talepleri
     ═══════════════════════════════════ */

  /** Tüm leads getir (admin için) */
  async function getLeads(filters) {
    const sb = getClient();
    if (!sb) return _fallbackLeads();

    let query = sb.from('leads').select('*');

    if (filters) {
      if (filters.status) query = query.eq('status', filters.status);
      if (filters.source) query = query.eq('source', filters.source);
    }

    query = query.order('created_at', { ascending: false });

    const { data, error } = await query;

    if (error) {
      console.error('[MR] Leads fetch error:', error);
      return _fallbackLeads();
    }

    localStorage.setItem('mr_leads_cache', JSON.stringify(data));
    return data;
  }

  /** Yeni lead oluştur (quote modal'dan) */
  async function createLead(lead) {
    const sb = getClient();
    if (!sb) {
      // Fallback: localStorage'a kaydet
      _saveLeadToLocalStorage(lead);
      return lead;
    }

    // Giriş yapmış kullanıcı varsa user_id ekle
    const user = await getUser();
    if (user) lead.user_id = user.id;

    const { data, error } = await sb
      .from('leads')
      .insert(lead)
      .select()
      .single();

    if (error) {
      console.error('[MR] Lead create error:', error);
      _saveLeadToLocalStorage(lead);
      return lead;
    }

    return data;
  }

  /** Lead status güncelle */
  async function updateLeadStatus(id, status) {
    const sb = getClient();
    if (!sb) throw new Error('Supabase not available');

    const { data, error } = await sb
      .from('leads')
      .update({ status: status })
      .eq('id', id)
      .select()
      .single();

    if (error) throw error;
    return data;
  }

  /** Kullanıcının kendi lead'lerini getir */
  async function getMyLeads() {
    const sb = getClient();
    const user = await getUser();
    if (!sb || !user) return [];

    const { data, error } = await sb
      .from('leads')
      .select('*')
      .eq('user_id', user.id)
      .order('created_at', { ascending: false });

    if (error) { console.error('[MR] My leads fetch error:', error); return []; }
    return data;
  }

  /** Offline fallback */
  function _fallbackLeads() {
    try {
      // First try mr_leads where local inserts go
      const local = localStorage.getItem('mr_leads');
      if (local) return JSON.parse(local);
      // Then try cache
      const cached = localStorage.getItem('mr_leads_cache');
      if (cached) return JSON.parse(cached);
    } catch (e) {}
    return [];
  }

  function _saveLeadToLocalStorage(lead) {
    try {
      const leads = JSON.parse(localStorage.getItem('mr_leads') || '[]');
      lead.id = leads.length ? Math.max(...leads.map(l => l.id)) + 1 : 1;
      lead.created_at = new Date().toISOString();
      leads.unshift(lead);
      localStorage.setItem('mr_leads', JSON.stringify(leads));
    } catch (e) { console.error('[MR] localStorage fallback error:', e); }
  }

  /* ═══════════════════════════════════
     HELPER — Oturum bilgisini basit objeye çevir
     (shared.js navbar uyumu için)
     ═══════════════════════════════════ */

  /** Supabase session → basit {name, email, loggedIn} objesi */
  async function getSimpleSession() {
    const session = await getSession();
    if (!session || !session.user) return null;

    const user = session.user;
    const meta = user.user_metadata || {};
    const name = (meta.first_name && meta.last_name)
      ? meta.first_name + ' ' + meta.last_name
      : meta.full_name || meta.name || user.email.split('@')[0];

    return {
      email: user.email,
      name: name,
      loggedIn: true,
      id: user.id,
      avatar: meta.avatar_url || null
    };
  }

  /* ═══════════════════════════════════
     BLOGS — Blog Yazıları
     ═══════════════════════════════════ */

  async function getBlogs() {
    const sb = getClient();
    if (!sb) return [];
    const { data, error } = await sb.from('blogs').select('*').order('created_at', { ascending: false });
    if (error) { console.error('[MR] Blogs fetch error:', error); return []; }
    return data;
  }

  async function getBlogBySlug(slug) {
    const sb = getClient();
    if (!sb) return null;
    const { data, error } = await sb.from('blogs').select('*').eq('slug', slug).single();
    if (error) { console.error('[MR] Blog fetch error:', error); return null; }
    return data;
  }

  async function createBlog(blog) {
    const sb = getClient();
    if (!sb) throw new Error('Supabase not available');
    const { data, error } = await sb.from('blogs').insert(blog).select().single();
    if (error) throw error;
    return data;
  }

  async function updateBlog(id, updates) {
    const sb = getClient();
    if (!sb) throw new Error('Supabase not available');
    const { data, error } = await sb.from('blogs').update(updates).eq('id', id).select().single();
    if (error) throw error;
    return data;
  }

  async function deleteBlog(id) {
    const sb = getClient();
    if (!sb) throw new Error('Supabase not available');
    const { error } = await sb.from('blogs').delete().eq('id', id);
    if (error) throw error;
  }

  /* ═══════════════════════════════════
     PUBLIC API — Global'e aç
     ═══════════════════════════════════ */

  window.MR = window.MR || {};
  window.MR.supabase = {
    // Client
    getClient: getClient,

    // Auth
    signUp: signUp,
    signIn: signIn,
    signInWithGoogle: signInWithGoogle,
    signOut: signOut,
    getSession: getSession,
    getUser: getUser,
    getProfile: getProfile,
    getSimpleSession: getSimpleSession,
    onAuthStateChange: onAuthStateChange,

    // Clinics
    getClinics: getClinics,
    getClinic: getClinic,
    createClinic: createClinic,
    updateClinic: updateClinic,
    deleteClinic: deleteClinic,

    // Leads
    getLeads: getLeads,
    createLead: createLead,
    updateLeadStatus: updateLeadStatus,
    getMyLeads: getMyLeads,

    // Blogs
    getBlogs: getBlogs,
    getBlogBySlug: getBlogBySlug,
    createBlog: createBlog,
    updateBlog: updateBlog,
    deleteBlog: deleteBlog
  };

})();
