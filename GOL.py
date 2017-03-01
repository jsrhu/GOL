"""
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
GOL.py
Created on 2017-02-14T15:48:00Z
@author:Joshua Hu
"""
from __future__ import print_function

import sys
import numpy as np

alive = 'ALIVE'
dead = 'DEAD'

class Board(object):
    def __init__(self, rows = 1, columns = 1, turn_speed = 1, max_turns = 0, initial_state = [[]]):
        self._rows = rows
        self._columns = columns
        self._world = self.buildWorld(rows = rows, columns = columns)
        self._turn_speed = turn_speed
        self._max_turns = max_turns
        self._initial_state = initial_state

    def rows():
        doc = "The rows property."
        def fget(self):
            return self._rows
        def fset(self, value):
            self._rows = value
        def fdel(self):
            del self._rows
        return locals()
    rows = property(**rows())

    def columns():
        doc = "The columns property."
        def fget(self):
            return self._columns
        def fset(self, value):
            self._columns = value
        def fdel(self):
            del self._columns
        return locals()
    columns = property(**columns())

    def world():
        doc = "The world property."
        def fget(self):
            return self._world
        def fset(self, value):
            self._world = value
        def fdel(self):
            del self._world
        return locals()
    world = property(**world())

    def turn_speed():
        doc = "The turn_speed property."
        def fget(self):
            return self._turn_speed
        def fset(self, value):
            self._turn_speed = value
        def fdel(self):
            del self._turn_speed
        return locals()
    turn_speed = property(**turn_speed())

    def max_turns():
        doc = "The max_turns property."
        def fget(self):
            return self._max_turns
        def fset(self, value):
            self._max_turns = value
        def fdel(self):
            del self._max_turns
        return locals()
    max_turns = property(**max_turns())

    def initial_state():
        doc = "The initial_state property."
        def fget(self):
            return self._initial_state
        def fset(self, value):
            self._initial_state = value
        def fdel(self):
            del self._initial_state
        return locals()
    initial_state = property(**initial_state())

    """
    CLASS METHODS
    """
    """
    PRIVATE
    """

    """
    PUBLIC
    """
    def buildWorld(self, rows, columns):
        return [[Cell(row = row+1, column = column+1) for column in xrange(columns)] for row in xrange(rows)]

    def printWorld(self):
        for row in self.world:
            for cell in row:
                if cell.state[dead] == True:
                    print('X', end=' ')
                elif cell.state[alive] == True:
                    print('O', end=' ')
            print()
        # print all elements to command line for now X:DEAD, O:ALIVE

class Cell(object):
    '''
    Rules for life:
    <2 neighbours = dead
    >2 <3 neighbours = alive
    >3 neighbours = dead
    == 3 neighbours = born (new alive)
    '''
    def __init__(self, row, column):
        self._row = row
        self._column = column
        self._state = {dead: True, alive: False}

    def row():
        doc = "The row property."
        def fget(self):
            return self._row
        def fset(self, value):
            self._row = value
        def fdel(self):
            del self._row
        return locals()
    row = property(**row())

    def column():
        doc = "The column property."
        def fget(self):
            return self._column
        def fset(self, value):
            self._column = value
        def fdel(self):
            del self._column
        return locals()
    column = property(**column())

    def state():
        doc = "The state property."
        def fget(self):
            return self._state
        def fset(self, value_state):
            if value_state == dead:
                self._state[dead] = True
                self._state[alive] = False
            elif value_state == alive:
                self._state[dead] = False
                self._state[alive] = True
        def fdel(self):
            del self._state
        return locals()
    state = property(**state())

    def getNeighbours(self,board):
        return board.world[self.row-2:self.row+1 , self.column-2:self.column+1]

    def checkNeighbours(self, board):
        neighbours = self.getNeighbours(board = board)
        count_neighbour = 0
        for row in xrange(len(neighbours)):
            for column in xrange(row):
                if id(neighbours[row][column]) == id(self):
                    pass
                if neighbours[row][column].state[alive] == True:
                    count_neighbour += 1
        return count_neighbour

    def updateState(self, neighbours = 0):
        if neighbours < 2:
            self.state = dead
        elif neighbours >= 2 and neighbours <= 3:
            self.state = alive
        elif neighbours > 3:
            self.state = dead

def main(argv):
    rows = int(argv[1])
    columns = int(argv[2])

    """
    print('rows:',rows,'\ncolumns:',columns)
    print(type(rows),type(columns))
    """

    board = Board(rows = rows, columns = columns)

    board.printWorld()

if __name__ == '__main__':
    main(sys.argv)
