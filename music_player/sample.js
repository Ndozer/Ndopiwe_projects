// Authorization token that must have been created previously. See : https://developer.spotify.com/documentation/web-api/concepts/authorization
const token = 'BQCYt03KMjQE1nIgBdku8_KPmGYvWvOLDcHaDbyZOhkawDSmmVnkyykafr_3goilrZb-a6fn6c2NCE_OcOQv1j4gvLFGIPFdaSqf2lBVYldiS-dzS4Hv49mYgcC2eWe9tV0_SWGWVKlJuc2gTxF0tdI1b6mAbtRlLpCV7D9QBBBu7ZaCeqTaOb-pOsoEoICRwtPROa-WympqIvC7W8vWll_LehpVpAhuxzTpYdXL0CLaXsLT_GTXOed2ELPknCoXjR7Zxsw1KfAh7xmKK33f4G2sBMBhZujj7UYxezCsuMJ2jsRR_IVmHkIrYodlAj_yodBUSso';
async function fetchWebApi(endpoint, method, body) {
  const res = await fetch(`https://api.spotify.com/${endpoint}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    method,
    body:JSON.stringify(body)
  });
  return await res.json();
}

async function getTopTracks(){
  // Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
  return (await fetchWebApi(
    'v1/me/top/tracks?time_range=long_term&limit=5', 'GET'
  )).items;
}

const topTracks = await getTopTracks();
console.log(
  topTracks?.map(
    ({name, artists}) =>
      `${name} by ${artists.map(artist => artist.name).join(', ')}`
  )
);

// Authorization token that must have been created previously. See : https://developer.spotify.com/documentation/web-api/concepts/authorization
const token = 'BQCYt03KMjQE1nIgBdku8_KPmGYvWvOLDcHaDbyZOhkawDSmmVnkyykafr_3goilrZb-a6fn6c2NCE_OcOQv1j4gvLFGIPFdaSqf2lBVYldiS-dzS4Hv49mYgcC2eWe9tV0_SWGWVKlJuc2gTxF0tdI1b6mAbtRlLpCV7D9QBBBu7ZaCeqTaOb-pOsoEoICRwtPROa-WympqIvC7W8vWll_LehpVpAhuxzTpYdXL0CLaXsLT_GTXOed2ELPknCoXjR7Zxsw1KfAh7xmKK33f4G2sBMBhZujj7UYxezCsuMJ2jsRR_IVmHkIrYodlAj_yodBUSso';
async function fetchWebApi(endpoint, method, body) {
  const res = await fetch(`https://api.spotify.com/${endpoint}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    method,
    body:JSON.stringify(body)
  });
  return await res.json();
}

const tracksUri = [
  'spotify:track:1V9AYsVkGvDL0XrkYvUOGv','spotify:track:7hTuu9yMzkd2WzUskxvXRD','spotify:track:0bMV7EnPQeKty8Jc8GQuwC','spotify:track:5doYljP28aXEnQryAPrcka','spotify:track:1YfPtfVO4gw6Oo4utlb4VL'
];

async function createPlaylist(tracksUri){
  const playlist = await fetchWebApi(
    'v1/me/playlists', 'POST', {
      "name": "My top tracks playlist",
      "description": "Playlist created by the tutorial on developer.spotify.com",
      "public": false
  })

  await fetchWebApi(
    `v1/playlists/${playlist.id}/items?uris=${tracksUri.join(',')}`,
    'POST'
  );

  return playlist;
}

const createdPlaylist = await createPlaylist(tracksUri);
console.log(createdPlaylist.name, createdPlaylist.id);

const playlistId = '3ndjVfbiBEN59m94ZaMPrn';

<iframe
  title="Spotify Embed: Recommendation Playlist "
  src={`https://open.spotify.com/embed/playlist/3ndjVfbiBEN59m94ZaMPrn?utm_source=generator&theme=0`}
  width="100%"
  height="100%"
  style={{ minHeight: '360px' }}
  frameBorder="0"
  allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
  loading="lazy"
/>