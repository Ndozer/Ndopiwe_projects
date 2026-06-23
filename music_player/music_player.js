const CLIENT_ID = '32c037ea12744f3d90314f5c7deb5027';
const playButton = document.getElementById('playButton');
const loginBtn = document.getElementById('loginBtn');
// INSERT YOUR CLIENT ID HERE
const REDIRECT_URI = window.location.origin + window.location.pathname; 
const SCOPES = 'streaming user-read-playback-state user-modify-playback-state';

let player;
let deviceId;
let accessToken = '';

// Cryptographic Utilities for PKCE Flow
const generateRandomString = (length) => {
    const possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const values = crypto.getRandomValues(new Uint8Array(length));
    return values.reduce((acc, x) => acc + possible[x % possible.length], "");
};

const sha256 = async (plain) => {
            const encoder = new TextEncoder();
            const data = encoder.encode(plain);
            return crypto.subtle.digest('SHA-256', data);
};

const base64urlencode = (a) => {
            return btoa(String.fromCharCode.apply(null, new Uint8Array(a)))
                .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
};

        // --- AUTH EXCHANGER ---
const urlParams = new URLSearchParams(window.location.search);
const code = urlParams.get('code');

if (code) {
            loginBtn.style.display = 'none';
            document.getElementById('trackName').textContent = "Exchanging authentication code...";
            
            const codeVerifier = window.localStorage.getItem('code_verifier');
            
            fetch('https://accounts.spotify.com/api/token', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams({
                    client_id: CLIENT_ID,
                    grant_type: 'authorization_code',
                    code: code,
                    redirect_uri: REDIRECT_URI,
                    code_verifier: codeVerifier,
                }),
            })
            .then(res => res.json())
            .then(data => {
                if (data.access_token) {
                    accessToken = data.access_token;
                    
                    // Critical: Clean the address bar completely so it stops redirect loops
                    window.history.replaceState({}, document.title, window.location.pathname);
                    
                    playButton.style.display = 'block'; 
                    document.getElementById('trackName').textContent = "Connected to Spotify App";
                    document.getElementById('artistName').textContent = "Open Spotify on your phone/PC to cast music";
                    
                    // Start player if SDK is already injected
                    if (window.Spotify) {
                        window.onSpotifyWebPlaybackSDKReady();
                    }
                } else {
                    console.error('Token Error:', data);
                    document.getElementById('trackName').textContent = "Authentication Failed";
                }
            })
            .catch(err => console.error("Fetch Exception:", err));
}

        // --- LOGIN CLICK HANDLER ---
loginBtn.addEventListener('click', async () => {
            const codeVerifier = generateRandomString(64);
            const hashed = await sha256(codeVerifier);
            const codeChallenge = base64urlencode(hashed);
            
            window.localStorage.setItem('code_verifier', codeVerifier);

            const authUrl = new URL("https://accounts.spotify.com/authorize");
            authUrl.search = new URLSearchParams({
                response_type: 'code',
                client_id: CLIENT_ID,
                scope: SCOPES,
                code_challenge_method: 'S256',
                code_challenge: codeChallenge,
                redirect_uri: REDIRECT_URI,
                show_dialog: 'true'
            }).toString();
            
            window.location.href = authUrl.toString();
});

        // --- SPOTIFY WEB PLAYBACK SDK INITIALIZATION ---
window.onSpotifyWebPlaybackSDKReady = () => {
            if (!accessToken || player) return;
            
            player = new Spotify.Player({
                name: "Ndops's Web Player",
                getOAuthToken: cb => { cb(accessToken); },
                volume: 0.5
            });

            player.addListener('ready', ({ device_id }) => {
                deviceId = device_id;
                document.getElementById('trackName').textContent = "Web Interface Ready!";
                document.getElementById('artistName').textContent = "Play something on Spotify!";
            });

            player.addListener('player_state_changed', state => {
                if (!state) return;
                const currentTrack = state.track_window.current_track;
                document.getElementById('trackName').textContent = currentTrack.name;
                document.getElementById('artistName').textContent = currentTrack.artists.map(a => a.name).join(', ');
                playButton.textContent = state.paused ? 'Play' : 'Pause';
            });

            player.connect();
};

playButton.addEventListener('click', () => {
            if (player) player.togglePlay();
});