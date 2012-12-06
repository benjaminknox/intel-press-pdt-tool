
import os, sys, time, logging, urllib2
from subprocess import Popen, PIPE
from libs.ThreadPool import *
from libs.Singleton import *
from libs.ConfigManager import ConfigManager

logger = logging.getLogger('Main')

@Singleton
class Converter():
	''' 
	This is a wraper for the ebook-converter program 

	This class is a singleton that will keep handle to the threadpool
	'''

	#Static conversion types
	EPUB = "epub"
	MOBI = "mobi"
	AZW3 = "azw3"
	FB2 = "fb2"
	OEB = "oeb"
	LIT = "lit"
	LRF = "lrf"
	HTMLZ = "htmlz"
	PDB = "pdb"
	PML = "pml"
	RB = "rb"
	PDF = "pdf"
	RTF = "rtf"
	SNB = "snb"
	TCR = "tcr"
	TXT = "txt"
	TXTZ = "txtz"
	TYPES = [AZW3, EPUB, FB2, OEB, LIT, LRF, MOBI, HTMLZ, PDB, PML, RB, PDF, RTF, SNB, TCR, TXT, TXTZ]

	def __init__(self):
		self.thread_pool = ThreadPool()

	def convert_file(self, message):
		''' This when supplied with a valid file path with convert the pdf to an epub '''
		file_path = message['file-location']
		file_name, file_extension = os.path.splitext(file_path)
		logger.debug("Name: %s Extension: %s", file_name, file_extension)
		process = ConverterProcess(file_name, file_extension, message['pdf-id'], message['out-format'])
		self.thread_pool.add_job(process.run, return_callback=process.finish)

class ConverterProcess():
	''' This is used to deal with the actual executable, and only works on linux '''

	def __init__(self, file_name, file_extension, pdf_id, out_format):
		self.file_name = file_name
		self.file_extension = file_extension
		self.pdf_id = pdf_id
		self.out_format = out_format
		self.config = ConfigManager.Instance()

	def run(self):
		''' Welcome to the meat '''
		#Confirm that the file exists
		if not os.path.isfile(self.file_name + self.file_extension):
			logger.error("File does not exist, cannot convert file: %s", self.file_name)
			return
		#Confirm we are a pdf
		if not ".pdf" == self.file_extension.lower():
			logger.error("This is not a PDF file")
			return
		logger.debug('Started the conversion process on %s.%s', (self.file_name, self.file_extension))
		process = Popen(['ebook-convert', self.file_name + self.file_extension, ('%s.%s' % (self.file_name, self.out_format))], stdout=PIPE, stderr=PIPE)
		return_value = process.wait()
		return return_value

	def finish(self, *args):
		''' Responds to the TA portal to let them know a book is finished '''
		#post converted file path & old book ID to the TA portal
		logger.debug("GET to TA portal!")
		location = "http://%s:%s/bookmanagement/finishedconvert/%s" % (self.config.address , self.config.server_port, self.pdf_id)
		logger.error(location)
		urllib2.urlopen(location)
		logger.debug("Email should be on its way!")