## Deployment

Testailtuamme eri koneenoppimismalleja päädyimme käyttämään lähintänaapuria tässä sovelluksessa, koska sillä pääsimme parhaaseen tulokseen. Tarkoituksena oli tuottaa sovellus, joka auttaisi automyymälän työntekijöitä arvioimaan auton hintaa paremmin ja näin ollen saamaan sille parhaan hinnan, joka tyydyttäisi autokauppaa ja ostajaa. Sovellus on tällä hetkellä ihan koevedos ja lähinnä sitä on testailtu, että kaikki toimii. Se pyörii myös lokaalisti eikä sitä ole sen kummemmin viety mihinkään. Olemme kuitenkin demonneet sovelluksen käyttöä, jotta siitä saisi vähän kuvaa mitä olemme hakeneet takaa. Päädyimme siis arvioimaan auton hintaa mahdollisimman tarkasti. Alla on muutama kohta mitä tulisi ottaa huomioon, kun lähdetään sovellusta tuomaan automyymälän käyttöön.

### Yhteenvetoa sovelluksen tuomisesta käyttöön

Ensin tulisi valita käyttöalusta millä tätä tullaan käyttämään. Meillä se toimii vielä omalla koneella, koska kyseessä on vielä keskeneräinen sovellus ja sitä ei vielä ole tuotu kunnolla käyttöön. Tämän jälkeen olemme optimoineet koodia, jotta se toimisi mahdollisimman hyvin. Sovellukseen tulisi varmasti myöhemmin tehdä tarkastus menetelmä, jolla tulokset voisi tarkistaa ja katsoa, että ne pitävät paikkansa. Tämä tulee kuitenkin vastaan vasta myöhemmin. Jos sovellus tuotaisiin käyttöön pitäisi miettiä mitä taustajärjestelmää käytetään, jotta saadaan auton tiedot syötettyä ja haettua oikea hinta autolle. Tähän tarvisi suunnitella myös testausmenetelmä millä API:n toimivuutta ja luotettavuutta voitaisiin testata. 

Olemme tällä hetkellä suunnitelleet sovelluksen käyttäen Pythonin Streamlit-kirjastoa ja tässä ei pääse hirveästi vaikuttamaan käyttöliittymän ulkonäköön. Myöhemmässä vaiheessa, jos todetaan, että sovellus tuotaisiin käyttöön tulisi käyttöliittymää kehittää myös parempaan suntaan ja käyttäjäystävällisemmäksi. 

Sovelluksen käyttöönotto tulisi suunnitella myös tarkasti ja kuvata/ohjeistaa vaiheet miten mennään eteenpäin. Käyttöönoton jälkeen tulisi sovellusta testata ja varmistua siitä, että kaikki toimii niinkuin pitää. Sovelluksen käyttöönoton jälkeen pitää miettiä miten tulemme seuraamaan, että kaikki toimii ja varmistetaan, että sovelluksella on tarvittava ylläpito. 

Tietysti kaikki vaiheet on dokumentoitava ja kirjoitettava kattava ohjeistus siitä miten sovellus tulee toimimaan ja miten ongelma tilanteessa tulee toimia. Varmistetaan myös, että työntekijöille järjestään tarvittava koulutus sovelluksen käytöstä. 


Alla vielä demo sovelluksesta: 

[Sovelluksen demo](testeja/Video/video5931722744.mp4)




