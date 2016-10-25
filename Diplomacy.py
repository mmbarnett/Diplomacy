COUNTRIES = ['Austria', 'England', 'France',
			'Germany', 'Italy', 'Russia', 'Turkey']

class Player(object):
	"""one offline player.  Will need to be updated
	once the P2P network comes into play"""

	def __init__(self, cntry):
		self.name = cntry # a string
		self.supplies = 0
		self.units = []

class Province(object):
	"""one province on the map"""

	def __init__(self, nme, abbv, country, 
		sply_flg, adjcnts, is_land):
		"""builds province; args are name, abbv, 
		country, boolean supply_flag, list of adjacent
		provinces, boolean is_sea_province"""

		self.name = nme
		self.abbv = abbv
		self.country = country
		self.is_supply = sply_flg
		self.adj_abbv = adjcnts # list of abbreviations
		self.is_land = is_land
		self.adjacents = None # to be set later

	def is_coastal(self):
		"""Returns True if is a land but is adjacent
		to a sea province"""

		if not self.is_land:
			return False

		for p in self.adjacents:
			if not p.is_land:
				return True
		return False

	def set_adjacents(self, provinces):
		"""Builds adjacents from list of provinces"""

		self.adjacents = []

		for abbv in self.adj_abbv:
			for p in provinces:
				if p.abbv == abbv:
					self.adjacents.append(p)
					break

class Board_Map(object):
	"""the gameboard, including the provinces and the
	edges between them, in addition to players"""

	def __init__(self, plyrs):
		global COUNTRIES

		self.players = plyrs # a list of Players

		# build name_to_player dict
		n_to_p = {}
		for c in COUNTRIES:
			for p in self.players:
				if c == p.name:
					n_to_p[c] = p
					break


		# build map
		self.provinces = [
			#Province(Name, abbv, country, supply, adj, is_land)
			Province('Adriatic Sea', 'adr', None, False, ['tri','alb','ion','app','ven'], False),
			Province('Aegean Sea', 'aeg', None, False, ['ion','gre','bul','con','smy','eas'], False),
			Province('Albania', 'alb', None, False, ['adr','ion','gre','ser','tri'], True),
			Province('Ankara', 'ank', n_to_p['Turkey'], True, ['con','smy','bla','arm'], True),
			Province('Apulia', 'app', n_to_p['Italy'], False, ['adr','ion','nap','rom','ven'], True),
			Province('Armenia', 'arm', n_to_p['Turkey'], False, ['sev', 'bla', 'ank', 'smy', 'syr'], True),
			Province('Baltic Sea', 'bal', None, False, ['pru','lvn','bot','swe','ska','den','kie','ber'], False),
			Province('Barents Sea', 'bar', None, False, ['stp', 'nrg', 'nwy'], False),
			Province('Belgium', 'bel', None, True, ['nth','eng','pic','bur','ruh','hol'], True),
			Province('Berlin', 'ber', n_to_p['Germany'], True, ['sil','pru','bal','kie','mun'], True),
			Province('Black Sea', 'bla', None, False, ['con','ank','arm','sev','rum','bul'], False),
			Province('Bohemia', 'boh', n_to_p['Austria'], False, ['sil','mun','trl','vie','gal'], True),
			Province('Brest', 'bre', n_to_p['France'], True, ['eng','mid','gas','par','pic'], True),
			Province('Budapest', 'bud', n_to_p['Austria'], True, ['vie','tri','ser','rum','gal'], True),
			Province('Bulgaria', 'bul', None, True, ['con', 'bla', 'rum', 'ser', 'gre', 'aeg'], True),
			Province('Burgundy', 'bur', n_to_p['France'], False, ['mar', 'gas', 'par', 'pic', 'bel', 'ruh', 'mun'], True),
			Province('Clyde', 'cly', n_to_p['England'], False, ['edi','nrg','nat','lpl'], True),
			Province('Constantinople', 'con', n_to_p['Turkey'], True, ['ank','bla','bul','aeg','smy'], True),
			Province('Denmark', 'den', None, True, ['ska','nth','hel','kie','bal'], True),
			Province('Eastern Mediterranean', 'eas', None, False, ['syr','smy','aeg','ion'], False),
			Province('Edinburgh', 'edi', n_to_p['England'], True, ['nth','nrg','cly','lpl','yor'], True),
			Province('English Channel', 'eng', None, False, ['lon','wal','iri','mid','bre','pic','nth','bel'], False),
			Province('Finland', 'fin', None, False, ['stp','swe','bot','nwy'], True),
			Province('Galicia', 'gal', n_to_p['Austria'], False, ['rum','ukr','war','sil','boh','vie','bud'], True),
			Province('Gascony', 'gas', n_to_p['France'], False, ['spa','mar','bur','par','bre','mid'], True),
			Province('Greece', 'gre', None, True, ['ion','aeg','bul','ser','alb'], True),
			Province('Gulf of Lyon', 'lyo', None, False, ['spa','mar','pie','tus','tyn','wes'], False),
			Province('Gulf of Bothnia', 'bot', None, False, ['lvn','stp','fin','swe','bal'], False),
			Province('Helgoland Bight', 'hel', None, False, ['hol','kie','den','nth'], False),
			Province('Holland', 'hol', None, True, ['hel','nth','bel','ruh','kie'], True),
			Province('Ionian Sea', 'ion', None, False, ['eas', 'aeg','gre','alb','adr','app','nap','tyn','tun'], False),
			Province('Irish Sea', 'iri', None, False, ['nat','mid','eng','wal','lpl'], False),
			Province('Kiel', 'kie', n_to_p['Germany'], True, ['mun','ber','bal','den','hel','hol','ruh'], True),
			Province('Liverpool', 'lpl', n_to_p['England'], True, ['wal','yor','edi','cly','nat','iri'], True),
			Province('Livonia', 'lvn', n_to_p['Russia'], False, ['war','mos','stp','bot','bal','pru'], True),
			Province('London', 'lon', n_to_p['England'], True, ['eng','nth','yor','wal'], True),
			Province('Marseilles', 'mar', n_to_p['France'], True, ['lyo','pie','bur','gas','spa'], True),
			Province('Mid-Atlantic Ocean', 'mid', None, False, ['naf','wes','por','spa','gas','bre','eng','iri','nat'], False),
			Province('Moscow', 'mos', n_to_p['Russia'], True, ['sev','stp','lvn','war','ukr'], True),
			Province('Munich', 'mun', n_to_p['Germany'], True, ['trl', 'boh', 'sil','ber','kie','ruh','bur'], True),
			Province('Naples', 'nap', n_to_p['Italy'], True, ['ion','app','rom','tyn'], True),
			Province('North Atlantic Ocean', 'nat', None, False, ['mid','iri','lpl','cly','nrg'], False),
			Province('North Africa', 'naf', None, False, ['tun','wes','mid'], True),
			Province('North Sea', 'nth', None, False, ['bel','hol','hel','den','ska','nwy','nrg','edi','yor','lon','eng'], False),
			Province('Norway', 'nwy', None, True, ['ska','swe','fin','bar','nrg','nth','stp'], True),
			Province('Norwegian Sea', 'nrg', None, False, ['nwy','bar','nat','cly','edi','nth'], False),
			Province('Paris', 'par', n_to_p['France'], True, ['gas','bur','pic','bre'], True),
			Province('Picardy', 'pic', n_to_p['France'], False, ['par','bur','bel','eng','bre'], True),
			Province('Piedmont', 'pie', n_to_p['Italy'], False, ['lyo','tus','ven','trl','mar'], True),
			Province('Portugal', 'por', None, True, ['mid','spa'], True),
			Province('Prussia', 'pru', n_to_p['Germany'], False, ['sil','war','lvn','bal','ber'], True),
			Province('Rome','rom',n_to_p['Italy'], True, ['tyn','nap','app','ven','tus'], True),
			Province('Ruhr', 'ruh', n_to_p['Germany'], False, ['mun','kie','hol','bel','bur'], True),
			Province('Rumania','rum',None, True, ['bul','bla','sev','ukr','gal','bud','ser'], True),
			Province('Serbia','ser',None,True,['gre','bul','rum','bud','tri','alb'], True),
			Province('Sevastapol','sev',n_to_p['Russia'],True,['bla','arm','rum','mos','ukr'], True),
			Province('Silesia', 'sil',n_to_p['Germany'],False,['boh','gal','war','pru','ber','mun'], True),
			Province('Skagerrak', 'ska', None, False, ['den','bal','swe','nwy','nth'], False),
			Province('Smyrna', 'smy', n_to_p['Turkey'], True, ['eas','syr','arm','ank','con','aeg'], True),
			Province('Spain', 'spa', None, True, ['wes','lyo','mar','gas','mid','por'], True),
			Province('St. Petersburg', 'stp', n_to_p['Russia'], True, ['mos','bar','nwy','fin','bot','lvn'], True),
			Province('Sweden', 'swe', None, True, ['bal','bot','fin','nwy','ska'], True),
			Province('Syria', 'syr', n_to_p['Turkey'], False, ['arm','smy','eas'], True),
			Province('Trieste', 'tri', n_to_p['Austria'], True, ['adr','alb','ser','bud','vie','trl','ven'], True),
			Province('Tunis', 'tun', None, True, ['ion','tyn','wes','naf'], True),
			Province('Tuscany','tus', n_to_p['Italy'], False, ['tyn','rom','ven','pie','lyo'], True),
			Province('Tyrolia', 'trl', n_to_p['Austria'], False, ['tri','vie','boh','mun','pie','ven'], True),
			Province('Tyrrhenian Sea', 'tyn', None, False, ['ion','nap','rom','tus','lyo','wes','tun'], False),
			Province('Ukraine', 'ukr', n_to_p['Russia'], False, ['rum','sev','mos','war','gal'], True),
			Province('Venice', 'ven', n_to_p['Italy'], True, ['rom','app','adr','tri','trl','pie','tus'], True),
			Province('Vienna', 'vie', n_to_p['Austria'], True, ['tri','bud','gal','boh','trl'], True),
			Province('Wales', 'wal', n_to_p['England'], False, ['eng','lon','yor','lpl','iri'], True),
			Province('Warsaw', 'war', n_to_p['Russia'], True, ['gal','ukr','mos','lvn','pru','sil'], True),
			Province('Western Mediterranean', 'wes', None, False, ['naf','tun','tyn','lyo','spa','mid'], False),
			Province('Yorkshire', 'yor', n_to_p['England'], False, ['lon','nth','edi','lpl','wal'], True),
			]

		for p in self.provinces:
			p.set_adjacents(self.provinces)

	def update(self):
		""" right now just adds units where necessary """
		
		for p in self.provinces:
			if p.is_supply and p.country != None:
				if p.is_coastal():
					response = ""
					while not response in ['army', 'fleet']:
						response = raw_input(p.country.name.upper() + ", would you like an army or a fleet for " + p.name + "?\n")

					if response == 'army':
						p.country.units.append(Army(p, p.country))
					elif response == 'fleet':
						p.country.units.append(Fleet(p, p.country))
					else:
						raise Exception('00. Neither army nor fleet')
				else: # not coastal
					p.country.units.append(Army(p, p.country))

class Unit(object):
	""" Super-class which encompasses armies and
	fleets """

	def __init__(self, loc, owner):
		self.province = loc
		self.country = owner

class Army(Unit):
	""" An army can only move on land """

	def __init__(self, loc, owner):
		Unit.__init__(self, loc, owner)

class Fleet(Unit):
	""" A fleet can only move in water and on
	coastal territories """

	def __init__(self, loc, owner):
		Unit.__init__(self, loc, owner)

def main():
	global COUNTRIES

	# initialize players
	players = []
	for c in COUNTRIES:
		players.append(Player(c))

	# initialize board
	board = Board_Map(players)

	board.update()


if __name__ == "__main__":
	main()
