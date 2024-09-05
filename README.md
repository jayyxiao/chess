# chess
Video Demo: [https://youtu.be/6AbY2r8Wnno](https://youtu.be/6AbY2r8Wnno)

Chess Engine with ~1800 ELO. Can play against a human or against itself. The engine accepts moves in [UCI](https://en.wikipedia.org/wiki/Universal_Chess_Interface) format.

The engine evaluates positions using an Alpha-beta Pruning algorithm and a Piece Square Table heuristic. The search depth is 5 moves.

To use, run 'jupyter notebook' in the terminal, then run either AgentVersusHuman or AgentVersusAgent. The engine may take several seconds in between moves.
