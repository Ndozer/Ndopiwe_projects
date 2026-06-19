// server.js
const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// Endpoint to get bus times based on location
app.post('/api/bus-times', async (req, require, res) => {
    const { latitude, longitude } = req.body;

    if (!latitude || !longitude) {
        return res.status(400).json({ error: 'Latitude and longitude are required.' });
    }

    try {
        // Example using a generic Transit API or Google Places/Directions API
        // For actual real-time buses, you often query a local GTFS-RT feed
        const apiKey = process.env.GOOGLE_MAPS_API_KEY;
        const url = `https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=${latitude},${longitude}&radius=500&type=bus_station&key=${apiKey}`;

        const response = await fetch(url);
        const data = await response.json();

        // Parse and format the data to send back to the frontend
        // (In a complete app, you'd fetch the actual departures for these stops)
        res.json({
            success: true,
            stops: data.results.map(stop => ({
                name: stop.name,
                id: stop.place_id,
                vicinity: stop.vicinity
            }))
        });

    } catch (error) {
        console.error('Error fetching transit data:', error);
        res.status(500).json({ error: 'Failed to fetch transit data.' });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});