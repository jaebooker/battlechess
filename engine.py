#!/usr/bin/env python3
import sys
import time
import random
import chess

def get_move(board, limit=None):
  # TODO: Fill this in with an actual chess engine
  # choice = list(board.legal_moves)
  # for i in choice:
  #     if i.Piece == "Q":
  #         return i
  # newBoard = board.mirror()
  # move = newBoard.peek()
  counter = 0
  while counter < 100:
      move = random.choice(list(board.legal_moves))
      if board.is_capture(move):
          return move
      counter += 1
  # if board.is_into_check(move):
  #     move = random.choice(list(board.legal_moves))
  # def minimax(board, depth=0, maximizingPlayer=1):
  #   if (depth = 0) or (node == terminal.node):
  #       return depth
  #   if maximizingPlayer:
  #       value := −∞
  #       for each child of node do
  #           value := max(value, minimax(child, depth − 1, FALSE))
  #       return value
  #   else (* minimizing player *)
  #       value := +∞
  #       for each child of node do
  #           value := min(value, minimax(child, depth − 1, TRUE))
  #       return value
  #print("playing", move, file=sys.stderr)
  #move = random.choice(list(board.legal_moves))
  return move

if __name__ == "__main__":
  while 1:
    cmd = input().split(" ")
    #print(cmd, file=sys.stderr)

    if cmd[0] == "uci":
      print("uciok")
    elif cmd[0] == "ucinewgame":
      pass
    elif cmd[0] == "isready":
      print("readyok")
    elif cmd[0] == "position":
      if cmd[1] == "startpos":
        board = chess.Board()
        if len(cmd) > 2 and cmd[2] == "moves":
          for m in cmd[3:]:
            board.push(chess.Move.from_uci(m))
    elif cmd[0] == "go":
      if len(cmd) > 1 and cmd[1] == "movetime":
        move = get_move(board, limit=int(cmd[2]))
      else:
        move = get_move(board)
      print("bestmove %s" % move)
    elif cmd[0] == "quit":
      exit(0)
