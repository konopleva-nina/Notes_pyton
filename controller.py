import text
import view
import model
import os

my_notes = model.Notes(os.path.dirname(__file__)+"\\"+text.notes_file_name)

def start():
	while True:
		choice = view.main_menu() # выводим меню
		match choice:
			case 1: # Открыть файл 
				my_notes.load_notes()
				view.print_message(text.load_successful)