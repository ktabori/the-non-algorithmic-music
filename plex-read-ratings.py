# USE AT YOUR OWN RISK!!!!
#
# Requires tinytag and plexapi libraries, written & tested in python 3.9

from plexapi.myplex import MyPlexAccount
from tinytag import TinyTag

#Plex Token
#https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/
TOKEN = 'YOUR_PLEX_TOKEN' 

#Your Plex Server Name
LIB = 'YOUR SERVER'

#Your Library Section
SEC = 'My Music'

# Counters
justsynced = 0
notag = 0
error = 0

account = MyPlexAccount(token=TOKEN)

# Just a Helper the first time you run the script 
# Print the names of all the resources (aka 'LIB') in the Plex account
for name in account.resources():
	print(name.name)

# Connect to the Plex resource/library
plex = account.resource(LIB).connect()

# Function to convert string or integer values to floats
def convert_to_float(value):
	try:
		if value:
			# Check if the value is numeric and convert to float
			return float(int(value) / 10)
		else: 
			return float(0.0)
	except ValueError as e:
		# Log the error if conversion fails
		print(f"Conversion error: {e} with value: {value}")
		return float(0.0)

# Main loop to go through all albums and tracks
for album in plex.library.section(SEC).albums():
	for track in album.tracks():    
		try:
			# Ensure the track location exists
			if not track.locations:
				print(f"... No track location found for {track.title}.")
				notag += 1
				continue

			if TinyTag.is_supported(track.locations[0]):
				# Try to read the M4A or supported file's metadata
				try:
					tag = TinyTag.get(track.locations[0])
				except Exception as e:
					print(f"... Error reading tags for {track.title}: {str(e)}")
					error += 1
					continue
				
				# Check if tag.comment exists and can be processed
				if tag.comment and tag.comment.isdigit():
					rating = convert_to_float(tag.comment)
					try:
						track.rate(rating)
						print(f"... M4A tag rating value of {rating} found and saved to Plex userRating field.")
						justsynced += 1
					except Exception as e:
						print(f"... Error updating Plex rating for {track.title}: {str(e)}")
						error += 1
				else:
					print(f"... No valid rating found in comment tag for {track.title}.")
					notag += 1
			else:
				print(f"... Unsupported file format for {track.title}.")
				error += 1
		except Exception as e:
			print(f"… General error for {track.title}: {str(e)}")
			error += 1

# Stats Output                          
print(f"{justsynced} newly synced files")
print(f"{notag} files with no tags")
print(f"{error} files had errors")