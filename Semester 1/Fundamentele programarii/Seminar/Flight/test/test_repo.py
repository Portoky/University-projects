import unittest

from Domain.entity import FlightValidator, Flight
from repo.flie_repo import FileRepo
from repo.mem_repo import MemoRepo, RepoException


class TestRepo(unittest.TestCase):
    def setUp(self):
        self.repo = MemoRepo(FlightValidator())
        self.filerepo = FileRepo("flights.txt", FlightValidator())
        self.flight1 = Flight("RO650","Cluj",345,"Bucuresti",400)

    def test_add(self):
        self.repo.add(self.flight1)
        self.assertEqual(self.repo.find_by_id("RO650"), self.flight1), "Not good"
        self.assertRaises(RepoException, self.repo.add, self.flight1)

    def test_loadfile(self):
        self.assertEqual(self.filerepo.find_by_id("RO650"), self.flight1)
        flight2 = Flight("SLD322","Timisoara",545,"Cluj",600)
        self.assertEqual(self.filerepo.find_by_id("SLD322"), None)
        self.filerepo.add(flight2)
        self.assertEqual(self.filerepo.find_by_id("SLD322"), flight2)