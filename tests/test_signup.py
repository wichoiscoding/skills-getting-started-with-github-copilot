def test_signup_for_activity_success(client, sample_activity):
    """Test successful signup for an activity."""
    # Arrange: Get sample data
    activity_name = sample_activity["name"]
    email = sample_activity["email"]
    
    # Act: Make signup request
    response = client.post(
        f"/activities/{activity_name}/signup?email={email}",
        params={"email": email}
    )
    
    # Assert: Verify success
    assert response.status_code == 200
    result = response.json()
    assert "message" in result
    assert email in result["message"]
    assert activity_name in result["message"]


def test_signup_adds_participant_to_activity(client, sample_activity):
    """Test that signup actually adds the participant to the activity."""
    # Arrange: Get current participant count
    activity_name = sample_activity["name"]
    email = sample_activity["email"]
    
    initial_response = client.get("/activities")
    initial_participants = initial_response.json()[activity_name]["participants"]
    initial_count = len(initial_participants)
    
    # Act: Sign up
    client.post(f"/activities/{activity_name}/signup?email={email}")
    
    # Assert: Verify participant was added
    updated_response = client.get("/activities")
    updated_participants = updated_response.json()[activity_name]["participants"]
    assert len(updated_participants) == initial_count + 1
    assert email in updated_participants


def test_signup_success_message_format(client, sample_activity):
    """Test that signup returns properly formatted success message."""
    # Arrange: Sample data ready
    activity_name = sample_activity["name"]
    email = sample_activity["email"]
    
    # Act: Sign up
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    result = response.json()
    
    # Assert: Verify message format
    assert response.status_code == 200
    assert "Signed up" in result["message"]
    assert email in result["message"]
    assert activity_name in result["message"]
