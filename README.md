# Sudoku Generaattori

Tehtävänä oli tehdä algoritmi, jolla generoidaan sudokuun taulukko. Python ei ole vahvin kieleni, mutta päätin nyt käyttää sitä kun pythonia on kurssilla käytetty usein muutenkin ja saman algoritmin voi toteuttaa helposti millä tahansa muullakin kielellä kun sitä varten ei tarvitse asentaa mitään ylimääräisiä kirjastoja. 

Keskityin tehtävässä vain algoritmin toimintaan, joten koodin toteutus ei ole kovin tarkkaan mietittyä. Alunperin algoritmi rakensi taulukkoon luvut 0-8, koska se oli helpompi toteuttaa, mutta vaihdoin nyt jälkikäteen, että käytössä on oikeat numerot eli 1-9.

Tehtävä ei teknisesti ollut kovinkaan haastavaa, mutta ongelmanratkaisut vei huomattavasti enemmän aikaa.

## Toteutukset

Päätin alussa jo, että toteutan taulukon 2d arrayna, vaikka sen voisi luoda muillakin listoilla, 2d taulukko on helpompi havannoida mielessä. Muut asiat päätin vasta koodauksen aikana, ensimmäiset päivät keskityin vain sudokun pelaamiseen ja yritin pelata sitä mahdollisen järjestelmällisesti, jotta voisin opettaa saman tietokoneellekin, mutta totesin lähes jokaisessa pelissä joutuvani ennakoimaan siirtoja, koska pelissä tuli sellaisia tilanteita ettei yksinkertaisella validoinnilla pysty arvoimaan, että tuohon menee vain yksi numero, joten samojen asioiden opettaminen olisi huomattavan hankalaa.

Yritin ensin miettiä sudokun kentän generointiin tapaa, jolla sen voisi luoda täysin satunnaisesti, mutta luovuin ideasta kun en keksinyt tapaa, jolla sen pystyisi luomaan tehokkaasti. Päätin lopulta generoida osan kentästä satunnaisesti ja loput kentästä ratkaistaan. Toteutuksista enemmän alapuolella.


### Ensimmäinen toteutus

Yritin ensimmäiseksi tehdä generaattoria, joka toteuttaisi generaattorin loopilla, jossa se generoi yksittäisen numeron rivi kerrallaan. Loopilla oli lista, jossa oli sarakkeet, joita ei ollut vielä käytetty ja myös täytetyt laatikot huomioitiin (3x3 kentät). 

Ratkaisu toimikin hyvin kunnes tuli 4 tai 5 numero toistoon, yleensä silloin tuli ristiriita kun numero ei sopinutkaan rivin ainoaan jäljellä olevaan laatikkoon, eikä muita vaihtoehtoja ollut jäljellä. Tajusin jälkikäteen, että tämänkin olisi voinut ratkaista samalla tavalla kuin ratkaisin toisen version lopulta, mutta generointi olisi ollut todennäköisesti hitaampaa satunnaisuuden aiheuttamien ristiriitojen takia.

Alla esimerkki:

- [1,x,4][3,x,x][2,x,x]
- [x,2,x][3,x,x][x,1,4]
- [x,x,x][3,1,2][x,x,x]
  
Esimerkissä on generoituna riveille 1 ja 2 luvut 1,2,3,4. Riville 3 on generoitu luvut 1,2 ja 3, mutta 4 on mahdoton sijoittaa, koska ainoa mahdollinen paikka olisi toinen laatikko (3x3 kenttä) ja siellä ei ole tilaa.

### Toinen toteutus

Toisella toteutuksella päätin kokeilla generoida satunnaisesti kolme laatikkoa, joilla ei ole riippuvuuksia toisistaan. Toteutin tämän yksinkertaisella loopilla, joka on myös mukana lopullisessa versiossa (esimerkki toteutuksessa alempana).

Loput sudokusta ratkaistaan eli muita ruutuja ei generoida satunnaisesti. Yritin aluksi toteuttaa ratkaisua yksinkertaisilla validoinneilla, mutta jokainen niistä myös kosahti ristiriitoihin, mietin jo itse toteutusta tehdessä, että olisi hyvä, jos virheen sattuessa voisi palata askeleen taaksepäin eli vaihtaakin edellisen numeron paikkaa ja kokeilla jatkaa ratkaisemista toisella numerolla.

Lopulta usean tunnin miettimisen jälkeen totesin, että aika avata google ja hakea mallia muualta, löysin sivulta https://www.geeksforgeeks.org/sudoku-backtracking-7/, backtracking algoritmiin perustuvan ratkaisun, jota päätin kokeilla. Olin itse miettinyt lähes samankaltaista toteutusta aiemmin, ratkaisu selitetään alempana tarkemmin.

## Generaattorin Algoritmi

Generaattori luo ensin 2d-taulukon, jonka sisällä jokaisessa ruudussa on -1 arvo

Taulukon luonnin jälkeen tehdään satunnaiset luvut kolmeen eri laatikkoon (ylävasen, keskimmäinen ja alaoikea). (laatikko = 3x3 alue)

esim.
- [2, 1, 6, -1, -1, -1, -1, -1, -1]
- [3, 9, 7, -1, -1, -1, -1, -1, -1]
- [4, 5, 8, -1, -1, -1, -1, -1, -1]
- [-1, -1, -1, 9, 2, 6, -1, -1, -1]
- [-1, -1, -1, 7, 1, 5, -1, -1, -1]
- [-1, -1, -1, 3, 8, 4, -1, -1, -1]
- [-1, -1, -1, -1, -1, -1, 3, 9, 2]
- [-1, -1, -1, -1, -1, -1, 6, 7, 8]
- [-1, -1, -1, -1, -1, -1, 5, 1, 4]

Jonka jälkeen Solver ratkaisee loput taulukosta, joten niitä ei generoida satunnaisesti.

## Taulukon ratkaisu

Ratkaisu tehdään niin, että Solver etsii ensimmäiseksi tyhjän ruudun (ruudun, jossa arvo -1), jos tyhjää ruutua ei löydy niin metodi palauttaa True eli taulukko on jo ratkaistu.

Ensimmäisen ruudun löytymisen jälkeen aloitetaan looppi, jossa tarkastetaan yksitellen numeroita ja validoidaan:
   
- onko rivillä kyseistä numeroa
- onko rivin sarakkeissa kyseistä numeroa
- onko laatikossa kyseistä numeroa

Validoinnin jälkeen kokeillaan seuraavaa numeroa (jos joku validoinneista ei mennyt läpi) tai merkitään numero ruutuun ja siirrytään eteenpäin.

Backtracking malli on tehty rekursiivisesti eli seuraavaksi ajetaankin solve metodi uudestaan, jolloin ensimmäinen ruutu on täytetty ja suoritetaan edeltävät vaiheet uudestaan eli etsitään tyhjä ruutu, validoidaan jne.

Metodia toistetaan kunnes kaikki ruudut on täytetty tai joudutaan umpikujaan. Umpikujaan jouduttua algoritmi ei aloita tarkastusta alusta vaan siirtyy vain askeleen taaksepäin eli poistaa viimeksi täytetyn numeron ja kokeilee siihen toista arvoa.

Lopulta kun kaikki mahdolliset vaihtoehdot on käyty läpi niin solve palauttaa joko True (taulukko ratkaistu) tai False (taulukko ei ole ratkaistavissa.)

Esimerkkitaulu ratkaistuna:

- [2, 1, 6, 4, 3, 7, 8, 5, 9]
- [3, 9, 7, 1, 5, 8, 2, 4, 6]
- [4, 5, 8, 2, 6, 9, 1, 3, 7]
- [1, 3, 4, 9, 2, 6, 7, 8, 5]
- [6, 8, 9, 7, 1, 5, 4, 2, 3]
- [5, 7, 2, 3, 8, 4, 9, 6, 1]
- [8, 4, 5, 6, 7, 1, 3, 9, 2]
- [9, 2, 1, 5, 4, 3, 6, 7, 8]
- [7, 6, 3, 8, 9, 2, 5, 1, 4]

## Pelattava sudoku
En tehnyt sudokusta pelattavaa versiota, mutta sen saa helposti liitettyä peliliittymään.

- olio = SudokuGenerator() # tekee olion ja sudokuun taulukon
- olio.generate_sudoku() # tekee uuden taulukon
- olio.remove_random_cells(40) # poistaa taulukosta numeroita argumentin verran
- olio.grid # attribuutilla pääsee käsiksi taulukkoon
- olio.solved # sisältää deepcopyn tarkastetusta taulukosta
- Solver(olio.grid) # ratkaisee taulukon

## Testit
Tein unit testit, jotka varmistavat taulun olevan oikean kokoinen ja jokaiselta riviltä löytyy kaikki numerot.

Kolmannessa testissä sudoku tekee taulukon, poistaa siitä lukuja ja koittaa ratkaista sen uudestaan, jonka jälkeen testi vertaa sudokua alkuperäiseen. Testi ei mene läpi joka kerta, koska Solver on löytänyt toisen ratkaisun sudokuun, joka oli kuitenkin hyväksyttävä tulos eli testissä on virhe eikä generaattorissa.

Generaattorin aika heittelee reippaasti, koska osa kentästä on satunnaisesti generoitu, mutta loput siitä pitää ratkaista, joten nopeus riippuu satunnaisista luvuista. Kokeilin generoida 100 sudokua kerralla, useamman kerran ja suoritus heitteli noin 0,7 - 3,8 sekunnin välillä