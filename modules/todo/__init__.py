#! /usr/bin/python
# -*- coding: utf-8 -*-
import todo

if __name__ == '__main__':
    #Placer ici les tests unitaires
    pass
else:
    from .. import register
    register(__name__, todo.CmdTodo)
