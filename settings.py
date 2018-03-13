class Settings():
	"""A class to store all of the settings for Alien Invasion."""
	def __init__(self):
		"""Initialize the game's settings."""
		
		# Screen Settings
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# Ship Settings
		self.ship_speed_factor = 15

		# Bullet Settings
		self.bullet_speed_factor = 20
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 5
		
		# Alien Settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1


