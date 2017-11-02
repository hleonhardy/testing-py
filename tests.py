"""Testsq for Balloonicorn's Flask app."""

import unittest
import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""
        #treat me like localhost:5000, but don't load the server
        self.client = party.app.test_client()
        party.app.config['TESTING'] = True
        print 'this works 0'

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn("having a party", result.data)
        print "this works 1"

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        result = self.client.get('/')
        self.assertIn('Please RSVP', result.data)
        # print 'this works 2'

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        #test you don't see rsvp form
        print "it works, bitches"
        self.assertNotIn('Please RSVP', result.data)
        print 'please rsvp, betch'
        self.assertIn('Please Don\'t RSVP', result.data)
        #test you DO see party details
        self.assertIn('Magic Unicorn Way', result.data)

        



        # FIXME: check that once we log in we see party details--but not the form!

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # FIXME: write a test that mel can't invite himself
        pass
        print "FIXME"


if __name__ == "__main__":
    unittest.main()
