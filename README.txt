SET!

By Cynthia Deng and Kevin Wang


Contents:

	Set.py
		Main content and program
		Plays the game Set where users try to create a set with the displayed cards
		Imports CardList and uses the cards as images

	CardList.py
		Contained all the values and cards in the program
		Gets imported into both Set.py and CardRandomize.py

	CardRandomize.py
		Contains the function for randomizing the cards
		*Not used in final program because a global variable from this function was required
		Imports CardList in order to load the card images

	Cards Folder
		Contains all the cards in .png form
		This is where CardList retrieves images for the cards

	Images Folder
		Contains all the images besides cards in .png form
		This is where Set.py retrieves images for main menu
