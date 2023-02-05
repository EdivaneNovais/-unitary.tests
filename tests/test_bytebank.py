from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        #Given-Contexto
        entrada = '13/03/2000'
        esperado = 23
        
        funconario_teste = Funcionario('Test', entrada, 1111)
        #When-ação
        resultado = funconario_teste.idade()
        
        #Then-Desfecho
        assert resultado == esperado
        
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' #Given
        esperado = 'Carvalho'
        
        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()#when
        
        assert resultado == esperado #then
        
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada = 100000 # given
        esperado = 90000
        
        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
        
        funcionario_teste.decrescimo_salario()# when
        resultado = funcionario_teste.salario
        
        assert resultado == esperado # then