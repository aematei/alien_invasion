"""Old code, DO NOT USE!!!"""

# Old check events function. Refactored into key up and key down funcs.
# From module game_finctions.py
def check_events(ship):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		# Moving Right
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				# Move ship to the right.
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				ship.moving_left = True

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			if event.key == pygame.K_LEFT:
				ship.moving_left = False


