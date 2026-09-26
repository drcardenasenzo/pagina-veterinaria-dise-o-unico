#!/usr/bin/env python3
"""Build the no-dependency static Mimo website.

Usage: python3 -B build.py
Optional before publication: SITE_URL=https://your-domain.example python3 -B build.py
"""
import html
import json
import os
import re
import shutil
from pathlib import Path
from urllib.parse import quote
from datetime import date

from content import ARTICLES

ROOT = Path(__file__).parent
OUTPUT_ROOT = Path(os.environ["OUTPUT_DIR"]).resolve() if os.environ.get("OUTPUT_DIR") else ROOT
ANIMALS = json.loads((ROOT / "animals.json").read_text())
BY_SLUG = {a["slug"]: a for a in ARTICLES}
SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")
BASE_PATH = os.environ.get("BASE_PATH", "").strip("/")
WHATSAPP_NUMBER = os.environ.get("WHATSAPP_NUMBER", "").strip("+ ")

assert len(BY_SLUG) == len(ARTICLES)
assert all(a["article"] in BY_SLUG for a in ANIMALS)
assert all(rel in BY_SLUG for a in ARTICLES for rel in a["related"])

GROUP_LABELS = {"perros": "Perros", "gatos": "Gatos", "aves": "Aves", "pequenos": "Pequeños", "salud": "Salud"}
GROUP_COLORS = {"perros": "pink", "gatos": "lilac", "aves": "mint", "pequenos": "yellow", "salud": "peach"}
CARD_TONES = ("pink", "mint", "lilac", "yellow", "peach")

def e(value):
    return html.escape(str(value), quote=True)

def article_url(slug):
    return f"/guias/{slug}/"

def wa_url(message="Hola, Mimo. Quisiera hacer una consulta."):
    target = f"https://wa.me/{WHATSAPP_NUMBER}" if WHATSAPP_NUMBER else "https://api.whatsapp.com/send"
    return f"{target}?text={quote(message)}"

def svg_icon(name, size=22):
    paths = {
      "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
      "close": '<path d="M5 5l14 14M19 5 5 19"/>',
      "location": '<path d="M20 10c0 5-8 11-8 11S4 15 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.4"/>',
      "whatsapp": '<path d="M20.5 11.7a8.5 8.5 0 0 1-12.4 7.5L3 20.6l1.4-4.9A8.5 8.5 0 1 1 20.5 11.7Z"/><path d="M9.1 8.2c-.2-.4-.4-.4-.7-.4h-.6c-.2 0-.5.1-.7.3-.2.2-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.9 4.4 4 .6.3 1.1.5 1.5.6.6.2 1.1.2 1.5.1.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2s-.2-.2-.5-.3l-1.5-.7c-.3-.1-.5-.2-.7.2l-.7.8c-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.6-2.1-.2-.3 0-.4.1-.6l.5-.6c.2-.2.2-.4.3-.6 0-.2 0-.4-.1-.6Z"/>',
    }
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>'

def header(active=""):
    links = [("/", "Inicio", "inicio"), ("/#animalitos", "Animalitos", "animales"), ("/guias/", "Guías", "guias"), ("/atencion/", "Atención", "atencion")]
    nav = "".join(f'<a href="{url}"{attr}>{label}</a>' for url, label, key in links
                  for attr in [' aria-current="page"' if active == key else ''])
    return f'''<a class="skip-link" href="#contenido">Ir al contenido</a>
<header class="site-header" id="top"><div class="header-inner">
  <a class="brand" href="/" aria-label="Mimo Veterinaria, inicio"><span class="brand-mark">m</span><span class="brand-lines"><strong>mimo</strong><small>VETERINARIA</small></span></a>
  <nav class="desktop-nav" aria-label="Navegación principal">{nav}</nav>
  <a class="header-contact" href="/contacto/">Hablemos</a>
  <button class="menu-toggle" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="mobileNav">{svg_icon('menu',24)}</button>
</div><nav class="mobile-nav" id="mobileNav" aria-label="Navegación móvil" hidden>{nav}<a href="/contacto/">Contacto</a></nav></header>'''

def footer():
    return f'''<footer class="site-footer"><div class="footer-inner">
      <div class="footer-brand"><a class="brand" href="/" aria-label="Mimo Veterinaria, inicio"><span class="brand-mark">m</span><span class="brand-lines"><strong>mimo</strong><small>VETERINARIA</small></span></a><p>Cuidar también es prestar atención a las pequeñas cosas.</p></div>
      <div class="footer-links"><strong>Explorá</strong><a href="/#animalitos">Animalitos</a><a href="/guias/">Guías de cuidado</a><a href="/atencion/">Atención</a></div>
      <div class="footer-links"><strong>Estamos cerca</strong><span>Los Polvorines · Buenos Aires</span><a href="/contacto/">Contacto</a><a href="/informacion/">Información legal</a></div>
    </div><div class="footer-bottom"><span>© {date.today().year} Mimo Veterinaria</span></div></footer>'''

def floating_wa():
    return f'<a class="wa-float" href="{e(wa_url())}" target="_blank" rel="noopener noreferrer" aria-label="Contactar por WhatsApp"><img src="/assets/whatsapp-brand.svg" width="48" height="48" alt=""></a>'

def layout(title, description, body, active="", path="/", extra_head=""):
    canonical = f'<link rel="canonical" href="{e(SITE_URL + path)}">' if SITE_URL else ""
    og_url = f'<meta property="og:url" content="{e(SITE_URL + path)}">' if SITE_URL else ""
    document = f'''<!doctype html><html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)} · Mimo Veterinaria</title><meta name="description" content="{e(description)}"><meta name="theme-color" content="#fff9ef">
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)} · Mimo Veterinaria"><meta property="og:description" content="{e(description)}">{og_url}{canonical}
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/styles.css">{extra_head}</head><body>
{header(active)}<main id="contenido">{body}</main>{footer()}{floating_wa()}<script defer src="/assets/site.js"></script></body></html>'''
    if BASE_PATH:
        document = re.sub(r'((?:href|src|content)=["\'])/(?!/)', rf'\1/{BASE_PATH}/', document)
        document = document.replace(
            f'<script defer src="/{BASE_PATH}/assets/site.js"></script>',
            f'<script>window.MIMO_BASE_PATH = "/{BASE_PATH}";</script><script defer src="/{BASE_PATH}/assets/site.js"></script>')
    return document

def guide_card(a, klass="", tone=None):
    img = f'/assets/stickers/{a["image"]}'
    return f'''<a class="guide-card {klass} tone-{tone or GROUP_COLORS[a['category']]}" href="{article_url(a['slug'])}" data-guide-category="{a['category']}">
    <div class="guide-image"><img src="{img}" alt="" loading="lazy" decoding="async"></div><div class="guide-card-copy"><span class="eyebrow-small">{GROUP_LABELS[a['category']]}</span><h3>{e(a['title'])}</h3><p>{e(a['deck'])}</p><span class="text-link">Leer guía</span></div></a>'''

def home():
    animal_cards = ''.join(f'''<button class="animal-card" type="button" data-animal-index="{i}" data-group="{a['group']}" data-tone="{CARD_TONES[i % len(CARD_TONES)]}" data-article="{a['article']}" data-article-title="{e(BY_SLUG[a['article']]['title'])}" data-line="{e(BY_SLUG[a['article']]['deck'])}" aria-label="Elegir {e(a['label'])}: {e(a['name'])}" aria-pressed="{'true' if i == 0 else 'false'}"><span class="animal-card-picture tone-{CARD_TONES[i % len(CARD_TONES)]}"><img src="{a['image']}" alt="" loading="{'eager' if i < 4 else 'lazy'}" decoding="async"></span><span class="animal-name">{e(a['name'])}</span><span class="animal-type">{e(a['label'])}</span></button>''' for i,a in enumerate(ANIMALS))
    featured = ANIMALS[0]
    latest = [BY_SLUG[s] for s in ("galgo-espanol", "gato-de-interior", "periquito")]
    qa = [
      ("¿Cómo pido un turno?", "Podés acercarte de lunes a viernes, de 10 a 18 h, sin turno previo. Si preferís organizar la visita, escribinos por WhatsApp para reservar."),
      ("¿Atienden aves y pequeños animales?", "Podés consultar por perros, gatos, aves y pequeños animales. Contanos la especie exacta antes de venir para organizar la atención adecuada."),
      ("¿Hacen castraciones?", "Sí, la castración se conversa en una consulta previa. La edad, el estado de salud y los cuidados posteriores se evalúan para cada animal."),
      ("¿Las guías reemplazan una consulta?", "No. Te ayudan a observar y preparar preguntas, pero un síntoma o cambio de conducta necesita una evaluación individual."),
      ("¿Puedo ir directamente a la veterinaria?", "Sí. Podés acercarte sin turno previo de lunes a viernes, entre las 10 y las 18 h. Si querés reservar un horario, escribinos por WhatsApp antes de venir."),
      ("¿Qué conviene llevar a la consulta?", "Si la tenés, traé su libreta sanitaria y anotá los medicamentos que usa y los cambios que observaste. Para aves y animales pequeños, consultanos antes cómo trasladarlos de forma segura."),
    ]
    faq = ''.join(f'<details><summary>{e(q)}<span class="faq-plus" aria-hidden="true">+</span></summary><p>{e(ans)}</p></details>' for q,ans in qa)
    body = f'''<section class="hero"><div class="hero-inner"><div class="hero-copy"><span class="eyebrow">MIMO VETERINARIA</span><h1>Hay alguien que hace de tu casa <em>un hogar.</em></h1><p class="hero-lead">Se adelanta en el paseo, se instala en tu almohada o te saluda desde una percha. Estamos para ayudarte a cuidarlo en cada etapa.</p><div class="hero-actions"><a class="button button-dark" href="#animalitos">Encontrá a tu compañero</a></div><div class="hero-footnote"><span class="tiny-rule"></span> Perros, gatos, aves y pequeños animales</div></div><div class="hero-scene" id="heroScene"><div class="hero-blob"></div><div class="hero-ring"></div><img class="hero-dog" id="heroAnimal" src="/assets/stickers/03-salchicha-milo.webp" alt="Milo, un perro salchicha" fetchpriority="high"><span class="scene-note scene-note-top" id="heroAnimalNote">Milo, experto<br>en explorar</span><span class="scene-note scene-note-bottom">Su mundo merece<br>ser conocido.</span></div></div></section>

<section class="animal-section section-pad" id="animalitos"><div class="section-heading animal-heading"><div><h2>¿Con quién compartís <em>la vida?</em></h2><p>Elegí a tu compañero. Cada uno tiene su forma de ser y cosas propias para cuidar.</p></div><div class="animal-count"><strong>{len(ANIMALS)}</strong><span>animalitos<br>para conocer</span></div></div>
<div class="animal-controls"><div class="filter-tabs" role="group" aria-label="Filtrar animalitos"><button type="button" class="filter-chip is-active" data-animal-filter="todos" aria-pressed="true">Todos</button><button type="button" class="filter-chip" data-animal-filter="perros" aria-pressed="false">Perros</button><button type="button" class="filter-chip" data-animal-filter="gatos" aria-pressed="false">Gatos</button><button type="button" class="filter-chip" data-animal-filter="aves" aria-pressed="false">Aves</button><button type="button" class="filter-chip" data-animal-filter="pequenos" aria-pressed="false">Pequeños</button></div><div class="carousel-controls"><span id="carouselStatus" aria-live="polite">01 / {len(ANIMALS):02d}</span><button type="button" class="circle-control" id="animalPrev" aria-label="Ver animales anteriores">Anterior</button><button type="button" class="circle-control" id="animalNext" aria-label="Ver más animales">Siguiente</button></div></div>
<div class="animal-viewport" id="animalViewport" aria-label="Carrusel de animalitos"><div class="animal-track" id="animalTrack">{animal_cards}</div></div><div class="carousel-hint"><span class="hint-line"></span><span>Podés tocar un animalito o deslizar para elegir.</span></div>
<div class="animal-feature tone-pink" id="animalFeature"><div class="feature-art"><span class="feature-orbit"></span><img id="featureImage" src="{featured['image']}" alt="Nube, caniche"></div><div class="feature-copy"><span class="eyebrow-small" id="featureCategory">PERROS · GUÍA PARA CONOCERLO</span><h3 id="featureTitle"><span class="feature-name">Hola, soy Nube</span><span>.</span></h3><p id="featureText">{e(BY_SLUG[featured['article']]['deck'])}</p><a class="button button-light" id="featureLink" href="{article_url(featured['article'])}"><span id="featureLinkText">Leer: {e(BY_SLUG[featured['article']]['title'])}</span></a></div></div></section>

<section class="editorial-section section-pad"><div class="section-heading editorial-heading"><div><span class="eyebrow-small">PALABRAS PARA EL DÍA A DÍA</span><h2>Preguntas que aparecen <em>en casa.</em></h2></div><a class="quiet-link" href="/guias/">Todas las guías</a></div><div class="featured-guides">{''.join(guide_card(a, 'home-guide') for a in latest)}</div></section>

<section class="care-section" id="atencion"><div class="care-inner"><div class="care-intro"><h2>Una consulta empieza por <em>escuchar.</em></h2><p>Traé tus preguntas, incluso las que parecen pequeñas. A veces ahí empieza el mejor cuidado.</p><a class="button button-dark" href="/atencion/">Así podemos ayudarte</a></div><div class="care-notes care-deck" id="careDeck" role="region" aria-roledescription="carrusel" aria-label="Servicios de Mimo. Deslizá o usá las flechas del teclado para recorrer las tarjetas." aria-live="off" tabindex="0"><article class="care-note is-active" data-deck-card="0" role="group" aria-roledescription="tarjeta" aria-label="1 de 3"><span class="note-pin" aria-hidden="true"></span><h3>Consulta general</h3><p>Para revisar su salud, conversar sobre cambios y acompañar cada etapa.</p></article><article class="care-note" data-deck-card="1" role="group" aria-roledescription="tarjeta" aria-label="2 de 3" aria-hidden="true"><span class="note-pin" aria-hidden="true"></span><h3>Prevención y vacunas</h3><p>Un plan pensado para la historia y el modo de vida de cada animal.</p></article><article class="care-note" data-deck-card="2" role="group" aria-roledescription="tarjeta" aria-label="3 de 3" aria-hidden="true"><span class="note-pin" aria-hidden="true"></span><h3>Castraciones</h3><p>Información clara antes de decidir y cuidados para acompañar la recuperación.</p></article></div></div></section>

<section class="faq-section section-pad"><div class="faq-layout"><div><span class="eyebrow-small">POR SI TE ESTÁS PREGUNTANDO</span><h2>Algunas respuestas, <em>sin vueltas.</em></h2><p>Y si tu duda es distinta, podemos conversar.</p></div><div class="faq-list">{faq}</div></div></section>

<section class="closing-section"><div class="closing-inner"><img id="closingAnimal" src="/assets/stickers/12-gato-mora.webp" alt="Mora, una gatita negra" loading="lazy"><div><span class="eyebrow-small">NOS GUSTA CONOCERLOS</span><h2>Contanos quién te espera en casa.</h2><p>Una consulta breve puede ser el comienzo de una vida mejor cuidada.</p><a class="button button-pink" href="/contacto/">Hablemos de él</a></div></div></section>'''
    return layout("Cuidarlos es conocerlos", "Veterinaria en Los Polvorines. Conocé a cada animal, explorá guías de cuidado y consultanos por atención general, prevención y castraciones.", body, "inicio", "/", extra_head='<link rel="preload" as="image" href="/assets/stickers/03-salchicha-milo.webp">')

def guides_index():
    categories = [("todas", "Todas"), ("perros", "Perros"), ("gatos", "Gatos"), ("aves", "Aves"), ("pequenos", "Pequeños"), ("salud", "Salud")]
    chips = ''.join(f'<button type="button" class="filter-chip{" is-active" if i==0 else ""}" data-guide-filter="{key}" aria-pressed="{"true" if i==0 else "false"}">{name}</button>' for i,(key,name) in enumerate(categories))
    lead_slugs = ("galgo-espanol", "gato-de-interior", "periquito")
    ordered = [BY_SLUG[slug] for slug in lead_slugs] + [a for a in ARTICLES if a["slug"] not in lead_slugs]
    cards = ''.join(guide_card(a, '', CARD_TONES[i % len(CARD_TONES)]) for i,a in enumerate(ordered))
    body = f'''<section class="page-intro page-intro-guides"><div class="page-intro-inner"><span class="eyebrow-small">BIBLIOTECA MIMO</span><h1>Cuidar mejor empieza por <em>entender.</em></h1><p>Guías para las preguntas que aparecen entre una visita y otra. Elegí la especie o recorré los temas a tu ritmo.</p><div class="intro-decoration"><img src="/assets/stickers/16-cobayo-kiwi.webp" alt="" loading="lazy"></div></div></section>
<section class="library-section section-pad"><div class="library-toolbar"><div class="filter-tabs" role="group" aria-label="Filtrar guías">{chips}</div></div><div class="library-count" id="guideCount" aria-live="polite">{len(ARTICLES)} guías para explorar</div><div class="library-grid" id="libraryGrid">{cards}</div></section>'''
    return layout("Guías de cuidado", "Guías para cuidar perros, gatos, aves y pequeños animales. Información clara sobre hábitos, prevención y señales de alerta.", body, "guias", "/guias/")

def article_page(a):
    group = GROUP_LABELS[a["category"]]
    faqs = ''.join(f'<details><summary>{e(q)}<span class="faq-plus" aria-hidden="true">+</span></summary><p>{e(ans)}</p></details>' for q,ans in a['faqs'])
    sources = ''.join(f'<li><a href="{e(url)}" target="_blank" rel="noopener noreferrer">{e(label)}</a></li>' for label,url in a['sources'])
    related = [BY_SLUG[s] for s in a['related'] if s in BY_SLUG]
    related_html = f'<section class="related-section section-pad"><div class="section-heading"><div><span class="eyebrow-small">PARA SEGUIR LEYENDO</span><h2>También te puede <em>servir.</em></h2></div></div><div class="related-grid">{"".join(guide_card(x) for x in related)}</div></section>' if related else ''
    body = f'''<article><header class="article-hero tone-{GROUP_COLORS[a['category']]}"><div class="article-hero-inner"><div class="article-hero-copy"><nav class="breadcrumbs" aria-label="Ruta"><a href="/">Inicio</a><span>/</span><a href="/guias/">Guías</a><span>/</span><span>{group}</span></nav><span class="eyebrow-small">GUÍA MIMO · {group.upper()}</span><h1>{e(a['title'])}</h1><p>{e(a['deck'])}</p><a class="article-jump" href="#lectura">Empezar a leer</a></div><div class="article-hero-art"><span></span><img src="/assets/stickers/{a['image']}" alt="" fetchpriority="high"></div></div></header>
<div class="article-main" id="lectura"><div class="article-sidebar"><span>EN ESTA GUÍA</span><ol>{''.join(f'<li><a href="#parte-{i}">{e(h)}</a></li>' for i,(h,_) in enumerate(a['sections'],1))}<li><a href="#dudas">Preguntas frecuentes</a></li></ol><a href="/guias/">Volver a todas las guías</a></div><div class="article-body"><p class="article-lead">{e(a['intro'])}</p><div class="article-meta"><span>Por Mimo Veterinaria</span><span>Actualizado el 25 de septiembre de 2026</span></div>{''.join(f'<section class="reading-section" id="parte-{i}"><h2>{e(h)}</h2><p>{e(text)}</p></section>' for i,(h,text) in enumerate(a['sections'],1))}<section class="article-faq" id="dudas"><h2>Preguntas frecuentes</h2><div class="faq-list">{faqs}</div></section><div class="source-box"><h2>Fuentes para seguir leyendo</h2><ul>{sources}</ul><p>Esta guía ofrece información general. No reemplaza una consulta veterinaria ni permite diagnosticar a distancia.</p></div></div></div></article>{related_html}<section class="article-contact"><div><h2>{e(a["cta"][0])}</h2><p>{e(a["cta"][1])}</p></div><a class="button button-pink" href="{e(wa_url('Hola, Mimo. Leí la guía sobre '+a['title']+' y quisiera consultar por mi animal.'))}" target="_blank" rel="noopener noreferrer">Escribir por WhatsApp</a></section>'''
    json_ld = {"@context":"https://schema.org","@type":"Article","headline":a["title"],"description":a["deck"],"image":f"{SITE_URL}/assets/stickers/{a['image']}" if SITE_URL else f"/assets/stickers/{a['image']}","author":{"@type":"Organization","name":"Mimo Veterinaria"},"dateModified":"2026-09-25T00:00:00-03:00","publisher":{"@type":"Organization","name":"Mimo Veterinaria"}}
    if SITE_URL: json_ld["mainEntityOfPage"] = SITE_URL + article_url(a['slug'])
    extra = '<script type="application/ld+json">'+json.dumps(json_ld, ensure_ascii=False).replace('</','<\\/')+'</script>'
    return layout(a['title'], a['deck'], body, "guias", article_url(a['slug']), extra)

def attention():
    body = f'''<section class="page-intro page-intro-attention"><div class="page-intro-inner"><span class="eyebrow-small">EL CONSULTORIO</span><h1>Venís con preguntas. <em>Empezamos por escucharlas.</em></h1><p>Conocer a tu animal y lo que cambió en su rutina es el primer paso para cuidarlo bien.</p><div class="intro-decoration"><img src="/assets/stickers/04-golden-miel.webp" alt="" loading="lazy"></div></div></section>
<section class="attention-body section-pad"><div class="attention-lead"><span class="eyebrow-small">EN MIMO</span><h2>La atención tiene tiempo para cada historia.</h2><p>Una visita puede empezar por un síntoma, una vacuna pendiente o una pregunta sobre lo que viene. Queremos que salgas entendiendo qué observamos y cuáles son los próximos pasos.</p></div><div class="care-notes attention-notes" aria-label="Servicios veterinarios"><article class="care-note"><span class="note-pin" aria-hidden="true"></span><h3>Consulta general</h3><p>Revisión clínica y conversación sobre alimentación, comportamiento, crecimiento o cambios que te preocupan.</p></article><article class="care-note"><span class="note-pin" aria-hidden="true"></span><h3>Prevención</h3><p>Controles, vacunas y cuidado antiparasitario según la especie, la edad y la forma de vida de cada animal.</p></article><article class="care-note"><span class="note-pin" aria-hidden="true"></span><h3>Castraciones</h3><p>Una decisión que merece información clara. La evaluación previa y los cuidados posteriores forman parte de la consulta.</p></article></div></section>
<section class="visit-note"><div><span class="eyebrow-small">ANTES DE VENIR</span><h2>Ayuda traer una pequeña historia.</h2><p>Libreta sanitaria, medicaciones, alimento habitual y una nota sobre lo que observaste. Si se trata de un ave o un animal pequeño, contanos su especie antes de coordinar.</p><a class="button button-dark" href="/contacto/">Ver horarios y ubicación</a></div><img id="visitAnimal" src="/assets/stickers/18-loro-lima.webp" alt="" loading="lazy" decoding="async"></section>'''
    return layout("Atención veterinaria", "Consulta general, prevención y castraciones para animales de compañía en Los Polvorines.", body, "atencion", "/atencion/")

def contact():
    body = f'''<section class="page-intro page-intro-contact"><div class="page-intro-inner"><span class="eyebrow-small">MIMO VETERINARIA</span><h1>Estamos para cuidar <em>a tu compañero.</em></h1><p>Acercate a conocernos en Los Polvorines. Podés venir durante nuestro horario de atención o escribirnos para reservar.</p></div></section>
<section class="contact-body section-pad"><div class="contact-main"><span class="eyebrow-small">HORARIO DE ATENCIÓN</span><h2>Lunes a viernes, de 10 a 18 h.</h2><p>Podés acercarte sin turno previo o contactarte por WhatsApp para reservar un turno.</p><a class="button button-pink" href="{e(wa_url('Hola, Mimo. Quisiera reservar un turno para mi compañero.'))}" target="_blank" rel="noopener noreferrer">Abrir WhatsApp</a></div><div class="contact-aside"><div class="contact-location">{svg_icon('location',25)}<div><strong>Nos encontrás en Los Polvorines</strong><p>Partido de Malvinas Argentinas, provincia de Buenos Aires.</p></div></div><div class="contact-small"><span>SI HAY UNA URGENCIA</span><p>Ante dificultad para respirar, convulsiones, un accidente o un animal muy decaído, buscá atención veterinaria de urgencia sin esperar una respuesta por mensaje.</p></div></div></section>'''
    return layout("Contacto", "Consultas y turnos por WhatsApp para Mimo Veterinaria en Los Polvorines, Buenos Aires.", body, "contacto", "/contacto/")

def information():
    body = '''<section class="page-intro page-intro-legal"><div class="page-intro-inner"><span class="eyebrow-small">TÉRMINOS Y CONDICIONES</span><h1>Información clara, <em>también acá.</em></h1><p>Estas condiciones explican el alcance del sitio, sus guías y las formas de contacto con Mimo Veterinaria.</p></div></section>
<div class="legal-body"><p class="legal-updated">Última actualización: 25 de septiembre de 2026.</p>
<section><h2>1. Quién publica este sitio</h2><p>Este sitio se presenta bajo el nombre Mimo Veterinaria y brinda información sobre atención veterinaria en Los Polvorines, provincia de Buenos Aires. Los datos de contacto, horarios y prestaciones publicados describen la información disponible en cada sección del sitio.</p><p>Antes de coordinar una visita, verificá por el canal de contacto que el horario y la prestación que necesitás estén disponibles.</p></section>
<section><h2>2. Aceptación y uso</h2><p>Al navegar este sitio, aceptás estas condiciones. Usalo de manera lícita y sin afectar su funcionamiento, la seguridad de otras personas ni los derechos de terceros. Si no estás de acuerdo, podés dejar de utilizarlo.</p><p>Estas condiciones se aplican al contenido de este sitio. Los servicios veterinarios que se acuerden con el profesional se rigen también por la información brindada durante la atención y por las normas que correspondan.</p></section>
<section><h2>3. Información de salud animal</h2><p>Las guías y notas tienen fines educativos y generales. Pueden ayudarte a observar hábitos, preparar preguntas y reconocer señales que ameritan atención, pero no reemplazan el examen clínico ni constituyen diagnóstico, receta o indicación de tratamiento para un animal en particular.</p><p>La especie, edad, antecedentes y estado de cada animal pueden cambiar qué cuidados necesita. No inicies, suspendas ni modifiques medicación a partir de una lectura en el sitio. Ante síntomas o cambios que te preocupen, consultá con un profesional veterinario.</p></section>
<section><h2>4. Prestaciones veterinarias</h2><p>El sitio presenta servicios de consulta general, prevención y castraciones. La indicación y realización de cualquier práctica requieren evaluación profesional y dependen de las características y condición de cada animal. La información publicada no garantiza que una prestación sea adecuada, esté disponible en una fecha determinada ni asegure un resultado clínico.</p><p>Durante la consulta, el profesional puede explicar alternativas, cuidados, riesgos y pasos posteriores para que puedas tomar decisiones informadas sobre tu compañero.</p></section>
<section><h2>5. Horarios, visitas y turnos</h2><p>El horario informado es de lunes a viernes, de 10 a 18 h. Podés acercarte sin turno previo o escribir por WhatsApp para solicitar una reserva. La disponibilidad puede variar; un mensaje enviado no confirma por sí solo un turno. La reserva queda coordinada cuando recibís confirmación del consultorio.</p><p>Si hay cambios de horario o necesitás confirmar una prestación antes de viajar, comunicate previamente por el canal indicado en Contacto.</p></section>
<section><h2>6. Situaciones de urgencia</h2><p>El sitio y WhatsApp no son servicios de emergencia ni garantizan una respuesta inmediata. Ante dificultad para respirar, convulsiones, un accidente, posible intoxicación, sangrado importante o un deterioro repentino, acudí sin demora a un centro veterinario de urgencias. No esperes una respuesta por mensaje para buscar atención.</p></section>
<section><h2>7. WhatsApp, enlaces y servicios de terceros</h2><p>Los botones de WhatsApp abren una plataforma operada por un tercero. Si elegís continuar, la aplicación o el sitio de WhatsApp se rigen por sus propias condiciones y políticas de privacidad. Mimo Veterinaria no administra esa plataforma ni puede garantizar su disponibilidad, entrega de mensajes o tiempos de respuesta.</p><p>El sitio puede enlazar fuentes externas para ampliar información. Esos sitios tienen sus propias reglas y contenidos; su inclusión no implica que Mimo Veterinaria controle o respalde todo lo que allí se publica.</p></section>
<section><h2>8. Datos personales</h2><p>La versión actual del sitio no tiene formularios, cuentas de usuario ni pagos en línea. Al abrir WhatsApp, no envíes información que no sea necesaria para tu consulta. Si decidís iniciar una conversación, los datos y mensajes que compartas serán tratados a través de la plataforma y por la cuenta destinataria conforme a las políticas aplicables.</p><p>La normativa argentina reconoce derechos de acceso, actualización, rectificación y supresión sobre los datos personales. Para saber cómo ejercerlos, consultá la <a href="https://www.argentina.gob.ar/aaip/datospersonales/derechos" target="_blank" rel="noopener noreferrer">información oficial de la AAIP</a>. Los pedidos vinculados con datos que hayas compartido deben dirigirse al responsable del tratamiento que corresponda.</p></section>
<section><h2>9. Contenidos, propiedad intelectual y disponibilidad</h2><p>Los textos, diseño, nombre e ilustraciones de este sitio están protegidos por las normas aplicables. No los reproduzcas ni los uses comercialmente sin autorización de quien tenga los derechos, salvo los usos permitidos por la ley. Los íconos de terceros conservan sus respectivas licencias; el ícono de WhatsApp utilizado en este sitio se distribuye bajo <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener noreferrer">licencia CC BY 4.0</a>.</p><p>Se procura mantener el contenido claro y actualizado, pero puede corregirse o modificarse. El acceso al sitio puede interrumpirse temporalmente por tareas técnicas o causas ajenas a su administración.</p></section>
<section><h2>10. Cambios y normativa aplicable</h2><p>Estas condiciones pueden actualizarse para reflejar cambios en el sitio o en sus canales de atención. La versión vigente estará publicada en esta página. Se interpretan conforme a las leyes de la República Argentina y no limitan los derechos irrenunciables que reconozca la normativa aplicable a consumidores y usuarios.</p><p>Podés consultar el texto actualizado de la <a href="https://www.argentina.gob.ar/normativa/nacional/638/actualizacion" target="_blank" rel="noopener noreferrer">Ley 24.240 de Defensa del Consumidor</a> y la <a href="https://www.argentina.gob.ar/normativa/nacional/64790/actualizacion" target="_blank" rel="noopener noreferrer">Ley 25.326 de Protección de Datos Personales</a>.</p></section>
<a class="quiet-link" href="/contacto/">Consultar horarios y formas de contacto</a></div>'''
    return layout("Términos y condiciones", "Términos de uso, alcance de la información veterinaria, turnos, urgencias, privacidad y enlaces de Mimo Veterinaria.", body, "", "/informacion/")

def write(path, value):
    target = OUTPUT_ROOT / path.lstrip("/")
    if path.endswith("/"): target = target / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(value, encoding="utf-8")

def main():
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    write("/index.html", home())
    write("/guias/", guides_index())
    write("/atencion/", attention())
    write("/contacto/", contact())
    write("/informacion/", information())
    for a in ARTICLES: write(article_url(a["slug"]), article_page(a))
    if SITE_URL:
        urls = ["/", "/guias/", "/atencion/", "/contacto/", "/informacion/"] + [article_url(a["slug"]) for a in ARTICLES]
        write("/sitemap.xml", '<?xml version="1.0" encoding="utf-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{e(SITE_URL+url)}</loc></url>\n' for url in urls)+'</urlset>\n')
    if OUTPUT_ROOT != ROOT:
        shutil.copytree(ROOT / "assets", OUTPUT_ROOT / "assets", dirs_exist_ok=True)
    print(f"Built {len(ARTICLES)} guides and {len(ANIMALS)} animals.")

if __name__ == "__main__": main()
