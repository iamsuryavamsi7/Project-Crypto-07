class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	
	def draw(self):
		print("draw")
	

	def move(self):
		print("move")


point = Point(10, 20)
print(point.x)
