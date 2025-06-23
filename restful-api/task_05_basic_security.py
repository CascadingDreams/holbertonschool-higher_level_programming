#!/usr/bin/env python3
"""
Flask API Security and Authentication Implementation

This module demonstrates comprehensive API security
implementation using Flask,
including basic HTTP authentication,
JWT-based authentication, and role-based
access control (RBAC).

Features:
    - Basic HTTP Authentication using Flask-HTTPAuth
    - JWT token-based authentication using Flask-JWT-Extended
    - Role-based access control with user and admin roles
    - Secure password hashing using werkzeug.security
    - Comprehensive error handling with proper HTTP status codes
    - In-memory user storage with predefined users

Security Considerations:
    - Passwords are hashed using werkzeug's secure
    hashing
    - JWT tokens include user role information for
    authorization
    - All authentication errors return consistent 401
    status codes
    - Admin-only routes return 403 for insufficient privileges

Usage:
    Install dependencies:
        pip install Flask Flask-HTTPAuth
        Flask-JWT-Extended

    Run the application:
        python task_05_basic_security.py

    Test endpoints:
        Basic Auth: curl -u user1:password
        http://localhost:5000/basic-protected
        Login: curl -X POST -H "Content-Type: application/json"
               -d '{"username":"user1","password":"password"}'
               http://localhost:5000/login
        JWT Protected: curl -H "Authorization: Bearer <token>"
                       http://localhost:5000/jwt-protected
"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)

# Flask application configuration
app.config['JWT_SECRET_KEY'] = 'your-secret-string-here-make-it-strong'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Initialize Flask extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify username and password for basic HTTP authentication.

    This function is called automatically by Flask-HTTPAuth
    when a request
    includes basic authentication headers
    It validates the provided
    credentials against the stored user data.

    Args:
        username (str): Username provided in the
        Authorization header
        password (str): Password provided in the
        Authorization header

    Returns:
        str: Username if authentication successful, None otherwise
    """
    if (username in users and
            check_password_hash(users[username]['password'], password)):
        return username
    return None


@auth.error_handler
def auth_error(status):
    """
    Handle basic authentication errors.

    This function is called when basic authentication fails
    and returns a standardized error response.

    Args:
        status (int): HTTP status code for the
        authentication error

    Returns:
        tuple: JSON error response and HTTP status code
    """
    return jsonify({"error": "Unauthorized access"}), 401


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle missing or invalid JWT token scenarios.

    This handler is triggered when:
    - No Authorization header is provided
    - Authorization header doesn't contain a Bearer token
    - Token format is invalid

    Args:
        err (str): Error message from JWT manager

    Returns:
        tuple: JSON error response and 401 status code
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid JWT token format or signature.

    This handler is triggered when the token
    cannot be decoded or has an invalid signature.

    Args:
        err (str): Error message from JWT manager

    Returns:
        tuple: JSON error response and 401 status code
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """
    Handle expired JWT tokens.

    This handler is triggered when a valid
    token has passed its expiration time as
    defined in JWT_ACCESS_TOKEN_EXPIRES.

    Args:
        jwt_header (dict): JWT header information
        jwt_payload (dict): JWT payload information

    Returns:
        tuple: JSON error response and 401 status code
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """
    Handle revoked JWT tokens.

    This handler is triggered when a token has been revoked
    (useful for logout functionality or security breaches).

    Args:
        jwt_header (dict): JWT header information
        jwt_payload (dict): JWT payload information

    Returns:
        tuple: JSON error response and 401 status code
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """
    Handle scenarios requiring fresh tokens.

    This handler is triggered when an endpoint requires
    a fresh token (recently issued) but receives a
    non-fresh token.

    Args:
        jwt_header (dict): JWT header information
        jwt_payload (dict): JWT payload information

    Returns:
        tuple: JSON error response and 401 status code
    """
    return jsonify({"error": "Fresh token required"}), 401


# API Routes

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Basic authentication protected endpoint.

    This route demonstrates basic HTTP authentication
    using the @auth.login_required decorator.
    Users must provide valid credentials in the
    Authorization header using Basic authentication scheme.

    Authentication:
        Basic HTTP Auth required (username:password
        base64 encoded)

    Returns:
        str: Success message indicating access was granted

    HTTP Status Codes:
        200: Authentication successful, access granted
        401: Authentication failed (handled by @auth.error_handler)
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    User authentication endpoint for JWT token generation.

    This endpoint accepts user credentials and returns
    a JWT access token if the credentials are valid.
    The token includes user information and
    role data for subsequent authorization checks.

    Request Body:
        {
            "username": "string",
            "password": "string"
        }

    Returns:
        JSON response with access token or error message

    HTTP Status Codes:
        200: Login successful, token provided
        400: Missing JSON data or required fields
        401: Invalid credentials
    """
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if (username in users and
            check_password_hash(users[username]['password'], password)):
        additional_claims = {
            "role": users[username]['role'],
            "username": username
        }
        access_token = create_access_token(
            identity=username,
            additional_claims=additional_claims
        )
        return jsonify({"access_token": access_token})
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    JWT token protected endpoint.

    This route demonstrates JWT-based authentication using
    the @jwt_required() decorator. Users must provide
    a valid JWT token in the Authorization header
    using Bearer token scheme.

    Authentication:
        JWT Bearer token required

    Returns:
        str: Success message indicating access was granted

    HTTP Status Codes:
        200: Token valid, access granted
        401: Token missing, invalid, or expired (handled by JWT error
             handlers)
    """
    current_user = get_jwt_identity()
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Admin-only protected endpoint with role-based
    access control.

    This route demonstrates role-based access control
    (RBAC) by checking the user's role from the JWT
    token claims. Only users with 'admin' role
    can access this endpoint.

    Authentication:
        JWT Bearer token required

    Authorization:
        Admin role required

    Returns:
        str: Success message for admin users
        JSON: Error message for non-admin users

    HTTP Status Codes:
        200: Admin access granted
        401: Token missing, invalid, or expired
        403: Valid token but insufficient privileges (non-admin user)
    """
    current_user = get_jwt_identity()
    claims = get_jwt()

    if claims.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@app.route('/', methods=['GET'])
def health_check():
    """
    API health check and documentation endpoint.

    This endpoint provides basic information about the API
    and its available endpoints. Useful for API
    discovery and health monitoring.

    Returns:
        JSON: API information and endpoint documentation

    HTTP Status Codes:
        200: API is healthy and operational
    """
    return jsonify({
        "message": "API Security Demo",
        "version": "1.0",
        "endpoints": {
            "health": "/ (GET) - API health check",
            "basic_auth": "/basic-protected (GET) - requires basic auth",
            "login": "/login (POST) - get JWT token",
            "jwt_protected": "/jwt-protected (GET) - requires JWT token",
            "admin_only": "/admin-only (GET) - requires admin JWT token"
        },
        "authentication": {
            "basic_auth": "Use Authorization: Basic <base64(username:password)>",
            "jwt_auth": "Use Authorization: Bearer <jwt_token>"
        }
    })


if __name__ == '__main__':
    """
    Application entry point for development server.

    When this script is run directly, it starts
    the Flask development server. The server will be
    accessible at http://localhost:5000 by default.

    Environment Variables:
        FLASK_ENV: Set to 'development' for debug mode
        FLASK_APP: Set to this file name for flask run command
    """
    app.run()
