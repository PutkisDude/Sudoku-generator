# Sudoku Generaattori

Tehtävänä oli tehdä algoritmi, jolla generoidaan sudokuun taulukko. Python ei ole vahvin kieleni, mutta päätin nyt käyttää sitä kun sitä on kurssilla käytetty eniten ja saman algoritmin voi toteuttaa helposti millä tahansa muullakin kielellä kun sitä varten ei tarvinnut asentaa mitään ylimääräisiä paketteja. 

Keskityin tehtävässä vain algoritmin toimintaan, joten koodin toteutus ei ole kovin tarkkaan mietittyä.

## Toimintatapa

Yritin aluksi suorittaa tehtävää yksinkertaisemmin ilman apukeinoja, mutta totesin jokaisen kokeilemani ratkaisun kaatuvan bugeihin, joten hain mallia muualta.

Päätin kokeilla toteuttaa https://www.geeksforgeeks.org/sudoku-backtracking-7/ sivulta löytyvillä ohjeilla backtracking algoritmiin perustuvan generaattorin.

## Generaattorin Algoritmi

Generaattori luo ensin 2d-taulukon, jonka sisällä jokaisessa ruudussa on -1 arvo

Taulukon luoonnin jälkeen tehdään satunnaiset luvut kolmeen eri laatikkoon (ylävasen, keskimmäinen ja alaoikea). (laatikko = 3x3 alue)

esim.
- [1, 0, 5, -1, -1, -1, -1, -1, -1]
- [2, 8, 6, -1, -1, -1, -1, -1, -1]
- [3, 4, 7, -1, -1, -1, -1, -1, -1]
- [-1, -1, -1, 8, 1, 5, -1, -1, -1]
- [-1, -1, -1, 6, 0, 4, -1, -1, -1]
- [-1, -1, -1, 2, 7, 3, -1, -1, -1]
- [-1, -1, -1, -1, -1, -1, 2, 8, 1]
- [-1, -1, -1, -1, -1, -1, 5, 6, 7]
- [-1, -1, -1, -1, -1, -1, 4, 0, 3]

Jonka jälkeen Solver ratkaisee loput taulukosta, joten niitä ei toteutata satunnaisesti.

## Taulukon ratkaisu

Ratkaisu tehdään niin, että Solver etsii ensimmäiseksi tyhjän ruudun (ruudun, jossa arvo -1), jos tyhjää ruutua ei löydy niin metodi palauttaa True eli taulukko on jo ratkaistu.

Ensimmäisen ruudun löytymisen jälkeen aloitetaan looppi, jossa tarkastetaan yksitellen numeroita ja validoidaan:
   
- onko rivillä kyseistä numeroa
- onko rivin sarakkeissa kyseistä numeroa
- onko laatikossa kyseistä numeroa

Validoinnin jälkeen kokeillaan seuraavaa numeroa (jos joku validoinneista ei mennyt läpi) tai merkitään numero ruutuun ja siirrytään eteenpäin.

Backtracking malli on tehty rekursiivisesti eli seuraavaksi ajetaankin solve metodi uudestaan, jolloin ensimmäinen ruutu on täytetty ja suoritetaan edeltävät vaiheet uudestaan eli etsitään tyhjä ruutu, validoidaan jne.

Metodia toistetaan kunnes kaikki ruudut on täytetty tai joudutaan umpikujaan. Umpikujaan jouduttua algoritmi ei aloita tarkastusta alusta vaan siirtyy vain askelen taaksepäin eli poistaa viimeksi täytetyn numeron ja kokeilee siihen toista arvoa.

Lopulta kun kaikki mahdolliset vaihtoehdot on käyty läpi niin solve palauttaa joko True (taulukko ratkaistu) tai False (taulukko ei ole ratkaistavissa.)

Esimerkkitaulu ratkaistuna:

- [1, 0, 5, 3, 2, 6, 7, 4, 8]
- [2, 8, 6, 0, 4, 7, 1, 3, 5]
- [3, 4, 7, 1, 5, 8, 0, 2, 6]
- [0, 2, 3, 8, 1, 5, 6, 7, 4]
- [5, 7, 8, 6, 0, 4, 3, 1, 2]
- [4, 6, 1, 2, 7, 3, 8, 5, 0]
- [7, 3, 4, 5, 6, 0, 2, 8, 1]
- [8, 1, 0, 4, 3, 2, 5, 6, 7]
- [6, 5, 2, 7, 8, 1, 4, 0, 3]