from flask import url_for
from flask_testing import TestCase
from app import app, db
from application.models import ForceUsers, Masters

class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        # Create test registree
        test = ForceUsers (name="BenSolo", power="Pull")
        test1 = Masters (name = "marko", side = "dark", forceusers_id = "1")
        # save users to database
        db.session.add(test)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

# Write a test class to test Read functionality
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('forceuser'))
        self.assertEqual(response.status_code, 200)

class TestCreate(TestBase):
    def test_forceusers_add(self):
        with self.client:
            response = self.client.post(
                '/forceusers',
                data=dict(
                    name = 'anakin',
                    power = 'pull'
                ),
                follow_redirects=True
            
            )
            self.assertIn(b'anakin', response.data)  


class TestCreateM(TestBase):
    def test_masters_add(self):
        with self.client:
            response = self.client.post(
                '/add_master',
                data=dict(
                    name = 'marko',
                    side = 'dark',
                    forceusers_id = "1"

                ),
                follow_redirects=True
            )
            self.assertIn(b'marko', response.data)     

class TestUpdate(TestBase):
    def test_forceusers_update(self):
        with self.client:
            response = self.client.post('/update',
                data=dict(
                    name = 'BenSolo',
                    power = 'pull'

                ),
                follow_redirects=True
                )
            self.assertNotIn(b'BenSolo', response.data)

class TestDelete(TestBase):
    def test_delete(self):
        with self.client:
            response = self.client.delete('/delete',
                data=dict(
                    name = 'BenSolo',
                    power = 'pull'
                ),
                follow_redirects=True
                )
            self.assertNotIn(b'BenSolo', response.data)


    