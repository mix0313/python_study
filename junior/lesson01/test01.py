import requests
import xml.etreeElementTree as ET
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
	"""docstring for DefaultSaxHandler"""
	def __init__(self, provinces):
		super(DefaultSaxHandler, self).__init__()
		self.provinces = provinces

	def start_element(self, name, attrs):
		if name != 'map':
			name = attrs['titile']
			number = attrs['href']
			self.provinces.append((name, number))
		pass


	def end_element(self, name):
		pass

	def char_data(self, text):
		pass

def get_provinces(url):
	content = requests.get(url).content.decode('gb2312')
	start = content.find('<map name=\"map_86\" id=\"map_86\">')
	end = content.find('</map>')
	content = content[start:end + len('</map>')].strip()
	print(content)
	provinces = []
	handler = DefaultSaxHandler(provinces)
	parser = ParserCreate()
	parser.StartElementHandler = handler.start_element
	parser.EndElement = handler.end_element
	parser.CharacterDataHandler = handler.char_data
	parser.Parser(content)
	return provinces
	pass
provinces = get_provinces('http://www.ip138.com/post')
print(provinces)