/* ── Admin Logic ────────────────────────────────── */

// ── Login Gate ──
function adminLogin(e){
  e.preventDefault();
  const pw=document.getElementById('admin-pw').value;
  if(pw==='admin123'){
    document.getElementById('login-gate').style.display='none';
    localStorage.setItem('mr_admin','1');
  } else {
    document.getElementById('login-error').classList.remove('hidden');
    document.getElementById('admin-pw').value='';
  }
}
function adminLogout(){
  localStorage.removeItem('mr_admin');
  document.getElementById('login-gate').style.display='flex';
}
if(localStorage.getItem('mr_admin')==='1'){
  document.getElementById('login-gate').style.display='none';
}

// ── Tab Switching ──
function switchTab(tab){
  document.querySelectorAll('.tab-content').forEach(t=>t.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  document.getElementById('tab-'+tab).classList.add('active');
  const navEl=document.getElementById('nav-'+tab);
  if(navEl) navEl.classList.add('active');
  const titles={dashboard:'Dashboard',clinics:'Klinik Yönetimi',leads:'Hasta Talepleri',blogs:'Blog Yönetimi'};
  document.getElementById('page-title').textContent=titles[tab]||'Dashboard';
}

// ── Clinic Data (Supabase backed) ──
async function getClinics(){
  if (window.MR && MR.supabase) return await MR.supabase.getClinics();
  return [];
}

function statusBadge(s){
  const map={active:['Aktif','status-active','fa-circle-check'],pending:['Onay Bekliyor','status-pending','fa-clock'],draft:['Taslak','status-draft','fa-file']};
  const m=map[s]||map.draft;
  return `<span class="status-badge ${m[1]}"><i class="fa-solid ${m[2]} text-[10px]"></i> ${m[0]}</span>`;
}

async function renderClinics(){
  const clinics=await getClinics();
  const tbody=document.getElementById('clinics-table');
  tbody.innerHTML=clinics.map(c=>{
    const pMin = c.price_min || c.priceMin || 0;
    const pMax = c.price_max || c.priceMax || 0;
    return `
    <tr class="table-row">
      <td class="px-4 py-3"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-xl bg-gradient-to-br from-navy-900 to-navy-700 flex items-center justify-center text-white text-xs font-bold flex-shrink-0">${c.name[0]}</div><div><p class="font-semibold text-gray-800 text-sm">${c.name}</p><p class="text-xs text-gray-400">${c.jci==='yes'?'<i class="fa-solid fa-shield-halved text-emerald-500 mr-1"></i>JCI Akrediteli':'<span class="text-gray-300">JCI Yok</span>'}</p></div></div></td>
      <td class="px-4 py-3 text-sm text-gray-600"><i class="fa-solid fa-location-dot text-gray-300 mr-1"></i>${c.city}, ${c.country}</td>
      <td class="px-4 py-3"><div class="flex flex-wrap gap-1">${(c.treatments||'').split(',').map(t=>`<span class="text-[11px] font-semibold bg-navy-50 text-navy-700 px-2 py-0.5 rounded-full">${t.trim()}</span>`).join('')}</div></td>
      <td class="px-4 py-3 text-sm font-bold text-navy-900">£${pMin.toLocaleString()} – £${pMax.toLocaleString()}</td>
      <td class="px-4 py-3"><div class="flex items-center gap-1"><span class="text-amber-400">★</span><span class="font-bold text-sm text-gray-700">${c.rating||'—'}</span></div></td>
      <td class="px-4 py-3">${statusBadge(c.status)}</td>
      <td class="px-4 py-3"><div class="flex items-center gap-2"><button onclick="editClinic(${c.id})" class="text-xs font-semibold text-navy-700 hover:underline flex items-center gap-1"><i class="fa-solid fa-pen text-[10px]"></i> Düzenle</button><button onclick="deleteClinic(${c.id})" class="text-xs font-semibold text-red-400 hover:underline flex items-center gap-1"><i class="fa-solid fa-trash text-[10px]"></i> Sil</button></div></td>
    </tr>
  `}).join('');
  document.getElementById('m-clinics').textContent=clinics.length;
}

// ── Clinic CRUD ──
function openClinicModal(){ document.getElementById('clinic-modal').classList.add('show'); document.getElementById('clinic-edit-id').value=''; document.getElementById('modal-title').textContent='Yeni Klinik Ekle'; document.getElementById('modal-btn-text').textContent='Kaydet'; ['c-name','c-city','c-country','c-treatments','c-price-min','c-price-max','c-rating','c-desc'].forEach(id=>document.getElementById(id).value=''); document.getElementById('c-jci').value='yes'; document.getElementById('c-status').value='active'; }
function closeClinicModal(){ document.getElementById('clinic-modal').classList.remove('show'); }

async function editClinic(id){
  const clinics=await getClinics();
  const c=clinics.find(x=>x.id==id); if(!c) return;
  document.getElementById('clinic-edit-id').value=id;
  document.getElementById('modal-title').textContent='Klinik Düzenle';
  document.getElementById('modal-btn-text').textContent='Güncelle';
  document.getElementById('c-name').value=c.name;
  document.getElementById('c-city').value=c.city;
  document.getElementById('c-country').value=c.country;
  document.getElementById('c-treatments').value=c.treatments;
  document.getElementById('c-price-min').value=c.price_min||c.priceMin||'';
  document.getElementById('c-price-max').value=c.price_max||c.priceMax||'';
  document.getElementById('c-rating').value=c.rating||'';
  document.getElementById('c-jci').value=c.jci||'yes';
  document.getElementById('c-status').value=c.status||'draft';
  document.getElementById('c-desc').value=c.description||c.desc||'';
  document.getElementById('clinic-modal').classList.add('show');
}

async function saveClinic(e){
  e.preventDefault();
  const editId=document.getElementById('clinic-edit-id').value;
  const data={
    name:document.getElementById('c-name').value,
    city:document.getElementById('c-city').value,
    country:document.getElementById('c-country').value,
    treatments:document.getElementById('c-treatments').value,
    price_min:parseInt(document.getElementById('c-price-min').value)||0,
    price_max:parseInt(document.getElementById('c-price-max').value)||0,
    rating:parseFloat(document.getElementById('c-rating').value)||0,
    jci:document.getElementById('c-jci').value,
    status:document.getElementById('c-status').value,
    description:document.getElementById('c-desc').value
  };
  
  const btn = document.getElementById('modal-btn-text');
  const ogText = btn.textContent;
  btn.textContent = 'Kaydediliyor...';
  
  try {
    if(editId){
      await MR.supabase.updateClinic(editId, data);
    } else {
      await MR.supabase.createClinic(data);
    }
    await renderClinics();
    closeClinicModal();
    showToast(editId?'Klinik güncellendi ✅':'Yeni klinik eklendi ✅');
  } catch(err) {
    alert('Hata: ' + err.message);
  }
  btn.textContent = ogText;
}

let deleteTargetId=null;
function deleteClinic(id){ deleteTargetId=id; document.getElementById('delete-modal').classList.add('show'); }
function closeDeleteModal(){ document.getElementById('delete-modal').classList.remove('show'); deleteTargetId=null; }
async function confirmDelete(){
  if(!deleteTargetId) return;
  try {
    await MR.supabase.deleteClinic(deleteTargetId);
    await renderClinics();
    closeDeleteModal();
    showToast('Klinik silindi 🗑️');
  } catch(err) {
    alert('Hata: ' + err.message);
  }
}

// ── Lead Status/Source definitions ──
const STATUS_OPTIONS=[
  {value:'new',label:'Yeni Talep',cls:'status-new'},
  {value:'contacted',label:'İletişime Geçildi',cls:'status-contacted'},
  {value:'confirmed',label:'Randevu Onaylandı',cls:'status-confirmed'},
  {value:'completed',label:'Tedavi Tamamlandı',cls:'status-completed'},
  {value:'cancelled',label:'İptal',cls:'status-cancelled'}
];
const SOURCE_META={
  organic:{label:'Organik',cls:'source-organic',icon:'fa-magnifying-glass'},
  paid:{label:'Reklam',cls:'source-paid',icon:'fa-bullhorn'},
  referral:{label:'Referans',cls:'source-referral',icon:'fa-share-nodes'},
  direct:{label:'Doğrudan',cls:'source-direct',icon:'fa-arrow-right'}
};

// ── Lead Data (Supabase backed) ──
async function getLeads(){
  if (window.MR && MR.supabase) return await MR.supabase.getLeads();
  return [];
}

const invoiceState={};

async function renderLeads(){
  const leads=await getLeads();
  leads.forEach(l=>{if(invoiceState[l.id]===undefined) invoiceState[l.id]=l.status==='completed';});
  const tbody=document.getElementById('leads-table');
  document.getElementById('m-leads').textContent=leads.length;
  tbody.innerHTML=leads.map(l=>`
    <tr class="table-row" data-id="${l.id}">
      <td class="px-4 py-3"><div class="flex items-center gap-3"><div class="w-8 h-8 rounded-full bg-gradient-to-br from-navy-800 to-navy-600 flex items-center justify-center text-white text-xs font-bold flex-shrink-0">${l.name[0]}</div><div><p class="font-semibold text-gray-800 text-sm">${l.name}</p><p class="text-xs text-gray-400"><i class="fa-solid fa-location-dot text-[9px]"></i> ${l.city||''}</p></div></div></td>
      <td class="px-4 py-3 text-sm text-gray-600">${l.treatment}</td>
      <td class="px-4 py-3"><span class="text-xs font-semibold text-navy-700 bg-navy-50 px-2 py-1 rounded-lg">${l.clinic||'-'}</span></td>
      <td class="px-4 py-3"><span class="status-badge ${(SOURCE_META[l.source]||SOURCE_META.direct).cls}"><i class="fa-solid ${(SOURCE_META[l.source]||SOURCE_META.direct).icon} text-[9px]"></i> ${(SOURCE_META[l.source]||SOURCE_META.direct).label}</span></td>
      <td class="px-4 py-3 text-xs text-gray-400">${new Date(l.created_at).toLocaleDateString('tr-TR')}</td>
      <td class="px-4 py-3"><select class="status-select" onchange="onStatusChange(this, ${l.id})">${STATUS_OPTIONS.map(o=>`<option value="${o.value}" ${o.value===l.status?'selected':''}>${o.label}</option>`).join('')}</select></td>
      <td class="px-4 py-3">${invoiceState[l.id]?`<span class="invoice-tag" id="inv-${l.id}"><i class="fa-solid fa-circle-check"></i> Fatura Oluşturuldu</span>`:`<span id="inv-${l.id}" class="text-gray-300 text-xs">—</span>`}</td>
    </tr>
  `).join('');
}

async function onStatusChange(sel, id){
  const newStatus = sel.value;
  sel.disabled = true;
  try {
    await MR.supabase.updateLeadStatus(id, newStatus);
    const isCompleted = newStatus==='completed'; 
    invoiceState[id] = isCompleted;
    const invCell = document.getElementById('inv-'+id);
    if(invCell) {
      invCell.outerHTML = isCompleted?`<span class="invoice-tag" id="inv-${id}"><i class="fa-solid fa-circle-check"></i> Fatura Oluşturuldu</span>`:`<span id="inv-${id}" class="text-gray-300 text-xs">—</span>`;
    }
    const leads = await getLeads();
    const completedCount=leads.filter(l=>l.status==='completed').length;
    document.getElementById('m-revenue').textContent=(completedCount*180).toLocaleString();
    showToast('Durum güncellendi ✅');
  } catch (err) {
    alert('Hata: ' + err.message);
    await renderLeads(); // refresh to old state
  }
  sel.disabled = false;
}

// ── Activity Feed ──
function renderActivity(){
  const acts=[
    {icon:'fa-user-check',col:'text-emerald-500',bg:'bg-emerald-50',t:'Yeni başvuru onaylandı: David S.',time:'2 saat önce'},
    {icon:'fa-hospital-user',col:'text-blue-500',bg:'bg-blue-50',t:'Estepera Medical yeni paket ekledi',time:'5 saat önce'},
    {icon:'fa-comment-dots',col:'text-amber-500',bg:'bg-amber-50',t:'Yeni yorum: "Harika deneyim!"',time:'1 gün önce'}
  ];
  document.getElementById('activity-list').innerHTML=acts.map(a=>`<div class="flex items-start gap-3"><div class="w-8 h-8 rounded-xl ${a.bg} flex items-center justify-center flex-shrink-0"><i class="fa-solid ${a.icon} ${a.col} text-sm"></i></div><div><p class="text-sm font-semibold text-gray-800">${a.t}</p><p class="text-[10px] font-bold text-gray-400 mt-0.5">${a.time}</p></div></div>`).join('');
}

// ── BLOG LOGIC (Supabase backed) ──
async function getBlogs(){
  if (window.MR && MR.supabase && MR.supabase.getBlogs) return await MR.supabase.getBlogs();
  return [];
}

async function renderBlogs(){
  const blogs = await getBlogs();
  const tbody = document.getElementById('blogs-table');
  if(!tbody) return;
  tbody.innerHTML = blogs.map(b => `
    <tr class="table-row">
      <td class="px-4 py-3"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-xl bg-gray-100 flex items-center justify-center overflow-hidden flex-shrink-0">${b.image_url ? `<img src="${b.image_url}" class="w-full h-full object-cover">` : '<i class="fa-solid fa-image text-gray-300"></i>'}</div><div><p class="font-semibold text-gray-800 text-sm max-w-[250px] truncate" title="${b.title}">${b.title}</p><p class="text-xs text-gray-400">/${b.slug}</p></div></div></td>
      <td class="px-4 py-3 text-sm text-gray-600"><span class="bg-blue-50 text-blue-600 font-bold px-2 py-1 rounded text-[10px]">${b.category}</span></td>
      <td class="px-4 py-3 text-xs text-gray-500">${new Date(b.created_at).toLocaleDateString('tr-TR')}</td>
      <td class="px-4 py-3">${b.status === 'published' ? '<span class="status-badge status-active"><i class="fa-solid fa-check text-[10px]"></i> Yayınlandı</span>' : '<span class="status-badge status-draft"><i class="fa-solid fa-file text-[10px]"></i> Taslak</span>'}</td>
      <td class="px-4 py-3"><div class="flex items-center gap-2"><button onclick="editBlog(${b.id})" class="text-xs font-semibold text-navy-700 hover:underline flex items-center gap-1"><i class="fa-solid fa-pen text-[10px]"></i> Düzenle</button><button onclick="deleteBlogBtn(${b.id})" class="text-xs font-semibold text-red-400 hover:underline flex items-center gap-1"><i class="fa-solid fa-trash text-[10px]"></i> Sil</button></div></td>
    </tr>
  `).join('');
}

let quillEditor = null;

function initQuill() {
  if (quillEditor) return; // already initialized
  const container = document.getElementById('editor-container');
  if (!container) return;
  quillEditor = new Quill('#editor-container', {
    theme: 'snow',
    placeholder: 'Blog içeriğini yazmaya başla...',
    modules: {
      toolbar: [
        [{ 'header': [2, 3, false] }],
        ['bold', 'italic', 'underline', 'strike'],
        [{ 'list': 'ordered'}, { 'list': 'bullet' }],
        ['link', 'image', 'video'],
        ['clean']
      ]
    }
  });
  quillEditor.on('text-change', function() {
    document.getElementById('b-content').value = quillEditor.root.innerHTML;
  });
}

function openBlogModal(){ 
  document.getElementById('blog-modal').classList.add('show'); 
  document.getElementById('blog-edit-id').value=''; 
  document.getElementById('blog-modal-title').textContent='Yeni Yazı Ekle'; 
  document.getElementById('blog-btn-text').textContent='Yayınla'; 
  ['b-title','b-slug','b-category','b-image','b-content','b-author','b-author-title','b-author-specialty','b-author-image'].forEach(id=>document.getElementById(id).value=''); 
  document.getElementById('b-status').value='published'; 
  initQuill();
  if (quillEditor) quillEditor.root.innerHTML = '';
}
function closeBlogModal(){ document.getElementById('blog-modal').classList.remove('show'); }

async function editBlog(id){
  const blogs = await getBlogs();
  const b = blogs.find(x => x.id == id); if(!b) return;
  document.getElementById('blog-edit-id').value = id;
  document.getElementById('blog-modal-title').textContent = 'Yazıyı Düzenle';
  document.getElementById('blog-btn-text').textContent = 'Güncelle';
  document.getElementById('b-title').value = b.title;
  document.getElementById('b-slug').value = b.slug;
  document.getElementById('b-category').value = b.category;
  document.getElementById('b-image').value = b.image_url || '';
  document.getElementById('b-author').value = b.author || '';
  document.getElementById('b-author-title').value = b.author_title || '';
  document.getElementById('b-author-specialty').value = b.author_specialty || '';
  document.getElementById('b-author-image').value = b.author_image || '';
  document.getElementById('b-status').value = b.status || 'draft';
  document.getElementById('b-content').value = b.content;
  initQuill();
  if (quillEditor) quillEditor.root.innerHTML = b.content || '';
  document.getElementById('blog-modal').classList.add('show');
}

async function saveBlog(e){
  e.preventDefault();
  const editId = document.getElementById('blog-edit-id').value;
  const data = {
    title: document.getElementById('b-title').value,
    slug: document.getElementById('b-slug').value,
    category: document.getElementById('b-category').value,
    image_url: document.getElementById('b-image').value,
    author: document.getElementById('b-author').value,
    author_title: document.getElementById('b-author-title').value,
    author_specialty: document.getElementById('b-author-specialty').value,
    author_image: document.getElementById('b-author-image').value,
    status: document.getElementById('b-status').value,
    content: document.getElementById('b-content').value
  };

  try {
    if(editId){
      await MR.supabase.updateBlog(editId, data);
    } else {
      await MR.supabase.createBlog(data);
    }
    closeBlogModal();
    renderBlogs();
  } catch(err) {
    alert("Kayıt hatası: " + err.message);
  }
}

// ── Toast ──
function showToast(msg){
  const t=document.createElement('div');
  t.className='fixed bottom-6 left-1/2 -translate-x-1/2 bg-navy-900 text-white text-sm font-semibold px-5 py-3 rounded-xl shadow-xl z-[300] flex items-center gap-2';
  t.innerHTML='<i class="fa-solid fa-circle-check text-emerald-400"></i> '+msg;
  document.body.appendChild(t);
  setTimeout(()=>t.remove(),2500);
}

// ── Modal close on backdrop ──
document.getElementById('clinic-modal').addEventListener('click',function(e){if(e.target===this)closeClinicModal();});
document.getElementById('delete-modal').addEventListener('click',function(e){if(e.target===this)closeDeleteModal();});
document.getElementById('blog-modal')?.addEventListener('click',function(e){if(e.target===this)closeBlogModal();});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeClinicModal();closeDeleteModal();closeBlogModal();}});

// ── Init ──
renderClinics();
renderLeads();
renderActivity();
renderBlogs();
