from blessed import Terminal
import json
import ilmsl

term = Terminal()
running = True

command = []
commands = None
with open("commands.json", "r") as f:
	commands = json.load(f)
message = ""

def runCommand(command, *args):
	global message
	if command == "help":
		message = f"help: {commands[args]}"
	elif command in commands:
		try:
			exec(commands[command])
		except Exception as e:
			message = "command error: " + str(e)
	else:
		message = "command not found"

# Check the input
def check_inp(inp):
	global term
	global command
	if inp == "KEY_BACKSPACE":
		if len(command) > 0: command.pop()
	elif inp == "KEY_ENTER":
		runCommand(remove_quotes_from_list(command))
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
		"startup.lua": "-- ILMSOS- I Love Making Stuff OS\n--print('')"
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
	if message != None: print(term.bold(term.red(f'! {message}')))