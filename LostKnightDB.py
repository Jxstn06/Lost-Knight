from sqlobject import *

sqlhub.processConnection = connectionForURI('sqlite:Spieler.sqlite')


class Spieler(SQLObject):
    Name = StringCol()
    Level = IntCol()
    Leben = IntCol()
    Kraft = IntCol()
    Verteidigung = IntCol()
    X = IntCol()
    Y = IntCol()
    Maze = StringCol()


# Existiert ja
Spieler.createTable(ifNotExists=True)
