# Hi, I'm Priya

I'm interested in backend development, real-time applications, and recommendation systems.

🎓 **Bachelor's:** Computer Science Engineering — Artificial Intelligence & Machine Learning  
🎓 **Master's:** Information Technology

## Java projects

Three runnable Java 17 projects, each with tests, a reproducible reliability demo, and documented limitations.

| Project | Current implementation | Built with |
| --- | --- | --- |
| [TaskFlow](https://github.com/priyamukkapati/TaskFlow) | Browser Kanban board, task/comment HTTP API, local snapshots, optimistic version checks | Java 17, JDK HTTP server, JavaScript, HTML/CSS |
| [InventoryLedger](https://github.com/priyamukkapati/InventoryLedger) | Inventory receipts and transfers, idempotent request IDs, journal replay, stock conservation | Java 17, file journal |
| [NotifyQueue](https://github.com/priyamukkapati/NotifyQueue) | Bounded event retention, duplicate detection, exponential retries, dead-letter handling, redrive | Java 17, PriorityQueue |

These are local projects. TaskFlow is one process; InventoryLedger is a CLI; NotifyQueue uses a simulated transport. None is deployed to AWS or implements a distributed service.

Clone each Java repository using its README instructions to run its tests and demos.

## Python prototypes

| Project | What the current version does | Built with |
| --- | --- | --- |
| [StreamCommerce](https://github.com/priyamukkapati/StreamCommerce) | Records subscriptions and gifts, handles purchase retries, and totals creator revenue | Python, SQLite |
| [LiveStream](https://github.com/priyamukkapati/LiveStream) | Models chat rooms with message delivery, moderation, and bounded queues | Python, asyncio |
| [CreatorPulse](https://github.com/priyamukkapati/CreatorPulse) | Ranks creators by interests and queues notification events without duplicates | Python, heapq |

These are early local prototypes. The larger platform features are documented in each project's roadmap.

## Run the Python prototypes

```sh
git clone https://github.com/priyamukkapati/priyamukkapati.git
cd priyamukkapati
# Python: requires Python 3.10+, no external packages
python3 projects/streamcommerce/app.py
python3 projects/livestream/app.py
python3 projects/creatorpulse/app.py
python3 -m unittest discover -s tests -v
```

For a hiring-oriented comparison and next proofs for the Python repositories, see [the backend project review](docs/backend-project-review.md).

## Connect

[GitHub](https://github.com/priyamukkapati)
