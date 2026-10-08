class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.id = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = int(anno_acquisto)
        self.valor = float(valore)

        def __str__(self):
            return f"[{self.id_strumento}] {self.tipo} {self.marca} - €{self.valore}"
