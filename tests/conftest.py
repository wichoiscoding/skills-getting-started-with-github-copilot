import pytest
from copy import deepcopy
from fastapi.testclient import TestClient
from src.app import app, activities


# Store original activities for resetting between tests
ORIGINAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture
def client():
    """Fixture: Provides a TestClient with fresh activities state for each test."""
    # Arrange: Reset activities to original state
    activities.clear()
    activities.update(deepcopy(ORIGINAL_ACTIVITIES))
    
    # Return TestClient instance
    yield TestClient(app)
    
    # Cleanup: Reset activities after test
    activities.clear()
    activities.update(deepcopy(ORIGINAL_ACTIVITIES))


@pytest.fixture
def sample_activity():
    """Fixture: Provides sample activity data for testing."""
    return {
        "name": "Chess Club",
        "email": "newstudent@mergington.edu"
    }
