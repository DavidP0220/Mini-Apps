(async function () {
  const res = await fetch('content.json');
  const data = await res.json();
  const STORAGE_KEY = 'progress_' + (data.meta.id || 'app');

  let state = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
  state.doneChapters = state.doneChapters || [];
  state.checklist = state.checklist || {};
  state.quiz = state.quiz || {};
  state.currentChapter = state.currentChapter ?? null;

  function save() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  }

  // Theme
  const root = document.documentElement;
  const savedTheme = localStorage.getItem('theme_' + data.meta.id);
  if (savedTheme) root.setAttribute('data-theme', savedTheme);
  document.getElementById('themeToggle').addEventListener('click', () => {
    const cur = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', cur);
    localStorage.setItem('theme_' + data.meta.id, cur);
    document.getElementById('themeToggle').textContent = cur === 'dark' ? '☀️' : '🌙';
  });
  document.getElementById('themeToggle').textContent = root.getAttribute('data-theme') === 'dark' ? '☀️' : '🌙';

  if (data.meta.themeColor) {
    document.documentElement.style.setProperty('--accent', data.meta.themeColor);
  }
  if (data.meta.accentColor) {
    document.documentElement.style.setProperty('--accent-2', data.meta.accentColor);
  }

  // Cover
  document.getElementById('coverIcon').textContent = data.chapters[0]?.icon || '📘';
  document.getElementById('coverTitle').textContent = data.meta.title;
  document.getElementById('coverSubtitle').textContent = data.meta.subtitle || '';
  document.getElementById('sidebarTitle').textContent = data.meta.title;
  document.title = data.meta.title;

  function progressPct() {
    return Math.round((state.doneChapters.length / data.chapters.length) * 100);
  }

  function refreshCoverProgress() {
    const pct = progressPct();
    document.getElementById('coverProgressFill').style.width = pct + '%';
    document.getElementById('coverProgressLabel').textContent = pct + '% completado';
    document.getElementById('continueBtn').classList.toggle('hidden', !state.currentChapter);
  }
  refreshCoverProgress();

  document.getElementById('startBtn').addEventListener('click', () => openApp(data.chapters[0].id));
  document.getElementById('continueBtn').addEventListener('click', () => openApp(state.currentChapter));

  function openApp(chapterId) {
    document.getElementById('cover').classList.add('hidden');
    document.getElementById('shell').classList.remove('hidden');
    renderSidebar();
    renderChapter(chapterId);
  }

  function renderSidebar() {
    const list = document.getElementById('chapterList');
    list.innerHTML = '';
    data.chapters.forEach(ch => {
      const li = document.createElement('li');
      li.className = 'chapter-item' + (state.doneChapters.includes(ch.id) ? ' done' : '');
      li.innerHTML = `<span class="chapter-check"></span><span>${ch.icon || ''} ${ch.title}</span>`;
      li.addEventListener('click', () => {
        renderChapter(ch.id);
        document.getElementById('sidebar').classList.remove('open');
        document.getElementById('overlay').classList.add('hidden');
      });
      list.appendChild(li);
    });
    document.getElementById('progressFill').style.width = progressPct() + '%';
  }

  function markActiveSidebar(chapterId) {
    document.querySelectorAll('.chapter-item').forEach((el, i) => {
      el.classList.toggle('active', data.chapters[i].id === chapterId);
    });
  }

  function renderChapter(chapterId) {
    const idx = data.chapters.findIndex(c => c.id === chapterId);
    const ch = data.chapters[idx];
    state.currentChapter = chapterId;
    if (!state.doneChapters.includes(chapterId)) {
      // mark previous as visited implicitly when navigating forward past it
    }
    save();
    markActiveSidebar(chapterId);

    const content = document.getElementById('content');
    const wrap = document.createElement('div');
    wrap.className = 'content-inner';

    const heading = document.createElement('h2');
    heading.className = 'chapter-heading';
    heading.innerHTML = `<span>${ch.icon || ''}</span><span>${ch.title}</span>`;
    wrap.appendChild(heading);

    ch.sections.forEach((section, sIdx) => {
      wrap.appendChild(renderSection(section, ch.id + '_' + sIdx));
    });

    const navRow = document.createElement('div');
    navRow.className = 'nav-buttons';
    const prevBtn = document.createElement('button');
    prevBtn.textContent = '← Anterior';
    prevBtn.disabled = idx === 0;
    prevBtn.addEventListener('click', () => renderChapter(data.chapters[idx - 1].id));

    const nextBtn = document.createElement('button');
    const isLast = idx === data.chapters.length - 1;
    nextBtn.textContent = isLast ? 'Completar ✓' : 'Siguiente →';
    nextBtn.className = 'primary';
    nextBtn.addEventListener('click', () => {
      if (!state.doneChapters.includes(chapterId)) {
        state.doneChapters.push(chapterId);
        save();
        renderSidebar();
        markActiveSidebar(chapterId);
      }
      if (!isLast) renderChapter(data.chapters[idx + 1].id);
      else refreshCoverProgress();
    });

    navRow.appendChild(prevBtn);
    navRow.appendChild(nextBtn);
    wrap.appendChild(navRow);

    content.innerHTML = '';
    content.appendChild(wrap);
    content.scrollTop = 0;
  }

  function renderSection(section, key) {
    const block = document.createElement('div');
    block.className = 'section-block';

    if (section.type === 'text') {
      if (section.heading) {
        const h = document.createElement('h3');
        h.textContent = section.heading;
        block.appendChild(h);
      }
      const p = document.createElement('p');
      p.textContent = section.body;
      block.appendChild(p);
    }

    if (section.type === 'callout') {
      const div = document.createElement('div');
      div.className = 'callout ' + (section.style || 'note');
      const span = document.createElement('span');
      span.textContent = section.body;
      div.appendChild(span);
      block.appendChild(div);
    }

    if (section.type === 'checklist') {
      if (section.heading) {
        const h = document.createElement('h3');
        h.textContent = section.heading;
        block.appendChild(h);
      }
      const box = document.createElement('div');
      box.className = 'checklist-box';
      section.items.forEach((item, i) => {
        const itemKey = key + '_' + i;
        const row = document.createElement('label');
        row.className = 'checklist-item' + (state.checklist[itemKey] ? ' checked' : '');
        row.innerHTML = `<input type="checkbox" ${state.checklist[itemKey] ? 'checked' : ''}><span>${item}</span>`;
        row.querySelector('input').addEventListener('change', (e) => {
          state.checklist[itemKey] = e.target.checked;
          row.classList.toggle('checked', e.target.checked);
          save();
        });
        box.appendChild(row);
      });
      block.appendChild(box);
    }

    if (section.type === 'quiz') {
      const box = document.createElement('div');
      box.className = 'quiz-box';
      const q = document.createElement('div');
      q.className = 'quiz-question';
      q.textContent = section.question;
      box.appendChild(q);

      const answered = state.quiz[key];

      section.options.forEach((opt, i) => {
        const btn = document.createElement('button');
        btn.className = 'quiz-option';
        btn.textContent = opt;
        if (answered !== undefined) {
          if (i === section.answerIndex) btn.classList.add('correct');
          else if (i === answered) btn.classList.add('incorrect');
        }
        btn.addEventListener('click', () => {
          if (state.quiz[key] !== undefined) return;
          state.quiz[key] = i;
          save();
          renderSectionInPlace();
        });
        box.appendChild(btn);
      });

      if (answered !== undefined) {
        const exp = document.createElement('div');
        exp.className = 'quiz-explanation';
        exp.textContent = section.explanation || '';
        box.appendChild(exp);
      }

      function renderSectionInPlace() {
        const fresh = renderSection(section, key);
        block.replaceWith(fresh);
      }

      block.appendChild(box);
    }

    if (section.type === 'table') {
      if (section.heading) {
        const h = document.createElement('h3');
        h.textContent = section.heading;
        block.appendChild(h);
      }
      const wrap = document.createElement('div');
      wrap.className = 'table-wrap';
      const table = document.createElement('table');
      table.className = 'data-table';

      const thead = document.createElement('thead');
      const headRow = document.createElement('tr');
      section.columns.forEach(col => {
        const th = document.createElement('th');
        th.textContent = col;
        headRow.appendChild(th);
      });
      thead.appendChild(headRow);
      table.appendChild(thead);

      const tbody = document.createElement('tbody');
      section.rows.forEach(row => {
        const tr = document.createElement('tr');
        row.forEach(cell => {
          const td = document.createElement('td');
          td.textContent = cell;
          tr.appendChild(td);
        });
        tbody.appendChild(tr);
      });
      table.appendChild(tbody);
      wrap.appendChild(table);
      block.appendChild(wrap);
    }

    return block;
  }

  // Mobile menu
  document.getElementById('menuToggle').addEventListener('click', () => {
    document.getElementById('sidebar').classList.add('open');
    document.getElementById('overlay').classList.remove('hidden');
  });
  document.getElementById('overlay').addEventListener('click', () => {
    document.getElementById('sidebar').classList.remove('open');
    document.getElementById('overlay').classList.add('hidden');
  });

  // Service worker for installability / offline
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js').catch(() => {});
  }
})();
