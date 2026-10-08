from strumento import Strumento
from prestito import Prestito
from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = []
        self.lista_prestiti = []


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        from csv import reader
        with open(file_path) as csv_file:
            csv_reader = reader(csv_file)
            for i, line in enumerate(csv_reader):
                if i == 0:
                    continue
                codice = line[0]
                tipo = line[1]
                marca = line[2]
                anno_acquisto = line[3]
                valore = line[4]

                strumento = Strumento(codice, tipo, marca, anno_acquisto, valore)
                self.strumenti.append(strumento)



    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        if len(self.strumenti) == 0:
            nuovo_codice = "S1"
        else:
            ultimo_elemento = self.strumenti[-1]
            codice_ultimo = ultimo_elemento.id
            numero = int(codice_ultimo[1:]) + 1
            nuovo_codice = "S" + str(numero)

        nuovo_strumento = Strumento(nuovo_codice, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(nuovo_strumento)
        return nuovo_strumento


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        self.strumenti.sort(key=attrgetter("marca"))
        return self.strumenti


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        esiste = False
        for elemento in self.strumenti:
            if elemento.id == id_strumento:
                esiste = True
        if not esiste:
            raise Exception("Strumento non trovato nel sistema.")

        for nuovo in self.lista_prestiti:
            if nuovo.id_strumento == id_strumento:
                raise Exception("Strumento già in prestito.")

        lunghezza = len(self.lista_prestiti) + 1
        id_prestito = "P" + str(lunghezza)

        prestito = Prestito(data, id_strumento, cognome_allievo, id_prestito)
        self.lista_prestiti.append(prestito)
        return prestito


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        condizione = True
        for termine in self.lista_prestiti:
            if termine.id_prestito == id_prestito:
                self.lista_prestiti.remove(termine)
                condizione = False

        if condizione:
            raise Exception("Prestito non trovato nel sistema.")