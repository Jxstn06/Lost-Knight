from sqlobject import *

sqlhub.processConnection = connectionForURI('sqlite:Spieler.sqlite')


class Spieler(SQLObject):
    Name = StringCol()
    Level = StringCol()
    Leben = IntCol()
    Kraft = IntCol()
    Verteidigung = IntCol()
    X = IntCol()
    Y = IntCol()

# Existiert ja
# Spieler.createTable(ifNotExists=True)
