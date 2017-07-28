import os
import re
import errno

class Kernel:
	"""Class Kernel would contain all important methods to handle the process"""


	def __init__(self):
		print "\nStarting Kernel...\n"
		self.startKernel()

	def startKernel(self):
		print "Kernelling....\n"		

	def createBasicApp(self,appName):
		"""
			Create a basic app using basic flask configurations
			by invoking this method, kernel is going to create a basic flask 
			application with necessary configurations........................
			.................................................................
		"""
		try:
			os.makedirs("/"+appName)
			self.createBasicAppStructure(appName)
			#print "Kernel Completed...\n"

			#print "Your project was sucessfully created....\n\n Thumbs Up..\n"

		except OSError as exception:

			if exception.errno != errno.EEXIST:
				print "Kernel Stopped working...\nand your task was left incomplete..\n"

			elif exception.errno == errno.EEXIST:

				print "MayDay...MayDay.. Kernel is reporting..\n"
				print "This Folder already exist...\n"

	def createBasicAppStructure(self,appName):
		"""
			Create basic folders for flask config, this is very 
			with all neccesities
		"""
		#extract basic app content from kernelling folder 	

		appContent=open('kernelling/setupFiles/basicApp.py').read()

		try:
			os.makedirs("/"+appName+"/templates")# create template folder
			os.makedirs("/"+appName+"/static") # create static folder
			os.makedirs("/"+appName+"/controller") #create controller folder
			os.makedirs("/"+appName+"/model") #create model folder
			os.makedirs("/"+appName+"/db") #create db folder- to handle db connections code..

			#now lets create the files

			main= open("/"+appName+'/app.py','w+')# create the main app

			main.write(appContent.format(appName,appName))# main writing process

			main.close()

			print "Kernel Completed...\n"

			print "Your project was sucessfully created....\n\n Thumbs Up..\n"

		except OSError as exception:

			if exception.errno != errno.EEXIST:
				print "Kernel Stopped working...\n Seems an error occured..\n"



	def createProductionApp(self,appName):
		"""
			Create basic folders for flask config, this is very 
			with all neccesities
		"""
		#extract basic app content from kernelling folder 	

		appContent=open('kernelling/setupFiles/basicApp.py').read()
		wsgiContent=open('kernelling/setupFiles/app.wsgi').read()#wsgi file content

		try:
			os.makedirs("/"+appName+"/"+appName)# create template folder
			os.makedirs("/"+appName+"/"+appName+"/templates")# create template folder
			os.makedirs("/"+appName+"/"+appName+"/static") # create static folder
			os.makedirs("/"+appName+"/"+appName+"/controller") #create controller folder
			os.makedirs("/"+appName+"/"+appName+"/model") #create model folder
			os.makedirs("/"+appName+"/"+appName+"/db") #create db folder- to handle db connections code..

			#now lets create the files

			main= open("/"+appName+'/app.py','w+')# create the main app
			wsgi= open("/"+appName+'/app.wsgi','w+')# create the main app

			main.write(appContent.format(appName,appName))# main writing process
			wsgi.write(wsgiContent.format(appName,appName))# main writing process

			main.close()

			print "Kernel Completed...\n"

			print "Your project was sucessfully created....\n\n Thumbs Up..\n"

		except OSError as exception:

			if exception.errno != errno.EEXIST:
				print "Kernel Stopped working...\n Seems an error occured..\n"