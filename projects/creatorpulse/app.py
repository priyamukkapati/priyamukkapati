"""Deterministic Top-K creator ranking with an idempotent notification outbox."""
import heapq


def recommend(creators, interests, followed=(), k=3):
    if type(k) is not int or k < 0:
        raise ValueError("k must be a nonnegative integer")
    interests, followed = set(interests), set(followed)
    candidates = []
    seen = set()
    for creator in creators:
        creator_id = creator["id"]
        if creator_id in seen:
            raise ValueError("Creator IDs must be unique")
        seen.add(creator_id)
        if creator_id in followed:
            continue
        overlap = len(interests & set(creator["tags"]))
        if overlap:
            candidates.append({"id": creator_id, "score": overlap,
                               "reason": f"Matches {overlap} of your interests"})
    return heapq.nsmallest(k, candidates, key=lambda c: (-c["score"], c["id"]))


class NotificationOutbox:
    def __init__(self):
        self.events = {}

    def enqueue(self, event_id, user, creator):
        payload = {"user": user, "creator": creator}
        if event_id in self.events and self.events[event_id] != payload:
            raise ValueError("Event ID already used with a different payload")
        self.events.setdefault(event_id, payload)


if __name__ == "__main__":
    creators = [{"id": "code-with-sam", "tags": ["python", "backend"]},
                {"id": "design-with-lee", "tags": ["design", "react"]},
                {"id": "data-with-jo", "tags": ["python", "data"]}]
    for result in recommend(creators, ["python", "backend"]):
        print(result)
