#!/usr/bin/env python3
import sys
import time
import random
import chess

# class Repeats(repeats,previous_move):
#     def _init_(self, repeats, previous_move):
#         self.repeats = repeats
#         self.previous_move = previous_move
# repeats = Repeats(0,None)
def check(board, move) -> bool:
    king = board.king(not board.turn)
    return king is not None and board.is_attacked_by(board.turn, king)
def enemy_into_check(board, move) -> bool:
        """
        Checks if the given move would leave the king in check or put it into
        check. The move must be at least pseudo legal.
        """
        king = board.king(not board.turn)
        if king is None:
            return False

        checkers = board.attackers_mask(board.turn, king)
        if checkers:
            # If already in check, look if it is an evasion.
            if move not in board._generate_evasions(checkers,king,BB_SQUARES[move.from_square], BB_SQUARES[move.to_square]):
                return True

        return not board._is_safe(king, board._slider_blockers(king), move)
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
      uci = board.uci(move)
      print(uci)
      copy = enemy_into_check(board, move)
      if copy == True:
          return move
      if board.is_capture(move):
          # if move == repeats.previous_move:
          #     if repeats.repeat == 3:
          #         move = random.choice(list(board.legal_moves))
          #         repeat = 0
          #         return move
          #     repeats.repeat += 1
          # else:
          #     repeats.repeat = 0
          # repeats.previous_move = move
          return move
      if board.is_castling(move):
          # if move == repeats.previous_move:
          #     if repeats.repeat == 3:
          #         move = random.choice(list(board.legal_moves))
          #         repeats.repeat = 0
          #         return move
          #     repeats.repeat += 1
          # else:
          #     repeats.repeat = 0
          # repeats.previous_move = move
          return move
      counter += 1
  counter = 0
  if board.is_repetition(2):
      move = random.choice(list(board.legal_moves))
      return move
  while counter < 10:
      move = random.choice(list(board.legal_moves))
      if board.is_irreversible(move):
          # if move == repeats.previous_move:
          #     if repeats.repeat == 3:
          #         move = random.choice(list(board.legal_moves))
          #         repeats.repeat = 0
          #         return move
          #     repeats.repeat += 1
          # repeats.previous_move = move
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
  # if move == repeats.previous_move:
  #     if repeats.repeat == 3:
  #         move = random.choice(list(board.legal_moves))
  #         repeats.repeat = 0
  #         return move
  #     repeats.repeat += 1
  # else:
  #     repeats.repeat = 0
  # repeats.previous_move = move
  move = random.choice(list(board.legal_moves))
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
