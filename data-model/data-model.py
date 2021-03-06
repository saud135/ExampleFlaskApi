class Polynomial:
	def __init__(self, *coeffs):
		self.coeffs = coeffs

	def __repr__(self):
		return 'Polynomial(*{!r})'.format(self.coeffs)

p1 = Polynomial(1,2,3)
p2 = Polynomial(3,4,3)
