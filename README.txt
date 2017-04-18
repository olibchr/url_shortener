Group 8, Migguel Nunes & Oliver Becher
Assignment I, Part II: Url Shortener with REST Interface

Acitvate the virtual environment with
source venv/bin/activate

Start the web service with
python url_shortener.py

It will start serving at 0.0.0.0:5000

We recommend using POSTMAN (chrome extension) to test the service.

The Url shortener offers the following service:
- Add an entry with POST to / and get back a shortened URL (the ID and an actual shortened URL)

- Get all IDs with GET to /

- Delete all Entries with DELETE to /

- Get an Url with GET to /<ID>

- Delete an Entry with DELETE to /<ID>

- Change a URL with POST to /<ID>

- Add an entry with POST to /<ID>

