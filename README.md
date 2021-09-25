# Intro_to_AI
AI final Project: 
In this project, I focused on using a simple game, tic-tac-toe, and implementing several agents of AI to play it.
I used 3 different algorithms:
	1) Random position generating
	2) Depth limited BFS (only to block from winning or win if possible)
	3) Minimax 
1) random algorithm 
	As the name implies, this uses a random generator to place an X or an O in one of the empty spots 
	This has no use of intelligence it was only built as to be the first stepping stone and the standard other algorithms would be tested against
2) depth limited bfs
	This improves on the random algorithm by going one step further. It checks if the next game would result in a win or a loss
	If there is a win possible it chooses to win, if there is a loss, it blocks the other player.
	My code does not follow a full BFS algorithm but it works in the same way; checking all possible outcomes for the one coming move to see if there is a win or a loss
3) Minimax
	
	In the third variation, I implemented a minimax agent to play tic tac toe.
	Minimax uses a recursive algorithm to search a game tree where it tries to minimize the opponent score, and maximizes its score. 
	Since the algorithm always gets the optimal game, and since tic-tac-toe has a relatively small search tree, it is impossible to beat. The maximum score you can get is a tie 
