import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
        
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    # Testataan search-metodi ja pelaajan arvot
    def test_search_returns_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 37)
        self.assertEqual(player.assists, 53)

    #Testataan search-metodi ja None palautus, kun pelaajaa ei löydy
    def test_search_returns_none_for_nonexistent_player(self):
        player = self.stats.search("Nemo Nemonen")
        self.assertIsNone(player)

    #Testataan team-metodi ja joukkueen pelaajien määrä
    def test_team_returns_correct_number_of_players(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)
        player = players[0]
        self.assertEqual(player.name, "Semenko")

    #Testataan top-metodi ja top-pelaajien määrä
    def test_top_returns_correct_number_of_players(self):   
        top_players = self.stats.top(1)
        self.assertEqual(len(top_players), 2)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")

    #Testataan Player-luokan __str__-metodia
    def test_player_str_method(self):
        player = Player("Testi", "TST", 10, 20)
        self.assertEqual(str(player), "Testi TST 10 + 20 = 30")
