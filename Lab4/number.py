
class Integer(object):
	def __init__(self, num, pn):
		self.num = num
		self.pn = pn

	def display(self):
		if self.pn=="p":
			print self.num
		if self.pn=="n":
			print self.num - (self.num*2)

class NegetiveInteger(Integer):
	def __init__(self, num):
		super(NegetiveInteger, self).__init__(num, "n")
		self.num= num

if __name__ == "__main__":
	test= Integer(5, "n")
	test.display()
	t= NegetiveInteger(9)
	t.display()
