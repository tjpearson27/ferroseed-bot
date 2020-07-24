class Person:
	def __init__(self, id, userChannel, user):
		self.idString = "<@"+str(id)+">"
		self.id = id
		self.userChannel = userChannel
		self.user = user

	def getUser(self):
		return self.user

	def getUserChannel(self):
		return self.userChannel

	def getIDString(self):
		return self.idString

	def getID(self):
		return self.id