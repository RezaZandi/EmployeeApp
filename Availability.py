
class Availability():

	def __init__(self):
		self.__mon = None
		self.__tue = None
		self.__wed = None
		self.__thu = None
		self.__fri = None
		self.__sat = None
		self.__sun = None


	#getters and setters for availability 

	def get_mon(self):	
		return self.__mon

	def set_mon(self,start,end):

		if self.__mon == None:
			self.__mon = [start, end]
		else:
			self.__mon[0] = start
			self.__mon[1] = end

	def get_tue(self):		
		return self.__tue
		
	def set_tue(self,start,end): 
		
		if self.__tue == None:
			self.__tue = [start,end]
		else:
			self.__tue[0] = start
			self.__tue[1]= end

	def get_wed(self):
		return self.__wed		

	def set_wed(self,start,end):

		if self.__wed == None:
			self.__wed = [start,end]
		else:
			self.__wed[0] = start
			self.__wed[1]= end
		
	def get_thu(self):
		return self.__thu

	def set_thu(self,start,end):
		
		if self.__thu == None:
			self.__thu = [start,end]
		else:
			self.__thu[0] = start
			self.__thu[1]= end

	def get_fri(self):
		return self.__fri	

	def set_fri(self,start,end):
		
		if self.__fri == None:
			self.__fri = [start,end]
		else:
			self.__fri[0] = start
			self.__fri[1]= end

	def get_sat(self):
		return self.__sat		

	def set_sat(self,start,end):
		
		if self.__sat == None :
			self.__sat= [start,end]
		else:
			self.__sat[0] = start
			self.__sat[1]= end

	def get_sun(self):
		return self.__sun		

	def set_sun(self,start,end):
		
		if self.__sun == None:
			self.__sun = [start,end]
		else:
			self.__sun[0] = start
			self.__sun[1]= end



	
	def is_available(self,day,time):

		if day == 'monday':
			if self.__mon:
				if self.__mon[0] <= time and self.__mon[1] >= time:
					return True
				
			return False

		if day == 'tuesday':
			if self.__tue:
				if self.__tue[0] <= time and self.__tue[1] >= time:
					return True
			
			return False

		if day == 'wednesday':
			if self.__wed:
				if self.__wed[0] <= time and self.__wed[1] >= time:
					return True
				
			return False

		if day == 'thursday':
			if self.__thu:
				if self.__thu[0] <= time and self.__thu[1] >= time:
					return True
				
			return False

		if day == 'friday':
			if self.__fri:
				if self.__fri[0] <= time and self.__fri[1] >= time:
					return True
				
			return False

		if day == 'saturday':
			if self.__sat:
				if self.__sat[0] <= time and self.__sat[1] >= time:
					return True
			
			return False

		if day == 'sunday':
			if self.__sun:
				if self.__sun[0] <= time and self.__sun[1] >= time:
					return True

			return False
		






