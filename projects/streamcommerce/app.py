"""Local subscription and gifting prototype. No real payments are processed."""
import sqlite3


class Store:
    def __init__(self, path=":memory:"):
        self.db = sqlite3.connect(path)
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS transactions (
          request_id TEXT PRIMARY KEY, buyer TEXT NOT NULL,
          creator TEXT NOT NULL, kind TEXT NOT NULL, cents INTEGER NOT NULL);
        """)

    def purchase(self, request_id, buyer, creator, kind, cents):
        if kind not in {"subscription", "gift"} or type(cents) is not int or cents <= 0:
            raise ValueError("Use subscription or gift and a positive integer amount in cents")
        if not all(isinstance(x, str) and x.strip() for x in (request_id, buyer, creator)):
            raise ValueError("Request ID, buyer, and creator are required")
        payload = (buyer, creator, kind, cents)
        with self.db:
            self.db.execute("INSERT OR IGNORE INTO transactions VALUES (?, ?, ?, ?, ?)",
                            (request_id, *payload))
            previous = self.db.execute("SELECT buyer, creator, kind, cents FROM transactions WHERE request_id=?",
                                       (request_id,)).fetchone()
            if previous != payload:
                raise ValueError("Request ID already used with a different purchase")
        return request_id

    def revenue(self, creator):
        return self.db.execute("SELECT COALESCE(SUM(cents),0) FROM transactions WHERE creator=?",
                               (creator,)).fetchone()[0]


if __name__ == "__main__":
    store = Store()
    store.purchase("demo-1", "viewer", "creator", "subscription", 499)
    store.purchase("demo-1", "viewer", "creator", "subscription", 499)
    store.purchase("demo-2", "viewer", "creator", "gift", 200)
    print(f"Creator revenue: ${store.revenue('creator') / 100:.2f}")
