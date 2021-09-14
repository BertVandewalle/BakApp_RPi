from PIL import Image
from PIL.ImageQt import ImageQt
from numpy import number
from image_functions import crop_max_square
from gui.core.functions import Functions
from models import *
from data_controller import DataController
from qt_core import *
import logging

class DataInitializer(QObject):
    playersSetupFinished = pyqtSignal()
    ranksSetupFinished = pyqtSignal()
    finished = pyqtSignal()
    players = []
    numberOfPlayers = int
    ranks = []
    duos = []
    lastGame = Game
    def __init__(self,dataController:DataController,settings,slot):
        super().__init__()
        self.count = 0
        self.dataController = dataController
        self.dataController.getPlayersResponse.connect(lambda e: self.addPlayers(e))
        self.dataController.getLastGameResponse.connect(lambda e: self.addLastGame(e))
        self.dataController.getRanksResponse.connect(lambda e: self.addRanks(e))
        self.dataController.getDuosResponse.connect(lambda e: self.addDuos(e))

        self.playersSetupFinished.connect(self.dataController.getLastGame)
        self.playersSetupFinished.connect(self.dataController.getDuos)
        self.ranksSetupFinished.connect(self.dataController.getPlayers)
        self.finished.connect(slot)

        self.dataController.getRanks()
        self.settings = settings

    def addPlayers(self,response):
        logging.warning("received playerResponse")
        for data in response:
            name = str(data.get('name'))
            id = str(data.get('id'))
            elo = str(data.get('elo'))
            rank_id = str(data.get('rankId'))
            for rank in self.ranks:
                if str(rank.id) == str(rank_id): player_rank = rank
            player = Player(id,name,elo=elo,rank=player_rank)
            player.image = self.settings['player_images'][name]
            pil_img = crop_max_square(Functions.set_image(player.image))
            pil_img.save('test.jpg')
            player.pixMap = QPixmap('test.jpg')
            print(player.pixMap)
            self.players.append(player)
        self.players.sort(key=lambda s : s.name)
        self.numberOfPlayers = len(self.players)
        logging.warning("Player Setup finished")
        self.count += 1
        self.checkIfFinished()
        self.playersSetupFinished.emit()

    def addLastGame(self,response):
        logging.warning("adding LastGame")
        game = response[0]
        self.lastGame = Game()
        self.lastGame.players = [self.findPlayerFromId(players=self.players,id=game.get('redDefId')),
                                self.findPlayerFromId(players=self.players,id=game.get('redOffId')),
                                self.findPlayerFromId(players=self.players,id=game.get('greDefId')),
                                self.findPlayerFromId(players=self.players,id=game.get('greOffId'))]
        self.lastGame.scores = [game.get('redDefScore'),
                                game.get('redOffScore'),
                                game.get('greDefScore'),
                                game.get('greOffScore')]

        self.lastGame.duration = game.get('duration')
        self.lastGame.startDateTime = game.get('startDateTime')
        self.lastGame.deltaElo = [game.get('redDefDeltaElo'),
                                game.get('redOffDeltaElo'),
                                game.get('greDefDeltaElo'),
                                game.get('greOffDeltaElo'),]

        self.count += 1
        print(self.lastGame.scores)
        self.checkIfFinished()    
        

    def addRanks(self,response):
        logging.warning("adding ranks")
        for data in response:
            id = str(data.get('id'))
            division = str(data.get('division'))
            subDivision = str(data.get('subDivision'))
            lowerbound = int(data.get('lowerBound'))
            upperbound = int(data.get('upperBound'))
            rank = Rank(id,division,subDivision,lowerbound,upperbound)
            self.ranks.append(rank)
        self.count += 1
        self.ranksSetupFinished.emit()
        self.checkIfFinished()

    def checkIfFinished(self):
        logging.warning("setup finished")
        if self.count == 4:
            self.finished.emit()

    def findPlayerFromId(self, players=None, id:str=None):
            for p in players: 
                if str(p.id) == str(id): return p
            #logging.error(f"player with id {id} not found in {players}") 

    def addDuos(self,response):
        logging.warning("adding duos")
        for data in response:
            def_player_id = data.get('defPlayerId')
            def_player = self.findPlayerFromId(self.players,def_player_id)
            off_player_id = data.get('offPlayerId')
            off_player = self.findPlayerFromId(self.players,off_player_id)
            winrate = float(data.get('winRate'))
            number_of_games = int(data.get('numberOfGames'))
            duo = Duo(def_player,off_player,winrate,number_of_games)
            self.duos.append(duo)
        self.count += 1
        self.checkIfFinished()