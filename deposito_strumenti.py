from strumento import Strumento

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        from csv import reader
        try:
            with open(file_path) as csv_file:
                dizionario = {}
                csv_reader = reader(open(file_path))
                for i, line in enumerate(csv_file):
                    if i == 0:
                        continue
                    codice = line[0]
                    tipo = line[1]
                    marca = line[2]
                    anno_acquisto = line[3]
                    valore = line[4]


        except FileNotFoundError:
            print("File non trovato")
            break



    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
