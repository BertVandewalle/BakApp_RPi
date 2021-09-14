import sys
sys.path.append('../BakApp_RPi')
from models import *
from data_controller import DataController
from PyQt5 import QtCore, QtGui, QtNetwork
import sys
import logging
import json
import datetime     
import time 
import requests
import pandas as pd
      
class DataBaseInitializer:
  
    playerNames = ['Bert',
                    'Guest',
                    'Jonas',
                    'Karel',
                    'Louis',
                    'Matthijs',
                    'Nicolas',
                    'Coghe',
                    'Stef D',
                    'Tiemen'
                    ]
    #API_URL = "https://localhost:44321/api"
    API_URL = 'https://bakapp.bertvandewalle.com/api'
    def __init__(self):    
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.cafile = requests.certs.where()
        self.deleteGames()
        self.deletePlayers()
        self.postPlayers()
        self.initGames()
        print("finished")
            # if (self.playerNames.index(name)==0):
            #     time.sleep(5)
            # else:
            #     time.sleep(1)

      

    def initGames(self):
        # self.dtc = DataController()
        # self.initData = DataBaseInitializer()
        self.players = []
        url = self.API_URL + "/Player"
        x = requests.get(url,verify=self.cafile)
        reply = x.json()
        print(json.dumps(reply,indent=4))
        for data in reply:
            name = data.get('name')
            id = data.get('id')
            elo = data.get('elo')
            rankId = data.get('rankId')
            player = Player(id,name,elo,rankId)
            self.players.append(player)
        self.df_sheet_s4 = pd.read_excel('historic_data\\gameHistory.xlsx',sheet_name='Season 4')
        for i in range(33):
            redDefId = [player.id for player in self.players if player.name == self.df_sheet_s4["Rood Verdediging"][i].rstrip()]
            redOffId = [player.id for player in self.players if player.name == self.df_sheet_s4["Rood Aanval"][i].rstrip()]
            greDefId = [player.id for player in self.players if player.name == self.df_sheet_s4["Groen Verdediging"][i].rstrip()]
            greOffId = [player.id for player in self.players if player.name == self.df_sheet_s4["Groen Aanval"][i].rstrip()]
            #print(redDefId)
            redDefScore = int(self.df_sheet_s4["Score"][i])
            redOffScore = int(self.df_sheet_s4["Score2"][i])
            greDefScore = int(self.df_sheet_s4["Score3"][i])
            greOffScore = int(self.df_sheet_s4["Score4"][i])
            game = {
                'redDefId':redDefId[0],
                'redOffId':redOffId[0],
                'greDefId':greDefId[0],
                'greOffId':greOffId[0],
                'redDefScore':redDefScore,
                'redOffScore':redOffScore,
                'greDefScore':greDefScore,
                'greOffScore':greOffScore
            }
            url = self.API_URL + "/Game"
            x = requests.post(url,json=game,verify=self.cafile)
            data = x.json()
            print(json.dumps(data,indent=4))
            gameId=data[0]
            url = self.API_URL + "/Goal"
            for i in range(redDefScore):
                input = {
                    'gameId':gameId,
                    'playerId':redDefId[0],
                }
                requests.post(url,json=input,verify=self.cafile)
            for i in range(redOffScore):
                input = {
                    'gameId':gameId,
                    'playerId':redOffId[0],
                }
                requests.post(url,json=input,verify=self.cafile)
            for i in range(greDefScore):
                input = {
                    'gameId':gameId,
                    'playerId':greDefId[0],
                }
                requests.post(url,json=input,verify=self.cafile)
            for i in range(greOffScore):
                input = {
                    'gameId':gameId,
                    'playerId':greOffId[0],
                }
                requests.post(url,json=input,verify=self.cafile)

        # self.game = {} 
        # input= {    'redDefId':game.players[0].id,
        #             'redOffId':game.players[1].id,
        #             'greDefId':game.players[2].id,
        #             'greOffId':game.players[3].id,
        #             'redDefScore':game.scores[0],
        #             'redOffScore':game.scores[1],
        #             'greDefScore':game.scores[2],
        #             'greOffScore':game.scores[3],
        #             'startDateTime':game.startDateTime.toString("yyyy-MM-ddThh:mm:ssZ"),
        #             'duration':str(datetime.timedelta(seconds=game.duration
        # print(self.df_sheet_s4["Score"][0])
        

    def deleteGames(self):
        url = self.API_URL + "/Game"
        r = requests.delete(url,verify=self.cafile)
        print(r.text)

    def deletePlayers(self):
        url = self.API_URL + "/Player"
        r = requests.delete(url,verify=self.cafile)
        print(r.text)
    def postPlayerOld(self,name):
        url = self.API_URL + "/Player"
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        req.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader,
            'application/json')

        input= {'name':str(name),'elo':str(2000)}
        inputDoc = QtCore.QJsonDocument(input)
        self.nam.post(req,inputDoc.toJson())
    def postPlayers(self):
        for name in self.playerNames:
            self.postPlayer(name)

    def postPlayer(self,name):
        url = self.API_URL + "/Player"
        #url ='https://httpbin.org/post'
        data = {'name':name,'elo':2000}
        x = requests.post(url,json=data,verify=self.cafile)
        print(x.text)
 

    def doRequest(self):   
    
        url = "https://localhost:44321/api/Player"
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.nam.get(req)
        

        
        url = "https://localhost:44321/api/Game"
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        req.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader,
            'application/json')

        input= {'redDefId':4,'RedOffId':2,'GreDefId':3,'GreOffId':1}
        test = QtCore.QJsonDocument(input)
        #self.nam.finished.connect(self.handleResponse)
        self.nam.post(req,test.toJson())

      
    def handleResponse(self, reply):

        er = reply.error()
        
        if er == QtNetwork.QNetworkReply.NoError:
    
            bytes_string = reply.readAll()
            jsonText = bytes(bytes_string)
            output = json.loads(jsonText)
            logging.warning("I will print response")
            # for player in output:
            #     print(player.get('name'))
            print(output)
            
        else:
            print("Error occured: ", er)
            print(reply.errorString())
            
        
        
if __name__ == '__main__':       
           
    ex = DataBaseInitializer()
