# lastfm-cli

`lfmcli` uses the [Last.fm API](https://www.last.fm/api) to act as a command-line interface to display music statistics for Last.fm users. `lfmcli` is written in Python and uses the `argparse` as a parser for command-line options.

## Usage

<pre><b>$ lfmcli --help</b> 

<b>OPTIONS</b>
  -u, --user          last.fm user to fetch info for. Defaults to user set in config/userinfo.py.
  -l, --limit         overall | 7day | 1month | 3month | 6month | 12month - the time period over which to retrieve stats for.
  -p, --period        the number of results to fetch. Defaults to 10.


<b>EXAMPLES</b>
  $ lfmcli -u alicifier topartists
  
  alicifer's top 10 artists for the past 7day period

  +-------------------+-----------+
  |       Artist      | Playcount |
  +-------------------+-----------+
  |     Elderwind     |     77    |
  |    Motorpsycho    |     76    |
  |    Evan Carson    |     50    |
  |      Delving      |     49    |
  | Pain of Salvation |     48    |
  |       Ihsahn      |     42    |
  |      Genesis      |     37    |
  |     White Ward    |     34    |
  |        Meer       |     29    |
  |      Agalloch     |     20    |
  +-------------------+-----------+

<b>COMMANDS</b>
  lfmcli topartists   displays top artists
  lfmcli topalbums    displays top albums
  lfmcli toptracks    displays top tracks
</pre>

## Currently supported method calls

Services with no authentication required:

`user.getTopAlbums`
`user.getTopArtists`
`user.getTopTracks`
