import values
import songColor
from flask import Flask, request, render_template

app = Flask(__name__)
    
@app.route('/', methods =["GET", "POST"])
def home():
    return render_template('index.html')

@app.route('/song', methods=["GET", "POST"])
def song():
    song = None
    image_url = None
    red = 0
    green = 0
    blue = 0
    if request.method=="POST":
        song = request.form.get("song")
    
    if(song != None):
        print("song name is " + song)

        track_info = values.search_for_song(song)
        token = values.get_token()
        song_name = values.get_song_name(song)
        song_valence = values.get_valence(song)
        song_time_signature = values.get_time_signature(song)
        song_tempo = values.get_tempo(song)
        song_instrumentalness = values.get_instrumentalness(song)
        song_energy = values.get_energy(song)
        song_danceability = values.get_danceability(song)
        song_mode = values.get_mode(song)
        
        red, green, blue = songColor.songAlgo(song_valence, song_tempo, song_instrumentalness, 
                                              song_energy, song_danceability, song_mode)
        
        print("##########################################################")
        print("Track Info --> ", track_info)
        print("Song Token --> ", token)
        print("Song Name --> ", song_name)
        print("Song Valence --> ", song_valence)
        print("Time Signature --> ", song_time_signature)
        print("Song Tempo --> ", song_tempo)
        print("Song Instrumentalness --> ", song_instrumentalness)
        print("Song Energy --> ", song_energy)
        print("Song Danceability --> ", song_danceability)
        print("-> Red Before sub <-", red)
        print("-> Green Before sub <-", green)
        print("-> Blue Before sub <-", blue)
        print("##########################################################")
        
        image_url = values.get_spotify_image_url(song)


    return render_template('song.html', song=song_name,  image_url=image_url, red = red, green = green, blue = blue)
 
if __name__ == '__main__':
   app.run(debug=True)