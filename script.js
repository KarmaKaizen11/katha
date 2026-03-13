/* ============================================
   KATHA TRAILS — Interactions v2
   50-site map · Category filter · Sidebar
   Reading progress · Count-up · Active nav
   Vanilla JS · No Dependencies
   ============================================ */

(function () {
  'use strict';

  /* ─── Katha Word Rotator (22 Official Languages) ──────────────── */
  const kathaTranslations = [
    "Katha",    // English/Phonetic
    "कथा",      // Hindi, Marathi, Nepali, Konkani, Sanskrit, Bodo, Dogri, Maithili
    "কথা",      // Bengali, Assamese
    "కథ",       // Telugu
    "கதை",      // Tamil
    "کہانی",     // Urdu, Kashmiri
    "વાર્તા",    // Gujarati
    "ಕಥೆ",      // Kannada
    "କଥା",      // Odia
    "കഥ",       // Malayalam
    "ਕਥਾ",      // Punjabi
    "କାହାଣୀ",    // Santali (often written in Ol Chiki: ᱠᱟᱹᱦᱱᱤ, but script support varies; using close phonetic/regional)
    "കഹാനി",    // Sindhi (Arabic script: ڪهاڻي, Devanagari/regional phonetics vary)
    "वारी",      // Manipuri (Meitei: ꯋꯥꯔꯤ)
  ];

  const kathaElement = document.getElementById('katha-rotator');
  if (kathaElement) {
    let currentKathaIndex = 0;
    setInterval(() => {
      kathaElement.classList.add('fade-out');

      setTimeout(() => {
        currentKathaIndex = (currentKathaIndex + 1) % kathaTranslations.length;
        kathaElement.textContent = kathaTranslations[currentKathaIndex];

        kathaElement.classList.remove('fade-out');
        kathaElement.classList.add('fade-in');

        // Remove fade-in class after transition completes to reset state
        setTimeout(() => {
          kathaElement.classList.remove('fade-in');
        }, 400); // matches CSS transition duration
      }, 400); // matches CSS transition duration
    }, 2500); // Change text every 2.5 seconds
  }

  /* ─── Category Color Map ──────────────────────────────────────── */
  const CAT_COLORS = {
    'tomb': '#9e3d1e',
    'mosque': '#c8873a',
    'fort': '#1a1208',
    'gate': '#4a7a40',
    'garden': '#2d8a60',
    'pillar': '#4040aa',
    'other': '#7a6a55',
  };

  /* ─── Scroll Reveal via Intersection Observer ─────────────────── */
  const revealElements = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
  );
  revealElements.forEach((el) => revealObserver.observe(el));

  /* ─── Audio Hook ──────────────────────────────────────────────── */
  const audioTriggerSection = document.getElementById('audio-trigger-section');
  if (audioTriggerSection) {
    const audioObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            console.log('Audio Triggered');
            audioObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.3 }
    );
    audioObserver.observe(audioTriggerSection);
  }

  /* ─── Reading Progress Bar ────────────────────────────────────── */
  const progressBar = document.getElementById('reading-progress');
  if (progressBar) {
    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      progressBar.style.width = progress + '%';
    }, { passive: true });
  }

  /* ─── Navbar: Scroll Effect + Active Section Highlighting ─────── */
  const nav = document.querySelector('.site-nav');
  const navAnchors = document.querySelectorAll('.nav-links a:not(.nav-cta)');
  const sections = document.querySelectorAll('main section[id], header[id]');

  if (nav) {
    window.addEventListener('scroll', () => {
      // Scrolled style
      nav.classList.toggle('scrolled', window.scrollY > 60);

      // Active nav link
      let currentId = '';
      sections.forEach((section) => {
        const top = section.getBoundingClientRect().top;
        if (top <= 120) currentId = section.id;
      });

      navAnchors.forEach((a) => {
        const href = a.getAttribute('href');
        a.classList.toggle('active', href === '#' + currentId);
      });
    }, { passive: true });
  }

  /* ─── Mobile Nav Toggle ───────────────────────────────────────── */
  const navToggle = document.querySelector('.nav-toggle');
  const navLinksEl = document.querySelector('.nav-links');

  if (navToggle && navLinksEl) {
    navToggle.addEventListener('click', () => {
      navLinksEl.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', navLinksEl.classList.contains('open'));
    });
    navLinksEl.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        navLinksEl.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ─── Count-Up Animation on Stats ────────────────────────────── */
  function animateCount(el, target, suffix, duration) {
    const start = performance.now();
    const isFloat = target % 1 !== 0;

    function tick(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      // Ease-out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      const value = isFloat
        ? (eased * target).toFixed(1)
        : Math.round(eased * target);
      el.textContent = value + suffix;
      if (progress < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  const statConfigs = [
    { selector: '[data-count="3"]', target: 3, suffix: ' hrs' },
    { selector: '[data-count="2.5"]', target: 2.5, suffix: ' km' },
  ];

  const statsSection = document.querySelector('.trail-stats');
  if (statsSection) {
    let hasAnimated = false;
    const statsObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && !hasAnimated) {
            hasAnimated = true;
            statConfigs.forEach(({ selector, target, suffix }) => {
              const el = document.querySelector(selector);
              if (el) animateCount(el, target, suffix, 1200);
            });
            statsObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );
    statsObserver.observe(statsSection);
  }

  /* ─── Site Detail Sidebar ─────────────────────────────────────── */
  const sidebar = document.getElementById('site-sidebar');
  const overlay = document.getElementById('sidebar-overlay');
  const closeBtn = document.getElementById('sidebar-close');
  const sidebarName = document.getElementById('sidebar-name');
  const sidebarBadge = document.getElementById('sidebar-badge');
  const sidebarUnesco = document.getElementById('sidebar-unesco');
  const sidebarKatha = document.getElementById('sidebar-katha');
  const sidebarCoords = document.getElementById('sidebar-coords');

  function openSidebar(props, lat, lng) {
    const color = CAT_COLORS[props.category] || '#7a6a55';
    const textCol = '#F4F4F0';
    const displayCat = props.category.charAt(0).toUpperCase() + props.category.slice(1);

    sidebarBadge.textContent = displayCat;
    sidebarBadge.style.background = color;
    sidebarBadge.style.color = textCol;
    sidebarName.textContent = props.name;
    sidebarKatha.textContent = props.katha;
    sidebarCoords.textContent = `📍 ${props.loc} | ${lat.toFixed(4)}° N, ${lng.toFixed(4)}° E`;

    if (props.unesco) {
      sidebarUnesco.style.display = 'inline-block';
    } else {
      sidebarUnesco.style.display = 'none';
    }

    sidebar.classList.add('open');
    overlay.classList.add('visible');
    document.body.style.overflow = 'hidden';
  }

  function closeSidebar() {
    sidebar.classList.remove('open');
    overlay.classList.remove('visible');
    document.body.style.overflow = '';
  }

  if (closeBtn) closeBtn.addEventListener('click', closeSidebar);
  if (overlay) overlay.addEventListener('click', closeSidebar);
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeSidebar();
  });

  /* ─── Trail Map (Leaflet + GeoJSON) ─────────────────────────── */
  const mapCanvas = document.getElementById('trail-map-canvas');

  if (mapCanvas && typeof L !== 'undefined') {// 1. Define the physical boundaries of Delhi NCR
    const delhiBounds = L.latLngBounds(
      [28.40, 76.80], // Southwest corner (Gurugram edge)
      [28.90, 77.50]  // Northeast corner (Ghaziabad edge)
    );

    // 2. Initialize the map with extreme restrictions
    const map = L.map('trail-map-canvas', {
      center: [28.5900, 77.2350], // Your original center
      zoom: 12,                   // Your original starting zoom
      scrollWheelZoom: false,     // Your original setting
      attributionControl: true,   // Your original setting
      minZoom: 12,                // CRITICAL: Prevents zooming out past the city
      maxZoom: 19,                // Allows deep zoom into the street level
      maxBounds: delhiBounds,     // CRITICAL: Traps the user inside the Delhi box
      maxBoundsViscosity: 1.0     // Makes the boundary act like a solid brick wall
    });

    // CARTO light — clean, muted, heritage-appropriate
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/">CARTO</a>',
      maxZoom: 19,
    }).addTo(map);

    // Layer groups per category
    const layerGroups = {};
    let allMarkers = [];
    let currentFilter = 'all';

    // Use the globally loaded trailData object directly
    if (typeof trailData !== 'undefined') {
      trailData.features.forEach((feature) => {
        const [lng, lat] = feature.geometry.coordinates;
        const props = feature.properties;
        const color = CAT_COLORS[props.category] || '#F59E0B';

        // Category layer group
        if (!layerGroups[props.category]) {
          layerGroups[props.category] = L.layerGroup().addTo(map);
        }

        // Circle marker with category color
        const marker = L.circleMarker([lat, lng], {
          radius: 7,
          fillColor: color,
          fillOpacity: 0.92,
          color: '#F4F4F0',
          weight: 2,
        });

        // Click → open sidebar (no popup)
        marker.on('click', () => openSidebar(props, lat, lng));

        // Hover tooltip
        marker.bindTooltip(props.name, {
          permanent: false,
          direction: 'top',
          offset: [0, -8],
          className: 'leaflet-tooltip',
        });

        layerGroups[props.category].addLayer(marker);
        allMarkers.push({ marker, category: props.category });
      });

      // Update visible count
      updateCount();

      // Fit map to content with ample padding
      if (trailData.features.length > 0) {
        const allCoords = trailData.features.map(
          (f) => [f.geometry.coordinates[1], f.geometry.coordinates[0]]
        );
        map.fitBounds(allCoords, { padding: [40, 40] });
      }
    } else {
      console.warn('trail_data.js is not loaded.');
    }

    function updateCount() {
      const countEl = document.getElementById('visible-count');
      if (!countEl) return;
      const visible = currentFilter === 'all'
        ? allMarkers.length
        : allMarkers.filter((m) => m.category === currentFilter).length;
      countEl.textContent = visible;
    }

    // Filter pills
    const filterPills = document.querySelectorAll('.filter-pill');
    filterPills.forEach((pill) => {
      pill.addEventListener('click', () => {
        const cat = pill.dataset.cat;
        currentFilter = cat;

        // Toggle active class
        filterPills.forEach((p) => p.classList.remove('active'));
        pill.classList.add('active');

        // Show/hide layer groups
        if (cat === 'all') {
          Object.values(layerGroups).forEach((lg) => map.addLayer(lg));
        } else {
          Object.entries(layerGroups).forEach(([name, lg]) => {
            if (name === cat) map.addLayer(lg);
            else map.removeLayer(lg);
          });
        }
        updateCount();
      });
    });

    // Re-invalidate size when map becomes visible
    const mapSection = document.querySelector('.trail-map-section');
    if (mapSection) {
      const mapResizeObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              map.invalidateSize();
              mapResizeObserver.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.1 }
      );
      mapResizeObserver.observe(mapSection);
    }
  }



  /* ─── Safdarjung Modal Logic ──────────────────────────────────── */
  const smodal = document.getElementById('safdarjung-modal');
  const sdetailsBtn = document.getElementById('safdarjung-details-btn');
  const smodalCloseBtn = document.getElementById('modal-close-btn');

  if (smodal && sdetailsBtn && smodalCloseBtn) {
    function openSafdarjungModal() {
      smodal.classList.add('open');
      smodal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }

    function closeSafdarjungModal() {
      smodal.classList.remove('open');
      smodal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    sdetailsBtn.addEventListener('click', openSafdarjungModal);
    smodalCloseBtn.addEventListener('click', closeSafdarjungModal);

    smodal.addEventListener('click', (e) => {
      if (e.target === smodal) closeSafdarjungModal();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && smodal.classList.contains('open')) {
        closeSafdarjungModal();
      }
    });
  }

})();
