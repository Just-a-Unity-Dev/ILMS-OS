from blessed import Terminal
import logging
import json

term = Terminal()
running = True

command = []
commands = None
with open("commands.json", "r") as f:
	commands = json.load(f)
message_type = "message"
message = ""

def runScript(path):
	global message_type
	global message
	try:
		
		message_type = "message"
		message = "script ran successfully"
	except Exception as e:
		message_type = "error"
		message = "script error: " + str(e)

def runCommand(command, *args_raw):
	global message_type
	global message
	args = list(args_raw)
	if command == "help":
		message = f"help: {commands[args]}"
	elif command in commands:
		try:
			exec(commands[command])
			message_type = "message"
		except Exception as e:
			message = "command error: " + str(e)
	else:
		message_type = "error"
		message = "command not found"

# Check the input
def check_inp(inp):
	global term
	global command
	if inp == "KEY_BACKSPACE":
		if len(command) > 0: command.pop()
	elif inp == "KEY_ENTER":
		x = remove_quotes_from_list(command).split(" ")
		runCommand(x[0], x[1:])
		command = []
	else:
		command.append(inp)
		term.clear()

def remove_quotes_from_list(list):
	# Hacky...
	x = []
	for item in list:
		x.append(item[1:-1])	
	return ''.join(x)

# Banner
print(term.home + term.clear + term.move_y(term.height // 2))
print(term.black_on_darkkhaki(term.center('ILMS - I Love Making Stuff')))
print(term.move_down(1) + term.black_on_darkkhaki(term.center('version 1.0.0.0')))

last_recorded_input = None

print(term.move_down(2) + term.bold(term.red('~ ')) + term.grey("type \"help\" for a list of commands"))

files = {
	"rom": {
		"startup.ilmsl": "-- ILMSOS- I Love Making Stuff OS\n--print('')"
	}
}

while running:
	with term.cbreak(), term.hidden_cursor():
		inp = term.inkey()

	print(term.home + term.clear + term.move_y(term.height // 2))
	print(term.black_on_darkkhaki(term.center('ILMS - I Love Making Stuff')))
	print(term.move_down(1) + term.black_on_darkkhaki(term.center('version 1.0.0.0')))

	check_inp(repr(inp))
	
	print(term.move_down(2) + term.bold(term.red('~ ')) + term.bold(remove_quotes_from_list(command)))
		
	if message != None:
		if message_type == "error":
			print(term.bold(term.red(f'! {message}')))
		if message_type == "message":
			print(term.bold(term.white(f'{message}')))