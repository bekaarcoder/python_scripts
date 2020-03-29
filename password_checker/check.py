import requests
import hashlib
import sys

def request_api_data(api_query):
  url = "https://api.pwnedpasswords.com/range/" + api_query
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error: {res.status_code}')
  return res

def check_leaks_count(hashes, hash_to_check):
  hashes = (hash.split(':') for hash in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def check_pwd(password):
  sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  sha1_first5, sha1_rest = sha1_password[:5], sha1_password[5:]
  response = request_api_data(sha1_first5)
  return check_leaks_count(response, sha1_rest)

def main(args):
  for arg in args:
    counts = check_pwd(arg)
    if counts == 0:
      print(f"{arg} -> Great! You are safe.")
    else:
      print(f"{arg} -> Oops! You have been pawned. {counts} times leaked.")


main(sys.argv[1:])

