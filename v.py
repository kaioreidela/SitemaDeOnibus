import random
class Pessoa:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo 
        
  
class Cartao (Pessoa):
    def __init__(self,numero, nome, saldo, saldoCartao):
         super().__init__(nome, saldo )
         self.numero = numero 
         self.saldoCartao = saldoCartao
              
class Cadeira:
    def __init__(self,numero, sentado):
        self.numero = numero 
        self.sentado = sentado
     
def verificaCartao(Cartao):
    if Cartao.numero == "":
        existe = False
    return existe
           
def criaCartao(Pessoa):
    dinheiro =int(input("quanto vc quer por no cartao"))
    if dinheiro <Pessoa.saldo:
        print("saldo insuficiente")
    else: 
        saldoCartao = saldoCartao + dinheiro 
        numero = int(random.randit(34,100))
        if __name__ == "__main__":
            pessoa12 = Cartao(numero,Pessoa.nome, Pessoa.saldo,saldoCartao)
    return pessoa12
               
def criarPessoa():
    nome = input("Digite o seu nome: ")
    saldo = int(input("Digite o seu saldo: "))
    if __name__ == "__main__":
        pessoa1 = Pessoa(nome, saldo)
    return pessoa1

if __name__ == "__main__":
    cadeira1 = Cadeira(1,True)
    cadeira2 = Cadeira(2,True)
    cadeira3 = Cadeira(3,True)
    cadeira4 = Cadeira(4,False)
    cadeira5 = Cadeira(5,True)

def passarNaCatraca(Cartao):
    verCartao = verificaCartao(Cartao)
    passou = False
    print("digite s para saldo e c para cartao\n")
    forma = input("forma de pagamento saldo ou cartao:\n")
    if forma == "s":
        if Cartao.saldo>= 4:
            passou = True
            print("vc passou\n",Cartao.nome)
            print("numero do cartao\n", Cartao.numero)
            print("seu saldo é\n", Cartao.saldo - 4.00)
        else:
            print("sai liso")   
    elif forma == "c":
        if verCartao == True:
            if  Cartao.saldoCartao>= 2.00:
                passou = True
                print("vc passou\n",Cartao.nome)
                print("numero do cartao\n", Cartao.numero)
                print("seu saldo do cartão é\n", Cartao.saldoCartao - 2.00)    
            else:
                print("sai liso") 
        else:
            print("usuario sem cartao")              
    elif forma != "c" or "s":
        print("opção invalida\n")
            
def escolherCadeira(Cadeira):
    ocupada = True
    if Cadeira.sentado == True:
        print("essa cadeira ta ocupada por")
        ocupada = True
    else:
        print("essa cadeira esta vazia") 
        ocupada = False 
        print("vc sentou na cadeira numero",Cadeira.numero) 

def fazer():
    pessoa = pessoa1
    fazer = input("deseja criar o cartao s ou n")
    if fazer == "s":
        pessoaCartao1 = criaCartao(pessoa)
    if fazer == "n":
        pessoaCartao1 =  Cartao("",pessoa.nome, pessoa.saldo,"")    
    return pessoaCartao1
pessoa1 = criarPessoa()
pessoa1 = fazer()
passarNaCatraca(pessoa1)
