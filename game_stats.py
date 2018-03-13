class GameStats():
	def __init__(self, ai_settings):
		"""Initialize stats."""
		self.ai_settings = ai_settings
		self.reset_stats()
		# Start Alien Invasion in active state.
		self.game_active = False

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit
