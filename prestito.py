class Prestito:
    def __init__(self, data, id_strumento, cognome_allievo, id_prestito):

        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo
        self.id_prestito = id_prestito

    def __str__(self):
        return f"{self.data}, {self.id_strumento}, {self.cognome_allievo}, {self.id_prestito}"