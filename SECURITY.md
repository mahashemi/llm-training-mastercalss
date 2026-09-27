# Security

This repository is primarily an educational and research resource.

## Do not commit

Never commit:

- API keys;
- access tokens;
- cloud credentials;
- private datasets;
- personally identifying information;
- proprietary model weights that are not licensed for redistribution.

## Security reports

Do not publish sensitive security details in a public issue. Contact the repository maintainer through the GitHub account associated with this project and provide enough information to reproduce the issue safely.

## Research infrastructure

Training and inference examples should follow least-privilege principles. Credentials should be supplied through the runtime environment or a supported secret manager, not notebook source code.
