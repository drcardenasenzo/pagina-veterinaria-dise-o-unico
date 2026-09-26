"""Editorial content for the static Mimo site.

The clinical articles are general education, not a diagnosis or a treatment
plan. Sources are displayed on each page so the content can be checked before
the site is assigned to a real veterinary practice.
"""

ARTICLES = []

DOG_SOURCE = ("Manual MSD · convivir con un perro", "https://www.merckvetmanual.com/dog-owners/selecting-and-providing-a-home-for-a-dog/providing-a-home-for-a-dog")
CAT_SOURCE = ("Manual MSD · nutrición felina", "https://www.merckvetmanual.com/cat-owners/selecting-and-providing-a-home-for-a-cat/proper-nutrition-for-cats")
BIRD_SOURCE = ("Association of Avian Veterinarians · recursos para tutores", "https://www.aav.org/page/birdowners")
RABBIT_SOURCE = ("RSPCA · cuidados del conejo", "https://www.rspca.org.uk/adviceandwelfare/pets/rabbits")
SMALL_SOURCE = ("Manual MSD · salud de animales de compañía", "https://www.merckvetmanual.com/resourcespages/pet-owners-overview")
VACCINE_SOURCE = ("WSAVA · guías de vacunación", "https://wsava.org/global-guidelines/vaccination-guidelines/")

def add(slug, category, title, deck, image, intro, sections, faqs, sources, related=()):
    ARTICLES.append(dict(slug=slug, category=category, title=title, deck=deck,
                         image=image, intro=intro, sections=sections, faqs=faqs,
                         sources=sources, related=related))


# PERROS — cada perfil responde a necesidades distintas. Los nombres de los
# stickers sirven para navegar; el contenido se centra en el animal, no en una
# mascota ficticia de la clínica.
add("caniche", "perros", "Caniche: rulos, juego y una rutina que le haga bien",
    "Un compañero atento que disfruta aprender. Qué mirar en su pelo, sus paseos y sus controles.", "01-caniche-nube.webp",
    "El caniche suele estar muy pendiente de lo que ocurre en casa. Su tamaño puede variar mucho, de modo que conviene pensar su actividad, su comida y sus controles según el perro que tenés delante, y no sólo según la raza.",
    [("Los rulos necesitan constancia", "Su pelo crece y puede formar nudos cerca de las orejas, axilas y patas. Cepillarlo con suavidad y acordar una frecuencia de corte ayuda a evitar tirones y molestias. Si aparecen enrojecimiento, mal olor o rascado insistente, consultá antes de aplicar productos."),
     ("Paseos con algo para pensar", "Además de salir a caminar, puede disfrutar juegos de búsqueda, juguetes que entregan comida y consignas breves. Cambiar pequeños desafíos mantiene el interés sin convertir cada paseo en una sesión exigente."),
     ("Una mirada completa", "En los controles vale la pena revisar peso, boca, oídos y piel. Llevá una lista de cambios que hayas notado: cuánto bebe, cómo duerme y si sigue disfrutando sus actividades habituales.")],
    [("¿Un caniche chico necesita pasear?", "Sí. El tamaño no reemplaza la necesidad de moverse, explorar y relacionarse con su entorno. La duración se adapta a su edad y estado de salud."),
     ("¿Cada cuánto se corta el pelo?", "Depende del tipo de manto y de la rutina de cepillado. Un profesional de estética puede ayudarte a encontrar una frecuencia cómoda.")], [DOG_SOURCE], ("salud-dental-perros-gatos", "vacunas-perros-gatos"))

add("corgi", "perros", "Corgi: patas cortas, muchas ganas de participar",
    "Ideas para acompañar su energía y cuidar su condición corporal sin dejar de jugar.", "02-corgi-coco.webp",
    "El corgi invita a jugar por su aspecto simpático, pero es un perro activo. Su cuerpo alargado y sus patas cortas hacen especialmente importante observar cómo se mueve y mantener una condición corporal saludable.",
    [("Actividad con medida", "Los paseos frecuentes y los juegos de olfato suelen ser más útiles que concentrar toda la actividad en un rato intenso. Ajustá el esfuerzo al clima, la edad y la respuesta de tu perro."),
     ("El peso se mira, no se adivina", "Una ración que parece pequeña puede resultar excesiva cuando se suman premios y restos de comida. En consulta pueden evaluar su condición corporal y acordar porciones adecuadas."),
     ("Cambios al subir o bajar", "Si evita saltar, se detiene en escaleras o camina distinto, no lo atribuyas automáticamente a la edad. Una evaluación temprana permite entender qué ocurre y cómo ayudarlo.")],
    [("¿Puede vivir en un departamento?", "Puede adaptarse si tiene salidas, descanso y actividades diarias. Los metros de la casa no sustituyen la rutina."),
     ("¿Se le puede dar comida como premio?", "Sí, pero los premios forman parte de la alimentación del día. Conviene elegirlos y contarlos con el veterinario.")], [DOG_SOURCE], ("peso-saludable-mascotas",))

add("perro-salchicha", "perros", "Perro salchicha: cuidar la espalda en la vida diaria",
    "Un cuerpo inconfundible que necesita movimiento, juego y algunas precauciones en casa.", "03-salchicha-milo.webp",
    "El perro salchicha es curioso y suele querer estar en todos lados. Su espalda larga invita a prestar atención a la forma en que sube, baja y se mueve, sin limitarle las experiencias que disfruta.",
    [("Una casa fácil de recorrer", "Evitar saltos repetidos desde muebles altos y ofrecer superficies firmes puede hacer más amable su rutina. Si usa una rampa, enseñale a usarla de a poco y sin forzarlo."),
     ("Moverse también es cuidarse", "Mantener una actividad regular y un peso adecuado ayuda a que conserve fuerza. Los paseos tranquilos, el olfato y los juegos en el suelo son buenas formas de participar juntos."),
     ("Señales que no esperan", "Si aparece dolor evidente, dificultad para caminar, debilidad o pérdida de control de esfínteres, necesitás atención veterinaria urgente. No pruebes masajes ni medicación humana.")],
    [("¿Conviene alzarlo?", "Si tenés que levantarlo, sostené a la vez el pecho y la parte posterior para no dejar el cuerpo colgando."),
     ("¿Puede subir escaleras?", "La recomendación depende de su edad, estado físico y antecedentes. Conversalo en un control, especialmente si ya mostró molestias.")], [DOG_SOURCE], ("peso-saludable-mascotas",))

add("golden-retriever", "perros", "Golden retriever: compañía grande, rutinas claras",
    "Movimiento, cepillado y observación cotidiana para un perro que suele querer estar cerca.", "04-golden-miel.webp",
    "Convivir con un golden implica hacer lugar a un perro de mayor tamaño y a sus ganas de participar. Una rutina estable combina paseos, tiempo compartido y descanso real.",
    [("Salir y volver a bajar el ritmo", "El ejercicio se adapta a la edad: un cachorro, un adulto y un perro mayor no necesitan la misma intensidad. Evitá exigir actividad fuerte en horas de mucho calor y ofrecé agua y pausas."),
     ("Pelo, piel y oídos", "El cepillado permite retirar pelo suelto y descubrir cambios en la piel. Después de mojarse, revisá que orejas y zonas con pelo denso queden limpias y secas."),
     ("Un registro sencillo", "Anotar peso, apetito, energía y cambios en la marcha ayuda a conversar con el veterinario. En perros grandes, detectar una dificultad para levantarse o jugar merece una consulta.")],
    [("¿Cuánto ejercicio necesita?", "No hay una cifra universal. La edad, el clima y la salud definen una rutina; empezá por paseos regulares y ajustala con su veterinario."),
     ("¿Hay que raparlo en verano?", "El cuidado del manto requiere criterio. Consultá antes de hacer un corte extremo: el pelo también cumple funciones de protección.")], [DOG_SOURCE], ("golpe-de-calor-mascotas",))

add("bulldog-frances", "perros", "Bulldog francés: respirar cómodo también es bienestar",
    "Cómo organizar paseos y descanso cuando el calor o el esfuerzo pueden pesar más.", "05-bulldog-lola.webp",
    "Su cara corta es parte de su aspecto, pero la respiración no debería darse por sentada. Observá cómo respira en reposo, durante el juego y cuando hace calor; esa información ayuda a decidir qué cuidados necesita.",
    [("Paseos en momentos frescos", "Elegí horarios templados, llevá agua y permití pausas. Si el esfuerzo provoca respiración muy ruidosa, agotamiento o dificultad para recuperarse, suspendé la actividad y buscá asistencia."),
     ("Un ambiente que lo ayude", "La sombra y la ventilación son importantes. Nunca lo dejes dentro de un auto estacionado, aunque el día parezca suave. Mantener un peso adecuado también facilita el movimiento."),
     ("Consultas que vale la pena hacer", "Preguntá por evaluación respiratoria, cuidado de pliegues y salud dental. No todos los bulldogs franceses tienen las mismas necesidades; una revisión individual evita normalizar molestias.")],
    [("¿Es normal que ronque?", "Los ruidos pueden ser frecuentes, pero no sirven para descartar un problema. Consultá si son intensos, nuevos o se acompañan de fatiga."),
     ("¿Puede pasear en verano?", "Sí, con horarios frescos y esfuerzos acordes a su tolerancia. Ante signos de sobrecalentamiento, buscá atención veterinaria.")], [DOG_SOURCE], ("golpe-de-calor-mascotas",))

add("dalmata", "perros", "Dálmata: energía, agua y una rutina con propósito",
    "Un perfil para pensar la actividad diaria y observar hábitos que cuentan mucho.", "06-dalmata-pipa.webp",
    "Las manchas hacen que sea fácil reconocerlo; su bienestar se entiende mirando el día completo. Un dálmata necesita oportunidades de movimiento, aprendizaje y descanso, ajustadas a su edad.",
    [("Actividad que se pueda sostener", "Más que una salida extraordinaria de vez en cuando, buscá regularidad. Los juegos de olfato, el paseo y las tareas compartidas pueden combinarse sin llevarlo al agotamiento."),
     ("Agua y hábitos de eliminación", "Mantené agua fresca disponible y observá si cambia la frecuencia con que orina, si hace esfuerzo o si aparece sangre. Esos cambios requieren consulta; no esperes a ver si se resuelven solos."),
     ("Piel y oído", "El pelo corto facilita revisar irritaciones, parásitos y pequeñas lesiones. Incluí esos hallazgos en sus controles, junto con peso y salud bucal.")],
    [("¿Necesita correr todos los días?", "Necesita actividad adecuada, pero la intensidad se adapta a cada individuo. También cuenta la estimulación mental."),
     ("¿Cuándo consultar por la orina?", "Ante dolor, sangre, intentos frecuentes o dificultad para orinar, buscá atención veterinaria pronto.")], [DOG_SOURCE], ("pulgas-y-garrapatas",))

add("husky-siberiano", "perros", "Husky: mucha curiosidad y un abrigo abundante",
    "Convivencia, actividad y calor: lo que conviene planear antes de salir.", "07-husky-nala.webp",
    "El husky suele disfrutar el movimiento y explorar. Su manto abundante no convierte al calor en un detalle menor: en días cálidos conviene ajustar horarios y observar su respuesta al ejercicio.",
    [("Salidas que no dependan del mediodía", "Elegí momentos frescos, agua y pausas. Revisá la temperatura del suelo con la mano antes de caminar sobre superficies calientes."),
     ("Cepillado sin apuro", "El pelo cambia con las estaciones. Un cepillado regular ayuda a retirar pelo suelto y a revisar la piel. Evitá decidir un rapado por tu cuenta; consultá sobre el manejo apropiado del manto."),
     ("Seguridad al explorar", "Un espacio bien cerrado, identificación y paseos supervisados son parte del cuidado. Sumá actividades de olfato y aprendizaje para canalizar su curiosidad.")],
    [("¿Le hace mal vivir en Buenos Aires?", "Puede vivir en climas más cálidos si su entorno y actividad se adaptan. El calor intenso requiere especial cuidado."),
     ("¿Cuándo frenar el paseo?", "Si respira con dificultad, se tambalea, está muy decaído o no se recupera tras descansar, buscá atención veterinaria.")], [DOG_SOURCE], ("golpe-de-calor-mascotas",))

add("shiba-inu", "perros", "Shiba inu: independencia con buenos acuerdos",
    "Paseos, límites seguros y una convivencia que respete su forma de comunicarse.", "08-shiba-kiko.webp",
    "El shiba inu puede ser reservado y tomar distancia antes de acercarse. Conocer esa forma de expresarse ayuda a construir una rutina amable, sin convertir cada encuentro en una exigencia.",
    [("Paseos con margen para elegir", "Dejale tiempo para olfatear y observar. Un arnés cómodo y una correa segura permiten disfrutar la salida sin depender de que responda siempre a un llamado."),
     ("Leer señales pequeñas", "Un cuerpo rígido, evitar el contacto o alejarse son formas de pedir espacio. En vez de forzar caricias, ofrecé opciones y reforzá las interacciones que elige."),
     ("Cuidar lo cotidiano", "Cepillado, revisión de piel, dientes y uñas forman parte de una rutina predecible. Si un cambio de conducta aparece de golpe, primero descartá dolor o enfermedad.")],
    [("¿Es un perro para vivir suelto?", "Incluso un perro entrenado puede distraerse o asustarse. En lugares abiertos, priorizá espacios seguros y las normas locales."),
     ("¿Por qué evita que lo toquen?", "Puede ser una preferencia, estrés o dolor. Si es un cambio nuevo, pedí una evaluación.")], [DOG_SOURCE], ("salud-dental-perros-gatos",))

add("beagle", "perros", "Beagle: dejar que la nariz también salga a pasear",
    "Un perro explorador necesita olfato, límites seguros y atención a las porciones.", "09-beagle-tito.webp",
    "Para un beagle, olfatear es parte importante del paseo. Darle tiempo para hacerlo puede enriquecer la salida tanto como caminar una distancia mayor.",
    [("Buscar sin perder seguridad", "Los juegos de rastreo en casa son una forma simple de ofrecerle actividad. Afuera, una correa segura ayuda cuando un olor le resulta más interesante que cualquier llamado."),
     ("La comida no es el único premio", "Registrar porciones y golosinas evita que los extras pasen inadvertidos. También podés premiar con juego, exploración o atención, según lo que disfrute."),
     ("Oídos y hábitos", "Durante el cepillado mirá la parte externa de las orejas. Mal olor, dolor, secreción o sacudidas de cabeza justifican una consulta; evitá limpiar en profundidad sin indicación.")],
    [("¿Necesita juegos de olfato si ya pasea?", "Pueden complementar el paseo y ofrecerle una actividad tranquila en casa."),
     ("¿Cómo sé si aumentó de peso?", "Pesalo y pedí una evaluación de condición corporal. La comparación con fotos antiguas no siempre alcanza.")], [DOG_SOURCE], ("peso-saludable-mascotas",))

add("pitbull", "perros", "Perros tipo pitbull: mirar al individuo, no la etiqueta",
    "Convivencia responsable, movimiento y salud pensados para el perro real.", "10-pitbull-bruno.webp",
    "El término «pitbull» se usa para perros de distintos orígenes y aspectos. Ninguna etiqueta describe por sí sola su conducta, su salud o lo que necesita en casa. Vale más observarlo como individuo.",
    [("Rutinas que enseñan", "Paseos previsibles, juego y aprendizaje con refuerzo positivo ayudan a construir buenos hábitos. Presentá personas, perros y entornos nuevos de forma gradual, sin forzar interacciones."),
     ("Fuerza con cuidado", "Un arnés bien ajustado, correa resistente e identificación permiten manejar la salida con tranquilidad. La condición física se construye de a poco y siempre según su edad y salud."),
     ("Señales propias", "Prestá atención a piel, dientes, peso y cambios de ánimo. Si evita movimientos, se rasca mucho o se muestra distinto, una consulta puede encontrar la causa.")],
    [("¿La raza define cómo se comporta?", "No. La conducta depende de muchos factores, entre ellos experiencias, ambiente, salud y aprendizaje."),
     ("¿Cómo organizar un encuentro con otro perro?", "Elegí un contexto tranquilo, mantené distancia inicial y respetá señales de ambos. Pedí ayuda profesional si hay miedo o tensión.")], [DOG_SOURCE], ("pulgas-y-garrapatas",))

add("perro-mestizo", "perros", "Perro mestizo: una guía hecha para el que tenés en casa",
    "El cuidado empieza por conocer su tamaño, su historia y sus hábitos, no por buscarle una raza.", "21-perro-mestizo.webp",
    "Un perro mestizo puede combinar rasgos muy distintos. Esa singularidad es una buena razón para registrar sus necesidades reales: cómo se mueve, qué le entusiasma y qué le cuesta.",
    [("Tu punto de partida", "En una consulta inicial pueden evaluar edad aproximada, peso, boca, piel y estado general. Si llegó hace poco, llevá toda la información disponible sobre vacunas, tratamientos y alimentación."),
     ("Una rutina propia", "Organizá paseos y juego según su energía, sin compararlo con perros de tamaño parecido. Algunos necesitan más pausas; otros disfrutan desafíos de olfato y aprendizaje."),
     ("Cambios que cuentan", "Anotar apetito, sed, sueño, materia fecal y comportamiento facilita detectar algo fuera de lo habitual. Es una herramienta sencilla, especialmente cuando todavía se están conociendo.")],
    [("¿Necesito saber su mezcla para cuidarlo bien?", "No. La evaluación individual y los controles periódicos dan información más útil para decidir su cuidado."),
     ("¿Puedo cambiarle la comida al adoptarlo?", "Conviene conocer qué comía antes y consultar cómo hacer una transición gradual, sobre todo si hay síntomas digestivos.")], [DOG_SOURCE], ("vacunas-perros-gatos",))

add("chihuahua", "perros", "Chihuahua: pequeño de tamaño, completo de necesidades",
    "Paseos, abrigo, boca y trato respetuoso para un compañero diminuto.", "24-chihuahua.webp",
    "Ser pequeño no lo convierte en un accesorio: un chihuahua necesita explorar, descansar, aprender y poder decidir cuándo quiere contacto. Mirarlo a su altura cambia la manera de acompañarlo.",
    [("Salidas acordes a su cuerpo", "Los paseos cortos y frecuentes pueden ser más cómodos que una única salida extensa. En días fríos o calurosos, observá cómo responde y ajustá el horario."),
     ("Cuidado al levantarlo", "Sostené el pecho y la parte posterior del cuerpo. Avisá a niñas y niños que sentarse cerca y esperar a que se acerque es más seguro que alzarlo sin permiso."),
     ("La boca también importa", "Los dientes de un perro pequeño merecen controles regulares. Preguntá cómo incorporar higiene bucal y consultá si hay mal aliento persistente, dolor o dificultad para comer.")],
    [("¿Debe pasear si vive adentro?", "Sí. Puede disfrutar de salidas adaptadas a su edad y estado de salud, además de juegos en casa."),
     ("¿Por qué tiembla?", "Puede haber distintas causas, desde temperatura hasta dolor o estrés. Si es nuevo o intenso, consultá.")], [DOG_SOURCE], ("salud-dental-perros-gatos",))


# GATOS — los colores de los stickers no se convierten en páginas casi iguales.
add("gato-primer-ano", "gatos", "El primer año de un gato: preparar la casa y conocerlo",
    "Arenero, juego, alimentación y controles para acompañar una etapa de muchos cambios.", "11-gato-oli.webp",
    "La llegada de un gatito mezcla descubrimiento y dudas. Un entorno tranquilo y predecible le permite explorar a su ritmo y te ayuda a reconocer pronto qué hábitos son normales para él.",
    [("Un lugar seguro para empezar", "Prepará un espacio con agua, comida, arenero, escondite y lugar para descansar. Dejá que conozca el resto de la casa de forma gradual y cuidá ventanas, balcones, cables y objetos pequeños."),
     ("Juego y alimentación", "Los juegos breves con cañas o juguetes apropiados ayudan a explorar sin convertir manos y pies en presas. Elegí alimento completo para su etapa de vida y consultá antes de cambiarlo."),
     ("La primera visita", "Llevá los antecedentes disponibles y preguntá por vacunas, control de parásitos, identificación y momento adecuado para castración. El plan se define según edad, historia y estilo de vida.")],
    [("¿Dónde pongo el arenero?", "En un lugar accesible y tranquilo, separado del agua y la comida. Observá si lo usa con comodidad."),
     ("¿Puede conocer a otro gato enseguida?", "Es mejor hacer una presentación gradual, con espacios y recursos separados al principio.")], [CAT_SOURCE, VACCINE_SOURCE], ("gato-de-interior", "vacunas-perros-gatos"))

add("gato-de-interior", "gatos", "Gatos de interior: una casa que también se pueda explorar",
    "Alturas, escondites, juego y descanso para que su mundo no termine en el sillón.", "25-gato-atigrado.webp",
    "Vivir adentro puede proteger a un gato de muchos peligros exteriores, pero necesita oportunidades para hacer cosas de gato: trepar, mirar, esconderse, rascar y jugar.",
    [("Más opciones que metros", "Una repisa segura, rascadores estables y escondites ofrecen distintos usos de una misma habitación. Ubicá recursos en lugares donde pueda elegir estar acompañado o solo."),
     ("Jugar como cazar", "Mové un juguete de forma variada, dejá que lo alcance y terminá antes de que pierda interés. Rotar juguetes mantiene la novedad sin llenar la casa de objetos."),
     ("Cambios de comportamiento", "Si deja de jugar, se esconde de repente o modifica su manera de usar el arenero, no lo atribuyas sólo a aburrimiento. Conviene descartar una causa física.")],
    [("¿Una ventana alcanza para entretenerlo?", "Mirar afuera puede gustarle, pero también necesita juego, movimiento y lugares para descansar."),
     ("¿Y si vive con otro gato?", "Cada uno debe poder acceder a recursos y retirarse sin quedar bloqueado por el otro.")], [CAT_SOURCE], ("gato-agua-y-arenero",))

add("gato-agua-y-arenero", "gatos", "Agua y arenero: dos pistas sobre la salud de tu gato",
    "Pequeños cambios cotidianos pueden contar mucho antes de que se vea enfermo.", "13-gato-canela.webp",
    "Los gatos pueden mantener una rutina aparentemente normal mientras algo cambia. Mirar cuánto beben y cómo usan el arenero es una forma simple de conocerlos mejor.",
    [("Agua en lugares cómodos", "Ofrecé agua fresca en recipientes limpios y ubicaciones tranquilas. Algunos gatos prefieren varios puntos de agua; la preferencia individual importa más que una regla única."),
     ("Un arenero que invite a usarlo", "Debe ser accesible, limpio y suficientemente amplio. Cambiar de golpe la ubicación o el tipo de arena puede alterar su uso; observá qué le resulta cómodo."),
     ("Cuándo consultar", "Hacer fuerza sin orinar, entrar muchas veces al arenero, vocalizar de dolor o ver sangre son motivos de atención veterinaria urgente. También merecen consulta los cambios persistentes en sed o eliminación.")],
    [("¿Es normal que no vea a mi gato tomar agua?", "Algunos beben en horarios discretos. Importa observar cambios respecto de su patrón habitual y conversar cualquier duda en consulta."),
     ("¿Qué hago si orina fuera del arenero?", "No lo castigues. Revisá el entorno y consultá para descartar causas médicas.")], [CAT_SOURCE], ("gato-de-interior",))

add("gato-mayor", "gatos", "Un gato mayor sigue teniendo cosas para descubrir",
    "Adaptar la casa y registrar cambios ayuda a cuidar su comodidad y autonomía.", "14-gato-copito.webp",
    "Al envejecer, un gato puede cambiar de ritmo sin perder su curiosidad. Vale la pena facilitarle lo cotidiano y no suponer que todo cambio es «normal por la edad».",
    [("Accesos más sencillos", "Un escalón estable hacia su lugar favorito, superficies antideslizantes y recursos cerca de donde descansa pueden reducir esfuerzos innecesarios. El arenero debe seguir siendo fácil de entrar."),
     ("Observar sin invadir", "Anotá peso, apetito, sed, uso del arenero, aseo y ganas de jugar. Un cambio gradual puede pasar inadvertido si no se mira en conjunto."),
     ("Controles con preguntas", "Llevá esas observaciones al veterinario. Puede valorar dolor, boca, movilidad y otras necesidades según el caso, y ayudarte a adaptar la rutina.")],
    [("¿Dormir más significa que está bien?", "Puede cambiar el descanso con la edad, pero un aumento marcado o acompañado de otros cambios merece consulta."),
     ("¿Todavía necesita jugar?", "Sí, si lo disfruta. Ofrecé juegos suaves y breves que pueda elegir.")], [CAT_SOURCE], ("salud-dental-perros-gatos",))


# AVES — fuentes de veterinaria aviar; no se presupone que una clínica pequeña
# real tenga especialistas en aves sin confirmarlo antes de publicarse.
add("loro", "aves", "Loros en casa: cuidar la curiosidad todos los días",
    "Alimentación, juego y señales discretas que conviene aprender a observar.", "18-loro-lima.webp",
    "Un loro necesita mucho más que una jaula vistosa. Su bienestar depende de una dieta adecuada para su especie, oportunidades para explorar y vínculos que respeten su comportamiento.",
    [("Una dieta para ese loro", "Las semillas solas no suelen aportar una alimentación equilibrada. La combinación apropiada de alimento formulado y otros componentes varía según especie y estado de salud: definila con un veterinario con experiencia en aves."),
     ("Buscar, manipular, elegir", "Ofrecé perchas de distintos tamaños, juguetes seguros y actividades de búsqueda de alimento. Rotar objetos y permitir descanso evita que la estimulación se vuelva agobiante."),
     ("Cambios silenciosos", "Las aves pueden ocultar enfermedad. Menos apetito, plumas erizadas, quietud inusual, cambio en las heces o dificultad respiratoria merecen consulta rápida.")],
    [("¿Cuánto vive un loro?", "Depende muchísimo de la especie. Antes de adoptar, identificá exactamente cuál es y consultá su expectativa de vida y compromiso de cuidado."),
     ("¿Puede salir de la jaula?", "Necesita actividad supervisada en un ambiente seguro, sin ventiladores en marcha, ventanas abiertas ni fuentes de humo.")], [BIRD_SOURCE], ("periquito",))

add("ninfa", "aves", "Ninfas: compañía, vuelo y un entorno tranquilo",
    "Cómo pensar sus espacios y reconocer cuándo algo dejó de ser habitual.", "19-ninfa-pina.webp",
    "La ninfa o carolina suele integrarse mucho a la vida de una casa. Un ambiente seguro y rutinas previsibles ayudan a que pueda moverse, descansar y expresar sus conductas naturales.",
    [("Espacio para moverse", "Además de una jaula adecuada, necesita oportunidades de vuelo o movimiento supervisado. Revisá vidrios, cables, ventiladores y otros animales antes de dejarla salir."),
     ("Alimentación sin improvisar", "Una dieta basada sólo en semillas puede ser insuficiente. Pedí orientación para elegir alimento apropiado y hacer cualquier cambio de forma gradual."),
     ("Mirar la rutina diaria", "Registrar apetito, postura, vocalizaciones y heces ayuda a detectar un problema. Una ninfa quieta, embolada o que deja de comer requiere atención veterinaria.")],
    [("¿Puede vivir sola?", "Sus necesidades sociales son importantes. La compañía humana, la de otras aves y el contexto de cada hogar deben evaluarse con cuidado."),
     ("¿Es normal que tire plumas?", "La muda es posible, pero arrancarse plumas o dejar zonas despobladas merece una evaluación.")], [BIRD_SOURCE], ("loro",))

add("periquito", "aves", "Periquitos: pequeños, activos y atentos a su ambiente",
    "Una guía inicial sobre movimiento, compañía, alimentación y señales de alerta.", "22-periquito.webp",
    "Un periquito ocupa poco espacio en la foto, pero necesita posibilidades reales de volar, explorar y relacionarse. La calidad del ambiente importa más que los adornos de la jaula.",
    [("Jaula, perchas y salida segura", "Elegí un espacio que le permita moverse y perchas apropiadas para sus patas. Cuando salga, cerrá ventanas, cubrí riesgos y supervisá el entorno."),
     ("Comer bien no es sólo picotear", "Una mezcla de semillas no garantiza todos los nutrientes. Un veterinario aviar puede orientar una dieta equilibrada y explicar cómo modificarla sin que deje de comer."),
     ("Señales para actuar", "Si está embolado, deja de comer, permanece en el piso de la jaula o cambia su respiración, buscá asistencia sin esperar a ver si mejora solo.")],
    [("¿Cuánto vive un periquito?", "Puede acompañarte durante años; la longevidad varía con genética, alimentación y cuidados. Antes de adoptarlo, pensá en ese compromiso a largo plazo."),
     ("¿Necesita juguetes?", "Sí, siempre que sean seguros y no ocupen todo el espacio disponible para moverse.")], [BIRD_SOURCE], ("canario",))

add("canario", "aves", "Canarios: escuchar su canto y mirar mucho más",
    "Alimentación, descanso y observación para una especie sensible a su entorno.", "23-canario.webp",
    "El canto llama la atención, pero la salud de un canario se observa también en sus movimientos, su apetito, las heces y la manera de descansar. Cambios pequeños pueden ser relevantes.",
    [("Un ambiente predecible", "Ubicá su espacio lejos de corrientes de aire, humo y cambios bruscos de temperatura. Necesita perchas y lugar para moverse, no una jaula llena de adornos."),
     ("Rutina de comida y agua", "Mantené agua limpia y consultá qué alimentación corresponde a su especie y etapa. Evitá asumir que toda mezcla comercial cubre sus necesidades."),
     ("Cuando el canto cambia", "Puede haber muchas razones para que vocalice menos. Si se suma quietud, plumas erizadas, dificultad respiratoria o menos apetito, buscá atención veterinaria.")],
    [("¿Tiene que cantar siempre?", "No. La vocalización cambia con la edad, el ambiente y otros factores. Importa mirar el conjunto de su conducta."),
     ("¿Se puede acercar la jaula a la cocina?", "Es mejor evitar humo, aerosoles y vapores de cocina; las aves son sensibles a la calidad del aire.")], [BIRD_SOURCE], ("periquito",))


# PEQUEÑOS ANIMALES
add("conejo", "pequenos", "Conejos: espacio, heno y un cuerpo delicado",
    "Una vida activa y tranquila necesita mucho más que una jaula.", "15-conejo-pompon.webp",
    "Un conejo puede ser curioso y sociable, pero también necesita esconderse y elegir cuándo acercarse. Preparar su ambiente es parte central del cuidado.",
    [("Heno y agua siempre disponibles", "El heno de buena calidad es una base importante de su alimentación. La proporción de otros alimentos depende de su edad y estado de salud; consultá antes de hacer cambios bruscos."),
     ("Más suelo para recorrer", "Necesita espacio para saltar, estirarse y explorar, además de un refugio. Protegé cables y plantas, y evitá pisos resbaladizos."),
     ("Comer y hacer heces importa mucho", "Si deja de comer, produce menos heces o parece dolorido, buscá atención veterinaria urgente. No esperes a que pase solo.")],
    [("¿Le gusta que lo alcen?", "Muchos conejos prefieren interactuar a nivel del suelo. Si debés levantarlo, pedí orientación para sostenerlo con seguridad."),
     ("¿Cuánto vive?", "Puede ser un compromiso de muchos años. La expectativa cambia según tamaño, genética y cuidados; conversalo antes de adoptar.")], [RABBIT_SOURCE], ("cobayo",))

add("cobayo", "pequenos", "Cobayos: compañía, refugios y una dieta bien pensada",
    "Qué necesita este animal social para moverse, comer y sentirse seguro.", "16-cobayo-kiwi.webp",
    "El cobayo o conejillo de Indias es un animal social. Su espacio debe permitirle caminar, esconderse y descansar sin competir por todos los recursos.",
    [("Heno, agua y vitamina C", "Necesita heno, agua limpia y una alimentación adecuada que aporte vitamina C. No todos los alimentos sirven; pedí una pauta específica antes de suplementar por tu cuenta."),
     ("Un piso que cuide sus patas", "El recinto debe tener superficie firme, ventilación y limpieza regular. Ofrecé refugios y evitá suelos de rejilla que puedan lastimarlo."),
     ("Cambios para tomar en serio", "Menos apetito, pérdida de peso, dificultad para respirar o cambios en las heces requieren consulta. Como animal presa, puede ocultar malestar.")],
    [("¿Puede vivir solo?", "La compañía de otros cobayos compatibles suele ser importante. La presentación y la organización del espacio necesitan cuidado."),
     ("¿Sirve una jaula pequeña?", "Necesita lugar para desplazarse y recursos separados. Evaluá el tamaño real del espacio con un profesional informado en la especie.")], [("Manual MSD · alojamiento y nutrición del cobayo", "https://www.merckvetmanual.com/exotic-and-laboratory-animals/guinea-pigs/housing-and-nutrition-of-guinea-pigs")], ("conejo",))

add("hamster", "pequenos", "Hámsters: una vida activa cuando la casa se apaga",
    "Descanso diurno, refugio y oportunidades para excavar y explorar.", "17-hamster-mani.webp",
    "Los hámsters suelen estar más activos al anochecer. Respetar ese ritmo y ofrecer un ambiente que les permita esconderse hace la convivencia más amable.",
    [("Un espacio para sus conductas", "Necesita sustrato apropiado para excavar, refugios y una rueda de tamaño adecuado que le permita correr con la espalda cómoda. Evitá accesorios inseguros o difíciles de limpiar."),
     ("Manipular sin asustar", "Despertarlo bruscamente o agarrarlo desde arriba puede asustarlo. Acercá la mano despacio, dejá que se aproxime y supervisá cualquier salida del recinto."),
     ("Observar comida y movimiento", "Revisá cada día agua, alimento, heces y actividad. Una disminución marcada de apetito, diarrea o dificultad para moverse merece atención veterinaria.")],
    [("¿Es una mascota para chicos pequeños?", "Necesita un adulto responsable que cuide su ambiente y respete sus horarios de descanso."),
     ("¿Debe vivir con otro hámster?", "Depende de la especie. Algunas son solitarias y juntarlas puede ser peligroso; identificá cuál tenés antes de decidir.")], [SMALL_SOURCE], ("cobayo",))

add("tortuga", "pequenos", "Tortugas: primero la especie, después el terrario",
    "Una tortuga de agua y una terrestre no necesitan la misma casa ni la misma alimentación.", "20-tortuga-lento.webp",
    "Decir «tengo una tortuga» es apenas el principio. Identificar su especie es indispensable para organizar temperatura, luz, espacio y comida adecuados.",
    [("Un hábitat que funcione", "Según la especie puede requerir agua, zona seca, calor y luz especial. Una caja o un recipiente pequeño no cubren por sí solos esas necesidades. Consultá con un profesional con experiencia en reptiles."),
     ("Comida sin recetas universales", "Las dietas cambian mucho entre especies y etapas. Evitá basarte en un único alimento o en consejos para otra tortuga que se ve parecida."),
     ("Señales para consultar", "Ojos cerrados, falta de apetito, respiración anormal, caparazón alterado o poca actividad sostenida requieren evaluación. No administres medicación de otras mascotas.")],
    [("¿Cuánto vive una tortuga?", "Muchas especies pueden vivir décadas. El dato útil depende de la especie exacta y de sus condiciones de cuidado."),
     ("¿Puede pasar el día al sol?", "La exposición, sombra y temperatura deben planificarse según especie; el sobrecalentamiento también es un riesgo.")], [SMALL_SOURCE], ("conejo",))


# CUIDADOS Y SALUD — no incluyen dosis, diagnósticos a distancia ni indicaciones
# que deban sustituir una evaluación clínica.
add("vacunas-perros-gatos", "salud", "Vacunas en perros y gatos: un plan para cada vida",
    "Qué llevar a la consulta y por qué el calendario depende de la historia de cada animal.", "01-caniche-nube.webp",
    "Las vacunas ayudan a prevenir enfermedades importantes, pero el plan no se resuelve con una lista universal. Edad, antecedentes, estilo de vida y riesgos locales importan.",
    [("Empezar por los datos", "Llevá libreta sanitaria y toda constancia previa. Si adoptaste y no conocés el historial, decilo con claridad: el veterinario puede organizar un plan desde esa información incompleta."),
     ("Una conversación, no sólo una aplicación", "Aprovechá la visita para hablar de alimentación, parásitos, crecimiento, convivencia con otros animales y viajes. La revisión del paciente es parte de la decisión."),
     ("Después de la consulta", "Guardá los registros y anotá la próxima fecha indicada. Si observás un síntoma que te preocupa tras la vacunación, contactá a la veterinaria que lo atendió.")],
    [("¿Todos reciben las mismas vacunas?", "No. Hay vacunas esenciales y otras que se indican según riesgo individual y contexto."),
     ("¿Puedo reiniciar un plan perdido por mi cuenta?", "Llevá lo que tengas de documentación y pedí que un veterinario indique cómo continuar.")], [VACCINE_SOURCE], ("gato-primer-ano", "perro-mestizo"))

add("salud-dental-perros-gatos", "salud", "La boca también se cuida: dientes en perros y gatos",
    "Señales que conviene mirar y una higiene que se aprende paso a paso.", "24-chihuahua.webp",
    "Comer con ganas no siempre significa que la boca esté cómoda. La salud dental forma parte de los controles de perros y gatos y merece atención antes de que el dolor sea evidente.",
    [("Qué observar", "Mal aliento persistente, encías inflamadas, dificultad para masticar, salivación diferente o rechazo al contacto en la cara son motivos para consultar. No intentes raspar sarro en casa."),
     ("Crear una rutina amable", "La higiene se introduce gradualmente, con productos adecuados para animales y sesiones breves. Un veterinario puede mostrarte cómo empezar sin forzar la boca."),
     ("Revisión profesional", "Algunos problemas están debajo de la encía y no se ven a simple vista. La evaluación define si hacen falta estudios o tratamiento; un premio dental no reemplaza esa revisión.")],
    [("¿Puedo usar pasta de dientes humana?", "No. Pedí un producto formulado para animales y orientación sobre su uso."),
     ("¿Si come bien, no le duele?", "Los animales pueden seguir comiendo aun con molestias. Mirá también cómo mastican y su comportamiento.")], [("AVMA · cuidado dental de mascotas", "https://ebusiness.avma.org/files/productdownloads/petdentalcare_brochure.pdf")], ("chihuahua", "gato-mayor"))

add("peso-saludable-mascotas", "salud", "Peso saludable: mirar más allá de la balanza",
    "Porciones, premios y condición corporal en perros y gatos.", "02-corgi-coco.webp",
    "El número de la balanza es útil, pero no cuenta toda la historia. El veterinario puede valorar la condición corporal, la musculatura y la evolución de cada animal.",
    [("Todo lo que come cuenta", "Anotá alimento habitual, premios, bocados compartidos y suplementos. Esa lista ayuda a ajustar una pauta sin pasar por alto pequeñas cantidades que se suman."),
     ("Actividad posible", "Moverse debe ser parte de una rutina disfrutable y segura. Un perro con dolor o un gato mayor quizá necesiten adaptar el tipo de juego antes que aumentar la intensidad."),
     ("Cambios acompañados", "Las dietas bruscas o caseras pueden dejar necesidades sin cubrir. Pedí un plan individual y controlá los avances con una frecuencia acordada.")],
    [("¿Un animal castrado engorda inevitablemente?", "No. Sus necesidades pueden cambiar, pero alimentación y actividad pueden ajustarse con orientación profesional."),
     ("¿Cómo sé si los premios son demasiados?", "Registralos durante unos días y llevalos a la consulta. Así se puede evaluar el conjunto.")], [("WSAVA · guías globales de nutrición", "https://wsava.org/Global-Guidelines/Global-Nutrition-Guidelines/")], ("corgi", "beagle"))

add("golpe-de-calor-mascotas", "salud", "Golpe de calor: reconocer el riesgo antes de salir",
    "Los días de calor requieren decisiones distintas para cada perro o gato.", "05-bulldog-lola.webp",
    "El calor puede afectar a cualquier mascota. Los animales de cara corta, mayores, con sobrepeso o con enfermedades pueden tener menos margen para tolerarlo, pero ninguno está seguro dentro de un auto estacionado.",
    [("Prevenir empieza por el horario", "Elegí momentos frescos para salir, ofrecé agua y sombra, y comprobá que el suelo no queme. Las actividades intensas pueden esperar a otro momento."),
     ("Signos que requieren acción", "Jadeo muy intenso, dificultad para respirar, debilidad, vómitos, desorientación o colapso son señales de alarma. Trasladá al animal a un lugar fresco y buscá atención veterinaria urgente."),
     ("No esperar a que «se le pase»", "Aunque parezca mejorar al enfriarse, puede necesitar evaluación. Llamá a una guardia o centro veterinario para recibir indicaciones durante el traslado.")],
    [("¿Una ventana entreabierta hace seguro el auto?", "No. Nunca dejes una mascota en un vehículo estacionado."),
     ("¿Puede ocurrir sin sol directo?", "Sí. También influyen temperatura ambiental, ventilación, humedad y esfuerzo.")], [("Manual MSD · emergencias en perros y gatos", "https://www.merckvetmanual.com/special-pet-topics/emergencies/what-to-do-in-a-dog-or-cat-emergency")], ("bulldog-frances", "husky-siberiano"))

add("parvovirus-en-perros", "salud", "Parvovirus en perros: una sospecha que no espera",
    "Qué señales requieren consulta rápida y por qué la prevención importa.", "21-perro-mestizo.webp",
    "El parvovirus canino es una infección muy contagiosa que afecta especialmente a perros jóvenes sin vacunación completa. Una página web no puede confirmar ni descartar el diagnóstico: hace falta evaluación veterinaria.",
    [("Señales posibles", "Decaimiento, falta de apetito, vómitos y diarrea pueden aparecer por distintas causas. En un cachorro o perro no vacunado, estas señales justifican atención rápida; no esperes a ver sangre en las heces."),
     ("Antes de llegar a la consulta", "Avisá que sospechás una enfermedad contagiosa para que el centro te indique cómo ingresar y reducir exposición de otros animales. No mediques por tu cuenta."),
     ("La prevención se planifica", "El calendario de vacunas y los cuidados mientras un cachorro completa su protección se deciden en consulta. Conservá sus constancias y preguntá qué ambientes son adecuados en cada etapa.")],
    [("¿Puede tener parvovirus sin diarrea con sangre?", "Sí. La ausencia de sangre no descarta la enfermedad ni hace menos importante la consulta."),
     ("¿Lo llevo junto con otros perros?", "Avisá al centro antes de ir para que puedan organizar una entrada segura.")], [("Manual MSD · infección por parvovirus canino", "https://www.merckvetmanual.com/digestive-system/infectious-diseases-of-the-gastrointestinal-tract-in-small-animals/canine-parvovirus-infection-parvoviral-enteritis-in-dogs"), VACCINE_SOURCE], ("vacunas-perros-gatos",))

add("vomitos-y-diarrea", "salud", "Vómitos y diarrea: qué observar y cuándo consultar",
    "Un registro claro puede ayudar; algunas señales requieren asistencia sin demora.", "09-beagle-tito.webp",
    "Los síntomas digestivos tienen muchas causas posibles. La edad, el estado general y la frecuencia de los episodios cambian la urgencia, por eso conviene mirar al animal completo.",
    [("Anotá lo que pasó", "Registrá cuándo empezó, cuántas veces ocurrió, si come y bebe, cómo está de ánimo y si pudo acceder a comida inusual, basura o sustancias peligrosas. Una foto puede ayudar a describir lo observado."),
     ("Señales para buscar ayuda pronto", "Un cachorro, un animal decaído, vómitos repetidos, sangre, abdomen hinchado, dolor o incapacidad para retener agua necesitan atención veterinaria. No esperes al día siguiente si su estado empeora."),
     ("Evitar soluciones improvisadas", "No administres medicamentos humanos ni sigas dietas restrictivas sin indicación. En consulta podrán decidir si necesita examen, hidratación o estudios.")],
    [("¿Siempre es algo que comió?", "No. Puede haber causas digestivas y también enfermedades de otros órganos."),
     ("¿Qué llevo a la consulta?", "Su historial, medicaciones, alimento habitual y un registro de síntomas ayudan a orientar la evaluación.")], [("Manual MSD · trastornos digestivos en perros", "https://www.merckvetmanual.com/dog-owners/digestive-disorders-of-dogs/introduction-to-digestive-disorders-of-dogs")], ("parvovirus-en-perros",))

add("pulgas-y-garrapatas", "salud", "Pulgas y garrapatas: revisar sin entrar en pánico",
    "Prevención individual y observación después de paseos o contacto con otros animales.", "06-dalmata-pipa.webp",
    "Encontrar un parásito despierta muchas preguntas. El producto adecuado depende de la especie, el peso, la edad y la salud de tu mascota; usar uno al azar puede ser riesgoso.",
    [("Revisar con calma", "Pasá la mano por pelo y piel, especialmente después de paseos en zonas verdes. Mirá orejas, cuello, axilas y entre los dedos, sin olvidar la cama y otros animales del hogar."),
     ("Elegir prevención", "Consultá qué antiparasitario corresponde y cada cuánto usarlo. Un producto para perros no debe asumirse seguro para gatos o animales pequeños."),
     ("Si encontrás una garrapata", "Pedí indicaciones para retirarla correctamente y observá la zona. Si el animal está decaído, tiene fiebre, deja de comer o presenta otros síntomas, buscá atención veterinaria.")],
    [("¿El baño reemplaza un antiparasitario?", "No necesariamente. El plan de control debe contemplar al animal y su entorno."),
     ("¿Puedo usar el mismo producto en perro y gato?", "No sin indicación profesional: algunas formulaciones para perros son peligrosas para gatos.")], [("Manual MSD · cuidados rutinarios del perro", "https://www.merckvetmanual.com/dog-owners/routine-care-of-dogs/routine-health-care-of-dogs")], ("perro-mestizo", "gato-de-interior"))

LIFE_FACTS = {
    "caniche": ("¿Cuánto puede vivir un caniche?", "Como referencia, el American Kennel Club sitúa al caniche entre 12 y 15 años. La edad de cada perro depende también de su salud y sus cuidados.", ("AKC · longevidad de perros", "https://www.akc.org/expert-advice/health/how-long-do-dogs-live/")),
    "golden-retriever": ("¿Cuánto suele vivir un golden retriever?", "El American Kennel Club señala una expectativa aproximada de 10 a 12 años. Es una referencia poblacional, no una predicción para tu perro.", ("AKC · golden retriever", "https://www.akc.org/dog-breeds/golden-retriever/")),
    "chihuahua": ("¿Cuánto suele vivir un chihuahua?", "El American Kennel Club indica aproximadamente 15 a 17 años. Los controles y la atención a sus necesidades siguen siendo importantes en cada etapa.", ("AKC · longevidad de perros", "https://www.akc.org/expert-advice/health/how-long-do-dogs-live/")),
    "periquito": ("¿Cuánto vive un periquito?", "Como orientación, el Manual MSD indica entre 5 y 10 años para los periquitos. Su salud y las condiciones de cuidado pueden modificar ese recorrido.", ("Manual MSD · elegir un ave", "https://www.merckvetmanual.com/bird-owners/choosing-and-taking-care-of-a-pet-bird/choosing-a-pet-bird")),
    "canario": ("¿Cuánto puede vivir un canario?", "El Manual MSD señala que puede llegar a los 15 años. Pensar en su espacio, alimentación y controles es parte de asumir ese compromiso.", ("Manual MSD · elegir un ave", "https://www.merckvetmanual.com/bird-owners/choosing-and-taking-care-of-a-pet-bird/choosing-a-pet-bird")),
    "conejo": ("¿Cuánto vive un conejo?", "La RSPCA estima habitualmente entre 8 y 12 años en un entorno seguro, con buena alimentación, compañía y controles. Algunos viven más.", RABBIT_SOURCE),
    "cobayo": ("¿Cuánto suele vivir un cobayo?", "El Manual MSD indica, como referencia, entre 5 y 8 años. Sus necesidades de alimentación y compañía se mantienen durante toda su vida.", ("Manual MSD · características del cobayo", "https://www.merckvetmanual.com/all-other-pets/guinea-pigs/description-and-physical-characteristics-of-guinea-pigs")),
    "hamster": ("¿Cuánto suele vivir un hámster?", "Según el Manual MSD, los hámsters de compañía suelen vivir entre 18 meses y 3 años. La especie y los cuidados influyen en cada caso.", ("Manual MSD · características del hámster", "https://www.merckvetmanual.com/all-other-pets/hamsters/description-and-physical-characteristics-of-hamsters")),
}

for article in ARTICLES:
    fact = LIFE_FACTS.get(article["slug"])
    if not fact:
        continue
    question, answer, source = fact
    existing = next((i for i, (q, _) in enumerate(article["faqs"]) if q.startswith("¿Cuánto vive")), None)
    if existing is None:
        article["faqs"].append((question, answer))
    else:
        article["faqs"][existing] = (question, answer)
    if source not in article["sources"]:
        article["sources"].append(source)

from article_expansions import EXPANSIONS, CTA
from article_depth import DEPTH

EXTRA_SOURCES = {
    "caniche": [("AKC · cuidados del caniche", "https://www.akc.org/dog-breeds/poodle-standard/")],
    "corgi": [("AKC · cuidados del corgi", "https://www.akc.org/dog-breeds/pembroke-welsh-corgi/")],
    "perro-salchicha": [("Manual MSD · trastornos de columna en perros", "https://www.merckvetmanual.com/dog-owners/brain-spinal-cord-and-nerve-disorders-of-dogs/disorders-of-the-spinal-column-and-cord-in-dogs"), ("AKC · cuidados del dachshund", "https://www.akc.org/dog-breeds/dachshund/")],
    "bulldog-frances": [("Universidad de Cambridge · salud respiratoria", "https://www.vet.cam.ac.uk/boas/about-boas/recognition-diagnosis")],
    "dalmata": [("AKC · salud del dálmata", "https://www.akc.org/dog-breeds/dalmatian/"), ("Manual MSD · cálculos urinarios en perros", "https://www.merckvetmanual.com/urinary-system/urolithiasis-in-small-animals/urolithiasis-in-dogs")],
    "husky-siberiano": [("AKC · cuidados del husky siberiano", "https://www.akc.org/dog-breeds/siberian-husky/")],
    "shiba-inu": [("AKC · cuidados del shiba inu", "https://www.akc.org/dog-breeds/shiba-inu/")],
    "beagle": [("AKC · educación del beagle", "https://www.akc.org/expert-advice/training/beagle-puppy-training-timeline-what-to-expect-and-when-to-expect-it/")],
    "pitbull": [("AVMA · prevenir mordidas sin etiquetar razas", "https://ebusiness.avma.org/Files/ProductDownloads/mcm-client-brochures-21-dog-bite-prevention.pdf"), ("AVSAB · entrenamiento respetuoso", "https://avsab.org/resources/position-statements/")],
    "chihuahua": [("AKC · cuidados del chihuahua", "https://www.akc.org/dog-breeds/chihuahua/")],
    "gato-primer-ano": [("Manual MSD · cuidados del gatito", "https://www.merckvetmanual.com/cat-owners/caring-for-cats/kitten-care")],
    "gato-de-interior": [("FelineVMA · necesidades del gato de interior", "https://catvets.com/news/2025-indoor-cats-position-statement/")],
    "gato-agua-y-arenero": [("Manual MSD · arenero para gatos", "https://www.merckvetmanual.com/cat-owners/selecting-and-providing-a-home-for-a-cat/providing-a-litter-box-for-a-cat")],
    "gato-mayor": [("Manual MSD · articulaciones del gato", "https://www.merckvetmanual.com/cat-owners/bone-joint-and-muscle-disorders-of-cats/joint-disorders-in-cats")],
    "loro": [("Manual MSD · alimentar a un ave", "https://www.merckvetmanual.com/bird-owners/choosing-and-taking-care-of-a-pet-bird/feeding-a-pet-bird"), ("Manual MSD · signos de enfermedad en aves", "https://www.merckvetmanual.com/bird-owners/routine-care-and-safety-of-birds/illness-in-pet-birds")],
    "ninfa": [("Manual MSD · alimentar a un ave", "https://www.merckvetmanual.com/bird-owners/choosing-and-taking-care-of-a-pet-bird/feeding-a-pet-bird"), ("Manual MSD · signos de enfermedad en aves", "https://www.merckvetmanual.com/bird-owners/routine-care-and-safety-of-birds/illness-in-pet-birds")],
    "periquito": [("Manual MSD · alimentar a un ave", "https://www.merckvetmanual.com/bird-owners/choosing-and-taking-care-of-a-pet-bird/feeding-a-pet-bird"), ("Manual MSD · signos de enfermedad en aves", "https://www.merckvetmanual.com/bird-owners/routine-care-and-safety-of-birds/illness-in-pet-birds")],
    "canario": [("Manual MSD · signos de enfermedad en aves", "https://www.merckvetmanual.com/bird-owners/routine-care-and-safety-of-birds/illness-in-pet-birds")],
    "conejo": [("RSPCA · dieta del conejo", "https://www.rspca.org.uk/adviceandwelfare/pets/rabbits/diet"), ("RSPCA · espacio para conejos", "https://www.rspca.org.uk/adviceandwelfare/pets/rabbits/environment"), ("RSPCA · compañía para conejos", "https://www.rspca.org.uk/adviceandwelfare/pets/rabbits/company")],
    "cobayo": [("Manual MSD · nutrición del cobayo", "https://www.merckvetmanual.com/all-other-pets/guinea-pigs/nutritional-problems-of-guinea-pigs")],
    "hamster": [("Manual MSD · hogar del hámster", "https://www.merckvetmanual.com/all-other-pets/hamsters/providing-a-home-for-a-hamster")],
    "tortuga": [("Manual MSD · hogar de reptiles", "https://www.merckvetmanual.com/all-other-pets/reptiles/providing-a-home-for-a-reptile"), ("Manual MSD · higiene y reptiles", "https://www.merckvetmanual.com/all-other-pets/reptiles/special-considerations-for-reptiles")],
    "vomitos-y-diarrea": [("Manual MSD · vómitos en perros", "https://www.merckvetmanual.com/dog-owners/digestive-disorders-of-dogs/vomiting-in-dogs"), ("Manual MSD · trastornos digestivos en gatos", "https://www.merckvetmanual.com/cat-owners/digestive-disorders-of-cats/introduction-to-digestive-disorders-of-cats")],
    "pulgas-y-garrapatas": [("Manual MSD · seguridad de antiparasitarios", "https://www.merckvetmanual.com/pharmacology/ectoparasiticides/ectoparasiticides-used-in-small-animals")],
}

for article in ARTICLES:
    article["sections"].extend(EXPANSIONS[article["slug"]])
    if article["slug"] in DEPTH:
        article["sections"].append(DEPTH[article["slug"]])
    article["cta"] = CTA[article["slug"]]
    if article["slug"] == "tortuga":
        article["sources"] = []
    if article["category"] == "aves":
        article["sources"] = [source for source in article["sources"] if source != BIRD_SOURCE]
    if article["slug"] == "hamster":
        article["sources"] = [source for source in article["sources"] if source != SMALL_SOURCE]
    if article["slug"] == "golpe-de-calor-mascotas":
        article["sources"] = []
    if article["slug"].startswith("gato-") and article["slug"] != "gato-primer-ano":
        article["sources"] = [source for source in article["sources"] if source != CAT_SOURCE]
    for source in EXTRA_SOURCES.get(article["slug"], []):
        if source not in article["sources"]:
            article["sources"].append(source)

assert len(ARTICLES) == 31, len(ARTICLES)
assert set(EXPANSIONS) == {article["slug"] for article in ARTICLES}
assert set(CTA) == {article["slug"] for article in ARTICLES}
assert set(DEPTH) == {article["slug"] for article in ARTICLES if article["category"] != "salud"}

from guide_enrichments import ENRICHMENTS
assert set(ENRICHMENTS) == {article["slug"] for article in ARTICLES}
for article in ARTICLES:
    extra = ENRICHMENTS[article["slug"]]
    if article["category"] == "perros" and article["slug"] != "perro-mestizo":
        article["sections"].insert(0, extra["section"])
    else:
        article["sections"].append(extra["section"])
    article["faqs"].extend(extra["faqs"])
    if extra["source"] and extra["source"] not in article["sources"]:
        article["sources"].append(extra["source"])

from new_breed_guides import ARTICLES as NEW_BREED_ARTICLES
ARTICLES.extend(NEW_BREED_ARTICLES)
assert len(ARTICLES) == 44, len(ARTICLES)
