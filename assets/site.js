(() => {
  'use strict';

  const heroAnimal = document.querySelector('#heroAnimal');
  const closingAnimal = document.querySelector('#closingAnimal');
  const prefersLessMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const deploymentBase = String(window.MIMO_BASE_PATH || '').replace(/\/+$/, '');
  const sitePath = (path) => `${deploymentBase}${String(path).startsWith('/') ? path : `/${path}`}` || '/';
  const heroScene = document.querySelector('#heroScene');
  if (heroScene && !prefersLessMotion.matches) {
    let parallaxFrame = 0;
    const updateParallax = () => {
      parallaxFrame = 0;
      if (prefersLessMotion.matches) {
        heroScene.style.setProperty('--parallax-shift', '0px');
        return;
      }
      const strength = window.innerWidth <= 760 ? 0.1 : 0.18;
      const limit = window.innerWidth <= 760 ? 36 : 82;
      heroScene.style.setProperty('--parallax-shift', `${Math.min(limit, window.scrollY * strength)}px`);
    };
    const requestParallax = () => {
      if (!parallaxFrame) parallaxFrame = window.requestAnimationFrame(updateParallax);
    };
    window.addEventListener('scroll', requestParallax, { passive: true });
    window.addEventListener('resize', requestParallax, { passive: true });
    updateParallax();
  }
  const rotateSticker = (image, items, interval, note = null) => {
    if (!image || prefersLessMotion.matches) return;
    let index = 0;
    let inView = false;
    let changing = false;
    const target = note ? image.closest('.hero-scene') : image;
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(([entry]) => { inView = entry.isIntersecting; }, { threshold: 0.2 }).observe(image);
    } else { inView = true; }
    window.setInterval(() => {
      if (document.hidden || !inView || changing || prefersLessMotion.matches) return;
      const next = (index + 1) % items.length;
      const candidate = new Image();
      changing = true;
      candidate.onload = () => {
        target.classList.add('is-changing');
        window.setTimeout(() => {
          image.src = sitePath(items[next].src);
          image.alt = items[next].alt;
          if (note) note.textContent = items[next].note;
          index = next;
          window.requestAnimationFrame(() => {
            target.classList.remove('is-changing');
            changing = false;
          });
        }, 280);
      };
      candidate.onerror = () => { changing = false; };
      candidate.src = sitePath(items[next].src);
    }, interval);
  };
  rotateSticker(heroAnimal, [
    { src: '/assets/stickers/03-salchicha-milo.webp', alt: 'Milo, un perro salchicha', note: 'Milo, experto\nen explorar' },
    { src: '/assets/stickers/12-gato-mora.webp', alt: 'Mora, una gata negra', note: 'Mora, dueña\nde la almohada' },
    { src: '/assets/stickers/18-loro-lima.webp', alt: 'Lima, un loro', note: 'Lima, curiosa\npor naturaleza' },
    { src: '/assets/stickers/34-galgo.webp', alt: 'Faro, un galgo español', note: 'Faro, veloz\ny sereno' },
    { src: '/assets/stickers/15-conejo-pompon.webp', alt: 'Pompón, un conejo', note: 'Pompón, amigo\ndel heno' },
    { src: '/assets/stickers/22-periquito.webp', alt: 'Cielo, un periquito', note: 'Cielo, pequeño\nexplorador' },
    { src: '/assets/stickers/38-shar-pei.webp', alt: 'Mochi, un shar-pei', note: 'Mochi, muchos\npliegues y calma' },
  ], 5500, document.querySelector('#heroAnimalNote'));
  rotateSticker(closingAnimal, [
    { src: '/assets/stickers/12-gato-mora.webp', alt: 'Mora, una gata negra' },
    { src: '/assets/stickers/01-caniche-nube.webp', alt: 'Nube, un caniche' },
    { src: '/assets/stickers/19-ninfa-pina.webp', alt: 'Piña, una ninfa' },
    { src: '/assets/stickers/16-cobayo-kiwi.webp', alt: 'Kiwi, un cobayo' },
    { src: '/assets/stickers/26-bull-terrier.webp', alt: 'Bimba, una bull terrier' },
  ], 6200);
  rotateSticker(document.querySelector('#visitAnimal'), [
    { src: '/assets/stickers/18-loro-lima.webp', alt: '' },
    { src: '/assets/stickers/03-salchicha-milo.webp', alt: '' },
    { src: '/assets/stickers/12-gato-mora.webp', alt: '' },
    { src: '/assets/stickers/22-periquito.webp', alt: '' },
    { src: '/assets/stickers/15-conejo-pompon.webp', alt: '' },
  ], 5600);

  const careDeck = document.querySelector('#careDeck');
  if (careDeck) {
    const deckCards = [...careDeck.querySelectorAll('[data-deck-card]')];
    const deckStates = ['is-active', 'is-back-one', 'is-back-two'];
    const deckMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let activeCard = 0;
    let deckVisible = false;
    let deckHovered = false;
    let deckFocused = false;
    let deckPausedUntil = 0;
    let deckBusyUntil = 0;
    let pointerOrigin = null;
    const arrangeCards = (newIndex) => {
      const previousCard = deckCards[activeCard];
      const nextIndex = (newIndex + deckCards.length) % deckCards.length;
      if (nextIndex === activeCard) return;
      deckBusyUntil = Date.now() + 500;
      if (!deckMotion.matches) previousCard.classList.add('is-leaving');
      activeCard = nextIndex;
      deckCards.forEach((card, index) => {
        const position = (index - activeCard + deckCards.length) % deckCards.length;
        card.classList.remove(...deckStates);
        card.classList.add(deckStates[position]);
        card.setAttribute('aria-hidden', String(position !== 0));
        card.setAttribute('aria-label', `${index + 1} de ${deckCards.length}`);
      });
      window.setTimeout(() => previousCard.classList.remove('is-leaving'), 490);
    };
    const moveDeck = (step) => {
      if (Date.now() < deckBusyUntil) return;
      deckPausedUntil = Date.now() + 12000;
      arrangeCards(activeCard + step);
    };
    deckCards.forEach((card, index) => {
      card.classList.add(deckStates[index]);
      card.setAttribute('aria-hidden', String(index !== 0));
    });
    careDeck.addEventListener('keydown', (event) => {
      if (event.key === 'ArrowRight') { event.preventDefault(); moveDeck(1); }
      if (event.key === 'ArrowLeft') { event.preventDefault(); moveDeck(-1); }
    });
    careDeck.addEventListener('pointerdown', (event) => {
      if (event.pointerType === 'mouse' && event.button !== 0) return;
      pointerOrigin = { x: event.clientX, y: event.clientY };
    });
    careDeck.addEventListener('pointerup', (event) => {
      if (!pointerOrigin) return;
      const dx = event.clientX - pointerOrigin.x;
      const dy = event.clientY - pointerOrigin.y;
      pointerOrigin = null;
      if (Math.abs(dx) > 38 && Math.abs(dx) > Math.abs(dy) * 1.2) moveDeck(dx < 0 ? 1 : -1);
    });
    careDeck.addEventListener('pointercancel', () => { pointerOrigin = null; });
    careDeck.addEventListener('mouseenter', () => { deckHovered = true; });
    careDeck.addEventListener('mouseleave', () => { deckHovered = false; });
    careDeck.addEventListener('focusin', () => { deckFocused = true; });
    careDeck.addEventListener('focusout', () => { deckFocused = careDeck.contains(document.activeElement); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(([entry]) => { deckVisible = entry.isIntersecting; }, { threshold: 0.25 }).observe(careDeck);
    } else { deckVisible = true; }
    window.setInterval(() => {
      if (document.hidden || !deckVisible || deckMotion.matches || deckHovered || deckFocused || Date.now() < deckPausedUntil) return;
      arrangeCards(activeCard + 1);
    }, 5200);
  }

  const menuButton = document.querySelector('.menu-toggle');
  const mobileNav = document.querySelector('#mobileNav');
  if (menuButton && mobileNav) {
    const setMenu = (open) => {
      mobileNav.hidden = !open;
      menuButton.setAttribute('aria-expanded', String(open));
      menuButton.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
      document.body.classList.toggle('menu-open', open);
    };
    menuButton.addEventListener('click', () => setMenu(mobileNav.hidden));
    mobileNav.addEventListener('click', (event) => {
      if (event.target.closest('a')) setMenu(false);
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') setMenu(false);
    });
  }

  const viewport = document.querySelector('#animalViewport');
  if (viewport) {
    const cards = [...viewport.querySelectorAll('.animal-card')];
    const filters = [...document.querySelectorAll('[data-animal-filter]')];
    const feature = document.querySelector('#animalFeature');
    const featureImage = document.querySelector('#featureImage');
    const featureCategory = document.querySelector('#featureCategory');
    const featureTitle = document.querySelector('#featureTitle');
    const featureText = document.querySelector('#featureText');
    const featureLink = document.querySelector('#featureLink');
    const featureLinkText = document.querySelector('#featureLinkText');
    const status = document.querySelector('#carouselStatus');
    const prev = document.querySelector('#animalPrev');
    const next = document.querySelector('#animalNext');
    const groups = { perros: 'PERROS', gatos: 'GATOS', aves: 'AVES', pequenos: 'PEQUEÑOS' };
    const toneClasses = ['tone-pink', 'tone-lilac', 'tone-mint', 'tone-yellow', 'tone-peach'];
    const animals = cards.map((card) => ({
      card,
      name: card.querySelector('.animal-name').textContent,
      label: card.querySelector('.animal-type').textContent,
      image: card.querySelector('img').getAttribute('src'),
      group: card.dataset.group,
      tone: card.dataset.tone,
      article: card.dataset.article || null,
      articleTitle: card.dataset.articleTitle || null,
      line: card.dataset.line || null,
    }));
    let selected = 0;
    let swapTimer;
    let pausedUntil = 0;
    let hovered = false;
    let hasFocus = false;
    let isInView = false;
    let userSwipe = false;
    let swipeTimer;
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    const visible = () => animals.map((_, i) => i).filter((i) => !cards[i].hidden);
    const noteInteraction = () => { pausedUntil = Date.now() + 12000; };
    const select = (index, userInitiated = false, scrollCard = true) => {
      const animal = animals[index];
      if (!animal || animal.card.hidden) return;
      if (scrollCard) userSwipe = false;
      selected = index;
      cards.forEach((card, i) => card.setAttribute('aria-pressed', String(i === index)));
      feature.classList.remove(...toneClasses);
      feature.classList.add(`tone-${animal.tone}`);
      featureImage.classList.add('changing');
      window.clearTimeout(swapTimer);
      const update = () => {
        featureImage.src = animal.image;
        featureImage.alt = `${animal.name}, ${animal.label.toLowerCase()}`;
        featureCategory.textContent = `${groups[animal.group]} · GUÍA PARA CONOCERLO`;
        featureTitle.querySelector('.feature-name').textContent = `Hola, soy ${animal.name}`;
        featureText.textContent = animal.line || '';
        featureLink.href = sitePath(animal.article ? `/guias/${animal.article}/` : '/guias/');
        featureLinkText.textContent = animal.articleTitle ? `Leer: ${animal.articleTitle}` : 'Leer la guía';
        featureImage.classList.remove('changing');
      };
      if (reducedMotion.matches) update(); else swapTimer = window.setTimeout(update, 170);
      const list = visible();
      status.textContent = `${String(list.indexOf(index) + 1).padStart(2, '0')} / ${String(list.length).padStart(2, '0')}`;
      if (scrollCard) {
        const left = animal.card.offsetLeft - cards[list[0]].offsetLeft;
        viewport.scrollTo({ left: Math.max(0, left - 5), behavior: reducedMotion.matches ? 'auto' : 'smooth' });
      }
      if (userInitiated) { noteInteraction(); status.setAttribute('aria-live', 'polite'); }
    };
    cards.forEach((card, i) => card.addEventListener('click', () => select(i, true)));
    const step = (direction, userInitiated = false) => {
      const list = visible();
      if (!list.length) return;
      let current = list.indexOf(selected);
      if (current < 0) current = 0;
      const target = list[(current + direction + list.length) % list.length];
      select(target, userInitiated);
    };
    prev.addEventListener('click', () => step(-1, true));
    next.addEventListener('click', () => step(1, true));
    filters.forEach((button) => button.addEventListener('click', () => {
      const category = button.dataset.animalFilter;
      filters.forEach((item) => {
        const active = item === button;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-pressed', String(active));
      });
      cards.forEach((card) => { card.hidden = category !== 'todos' && card.dataset.group !== category; });
      viewport.scrollLeft = 0;
      const first = visible()[0];
      if (first !== undefined) select(first, true);
    }));
    viewport.addEventListener('pointerdown', () => { noteInteraction(); userSwipe = true; }, { passive: true });
    viewport.addEventListener('scroll', () => {
      if (!userSwipe) return;
      window.clearTimeout(swipeTimer);
      swipeTimer = window.setTimeout(() => {
        const list = visible();
        const nearest = list.reduce((best, i) =>
          Math.abs(cards[i].offsetLeft - cards[list[0]].offsetLeft - viewport.scrollLeft) <
          Math.abs(cards[best].offsetLeft - cards[list[0]].offsetLeft - viewport.scrollLeft) ? i : best,
        list[0]);
        if (nearest !== undefined && nearest !== selected) select(nearest, true, false);
        userSwipe = false;
      }, 210);
    }, { passive: true });
    viewport.addEventListener('mouseenter', () => { hovered = true; });
    viewport.addEventListener('mouseleave', () => { hovered = false; });
    viewport.addEventListener('focusin', () => { hasFocus = true; });
    viewport.addEventListener('focusout', () => { hasFocus = viewport.contains(document.activeElement); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver((entries) => { isInView = entries[0].isIntersecting; }, { threshold: 0.25 }).observe(viewport);
    } else { isInView = true; }
    window.setInterval(() => {
      if (document.hidden || !isInView || reducedMotion.matches || hovered || hasFocus || Date.now() < pausedUntil) return;
      status.setAttribute('aria-live', 'off');
      step(1);
    }, 4300);
  }

  const libraryGrid = document.querySelector('#libraryGrid');
  if (libraryGrid) {
    const guideCards = [...libraryGrid.querySelectorAll('[data-guide-category]')];
    const guideFilters = [...libraryGrid.parentElement.querySelectorAll('[data-guide-filter]')];
    const count = document.querySelector('#guideCount');
    let current = 'todas';
    const refresh = () => {
      let visibleCount = 0;
      guideCards.forEach((card) => {
        const categories = String(card.dataset.guideCategory || '').trim().toLocaleLowerCase('es-AR').split(/[\s,]+/);
        const matches = current === 'todas' || categories.includes(current);
        card.hidden = !matches;
        if (matches) visibleCount += 1;
      });
      count.textContent = `${visibleCount} ${visibleCount === 1 ? 'guía' : 'guías'} para explorar`;
    };
    guideFilters.forEach((button) => button.addEventListener('click', () => {
      current = String(button.dataset.guideFilter || 'todas').trim().toLocaleLowerCase('es-AR');
      guideFilters.forEach((item) => {
        const active = item === button;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-pressed', String(active));
      });
      refresh();
    }));
    refresh();
  }
})();
