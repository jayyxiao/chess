
from Node import ChessNode
from Engine import ChessEngine
from Evaluator import SimplifiedEvaluator

class Agent:
    def __init__(self, gameStart, depth, engine, evaluator):
        self.engine = engine
        self.root = ChessNode(engine.createBoardFromFen(gameStart),
                              None,
                              0)
        self.depth = depth
        self.player = self.root.state.turn
        self.engine = engine
        self.evaluator = evaluator
        self.MIN = -float('inf')
        self.MAX = float('inf')
        self.MATE_THRESHOLD = 999000000
        self.MATE_SCORE = 1000000000

    def setStart(self, board):
        self.root = ChessNode(board,
                              None,
                              0)
        self.player = self.root.state.turn

    # create the children of a node using ChessEngine
    # if the node is a fringe node, the children have their heuristic score computed
    # a depth of 0 means a leaf
    def expandNode(self, node, depth):
        if depth == 1:
            return node.generateWithHeuristic(self.engine, self.evaluator)
        else:
            return node.generateWithoutHeuristic(self.engine, self.evaluator)

    # helper to wrap around the output
    def getMinimaxMoveSequence(self):
        score, movesWithRoot = self.h_minimax(self.depth, self.root, True, self.MIN, self.MAX)
        if (len(movesWithRoot) > 0) and (movesWithRoot[0] == None):
            return movesWithRoot[1:]
        return movesWithRoot

    # Minimax algorithm with alpha-beta pruning
    def h_minimax(self, depth, node, maximizingPlayer, alpha, beta):
        """
        Inputs -
        1. self (Agent object reference)
        2. depth (int)
        3. node (chessNode)
        4. maximizingPlayer (bool)
        5. alpha (float)
        6. beta (float)
        
        Outputs -
        1. score (float)
        2. moves (list(string))
        
        stops at depth = 0
        """
        if depth == 0 or node.isTerminalNode:
            move = []
            return node.score, move
        
        elif maximizingPlayer:
            v = self.MIN
            best_moves = []
            for child in self.expandNode(node, depth):
                (score, moves) = self.h_minimax(depth-1, child, False, alpha, beta)
                if v < score:
                    v = score
                    best_moves = moves.copy()
                    best_moves.insert(0, child.move)
                if v >= beta:
                    return v, best_moves
                if alpha < v:
                    alpha = v
            return v, best_moves
        
        else:
            v = self.MAX
            best_moves2 = []
            for child in self.expandNode(node, depth):
                (score2, moves2) = self.h_minimax(depth-1, child, True, alpha, beta)
                if v > score2:
                    v = score2
                    best_moves2 = moves2.copy()
                    best_moves2.insert(0, child.move)
                if v <= alpha:
                    return v, best_moves2
                if beta > v:
                    beta = v
            return v, best_moves2
    