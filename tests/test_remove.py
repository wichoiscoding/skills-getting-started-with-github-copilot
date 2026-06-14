def test_remove_participant_success(client):
    """Test successful removal of a participant from an activity."""
    # Arrange: Use existing participant
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Known participant from initial data
    
    # Act: Remove participant
    response = client.post(f"/activities/{activity_name}/remove?email={email}")
    
    # Assert: Verify success
    assert response.status_code == 200
    result = response.json()
    assert "message" in result
    assert email in result["message"]
    assert activity_name in result["message"]


def test_remove_removes_participant_from_activity(client):
    """Test that removal actually removes the participant."""
    # Arrange: Get current participants
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    
    initial_response = client.get("/activities")
    initial_participants = initial_response.json()[activity_name]["participants"]
    initial_count = len(initial_participants)
    assert email in initial_participants
    
    # Act: Remove participant
    client.post(f"/activities/{activity_name}/remove?email={email}")
    
    # Assert: Verify participant was removed
    updated_response = client.get("/activities")
    updated_participants = updated_response.json()[activity_name]["participants"]
    assert len(updated_participants) == initial_count - 1
    assert email not in updated_participants


def test_remove_success_message_format(client):
    """Test that removal returns properly formatted success message."""
    # Arrange: Existing participant data
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    
    # Act: Remove
    response = client.post(f"/activities/{activity_name}/remove?email={email}")
    result = response.json()
    
    # Assert: Verify message format
    assert response.status_code == 200
    assert "Removed" in result["message"]
    assert email in result["message"]
    assert activity_name in result["message"]
