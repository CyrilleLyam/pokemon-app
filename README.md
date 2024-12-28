# System Architecture Overview

This project uses **Nginx** as a reverse proxy to handle user requests and direct them to the correct backend services. It also includes a Lua script for verifying user tokens, making the system secure and efficient.

## Components of the System

### 1. **Nginx (Reverse Proxy)**

- Nginx acts as the central traffic manager.
- It decides where to send user requests based on the URL (e.g., authentication or Pokémon data).
- It includes a Lua script to verify user tokens for security.

### 2. **Lua Script (Verify Token)**

- The Lua script checks if a user’s token is valid.
- This ensures only authorized users can access the system.
- The script uses a shared cache (`jwt_cache`) to improve performance and avoid repeated checks for the same token.

### 3. **Authentication Service**

- Handles login requests.
- Verifies user credentials (email and password) and issues tokens for secure communication.

### 4. **Pokémon Service**

- Manages Pokémon-related data.
- Handles requests like retrieving Pokémon details.

## How It Works

### Request Flow

1. **User Request**:

   - A user sends a request to the system.
   - For example, they might log in or request Pokémon data.

2. **Nginx Routing**:

   - Nginx checks the request path.
   - If it starts with `/auth/`, it forwards the request to the Authentication Service.
   - If it starts with `/pokemon/`, it forwards the request to the Pokémon Service.

3. **Token Verification**:

   - For protected routes, Nginx uses the Lua script to verify the user’s token.
   - If the token is valid, the request is processed further.
   - If the token is invalid, the user gets an error response.

4. **Service Response**:
   - The backend service processes the request and sends the result back to Nginx.
   - Nginx delivers the response to the user.

## Key Features

### Token-Based Security

- Tokens ensure only logged-in users can access protected parts of the system.
- The Lua script makes this process fast and secure.

### Dynamic CORS Support

- The system allows requests from different websites (origins).
- It ensures secure cross-origin requests.

### Easy Scaling

- The system can handle more users by adding more service instances.
- Nginx efficiently distributes the traffic to these instances.

### Logging

- All activities are logged (e.g., successful requests and errors).
- This helps monitor and debug the system.

## System Diagram

Below is a simplified diagram of the system:

```
              +-------------------------+
              |       User Requests     |
              +-------------------------+
                          |
                          v
                   +--------------+
                   |    Nginx     |
                   +--------------+
                   /       |       \
                  /        |        \
        +----------------+  |   +----------------+
        | Pokémon Service|  |   | Auth Service   |
        +----------------+  |   +----------------+
                ^                     ^
                |                     |
        [Verify Token]         [Issue Token]
```

## Notes for Non-Technical Users

- **Purpose**: This system manages user requests efficiently and securely.
- **Security**: Tokens are checked to ensure only authorized users can access resources.
- **Scalability**: The system can handle more users by adding backend instances.
- **Logging**: Activities are recorded to help track system usage and fix issues.
