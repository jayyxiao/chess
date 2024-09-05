
class ChessNode:
    
    def __init__(self, board, previousMove, score, isTerminal=False):
        self.state = board
        self.move = previousMove
        self.score = score

        # A terminal node has no children, and has a score of 0 if tied, and +/- CHECKMATE_SCORE otherwise
        self.isTerminalNode = isTerminal
        self.CHECKMATE_SCORE = 1000000
        
    # generate child nodes without the heuristic value
    def generateWithoutHeuristic(self, engine, evaluator):
        childStates = engine.generateBoardStateTuples(self.state)
        children = []
        for child in childStates:
            terminal = False
            childBoardState = child[0]
            if childBoardState.is_checkmate():
                terminal = True
                if childBoardState.turn == evaluator.player:
                    score = -self.CHECKMATE_SCORE
                else:
                    score = self.CHECKMATE_SCORE
            elif childBoardState.is_game_over():
                terminal = True
                score = 0
            else:
                score = 0
            children.append(ChessNode(child[0], child[1].uci(), score, terminal))
        return children
        
    # generate child nodes with the heuristic value
    def generateWithHeuristic(self, engine, evaluator):
        childStates = engine.generateBoardStateTuples(self.state)
        children = []
        for child in childStates:
            terminal = False
            childBoardState = child[0]
            if childBoardState.is_checkmate():
                terminal = True
                if childBoardState.turn == evaluator.player:
                    score = -self.CHECKMATE_SCORE
                else:
                    score = self.CHECKMATE_SCORE
            elif childBoardState.is_game_over():
                terminal = True
                score = 0
            else:
                score = evaluator.getMoveScore(self.state, child[1], evaluator.player)
            children.append(ChessNode(child[0], child[1].uci(), score, terminal))
        children.sort(reverse=(self.state.turn == evaluator.player), key = lambda x : x.score)
        return children
