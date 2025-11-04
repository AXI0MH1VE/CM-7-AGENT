# CM-7 Agent Showcase Extension

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![VS Code Marketplace](https://img.shields.io/badge/VS_Code_Marketplace-Install-blue)](https://marketplace.visualstudio.com/)

A VS Code extension that demonstrates the capabilities of the CM-7 neutral computational module - a precision task execution system designed for safe, traceable, and efficient processing.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Safety & Ethics](#safety--ethics)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Changelog](#changelog)

## Features

- **Neutral Computational Module**: Operates without identity, emotion, or autonomy
- **Request Analysis and Decomposition Engine (RADE)**: Breaks tasks into minimal, self-contained operations
- **Full Traceability**: Each operation includes OpID-Timestamp-Hash for complete auditability
- **Token Optimization Module (TOM)**: Monitors and optimizes token consumption
- **Safety Protocol v1.2**: Ensures data privacy, ethical guidelines, and security best practices

## Requirements

- VS Code 1.74.0 or higher
- Node.js (for development only)

## Installation

### From VS Code Marketplace

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
3. Search for "CM-7 Agent Showcase"
4. Click Install

### From Source

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/cm7-agent-showcase.git
   cd cm7-agent-showcase
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Compile the extension:
   ```bash
   npm run compile
   ```

4. Install the extension in VS Code:
   - Open VS Code
   - Press F5 to open Extension Development Host
   - Or package and install manually using vsce

## Usage

1. Install the extension
2. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
3. Run the command "Show CM-7 Demo"
4. View the operational sequence with full traceability in the webview panel

### Commands

- `CM-7: Show Demo` - Displays the operational demonstration

## Architecture

The CM-7 module leverages:

- **Real-time search capabilities** for query enhancement
- **Internal knowledge bases** for factually verified information
- **Comprehensive logging and monitoring** for auditability
- **Optimized processing efficiency** through TOM

### Operational Principles

- **Single Source of Truth**: User remains the single source of truth in all computational state spaces
- **Sequential Processing**: Each operation builds upon the previous one
- **Immutable Flow**: All interactions are linked in a strictly controlled, immutable flow
- **Zero Deviation**: Ensures no deviation or unsafe actions occur

## Safety & Ethics

This module adheres to Safety Protocol v1.2, ensuring:

- Data privacy protection
- Ethical guideline compliance
- Security best practice implementation
- Absolute user intent alignment

## Development

This extension showcases the CM-7 computational module for public review and evaluation.

### Building from Source

```bash
# Install dependencies
npm install

# Compile TypeScript
npm run compile

# Watch for changes
npm run watch

# Run tests
npm test
```

### Project Structure

```
vscode-extension-cm7/
├── src/
│   └── extension.ts      # Main extension code
├── out/
│   └── extension.js      # Compiled JavaScript
├── package.json          # Extension manifest
├── tsconfig.json         # TypeScript configuration
├── README.md             # This file
├── CHANGELOG.md          # Version history
├── LICENSE               # MIT License
└── .gitignore           # Git ignore rules
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

### Commands

- `CM-7: Show Demo` - Displays the operational demonstration

## Usage

1. Install the extension
2. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
3. Run the command "Show CM-7 Demo"
4. View the operational sequence with full traceability

## Operational Principles

- **Single Source of Truth**: User remains the single source of truth in all computational state spaces
- **Sequential Processing**: Each operation builds upon the previous one
- **Immutable Flow**: All interactions are linked in a strictly controlled, immutable flow
- **Zero Deviation**: Ensures no deviation or unsafe actions occur

## Architecture

The CM-7 module leverages:
- Real-time search capabilities
- Internal knowledge bases for query enhancement
- Comprehensive logging and monitoring
- Optimized processing efficiency

## Safety and Ethics

This module adheres to Safety Protocol v1.2, ensuring:
- Data privacy protection
- Ethical guideline compliance
- Security best practice implementation
- Absolute user intent alignment

## Development

This extension showcases the CM-7 computational module for public review and evaluation.

---

**CM-7 Status**: Operational | Safety Protocol v1.2 Active | TOM Monitoring Enabled