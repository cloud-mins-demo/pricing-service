# Pricing Service

## Overview
This repository contains a dummy pricing service used to test a GitHub tech stack extractor. The codebase is intentionally simple and focused on predictable structure and dependency signals so tooling can reliably detect technologies across the stack.

## Features
- Exposes a lightweight pricing API for ride fare estimation scenarios.
- Includes modular service components for pricing logic and caching.
- Uses container-friendly setup for repeatable local runs.
- Provides a clear project layout for automated repository analysis.
- Serves as a safe non-production sample for CI/CD and parsing experiments.

## Tech Stack
- Frontend
	- React
- Backend
	- Node.js
	- Python
	- FastAPI
- Database
	- PostgreSQL
- DevOps
	- Docker
	- AWS
	- GitHub Actions
- Testing
	- Pytest

## Project Structure
```text
pricing-service/
|-- app/
|   |-- app.py
|   |-- cache.py
|   `-- pricing.py
|-- Dockerfile
|-- requirements.txt
`-- README.md
```

## Installation
1. Clone the repository.
2. Move into the project directory.
3. Create and activate a Python virtual environment.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage
Run the service locally:

```bash
python app/app.py
```

Run with Docker:

```bash
docker build -t pricing-service .
docker run --rm -p 8000:8000 pricing-service
```

## API Endpoints (if applicable)
Example endpoints for this dummy service:

- `GET /health` - Service health check.
- `POST /pricing/calculate` - Calculate estimated ride fare.
- `GET /pricing/config` - Fetch pricing configuration metadata.

Note: Endpoint availability depends on implementation details in `app/app.py`.

## Environment Variables
Configure runtime behavior using environment variables as needed:

- `PORT` - Application port (default: `8000`).
- `LOG_LEVEL` - Logging verbosity (for example: `INFO`, `DEBUG`).
- `CACHE_TTL_SECONDS` - Cache expiration duration.
- `DATABASE_URL` - PostgreSQL connection string (if persistence is enabled).

## Testing
Run tests with:

```bash
pytest -q
```

If no tests are present yet, add a `tests/` directory and create test cases for pricing and caching behavior.

## Roadmap
- Add versioned API routes.
- Expand unit and integration test coverage.
- Add OpenAPI documentation generation.
- Add database-backed pricing rule storage.
- Add CI quality gates for linting, tests, and build artifacts.

## License
This project is provided for educational and testing purposes. Add a license file (for example, MIT) before public distribution.