import actions
import speech_recognition as sr
import program_list
from lang import BasicLexer, BasicParser, BasicExecute
#command = ('Speak command')

r = sr.Recognizer()

with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source,duration=1)
	print('Listening')
	audio = r.listen(source)
	print('Executing')

command = str(r.recognize_google(audio))

print(command)

if 'open' in command.lower():
	print('open')
	program_list.open_app(command)
	
	
if command.lower() == 'program':
	print('Starting language')
	lexer = BasicLexer()
	parser = BasicParser()
	print('No Code')
	env = {}
	  
	while True:
		  
		try:
			text = input('')
	  
		except EOFError:
			break
	  
		if text:
			tree = parser.parse(lexer.tokenize(text))
			print(tree)
			BasicExecute(tree, env)
#program_list.find_path(command)

	