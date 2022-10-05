import win32api, win32con, time, win32com.client
import pyautogui as pg

shell = win32com.client.Dispatch("WScript.Shell")

#BLEACH

time.sleep(3)
win32api.SetCursorPos((131,74))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("URL3.html") #nombre archivo
time.sleep(1)
pg.typewrite("\n")
time.sleep(1)
win32api.SetCursorPos((506,371))
time.sleep(1)
pg.hotkey("ctrl", "v") #pegar plantilla
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((1358,97)) #subir al top del archivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((400,170))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("Bleach") #Titulo de la página
time.sleep(1)
win32api.SetCursorPos((1363,564)) #bajada del arrchivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((577,142)) #coordenadas Foto
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("bleach.jpg") #foto
time.sleep(1)
win32api.SetCursorPos((596,197)) #coordenadas titulo manga
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.5)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("BLEACH 1") #titulo manga
time.sleep(1)
win32api.SetCursorPos((593,216)) #Coordenadas autor
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("TITE KUBO") #Autor
time.sleep(1)
win32api.SetCursorPos((508,273)) #Coordenadas resumen
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
shell.SendKeys("{TAB}")
time.sleep(1)
pg.typewrite("Ichigo Kurosaki no es un quinceañero normal y corriente… puede ver espíritus y tiene un contacto innato con el más allá, al que sacará provecho tras conocer a un shinigami (ángel de la muerte) que le proporciona una espada a juego con sus habilidades. Bleach es el manga que ha arrasado en Japón. Se trata de una serie abierta que mes tras mes gana nuevos incondicionales.") #resumen


#ONE PIECE

time.sleep(6)
win32api.SetCursorPos((131,74))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("URL4.html") #nombre archivo
time.sleep(1)
pg.typewrite("\n")
time.sleep(1)
win32api.SetCursorPos((506,371))
time.sleep(1)
pg.hotkey("ctrl", "v") #pegar plantilla
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((1358,97)) #subir al top del archivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((400,170))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("One piece") #Titulo de la página
time.sleep(1)
win32api.SetCursorPos((1363,564)) #bajada del arrchivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((577,142)) #coordenadas Foto
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("one-piece-ep100.jpg") #foto
time.sleep(1)
win32api.SetCursorPos((596,197)) #coordenadas titulo manga
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.5)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("ONE PIECE 1") #titulo manga
time.sleep(1)
win32api.SetCursorPos((593,216)) #Coordenadas autor
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("EIICHIRO ODA") #Autor
time.sleep(1)
win32api.SetCursorPos((508,273)) #Coordenadas resumen
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
shell.SendKeys("{TAB}")
time.sleep(1)
pg.typewrite("El manga de la serie más pirata de la teleSigue las aventuras de Monkey D. Luffy, un chico muy especial y elástico, que sueña con ser el rey de los piratas y encontrar una gran tesoro: el One Piece. Para ello, se hace a la mar en un bote con el que buscará la tripulación que le pueda ayudar en su misión.Uno de los manga shônen más exitosos de la Historia, junto con Dragon Ball y Naruto. El argumento destaca valores como el espíritu superación, la tolerancia hacia la diferencia y el compañerismo. Creado por el mangaka Eiichiro Oda.") #resumen


#BOKU NO HERO

time.sleep(6)
win32api.SetCursorPos((131,74))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("URL5.html") #nombre archivo
time.sleep(1)
pg.typewrite("\n")
time.sleep(1)
win32api.SetCursorPos((506,371))
time.sleep(1)
pg.hotkey("ctrl", "v") #pegar plantilla
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((1358,97)) #subir al top del archivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((400,170))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("Boku no hero") #Titulo de la página
time.sleep(1)
win32api.SetCursorPos((1363,564)) #bajada del arrchivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((577,142)) #coordenadas Foto
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("boku-no-hero-ep1.png") #foto
time.sleep(1)
win32api.SetCursorPos((596,197)) #coordenadas titulo manga
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.5)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("BOKU NO HERO 1") #titulo manga
time.sleep(1)
win32api.SetCursorPos((593,216)) #Coordenadas autor
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("KOHEI HORIKOSHI") #Autor
time.sleep(1)
win32api.SetCursorPos((508,273)) #Coordenadas resumen
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
shell.SendKeys("{TAB}")
time.sleep(1)
pg.typewrite("En la carrera de obstáculos, nuestro amigo Deku ha quedado el primero, lo que le hará pasarlo mal en la siguiente prueba por equipos. ¡Pero significa que todos estarán pendientes de él, seguro que Deku saldrá bien parado! ¡Yo tampoco puedo quedarme atrás! ¡Un saludo a papá y a mamá! ¡Plus ultra (más allá)!") #resumen


#DRAGON BALL GT

time.sleep(6)
win32api.SetCursorPos((131,74))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("URL6.html") #nombre archivo
time.sleep(1)
pg.typewrite("\n")
time.sleep(1)
win32api.SetCursorPos((506,371))
time.sleep(1)
pg.hotkey("ctrl", "v") #pegar plantilla
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((1358,97)) #subir al top del archivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((400,170))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("Dragon ball") #Titulo de la página
time.sleep(1)
win32api.SetCursorPos((1363,564)) #bajada del arrchivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((577,142)) #coordenadas Foto
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("dragon-ball-gt.png") #foto
time.sleep(1)
win32api.SetCursorPos((596,197)) #coordenadas titulo manga
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.5)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("DRAGON BALL 1") #titulo manga
time.sleep(1)
win32api.SetCursorPos((593,216)) #Coordenadas autor
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("AKIRA TORIYAMA") #Autor
time.sleep(1)
win32api.SetCursorPos((508,273)) #Coordenadas resumen
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
shell.SendKeys("{TAB}")
time.sleep(1)
pg.typewrite("¡Han surgido unos dragones oscuros debido al uso abusivo que han hecho Goku y sus amigos de las bolas de dragón! ¡¡Como no lo remedien, la energía negativa destruirá la galaxia!! Goku y Pan salen en un viaje para eliminar a los siete dragones oscuros y se encuentran con Erxinglong, Wuxinglong, Liuxinglong y Qixinglong...") #resumen


#kuro

time.sleep(6)
win32api.SetCursorPos((131,74))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("URL7.html") #nombre archivo
time.sleep(1)
pg.typewrite("\n")
time.sleep(1)
win32api.SetCursorPos((506,371))
time.sleep(1)
pg.hotkey("ctrl", "v") #pegar plantilla
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((1358,97)) #subir al top del archivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((400,170))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("Kuroshitsuji") #Titulo de la página
time.sleep(1)
win32api.SetCursorPos((1363,564)) #bajada del arrchivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((577,142)) #coordenadas Foto
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("kuroshitsuji.png") #foto
time.sleep(1)
win32api.SetCursorPos((596,197)) #coordenadas titulo manga
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.5)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("KUROSHITSUJI 1") #titulo manga
time.sleep(1)
win32api.SetCursorPos((593,216)) #Coordenadas autor
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("YANA TOBOSO") #Autor
time.sleep(1)
win32api.SetCursorPos((508,273)) #Coordenadas resumen
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
shell.SendKeys("{TAB}")
time.sleep(1)
pg.typewrite("La relación que los une a ambos no es simplemente de amo y mayordomo; Sebastian es un demonio que está unido a Ciel a través de un contrato, debido al cual deberá servirlo hasta que este concluya su venganza hacia las personas que asesinaron y mancharon el honor de su familia. Una vez que el contrato se cumpla, Sebastian tomará posesión del alma de Ciel. A lo largo de la historia, Ciel y Sebastian resolverán numerosos misterios y crímenes, mientras se enfrentan a la posibilidad de salir involucrados en el proceso.") #resumen


#bERSERKER

time.sleep(6)
win32api.SetCursorPos((131,74))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("URL8.html") #nombre archivo
time.sleep(1)
pg.typewrite("\n")
time.sleep(1)
win32api.SetCursorPos((506,371))
time.sleep(1)
pg.hotkey("ctrl", "v") #pegar plantilla
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((1358,97)) #subir al top del archivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((400,170))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("Berserker") #Titulo de la página
time.sleep(1)
win32api.SetCursorPos((1363,564)) #bajada del arrchivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((577,142)) #coordenadas Foto
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("berserker.png") #foto
time.sleep(1)
win32api.SetCursorPos((596,197)) #coordenadas titulo manga
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.5)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("BERSERKER 1") #titulo manga
time.sleep(1)
win32api.SetCursorPos((593,216)) #Coordenadas autor
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("KENTARO MIURA") #Autor
time.sleep(1)
win32api.SetCursorPos((508,273)) #Coordenadas resumen
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
shell.SendKeys("{TAB}")
time.sleep(1)
pg.typewrite("Edición de lujo de una de las más aclamadas series manga de todos los tiempos. Un viaje épico y salvaje a un reino de fantasía. Guts es un guerrero vestido de negro de los pies a la cabeza que porta una gigantesca espada más larga que su propia estatura y un robusto brazo ortopédico de hierro... Berserk es una historia de batallas épicas, de venganzas, de muerte y de luchas por conseguir el poder, por conseguir un nombre en una sociedad noble y despreciativa con las clases “inferiores”. A esto se le une la línea evolutiva que siguen los personajes implicados en la trama y el conocimiento que poco a poco van teniendo los protagonistas sobre ellos mismos y sus motivaciones. A Todo esto, sumado a los elementos fantásticos más comunes de las novelas del género convierten a Berserk en una obra de arte dentro del género. El protagonista es Gutts (Gatsu), un mercenario que comenzó sus andaduras cuando era niño, y que se mueve y actúa por venganza y por un odio mucho mayor que cualquier miedo o dolor físico. Su enorme espada (tan alta como él) y su increíble destreza atraerán la atención de Grifith, el jefe de la Banda del Halcón, un grupo de mercenarios famoso por sus victorias. Grifith va a reclutar a Gutts y le hará miembro de su banda, de la que forman parte el resto de los protagonistas: Caska, Judeau, Ricket y Pippin serán los personajes más cercanos a Gutts.") #resumen


#NORAGAMI

time.sleep(6)
win32api.SetCursorPos((131,74))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("URL9.html") #nombre archivo
time.sleep(1)
pg.typewrite("\n")
time.sleep(1)
win32api.SetCursorPos((506,371))
time.sleep(1)
pg.hotkey("ctrl", "v") #pegar plantilla
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((1358,97)) #subir al top del archivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((400,170))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("Noragami") #Titulo de la página
time.sleep(1)
win32api.SetCursorPos((1363,564)) #bajada del arrchivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((577,142)) #coordenadas Foto
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("noragami.png") #foto
time.sleep(1)
win32api.SetCursorPos((596,197)) #coordenadas titulo manga
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.5)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("NORAGAMI 1") #titulo manga
time.sleep(1)
win32api.SetCursorPos((593,216)) #Coordenadas autor
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("ADACHITOKA") #Autor
time.sleep(1)
win32api.SetCursorPos((508,273)) #Coordenadas resumen
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
shell.SendKeys("{TAB}")
time.sleep(1)
pg.typewrite("Hiyori, una joven humana, arriesga su vida para salvar a un chicode un atropello. Lo que no sabe es que se trata de Yato, una deidadmenor que desea convertirse en dios, y tras su sacrificio la chicaadquiere el poder de abandonar su cuerpo casi a voluntad loque la liga a Yato y a su misión") #resumen


#NANA

time.sleep(6)
win32api.SetCursorPos((131,74))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("URL10.html") #nombre archivo
time.sleep(1)
pg.typewrite("\n")
time.sleep(1)
win32api.SetCursorPos((506,371))
time.sleep(1)
pg.hotkey("ctrl", "v") #pegar plantilla
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((1358,97)) #subir al top del archivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((400,170))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("Nana") #Titulo de la página
time.sleep(1)
win32api.SetCursorPos((1363,564)) #bajada del arrchivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((577,142)) #coordenadas Foto
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("nana.jpg") #foto
time.sleep(1)
win32api.SetCursorPos((596,197)) #coordenadas titulo manga
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.5)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("NANA 1") #titulo manga
time.sleep(1)
win32api.SetCursorPos((593,216)) #Coordenadas autor
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("AI YAZAWA") #Autor
time.sleep(1)
win32api.SetCursorPos((508,273)) #Coordenadas resumen
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
shell.SendKeys("{TAB}")
time.sleep(1)
pg.typewrite("Tokio, la gran metrópolis. Dos chicas llegan a la ciudad dispuestas a cumplir sus sueños, aunque aparentemente son totalmente opuestas: Nana Komatsu es dulce, ingenua, enamoradiza, y arrastra un largo historial de amores malogrados. Nana Oosaki es madura y segura de sí misma, sabe lo que quiere y qué debe hacer para conseguirlo. Los caminos de estas chicas tan distintas se cruzarán en la capital, donde empezarán compartiendo piso y acabarán apoyándose la una en la otra. ") #resumen


#Kingdom

time.sleep(6)
win32api.SetCursorPos((131,74))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("URL11.html") #nombre archivo
time.sleep(1)
pg.typewrite("\n")
time.sleep(1)
win32api.SetCursorPos((506,371))
time.sleep(1)
pg.hotkey("ctrl", "v") #pegar plantilla
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((1358,97)) #subir al top del archivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((400,170))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("Kingdom") #Titulo de la página
time.sleep(1)
win32api.SetCursorPos((1363,564)) #bajada del arrchivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((577,142)) #coordenadas Foto
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("kingdom.jpg") #foto
time.sleep(1)
win32api.SetCursorPos((596,197)) #coordenadas titulo manga
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.5)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("KINGDOM 1") #titulo manga
time.sleep(1)
win32api.SetCursorPos((593,216)) #Coordenadas autor
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("YASUHISA HARA") #Autor
time.sleep(1)
win32api.SetCursorPos((508,273)) #Coordenadas resumen
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
shell.SendKeys("{TAB}")
time.sleep(1)
pg.typewrite("La historia nos traslada a lo que ahora es China hacia el año 300 a.c., una época en la que la zona está dividida en siete reinos que luchan por cada palmo de terreno con sus vecinos, mientras estallan continuas guerras civiles intestinas y también con clanes que tienen su propio modo de vida. Shin es niño huérfano de guerra que vive en el reino de Qin y que ha acabado convertido en esclavo. Junto a su amigo Hyou, sueña con convertirse en un gran general como los legendarios que condujeron enormes ejércitos. Su vida da un vuelco el día que reclutan a Hyou como doble de Ei Sei, Rey de Qin, y ahí empiezan una serie de acontecimientos que lo llevan a unirse al ejército y vivir el mismo sueño que su Rey: unificar los siete reinos en uno solo, China. Las guerras que aparecen son de una escala enorme, con decenas de miles de soldados y conoceremos a decenas de personajes de cada reino que tendrán un papel crucial en ellas, haciendo uso de la estrategia, de las tácticas y del puro instinto. El dibujo de Yasuhisa Hara, que fue ayudante y es amigo de Takehiko Inoue, tiene una evolución espectacular y nos refleja perfectamente tanto la grandeza, como el horror, el gore y la dureza de las guerras. A través de grandes campañas, cada capítulo nos deja con ganas de más en una historia perfectamente hilada, llena de momentos épicos y que hacen que te acabes preguntando ¿Cómo se las arreglarán?.") #resumen

#Dandadan

time.sleep(6)
win32api.SetCursorPos((131,74))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("URL12.html") #nombre archivo
time.sleep(1)
pg.typewrite("\n")
time.sleep(1)
win32api.SetCursorPos((506,371))
time.sleep(1)
pg.hotkey("ctrl", "v") #pegar plantilla
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((1358,97)) #subir al top del archivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((400,170))
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("Dandadan") #Titulo de la página
time.sleep(1)
win32api.SetCursorPos((1363,564)) #bajada del arrchivo
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
win32api.SetCursorPos((577,142)) #coordenadas Foto
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("dandadan.jpg") #foto
time.sleep(1)
win32api.SetCursorPos((596,197)) #coordenadas titulo manga
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.5)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("DANDADAN 1") #titulo manga
time.sleep(1)
win32api.SetCursorPos((593,216)) #Coordenadas autor
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
pg.typewrite("TATSU YUKINOBU") #Autor
time.sleep(1)
win32api.SetCursorPos((508,273)) #Coordenadas resumen
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(1)
shell.SendKeys("{TAB}")
time.sleep(1)
pg.typewrite("Takakura es un joven amante de lo oculto que no cree en fantasmas, mientras que su amiga, Ayase, no cree en los alienígenas, pero juntos se toparán con un misterio que desafiará todas sus creencias y convenciones. ¡¡Comienza una historia adolescente terrorífica!!") #resumen