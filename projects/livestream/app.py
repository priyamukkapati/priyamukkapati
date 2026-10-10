"""In-process community chat prototype with bounded queues and moderation."""
import asyncio


class Community:
    def __init__(self):
        self.rooms = {}
        self.banned = set()

    def join(self, room, user):
        if not room.strip() or not user.strip() or user in self.banned:
            raise ValueError("A valid room and unbanned user are required")
        members = self.rooms.setdefault(room, {})
        if user in members:
            raise ValueError("User already joined this room")
        queue = asyncio.Queue(maxsize=100)
        members[user] = queue
        return queue

    def leave(self, room, user):
        members = self.rooms.get(room, {})
        members.pop(user, None)
        if not members:
            self.rooms.pop(room, None)

    def ban(self, user):
        self.banned.add(user)
        for room in list(self.rooms):
            self.leave(room, user)

    def publish(self, room, user, text):
        members = self.rooms.get(room, {})
        if user in self.banned or user not in members:
            raise ValueError("Join the room before posting")
        text = text.strip()
        if not text or len(text) > 500:
            raise ValueError("Messages must contain 1–500 characters")
        message = {"user": user, "text": text}
        for queue in members.values():
            if queue.full():
                queue.get_nowait()  # Drop oldest message for slow consumers.
            queue.put_nowait(dict(message))


async def demo():
    community = Community()
    community.join("coding", "host")
    viewer = community.join("coding", "viewer")
    community.publish("coding", "host", "Welcome to the coding session!")
    print(await viewer.get())


if __name__ == "__main__":
    asyncio.run(demo())
