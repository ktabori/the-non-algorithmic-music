# The Non-Algorithmic Music Library Experiment

## Intro  
Over the last couple of years, I’ve been bouncing between music services—Spotify, Apple Music, TIDAL, Beatport Play, Deezer, YouTube Music—you name it, I’ve tried it. My hope was always the same: to discover new music. But every time, I ended up cycling through the same 10 playlists I had created. The discovery feeds and algorithm-based recommendations just didn’t cut it, especially since my taste spans across a wide variety of genres.

So, I decided to go back to basics. I dusted off my old library of ripped music, started buying new albums, and rekindled the joy of digging through second-hand CDs at local markets and ripping them myself.

## Why am I sharing this?  
Over the past few weeks, I’ve been on a mission to clean up MP3 tags, sync music across devices, and set up systems using both [Rockbox](https://www.rockbox.org/) on iPods and vanilla firmware. I want to share my journey in the hope that others looking to build their own music libraries can benefit from some of the lessons I’ve learned along the way.

## My Setup  
As a primarily Apple user, my player of choice is [Swinsian](https://swinsian.com/). I like the iTunes aesthetic and how easy it is to build and manage my library. I also run a Plex media server, so [Plexamp](https://www.plex.tv/plexamp/) is a great addition when I want to listen to music on any device. My DAC? A trusty iPod Classic, 5th/6th/7th gen, depending on the day.

## My Workflow

1. **Converting Music to ALAC**  
   When I acquire new music—whether it’s ripped from a CD or digitally purchased—my first step is always converting it to ALAC (Apple Lossless Audio Codec) while maintaining the original bitrate. I chose ALAC for its native support within the Apple ecosystem.

2. **Tag Cleanup in MP3tag**  
   After conversion, I use [MP3tag](https://www.mp3tag.de/en/) to clean up metadata. This includes fetching missing album artwork, organizing file names based on my preferred format, and structuring everything into the right folders. Both *Swinsian* and *Plex* seem happy with the results, so it’s a win-win.

3. **Curating the Library**  
   Once the music is in my library, I start curating. I use the star rating system and create playlists. One major challenge was syncing ratings across different platforms—this was by far the trickiest part.  
   
   I should mention here that I use [Synology Drive](https://www.synology.com/en-global/dsm/feature/drive) to keep my entire library synced and backed up between my local setup and my NAS/Plex server. It can be heavy when using *MP3tag* because every time I modify a tag, the whole track gets re-synced. But I’m fortunate to have a 2.5Gb internet connection and a 10Gb local network, so speed isn’t an issue for me. That said, this part of the workflow could probably be more efficient.

4. **Syncing Ratings**  
   I do all my rating in *Swinsian* since I don’t rate music on the fly. Swinsian uses a 0-100 rating scale, where 100 is 5 stars, 50 is 2.5 stars, and so on. *Plex*, however, uses a 0.0-10.0 scale, where 10.0 is 5 stars and 5.0 is 2.5 stars. To sync these, I wrote a Python script that runs on my [Synology NAS](https://www.synology.com/en-global/products/NAS) converting Swinsian’s ratings into Plex’s format.  
   
   Another obstacle was that rating tags aren’t standardized across platforms. To work around this, I used *MP3tag* to copy the rating tags into the comment field, allowing my script to read and sync ratings properly. And yes, Swinsian ratings show up on the iPod too!

5. **Playlists**  
   I build all my playlists in *Swinsian*, and they work perfectly on my iPod Classic. Syncing playlists with *Plex* isn’t a priority for me right now, but I might explore that in the future (stay tuned for an update).

## iPod Modding & Firmware  
When it comes to firmware, I experimented with [Rockbox](https://www.rockbox.org/). While Rockbox is an incredible tool, I found it to be overkill for my needs. I just want to listen to music, access playlists quickly, and have a reliable playback experience—without the device rebooting or the database constantly rebuilding. As nice as custom themes are, the quirks weren’t worth it for me. So, I settled on the vanilla firmware, which has been faster and more reliable for my setup.

## Pro Tips for iPod Modding  
Before diving into hardware mods, make sure to read this [iFlash guide](https://www.iflash.xyz/helpful-tips-and-advice/). I didn’t, and ended up buying three 6th-gen iPods only to find out I couldn’t get past the 128GB limit, even with a 1TB SD card installed. Some models cap the disk size unless you install *Rockbox*.

Despite these limitations, the modding experience has been a blast. There’s a whole community of videos and guides online that walk you through how to swap parts and customize your iPod.

---

If you’re in a similar situation, or just want to start curating your own non-algorithmic music library, I hope this post helps you get started. Happy listening!
