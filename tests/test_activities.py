def test_get_activities_returns_all_activities(client):
    """Test that GET /activities returns all available activities."""
    # Arrange: client is already set up with activities
    
    # Act: Make GET request
    response = client.get("/activities")
    
    # Assert: Verify response
    assert response.status_code == 200
    activities = response.json()
    assert len(activities) == 9
    assert "Chess Club" in activities
    assert "Programming Class" in activities


def test_get_activities_contains_required_fields(client):
    """Test that each activity has required fields."""
    # Arrange: client is set up
    
    # Act: Get activities
    response = client.get("/activities")
    activities = response.json()
    
    # Assert: Check structure
    chess_club = activities["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)


def test_get_activities_participants_not_empty(client):
    """Test that activities have participants."""
    # Arrange: client is set up
    
    # Act: Get activities
    response = client.get("/activities")
    activities = response.json()
    
    # Assert: Chess Club should have participants
    assert len(activities["Chess Club"]["participants"]) > 0
