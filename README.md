# Mimo Veterinaria

Sitio estático para una veterinaria de Los Polvorines, Buenos Aires. Incluye 34 animalitos ilustrados, un carrusel con selección por especie, 44 guías con direcciones propias y páginas de atención, contacto e información del sitio. La portada y el cierre alternan animalitos automáticamente; la portada tiene un parallax suave. En celular, los servicios se recorren como notas deslizables. Las animaciones respetan la preferencia de movimiento reducido.

## Verlo en la computadora

Desde esta carpeta, ejecutar `python3 -m http.server 4175 --bind 127.0.0.1` y abrir [http://127.0.0.1:4175/](http://127.0.0.1:4175/). Conviene verlo por HTTP para que todas las rutas de las guías funcionen.

## Publicación en GitHub Pages

El repositorio `drcardenasenzo/pagina-veterinaria-dise-o-unico` publica automáticamente el sitio cuando hay cambios en `main`. El flujo de GitHub Actions genera una copia en `dist/`, adapta los enlaces a la ruta del repositorio y la publica en [drcardenasenzo.github.io/pagina-veterinaria-dise-o-unico](https://drcardenasenzo.github.io/pagina-veterinaria-dise-o-unico/).

## Completar antes de publicarlo

- Confirmar nombre, localidad, dirección, horarios, especies atendidas y servicios de la veterinaria que lo compre.
- Configurar el número real de WhatsApp en formato internacional, sin `+` ni espacios. Por ejemplo: `WHATSAPP_NUMBER=54911XXXXXXXX python3 -B build.py`. Hasta entonces, el botón abre WhatsApp con un mensaje escrito, pero sin destinatario.
- Revisar las guías clínicas con el profesional responsable. Las fuentes figuran al pie de cada artículo.
- Una vez elegido el dominio, ejecutar `SITE_URL=https://dominio.example WHATSAPP_NUMBER=54911XXXXXXXX python3 -B build.py`. Esto añade direcciones canónicas y genera `sitemap.xml`.

No se necesitan paquetes para generar ni servir el sitio. Los textos están en `content.py`, `article_expansions.py`, `article_depth.py`, `guide_enrichments.py` y `new_breed_guides.py`; los animalitos en `animals.json`, la plantilla en `build.py` y la presentación en `assets/`.

Las 13 nuevas ilustraciones de razas se muestran en WebP para reducir su peso. El carrusel presenta un único gato con guía general; las otras guías felinas siguen disponibles en la biblioteca. El ícono flotante de WhatsApp procede de Font Awesome Free 6.7.2 (CC BY 4.0); el crédito también aparece en la página de información del sitio.
