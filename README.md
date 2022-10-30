
# Automation of your Spotify testing playlist

I've always had a playlist for new music I was listening to that I didn't know if I would like it. And after finally deciding that it was good I would have to add it to my main playlist and delete it from my testing one. \
So I decided to make a program that would detect when a song was in both playlist and if so then delete it from your testing playlist automatically.


## How to use

To run the script first install the requirements.txt. After that add the **client ID** and the **client secret** in the authorization file. You can leave them hardcoded or set them up as env variables or store them in a DB, that's up to you. Also you can add a username for the authorize function. \
After that just run the script. It will ask for the main playlist ID and the test playlist ID. To get the ID  of a playlist just right click it, share, copy link to playlist. \
This will get you a full playlist link that looks like the following: \
`https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U?si=9f6A6U2jTk-njyZJ64rk3g` \
The playlist id is the string right after playlist/ and until the ?. 

If you'd like to not have to input your playlist id everytime you can just leave them hardcoded in the script.

