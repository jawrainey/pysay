#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib2


def getResponse(url):
  try:
    response = urllib2.urlopen(url)
  except urllib2.URLError, e:
    sys.exit("URLError: " + str(e.reason))
  return response

if __name__ == "__main__":
  APIKEY = "1953c74c5b60c0e3bdabaeb822e4e14c"

  parser = argparse.ArgumentParser(prog='pySay', usage='%(prog)s [options]',
    description='Pronounce a specified word or phrase in its native language.')

  parser.add_argument('word', help="A word or phrase to pronounce.")
  parser.add_argument('-l', '--lang',
    help="A two character language code, e.g. 'en' or 'ru'."
    "(default: automatically inferred from word or phrase entered.)")
  parser.add_argument('-s', '--sex',
    help="The sex of the speaker pronouncing the specified word.")
  parser.add_argument('-a', '--action', default="standard-pronunciation",
    help="Set to 'word-pronunciations' for varying audio examples, or"
    "'standard-pronounciation' for top rated result."
    "(default: Top rated pronunciation of desired word)")

  args = parser.parse_args()

  url = "http://apifree.forvo.com/limit/1/format/json/key/" + APIKEY
  url += "/word/" + args.word

  if args.lang:
    url += "/language/" + args.lang

  if args.sex:
    url += "/sex/" + args.sex
    url += "/action/" + "word-pronunciations/"
  else:
    url += "/action/" + args.action

  try:
    data = json.load(getResponse(url))
  except ValueError:
    sys.exit("Invalid JSON returned from URL.")

  if not data['items']:
    sys.exit("No results were found for the word: " + args.word)

  audioRequest = getResponse(data['items'][0]['pathmp3'])

  tf = tempfile.NamedTemporaryFile()

  with open(tf.name, 'wb') as f:
    shutil.copyfileobj(audioRequest, f)

  if platform.system() == 'Darwin':
    subprocess.call(["afplay", tf.name])
  else:
    subprocess.call(["mplayer", "-really-quiet", "-nolirc", tf.name])
