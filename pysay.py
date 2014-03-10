#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import urllib2

if __name__ == "__main__":
  APIKEY = "1953c74c5b60c0e3bdabaeb822e4e14c"

  parser = argparse.ArgumentParser(prog='pySay', usage='%(prog)s [options]',
      description='Pronounce a specified word or phrase in its native language.')

  parser.add_argument('word', help="A word or phrase to pronounce.")
  parser.add_argument('-l','--lang', help="A two character language code, e.g. 'en' or 'ru'."
      "(default: automatically inferred from word or phrase entered.)")
  parser.add_argument('-s','--sex', help="The sex of the speaker pronouncing the specified word.")
  parser.add_argument('-a','--action', default="standard-pronunciation",
      help="Set to 'word-pronunciations' for varying audio examples, or 'standard-pronounciation' for top rated result." +
      "(default: Top rated pronunciation of desired word)")

  args = parser.parse_args()

  url =  "http://apifree.forvo.com/limit/1/format/json/key/" + APIKEY
  url += "/action/" + args.action
  url += "/word/" + args.word #No need to validate as 'too few arguments' error is throw if no argument passed.

  if args.lang:
    url += "/language/" + args.lang

  if args.sex:
    url += "/sex/" + args.sex

  data = json.load(urllib2.urlopen(url))

  if not data['items']:
    print "No results were found for the word (" + args.word + ") that you specified."
    sys.exit()

  audioRequest = urllib2.urlopen(data['items'][0]['pathmp3'])

  tf = tempfile.NamedTemporaryFile()

  with open(tf.name, 'wb') as f:
    shutil.copyfileobj(audioRequest,f)

  subprocess.call(["afplay", tf.name]) # Currently only supports osx.
