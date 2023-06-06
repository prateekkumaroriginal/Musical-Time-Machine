# Musical Time Machine
This Python program creates a Spotify playlist of the Billboard Hot 100 songs for a specific date.

## Setup

1. Clone the repository or download the Python file.
2. Install the required libraries using pip.
3. Obtain the necessary credentials:
- Spotify: Create a Spotify developer account and create an application to obtain the `CLIENT_ID`, `CLIENT_SECRET`, and `REDIRECT_URI`. Set the `REDIRECT_URI` as a valid redirect URI for your Spotify application.
4. Set the environment variables:
- `CLIENT_ID`: Your Spotify application's client ID.
- `CLIENT_SECRET`: Your Spotify application's client secret.
- `REDIRECT_URI`: Your Spotify application's redirect URI.

## Usage
1. Run the Python script in your terminal or IDE.
2. Enter the date you want to travel to in the format `YYYY-MM-DD` when prompted.
3. The program will scrape the Billboard Hot 100 songs for the specified date from [billboard.com](https://www.billboard.com/charts/hot-100/).
4. It will authenticate with Spotify using your provided credentials.
5. The program will search for each song on Spotify and retrieve the track URI.
6. It will create a new private Spotify playlist with the name `[travel_date] Billboard 100` (e.g., `2023-06-06 Billboard 100`) if it doesn't already exist.
7. Finally, the program will add the retrieved song URIs to the playlist.

## Note
Ensure that your Spotify account has the necessary permissions to create private playlists and modify your playlists.

## Tech Stack
Language: `Python` <br>
Libraries: `spotipy`, `BeautifulSoup`, `requests`, `datetime`, and `os`

## API's 
<a href="https://developer.spotify.com/documentation/web-api">Spotify Web API</a> - `spotipy` uses `Spotify Web API` behind the scenes.
