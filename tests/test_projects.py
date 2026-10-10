import importlib.util
import pathlib
import unittest


def load(name):
    path = pathlib.Path(__file__).resolve().parents[1] / "projects" / name / "app.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ProjectTests(unittest.TestCase):
    def test_purchase_retry_and_conflict(self):
        store = load("streamcommerce").Store()
        for _ in range(2):
            store.purchase("req", "viewer", "creator", "gift", 500)
        self.assertEqual(store.revenue("creator"), 500)
        with self.assertRaises(ValueError):
            store.purchase("req", "viewer", "creator", "gift", 900)
        self.assertEqual(store.revenue("creator"), 500)
        with self.assertRaises(ValueError):
            store.purchase("bad", "viewer", "creator", "gift", -1)

    def test_chat_delivery_moderation_and_backpressure(self):
        room = load("livestream").Community()
        host = room.join("coding", "host")
        viewer = room.join("coding", "viewer")
        for i in range(105):
            room.publish("coding", "host", str(i))
        self.assertEqual(viewer.qsize(), 100)
        self.assertEqual(viewer.get_nowait()["text"], "5")
        room.ban("viewer")
        with self.assertRaises(ValueError):
            room.publish("coding", "viewer", "hello")
        self.assertEqual(host.qsize(), 100)

    def test_ranking_and_notification_retries(self):
        module = load("creatorpulse")
        creators = [{"id": "b", "tags": ["python"]},
                    {"id": "a", "tags": ["python", "sql"]},
                    {"id": "c", "tags": ["music"]}]
        self.assertEqual([c["id"] for c in module.recommend(creators, ["python", "sql"])], ["a", "b"])
        self.assertEqual([c["id"] for c in module.recommend(creators, ["python"], followed=["a"])], ["b"])
        self.assertEqual(module.recommend(creators, ["python"], k=0), [])
        outbox = module.NotificationOutbox()
        outbox.enqueue("event", "user", "a")
        outbox.enqueue("event", "user", "a")
        self.assertEqual(len(outbox.events), 1)
        with self.assertRaises(ValueError):
            outbox.enqueue("event", "user", "b")
