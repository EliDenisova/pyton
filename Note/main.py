from Notes import Notes
from UserDialog import UserDialog

if __name__ == '__main__':
    notes = Notes('Notes.csv')
    UserDialog().menu_cycle(notes)