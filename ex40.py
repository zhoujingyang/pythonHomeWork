class Song(object):

	mysong = "rolling in the deep"
	def __init__(self,lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			print self.mysong
			
happy_bday = Song(['happy birthday to you ',
					'I don\'t want to get sued',
					'so I will stop right there'])
					
					
					
bulls_on_parade = Song(["they rally around the family",
						"with pockets full of shells"])


happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()