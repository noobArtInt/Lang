import os

initial_path = os.getcwd()

program_name = []

program_dir = [r'C:\Program Files',r'C:\Program Files (x86)']
ignore_terms = ['window', 'Microsoft Visual Studio']
exe_path = []

#os.chdir()
'''
for file_path in program_dir:
	program_name += os.listdir(file_path)
	for root, dirs, files in os.walk(file_path, topdown=False):
		if 'window' not in root.lower():
			for file in files:
				if file.endswith('.exe'):
					for term in ignore_terms:
						
						if term.lower() not in root.lower():
							exe_path.append(root+'\\'+file)
							
print("Program installed are: ",program_name)
'''
print("Done")
def find_path(application):
	for exe in exe_path:
		if application in exe.lower():
			print(exe)

def open_app(cmd):
	chrome = r"C:\Program Files (x86)\Google\Chrome\Application\\"
	python = r"C:\ProgramData\Anaconda3\python.exe"

	if 'chrome' in cmd.lower():
		print(f'{chrome}chrome.exe')
		os.chdir(chrome)
		os.system(f'cmd / chrome.exe')
	os.chdir(initial_path)
