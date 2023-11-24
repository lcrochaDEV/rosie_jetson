from ControllerClass import ControllerCar;
import time as time

supremaseminovos = ControllerCar.ControllerCar(
   "SUPREMA SEMINOVOS", 
   "https://www.supremaseminovos.com.br/Veiculos", 
   "//h4 [@class='result-item-title']", #CAR
   "//div [@class='price']", #VALOR
   "//h4 [@class='result-item-title']// a[contains(string(), 'FIAT ARGO')]", #FILTRO
   "//div [contains(text(), '')]", #FILTROVALOR
   "//li [@class='primeiro']", #ANO
   "//li [@class='usado']", #KM
)

seminovoslocaliza = ControllerCar.ControllerCar(
    "LOCALIZA SEMINOVOS", 
    "https://seminovos.localiza.com/carros/rj-rio-de-janeiro?cidade=rj-rio-de-janeiro", 
    "//h1[@class='title-car']", #CAR
    "//span [@class='text-price']", #VALOR
    "//h2 [contains(string(), 'ARGO')]", #FILTRO
    "//span [contains(text(), '')]", #FILTROVALOR
    "//span [@class='text-km']", #ANO
    "//span [@class='text-milage']", #KM
)

seminovosmovida = ControllerCar.ControllerCar(
    "SEMINOVOS MOVIDA", 
    "https://www.seminovosmovida.com.br/busca", 
    "//div [@class='info__title']//p", #CAR
    "//div [@class='price']//label [@_ngcontent-serverapp-c66]", #VALOR
    "//p [contains(string(), 'Fiat Argo')]", #FILTRO
    "//span [contains(text(), '')]", #FILTROVALOR
    "//p [@class='add__info'] //span", #ANO
    "//p [@class='add__info'] //span" #KM
)

while True: # EXECUTA O COMANDO DE HORA EM HORA
    supremaseminovos.varrerDados()
    seminovoslocaliza.varrerDados()
    seminovosmovida.varrerDados()
    time.sleep(3600)
#//span[@title='Maria Louca']



