# LiveStream

A small prototype for the community chat part of a streaming platform.

## Current implementation

Provides room membership, message fan-out, user bans, a 500-character limit, and a 100-message queue per member. Slow readers lose their oldest message when their queue fills.

## Run

From the repository root, with Python 3.10+:

```bash
python3 projects/livestream/app.py
```

{'user': 'host', 'text': 'Welcome to the coding session!'}

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Limitations

Messages and membership exist in one process. This is not a video streaming server or a networked WebSocket application. Moderation methods are local calls and have no authentication layer.

## Roadmap

Add an authenticated WebSocket server, room-level moderator permissions, rate limiting, and a React client. Video streaming would require a separate media service.
