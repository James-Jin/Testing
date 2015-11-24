class Parent:
	parentAttr = 100
	def __init__(self):
		print "calling  parent constructor"
		
	def parentMethod(self):
		print "calling parent Method"
		
	def setAttr(self, attr):
		Parent.parentAttr = attr
		
	def getAttr(self):
		print "parent attributes =",Parent.parentAttr
		
	def commonMethod(self):
		print "calling parent common Method"

class Child(Parent):
	def __init__(self):
		print "calling child constructor"
	
	def childMethod(self):
		print "Calling child method"
		
	def commonMethod(self):
		print "Child common method. Override!"
		
		
c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
c.commonMethod()
#here are some comments
