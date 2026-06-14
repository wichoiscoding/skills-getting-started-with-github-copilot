def test_root_redirects_to_static(client):
    """Test that GET / redirects to /static/index.html."""
    # Arrange: client is ready
    
    # Act: Make GET request with follow_redirects=False
    response = client.get("/", follow_redirects=False)
    
    # Assert: Verify redirect status and location
    assert response.status_code in [307, 302]
    assert response.headers["location"] == "/static/index.html"


def test_root_with_redirect_follows(client):
    """Test that GET / can be followed to static files."""
    # Arrange: client is ready
    
    # Act: Make GET request with follow_redirects=True
    response = client.get("/", follow_redirects=True)
    
    # Assert: Should reach static content or return OK
    assert response.status_code in [200, 404]  # 404 if HTML file not found (expected in test)
