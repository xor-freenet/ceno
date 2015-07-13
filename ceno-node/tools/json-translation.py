'''Prepare the CENO Client's content for translation.
goi18n expects JSON files for translation to be of the following form:

[
  {
    "id": "some_identifier",
    "translation": "Text in some language"
  }
]

However Transifex's JSON format is a simple

{
  "some_identifier": "Text in some language"
}

Format.  This utility converts the existing en-en.json file into the format preferred
by Transifex and back.

To convert to the Transifex format, run

    python json-translation.py to

To convert back to the goi18n format, run

    python json-translation.py from <locale> <filename>

After we have a translated file from Transifex, such as a French translation, stored
in, for example, fr-fr.json, we replace <locale> with fr-fr and <filename> with
fr-fr.json in the above command template.
'''

import sys
import json

def convert_to_transifex():
  '''Convert the en-en.json file contents to a simple "id": "text" format'''
  content = json.load(open('../translations/en-en.json', 'r'))
  id_texts = {}
  for pair in content:
    id_texts[pair['id']] = pair['translation']
  json.dump(id_texts, open('./en-en.json', 'w'))


def convert_from_transifex(locale, filename)
  '''Convert a translated file from transifex's format to goi18n's format'''
  content = json.load(open(filename, 'r'))
  pairs = []
  for identifier in content.keys():
    pairs.append({ 'id': identifier, 'translation': content[identifier] })
  json.dump(pairs, open('../translations' + locale + '.json', 'w'))


def main():
  if len(sys.argv) < 2:
    print 'Run as: python {0} <to|from> [locale] [filename]'.format(sys.argv[0])
    sys.exit(1)
  if sys.argv[1] == 'to':
    convert_to_transifex()
  else:
    convert_from_transifex()


if __name__ == '__main__':
  main()
