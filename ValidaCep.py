import requests


class EnderecoCep:

    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def retorna_endereco(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        if 'erro' in dados:
            raise ValueError('CEP inválido!')
        else:
            return (
                dados['cep'],
                dados['logradouro'],
                dados['localidade'],
                dados['uf'])
