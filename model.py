from contextlib import suppress


class Notes:

    def __init__(self, path: str = ''):
        self._notes: list[dict[str, str]] = []
        self._path = path

    def load_notes(self):
        with suppress(Exception):
          with open(self._path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for note in data:
              note = note.strip().split(';')
              self._notes.append({'id': note[0], 'datetime': note[1], 'title': note[2], 'note': note[3]})

    def save_notes(self):
        data = []
        for note in self._notes:
            data.append(';'.join([value for value in note.values()]))
        with open(self._path, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(data))