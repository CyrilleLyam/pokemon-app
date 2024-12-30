## Setting Up the Environment File in Each Directory

1. **Locate the `env.example` file in each directory**
   In every directory of your project, locate the file named `env.example`.

2. **Copy `env.example` to `.env`**
   For each directory where `env.example` exists, run the following command:
   ```bash
   cp env.example .env
   ```
3. **Run make help for instructions**
   If a Makefile exists in the directory, you can run the following command to see the available instructions:
   ```bash
   make help
   ```
