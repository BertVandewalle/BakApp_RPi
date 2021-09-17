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
    gamesToday = [Game]
    def __init__(self,dataController:DataController,settings,slot):
        super().__init__()
        self.count = 0
        self.dataController = dataController
        self.dataController.getPlayersResponse.connect(lambda e: self.addPlayers(e))
        self.dataController.getLastGameResponse.connect(lambda e: self.addLastGame(e))
        self.dataController.getRanksResponse.connect(lambda e: self.addRanks(e))
        self.dataController.getDuosResponse.connect(lambda e: self.addDuos(e))
        self.dataController.getGamesTodayResponse.connect(lambda e: self.addGamesToday(e))
        self.dataController.postGameFinished.connect(self.updateModels)


        self.ranksSetupFinished.connect(self.dataController.getPlayers)

        self.playersSetupFinished.connect(self.dataController.getLastGame)
        self.playersSetupFinished.connect(self.dataController.getDuos)
        self.playersSetupFinished.connect(self.dataController.getGamesToday)

        self.finished.connect(slot)

        self.updateModels()
        self.settings = settings

    def addPlayers(self,response):
        logging.warning("received playerResponse")
        self.players = []
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
        self.lastGame.deltaEloTotal = [game.get('redDefDeltaElo'),
                                game.get('redOffDeltaElo'),
                                game.get('greDefDeltaElo'),
                                game.get('greOffDeltaElo')]
        self.lastGame.deltaEloBase = [game.get('eloRedDefBase'),
                                game.get('eloRedOffBase'),
                                game.get('eloGreDefBase'),
                                game.get('eloGreOffBase')]

        self.lastGame.deltaEloIndividualBonus = [game.get('eloRedDefBonus'),
                                game.get('eloRedOffBonus'),
                                game.get('eloGreDefBonus'),
                                game.get('eloGreOffBonus')]
        self.lastGame.deltaEloTeamBonus = [game.get('eloRedTeamBonus'),
                                game.get('eloRedTeamBonus'),
                                game.get('eloGreTeamBonus'),
                                game.get('eloGreTeamBonus')]

        self.count += 1
        self.checkIfFinished()    
    
    def addGamesToday(self,response):
        logging.warning("add GamesToday")
        self.gamesToday = []
        for data in response:
            game = Game()
            game.players = [self.findPlayerFromId(players=self.players,id=data.get('redDefId')),
                                self.findPlayerFromId(players=self.players,id=data.get('redOffId')),
                                self.findPlayerFromId(players=self.players,id=data.get('greDefId')),
                                self.findPlayerFromId(players=self.players,id=data.get('greOffId'))]
            game.scores = [data.get('redDefScore'),
                                    data.get('redOffScore'),
                                    data.get('greDefScore'),
                                    data.get('greOffScore')]

            game.duration = data.get('duration')
            game.startDateTime = data.get('startDateTime')
            game.deltaEloTotal = [data.get('redDefDeltaElo'),
                                data.get('redOffDeltaElo'),
                                data.get('greDefDeltaElo'),
                                data.get('greOffDeltaElo')]
            game.deltaEloBase = [data.get('eloRedDefBase'),
                                data.get('eloRedOffBase'),
                                data.get('eloGreDefBase'),
                                data.get('eloGreOffBase')]

            game.deltaEloIndividualBonus = [data.get('eloRedDefBonus'),
                                data.get('eloRedOffBonus'),
                                data.get('eloGreDefBonus'),
                                data.get('eloGreOffBonus')]
            game.deltaEloTeamBonus = [data.get('eloRedTeamBonus'),
                                data.get('eloRedTeamBonus'),
                                data.get('eloGreTeamBonus'),
                                data.get('eloGreTeamBonus')]
            self.gamesToday.append(game)

        self.count += 1
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
        if self.count == 5:
            logging.warning("setup finished")

            self.finished.emit()

    def findPlayerFromId(self, players=None, id:str=None):
            for p in players: 
                if str(p.id) == str(id): return p
            #logging.error(f"player with id {id} not found in {players}") 

    def addDuos(self,response):
        logging.warning("adding duos")
        self.duos =[]
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

    def updateModels(self):
        self.count = 0
        self.dataController.getRanks()

