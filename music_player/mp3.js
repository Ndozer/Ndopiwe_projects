const statusDiv = document.getElementById('status');
const masterToggle = document.getElementById('master-toggle');
const masterIcon = document.getElementById('master-icon');
const progressBar = document.getElementById('song-progress');
const currentTimeLabel = document.getElementById('current-time');
const totalTimeLabel = document.getElementById('total-time');

// Search & Metadata Tracking Nodes
const searchInput = document.getElementById('track-search');
const uiTitle = document.getElementById('ui-title');
const uiArtist = document.getElementById('ui-artist');
const uiArt = document.getElementById('ui-art');

// Toggles
const repeatBtn = document.getElementById('btn-repeat');
const queueBtn = document.getElementById('btn-queue');
const nextBtn = document.getElementById('btn-next');
const prevBtn = document.getElementById('btn-prev');

let player;
let updateInterval;
let isUserDragging = false;
let isRepeatActive = false;
let isQueueActive = false;

// Local Fallback Mock Track Database for Text Search Matching
const localMockLibrary = [
    { title: "THANK GOD I'M FREE", artist: "Elevation Rhythm", id: "Ok3CunjHKLI" },
    { title: "Revival’s In The Air", artist: "Bethel Music & Melissa Helser", id: "u9TCQuni5Jw" },
    { title: "WASHED", artist: "Elevation Rhythm", id: "JjgkhHlTROQ" }
];
let currentTrackIndex = 0;

// 1. YouTube API asynchronous bootstrapping script loading
const tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
document.head.appendChild(tag);

function onYouTubeIframeAPIReady() {
    statusDiv.innerText = "Video Loaded :)";
    
    // Set the initial thumbnail on startup
    const initialTrack = localMockLibrary[currentTrackIndex];
    const initialThumb = `https://img.youtube.com/vi/${initialTrack.id}/maxresdefault.jpg`;
    uiArt.innerHTML = `<img src="${initialThumb}" alt="Cover" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px;" onerror="this.src='https://img.youtube.com/vi/${initialTrack.id}/hqdefault.jpg'">`;

    player = new YT.Player('youtube-audio-player', {
        height: '200',
        width: '200',
        videoId: initialTrack.id,
        host: 'https://www.youtube-nocookie.com',
        playerVars: {
            'playsinline': 1,
            'controls': 0,
            'disablekb': 1,
            'origin': window.location.origin || 'http://localhost'
        },
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange,
            'onError': onPlayerError
        }
    });
}

function onPlayerReady(event) {
    statusDiv.innerText = "Jammy time!";
    setupEventListeners();
}

function setupEventListeners() {
    // Master Action Toggle Logic
    masterToggle.addEventListener('click', () => {
        const state = player.getPlayerState();
        if (state === YT.PlayerState.PLAYING) {
            player.pauseVideo();
        } else {
            player.playVideo();
        }
    });

    // Timeline Dragging Hook Mechanics
    progressBar.addEventListener('input', () => { isUserDragging = true; });
    progressBar.addEventListener('change', () => {
        const newTime = (progressBar.value / 100) * player.getDuration();
        player.seekTo(newTime, true);
        isUserDragging = false;
    });

    // Functional Layout Feature Modifiers
    repeatBtn.addEventListener('click', () => {
        isRepeatActive = !isRepeatActive;
        repeatBtn.classList.toggle('active', isRepeatActive);
    });

    queueBtn.addEventListener('click', () => {
        isQueueActive = !isQueueActive;
        queueBtn.classList.toggle('active', isQueueActive);
        if(isQueueActive) statusDiv.innerText = "Queue formed with local library";
    });

    nextBtn.addEventListener('click', () => changeTrack(1));
    prevBtn.addEventListener('click', () => changeTrack(-1));

    // Custom Text Entry Search Wrapper 
    searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            processSearch(searchInput.value);
        }
    });
}

let currentSearchResults = [];
let currentResultIndex = 0;

async function processSearch(query) {
    if (!query.trim()) return;
    statusDiv.innerText = "Searching YouTube...";
    const urlMatch = query.match(
        /(?:https?:\/\/)?(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w-]{11})/
    );
    if (urlMatch) {
        playDirectId(urlMatch[1], "YouTube Video", "Direct Link");
        return;
    }
    try {
        const response = await fetch(
            `https://pipedapi.kavin.rocks/search?q=${encodeURIComponent(query)}`
        );
        const data = await response.json();
        if (!data?.videos?.length) {
            statusDiv.innerText = "No results found.";
            return;
        }
        currentSearchResults = data.videos;
        currentResultIndex = 0;
        playSearchResult(currentResultIndex);
    } catch (err) {
        console.error(err);
        statusDiv.innerText = "Search failed.";
    }
}

function playSearchResult(index) {
    const video = currentSearchResults[index];
    if (!video) {
        statusDiv.innerText = "No playable version found.";
        return;
    }
    let videoId = "";
    if (video.url.includes("v=")) {
        videoId = video.url.split("v=")[1].split("&")[0];
    } else {
        videoId = video.url.split("/").pop();
    }
    uiTitle.innerText = video.title;
    uiArtist.innerText = video.uploaderName || "Unknown Artist";
    player.loadVideoById(videoId);
}

function playDirectId(id, title, artist) {
    uiTitle.innerText = title;
    uiArtist.innerText = artist;
    const thumbnailUrl = `https://img.youtube.com/vi/${id}/maxresdefault.jpg`;
    uiArt.innerHTML = `
        <img src="${thumbnailUrl}" alt="${title} Cover" 
             style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px;"
             onerror="this.src='https://img.youtube.com/vi/${id}/hqdefault.jpg'">
    `;
    player.loadVideoById(id);
    searchInput.value = '';
}

function changeTrack(direction) {
    currentTrackIndex = (currentTrackIndex + direction + localMockLibrary.length) % localMockLibrary.length;
    const track = localMockLibrary[currentTrackIndex];
    playDirectId(track.id, track.title, track.artist);
}

function onPlayerStateChange(event) {
    clearInterval(updateInterval);
    
    if (event.data === YT.PlayerState.PLAYING) {
        masterIcon.innerText = "pause";
        uiArt.classList.add('playing');
        statusDiv.innerText = "Now Playing";
        
        // Track synchronization intervals
        updateInterval = setInterval(syncTimelineDisplay, 500);
    } else {
        masterIcon.innerText = "play_arrow";
        uiArt.classList.remove('playing');
        if (event.data === YT.PlayerState.PAUSED) statusDiv.innerText = "Paused";
        
        // Active video loop termination evaluation
        if (event.data === YT.PlayerState.ENDED) {
            if (isRepeatActive) {
                player.playVideo();
            } else {
                changeTrack(1); 
            }
        }
    }
}

function syncTimelineDisplay() {
    if (!player || isUserDragging) return;

    const current = player.getCurrentTime() || 0;
    const total = player.getDuration() || 0;

    if (total > 0) {
        const percentage = (current / total) * 100;
        progressBar.value = percentage;
        currentTimeLabel.innerText = formatTimeFormat(current);
        totalTimeLabel.innerText = formatTimeFormat(total);
    }
}

function formatTimeFormat(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
}

function onPlayerError(event) {
    if (event.data === 150 || event.data === 101) {
        statusDiv.innerText = "Playback restricted. Finding alternative...";
        if (searchInput.value) {
            const retryQuery = searchInput.value + " audio";
            fallbackSearch(retryQuery);
        } else {
            statusDiv.innerText = "Track restricted. Try typing the song name with 'lyrics'.";
        }
    } else {
        statusDiv.innerText = "Error Code: " + event.data;
    }
}

async function fallbackSearch(query) {
    try {
        const response = await fetch(`https://pipedapi.kavin.rocks/search?q=${encodeURIComponent(query)}&filter=music_songs`);
        const data = await response.json();
        if (data && data.videos && data.videos.length > 1) {
            const backupResult = data.videos[1]; 
            const videoId = backupResult.url.includes("v=") ? backupResult.url.split("v=")[1] : backupResult.url.split("/").pop();
            playDirectId(videoId, backupResult.title, backupResult.uploaderName);
        }
    } catch(e) {
        statusDiv.innerText = "Could not find an unrestricted version.";
    }
}