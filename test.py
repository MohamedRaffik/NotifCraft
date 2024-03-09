import json

f = open("test.json", "w")
json.dump(
    {
        "series": {
            "id": 43,
            "title": "90 Day Fiancé: Before the 90 Days",
            "titleSlug": "90-day-fiance-before-the-90-days",
            "path": "/shared/TV_Shows/90 Day Fiancé - Before the 90 Days (2017)",
            "tvdbId": 332747,
            "tvMazeId": 26534,
            "imdbId": "tt7252812",
            "type": "standard",
            "year": 2017,
        },
        "episodes": [
            {
                "id": 3578,
                "episodeNumber": 2,
                "seasonNumber": 5,
                "title": "Catching Flights and Feelings",
                "overview": "Jasmine's jealousy rears its head; Memphis has a secret about her ex; Alina worries that Caleb doesn't understand her abilities; Usman's friends do not support his relationship with Kim; Mike's friends believe his girlfriend Ximena is using him.",
                "airDate": "2021-12-19",
                "airDateUtc": "2021-12-20T01:00:00Z",
                "seriesId": 43,
                "tvdbId": 8878633,
            }
        ],
        "release": {
            "quality": "WEBRip-480p",
            "qualityVersion": 1,
            "releaseTitle": "90.Day.Fiance.Before.The.90.Days.S05E02.WebRip.allone",
            "indexer": "Isohunt2 (Prowlarr)",
            "size": 485385824,
            "customFormatScore": 0,
            "customFormats": ["English"],
        },
        "downloadClient": "qbittorrent",
        "downloadClientType": "qBittorrent",
        "downloadId": "988C756139CAF745A8ECF89444F69E6E8D803319",
        "customFormatInfo": {
            "customFormats": [{"id": 25, "name": "English"}],
            "customFormatScore": 0,
        },
        "eventType": "Grab",
        "instanceName": "Sonarr",
        "applicationUrl": "",
    },
    f,
)
f.close()
