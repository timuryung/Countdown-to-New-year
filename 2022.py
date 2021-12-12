from pywebio.input import *
from pywebio.output import *
from pywebio import start_server

from time import sleep
import datetime



def main():

    def newyeardef(): #receiving time to new year
        newyear = datetime.datetime(datetime.datetime.today().year + 1, 1, 1, 0, 17)
        

        lefttonewyear = newyear - datetime.datetime.today()
        if newyear == datetime.datetime.today():
            newyeartext = 'Happy new' + ' ' + datetime.datetime.today().year + 1 + 'Year! \n'
            put_text(newyeartext * 6).style('font-size: 60px;')
            sleep(3153600)
        else:
            sleep(1)
            clear()
            yearstr = str(datetime.datetime.today().year + 1)
            put_html('<center> Until the New Year' +  ' ' + yearstr + ', exactly </center>').style('font-size : 60px')
            put_text(lefttonewyear).style('font-size : 60px; align : center')
            
            



    while True:
        newyeardef()

start_server(main, port=3588)





         



