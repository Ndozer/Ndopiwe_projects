const playButton = document.getElementById('playButton');
const CLIENT_ID = '32c037ea12744f3d90314f5c7deb5027';
// Clean redirect URI without parameters
const REDIRECT_URI = window.location.origin + window.location.pathname; 
const SCOPES = 'streaming user-read-playback-state user-modify-playback-state';

let player;
let deviceId;
let accessToken = '';

// Helper function to generate a random string for PKCE cryptographics
const generateRandomString = (length) => {
    const possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const values = crypto.getRandomValues(new Uint8Array(length));
    return values.reduce((acc, x) => acc + possible[x % possible.length], "");
};

// Helper function to hash the code verifier
const sha256 = async (plain) => {
    const encoder = new TextEncoder();
    const data = encoder.encode(plain);
    return crypto.subtle.digest('SHA-256', data);
};

const base64urlencode = (a) => {
    return btoa(String.fromCharCode.apply(null, new Uint8Array(a)))
        .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
};

// --- START AUTH HANDLING ---

// Check if we are returning from Spotify with an Auth Code (?code=...)
const urlParams = new URLSearchParams(window.location.search);
const code = urlParams.get('code');

if (code) {
    // Hide login right away while we fetch the token
    document.getElementById('loginBtn').style.display = 'none';
    document.getElementById('trackName').textContent = "Exchanging code for token...";
    
    // Exchange the Auth Code for an Access Token
    const codeVerifier = window.localStorage.getItem('code_verifier');
    
    const payload = {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({
            client_id: CLIENT_ID,
            grant_type: 'authorization_code',
            code: code,
            redirect_uri: REDIRECT_URI,
            code_verifier: codeVerifier,
        }),
    };

    fetch('https://accounts.spotify.com/api/token', payload)
        .then(response => response.json())
        .then(data => {
            if (data.access_token) {
                accessToken = data.access_token;
                // Clean the browser URL bar
                window.history.replaceState({}, document.title, window.location.pathname);
                
                // Show play controls
                playButton.style.display = 'block'; 
                document.getElementById('trackName').textContent = "Connecting to Spotify SDK...";
                document.getElementById('artistName').textContent = "Please wait...";
                
                // Trigger SDK connection manually if it already loaded
                if (window.Spotify) {
                    window.onSpotifyWebPlaybackSDKReady();
                }
            } else {
                console.error('Failed token exchange', data);
                document.getElementById('trackName').textContent = "Auth Error";
            }
        });
}

// Redirect user to Spotify Login when clicking connect
document.getElementById('loginBtn').addEventListener('click', async () => {
    const codeVerifier = generateRandomString(64);
    const hashed = await sha256(codeVerifier);
    const codeChallenge = base64urlencode(hashed);
    
    window.localStorage.setItem('code_verifier', codeVerifier);

    const params = {
        response_type: 'code', // Fixed: Explicitly requesting code now!
        client_id: CLIENT_ID,
        scope: SCOPES,
        code_challenge_method: 'S256',
        code_challenge: codeChallenge,
        redirect_uri: REDIRECT_URI,
        show_dialog: 'true'
    };

    const authUrl = new URL("https://accounts.spotify.com/authorize");
    authUrl.search = new URLSearchParams(params).toString();
    window.location.href = authUrl.toString();
});

// --- SPOTIFY WEB PLAYBACK SDK ---

window.onSpotifyWebPlaybackSDKReady = () => {
    if (!accessToken || player) return; // Don't re-initialize if already done
    
    player = new Spotify.Player({
        name: "Ndops's Web Player",
        getOAuthToken: cb => { cb(accessToken); },
        volume: 0.5
    });

    player.addListener('ready', ({ device_id }) => {
        console.log('Ready with Device ID', device_id);
        deviceId = device_id;
        document.getElementById('trackName').textContent = "Connected to Spotify";
        document.getElementById('artistName').textContent = "Ready to Play";
    });

    player.addListener('player_state_changed', state => {
        if (!state) return;
        
        const currentTrack = state.track_window.current_track;
        document.getElementById('trackName').textContent = currentTrack.name;
        document.getElementById('artistName').textContent = currentTrack.artists.map(a => a.name).join(', ');
        
        if (state.paused) {
            playButton.textContent = 'Play';
        } else {
            playButton.textContent = 'Pause';
        }
    });

    player.connect();
};

// Control Playback
playButton.addEventListener('click', () => {
    if (player) {
        player.togglePlay().then(() => {
            console.log('Toggled playback!');
        });
    }
});