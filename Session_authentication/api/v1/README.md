# Project Update: Enhanced User Retrieval with `/api/v1/users/me`

## 🚀 Overview

This update enhances the existing User service (from project "0x06. Basic authentication") by allowing an authenticated user to retrieve their own user details using a dedicated endpoint alias: `GET /api/v1/users/me`.

## 🎯 Objective

The goal was to provide a convenient way for an authenticated user to access their own information without needing to know their specific User ID. This is a common feature in many APIs, often represented by a `/me` or `/self` endpoint.

## ✨ Key Changes Implemented

To achieve this functionality, the following modifications were made:

1.  **`api/v1/app.py`**:
    * The `@app.before_request` handler was updated to ensure that the currently authenticated user object (retrieved via `auth.current_user(request)`) is assigned to `request.current_user`. This makes the authenticated user readily accessible in subsequent request handling logic.

2.  **`api/v1/views/users.py`**:
    * The existing route `GET /api/v1/users/<user_id>` was enhanced:
        * It now recognizes a special `user_id` value: `"me"`.
        * If `<user_id>` is `"me"`, the handler checks for an authenticated user on `request.current_user`.
            * If an authenticated user exists, their details are returned in the JSON response.
            * If no user is authenticated for the request (i.e., `request.current_user` is `None`), a `404 Not Found` error is returned, as per the project requirements for this specific case.
        * If `<user_id>` is any other value, the original behavior of fetching a user by their explicit ID is maintained.

## ⚙️ Functionality

* **Endpoint**: `GET /api/v1/users/me`
* **Authentication**: Requires valid Basic Authentication credentials to be sent with the request.
* **Successful Response**: If authenticated, returns a JSON object containing the details of the currently logged-in user. The structure of this JSON object is identical to that returned by `GET /api/v1/users/<user_id>` for a specific user.
* **Unauthenticated/Invalid User Access to `/me`**: If the request to `/api/v1/users/me` is made without authentication, or if the `request.current_user` is not set after the authentication attempt (e.g. bad credentials would lead to an earlier 401/403 from the `before_request` handler, but if `current_user` is `None` specifically for the `/me` check), the endpoint will respond with a `404 Not Found`. Standard `401 Unauthorized` or `403 Forbidden` errors will be triggered by the global `before_request` handler if credentials are missing or fundamentally invalid.

## 📋 Prerequisites

This update assumes the successful completion and availability of the "0x06. Basic authentication" project, which provides the foundational User model, Basic Authentication mechanisms, and existing User API endpoints.

## 📁 Files Modified

* `api/v1/app.py`
* `api/v1/views/users.py`

---

This `README.md` should clearly explain the purpose and changes related to this specific task. You can place it in the root of this particular project or feature branch.# Project Update: Enhanced User Retrieval with `/api/v1/users/me`

## 🚀 Overview

This update enhances the existing User service (from project "0x06. Basic authentication") by allowing an authenticated user to retrieve their own user details using a dedicated endpoint alias: `GET /api/v1/users/me`.

## 🎯 Objective

The goal was to provide a convenient way for an authenticated user to access their own information without needing to know their specific User ID. This is a common feature in many APIs, often represented by a `/me` or `/self` endpoint.

## ✨ Key Changes Implemented

To achieve this functionality, the following modifications were made:

1.  **`api/v1/app.py`**:
    * The `@app.before_request` handler was updated to ensure that the currently authenticated user object (retrieved via `auth.current_user(request)`) is assigned to `request.current_user`. This makes the authenticated user readily accessible in subsequent request handling logic.

2.  **`api/v1/views/users.py`**:
    * The existing route `GET /api/v1/users/<user_id>` was enhanced:
        * It now recognizes a special `user_id` value: `"me"`.
        * If `<user_id>` is `"me"`, the handler checks for an authenticated user on `request.current_user`.
            * If an authenticated user exists, their details are returned in the JSON response.
            * If no user is authenticated for the request (i.e., `request.current_user` is `None`), a `404 Not Found` error is returned, as per the project requirements for this specific case.
        * If `<user_id>` is any other value, the original behavior of fetching a user by their explicit ID is maintained.

## ⚙️ Functionality

* **Endpoint**: `GET /api/v1/users/me`
* **Authentication**: Requires valid Basic Authentication credentials to be sent with the request.
* **Successful Response**: If authenticated, returns a JSON object containing the details of the currently logged-in user. The structure of this JSON object is identical to that returned by `GET /api/v1/users/<user_id>` for a specific user.
* **Unauthenticated/Invalid User Access to `/me`**: If the request to `/api/v1/users/me` is made without authentication, or if the `request.current_user` is not set after the authentication attempt (e.g. bad credentials would lead to an earlier 401/403 from the `before_request` handler, but if `current_user` is `None` specifically for the `/me` check), the endpoint will respond with a `404 Not Found`. Standard `401 Unauthorized` or `403 Forbidden` errors will be triggered by the global `before_request` handler if credentials are missing or fundamentally invalid.

## 📋 Prerequisites

This update assumes the successful completion and availability of the "0x06. Basic authentication" project, which provides the foundational User model, Basic Authentication mechanisms, and existing User API endpoints.

## 📁 Files Modified

* `api/v1/app.py`
* `api/v1/views/users.py`

---

This `README.md` should clearly explain the purpose and changes related to this specific task. You can place it in the root of this particular project or feature branch.# Project Update: Enhanced User Retrieval with `/api/v1/users/me`

## 🚀 Overview

This update enhances the existing User service (from project "0x06. Basic authentication") by allowing an authenticated user to retrieve their own user details using a dedicated endpoint alias: `GET /api/v1/users/me`.

## 🎯 Objective

