import datetime
from models import *
from qt_core import *
from gui.core.json_settings import Settings
import json
import logging

class DataController(QObject):
    # Signals
    # ///////////////////////////////////////////////////////////////
    # Signal to indicate getPlayers request is completed
    getPlayersResponse = pyqtSignal(list)
    # Signal to indicate getRanks request is completed
    getRanksResponse = pyqtSignal(list)
    getDuosResponse = pyqtSignal(list)
    getLastGameResponse = pyqtSignal(list)
    getGamesTodayResponse = pyqtSignal(list)
    postGameFinished = pyqtSignal()

    def __init__(self):
        super().__init__()
        settings = Settings()
        self.settings = settings.items
        self.apiUrl = self.settings['apiURL']
        self.nam = QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)

    # Handle response from http requests
    # ///////////////////////////////////////////////////////////////
    def handleResponse(self,reply:QNetworkReply):
        er = reply.error()
        
        if er == QNetworkReply.NoError:
    
            bytes_string = reply.readAll()
            jsonText = bytes(bytes_string)
            output = json.loads(jsonText)
            #print("output" + str(output))
            logging.warning("response received")
            if str(reply.property("login")) == "getPlayers":
                self.handleGetPlayersResponse(output)
            elif str(reply.property("login")) == "postGame":
                self.handlePostGameResponse(output)
            elif str(reply.property("login")) == "getLastGame":
                self.handleGetLastGameResponse(output)
            elif str(reply.property("login")) == "getRanks":
                self.handleGetRanksResponse(output)
            elif str(reply.property("login")) == "getDuos":
                self.handleGetDuosResponse(output)
            elif str(reply.property("login")) == "getGamesToday":
                self.handleGetGamesTodayResponse(output)
        else:
            print(reply.errorString())

    # Get all player data
    # ///////////////////////////////////////////////////////////////
    def getPlayers(self):
        self.url = self.apiUrl + "/Player"
        req = QNetworkRequest(QUrl(self.url))
        logging.warning("getPlayers")
        reply = self.nam.get(req)
        reply.setProperty("login",QVariant("getPlayers"))

    def handleGetPlayersResponse(self,response):
        logging.warning("handling getPlayersResponse")
        try:
            self.getPlayersResponse.emit(response)
        except:
            logging.warning("could not emit getPlayersResponse")
            #print(str(response))

    # Get last Game
    # ///////////////////////////////////////////////////////////////
    def getLastGame(self):
        self.url = self.apiUrl + "/Game?PageNumber=1&PageSize=1"
        req = QNetworkRequest(QUrl(self.url))
        logging.warning("getLastGame")
        reply = self.nam.get(req)
        reply.setProperty("login",QVariant("getLastGame"))

    def handleGetLastGameResponse(self,response):
        logging.info("handling getLastGameResponse")
        try:
            self.getLastGameResponse.emit(response)
        except:
            logging.warning("failed to emit LastGameRespones")
            #print(str(response))
    
    # Get today games
    # ///////////////////////////////////////////////////////////////
    def getGamesToday(self):
        self.url = self.apiUrl + "/Game/Today"
        req = QNetworkRequest(QUrl(self.url))
        logging.warning("getGamesToday")
        reply = self.nam.get(req)
        reply.setProperty("login",QVariant("getGamesToday"))

    def handleGetGamesTodayResponse(self,response):
        logging.info("handling getGamesTodayResponse")
        try:
            self.getGamesTodayResponse.emit(response)
        except:
            logging.warning("failed to emit GetGamesTodayRespones")
            #print(str(response))



    # Get all rank data
    # ///////////////////////////////////////////////////////////////
    def getRanks(self):
        logging.warning("getRanks")
        self.url = self.apiUrl + "/Rank"
        req = QNetworkRequest(QUrl(self.url))
        reply = self.nam.get(req)
        reply.setProperty("login",QVariant("getRanks"))

    def handleGetRanksResponse(self,response):
        logging.info("handling getRanksResponse")
        try:
            self.getRanksResponse.emit(response)
        except:
            logging.warning("could not emit getRanksResponse")
            #print(str(response))                


    # Get all duo data
    # ///////////////////////////////////////////////////////////////
    def getDuos(self):
        logging.warning("getDuos")
        self.url = self.apiUrl + "/Duo"
        req = QNetworkRequest(QUrl(self.url))
        reply = self.nam.get(req)
        reply.setProperty("login",QVariant("getDuos"))

    def handleGetDuosResponse(self,response):
        logging.info("handling getDusResponse")
        try:
            self.getDuosResponse.emit(response)
        except:
            logging.warning("could not emit getDuosResponse")
            #print(str(response))

    # Post current game
    # ///////////////////////////////////////////////////////////////
    def postGame(self,game:Game):
        self.game = game
        url = self.apiUrl + "/Game"
        req = QNetworkRequest(QUrl(url))
        req.setHeader(QNetworkRequest.ContentTypeHeader,
            'application/json')
        try:
            input= {'redDefId':game.players[0].id,
                    'redOffId':game.players[1].id,
                    'greDefId':game.players[2].id,
                    'greOffId':game.players[3].id,
                    'redDefScore':game.scores[0],
                    'redOffScore':game.scores[1],
                    'greDefScore':game.scores[2],
                    'greOffScore':game.scores[3],
                    'startDateTime':game.startDateTime.toString("yyyy-MM-ddThh:mm:ssZ"),
                    'duration':str(datetime.timedelta(seconds=game.duration))}
            
            test = QJsonDocument(input)
            reply = self.nam.post(req,test.toJson())
            reply.setProperty("login",QVariant("postGame"))

        except:
            print("game attributes not yet initialized properly")

    # Post all goals from game
    def postGoal(self,gameId,playerId,time):
        url = self.apiUrl + "/Goal"
        req = QNetworkRequest(QUrl(url))
        req.setHeader(QNetworkRequest.ContentTypeHeader,
            'application/json')

        input = {
                'gameId':gameId,
                'playerId':playerId,
                'time':time
                }

        inputDoc = QJsonDocument(input)
        reply = self.nam.post(req,inputDoc.toJson())
        reply.setProperty("login",QVariant("postGoal"))        
        

    def handlePostGameResponse(self,response):
        try:
            gameId = response[0]
            goals = self.game.goals
            for goal in goals:
                self.postGoal(gameId,goal.player.id,str(datetime.timedelta(seconds=goal.time)))
            self.postGameFinished.emit()
        except:
            print("No valid game to post goals")
