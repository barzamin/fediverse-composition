def domains(data):
	return [
		u['addr'].split('@')[2]
		for u in data
	]

