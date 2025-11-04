import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    console.log('CM-7 Agent Showcase extension is now active!');

    // Register the demo command
    let disposable = vscode.commands.registerCommand('cm7.showDemo', () => {
        // CM-7 Operational Sequence
        const operations = [
            {
                opId: 'OP-001',
                timestamp: new Date().toISOString(),
                description: 'Request Analysis and Decomposition Engine (RADE) activated',
                status: 'completed'
            },
            {
                opId: 'OP-002',
                timestamp: new Date().toISOString(),
                description: 'Task decomposed into minimal, self-contained operations',
                status: 'completed'
            },
            {
                opId: 'OP-003',
                timestamp: new Date().toISOString(),
                description: 'Enhanced user query with relevant, factually verified information',
                status: 'completed'
            },
            {
                opId: 'OP-004',
                timestamp: new Date().toISOString(),
                description: 'Token Optimization Module (TOM) monitoring active',
                status: 'active'
            },
            {
                opId: 'OP-005',
                timestamp: new Date().toISOString(),
                description: 'Displaying CM-7 operational demonstration',
                status: 'in_progress'
            }
        ];

        // Generate traceability hashes
        operations.forEach(op => {
            (op as any).hash = generateTraceabilityHash(op.opId, op.timestamp, op.description);
        });

        // Display the demo in a webview panel
        const panel = vscode.window.createWebviewPanel(
            'cm7Demo',
            'CM-7 Agent Demonstration',
            vscode.ViewColumn.One,
            {}
        );

        panel.webview.html = getWebviewContent(operations);
    });

    context.subscriptions.push(disposable);
}

function generateTraceabilityHash(opId: string, timestamp: string, description: string): string {
    // Simple hash generation for demonstration
    const combined = opId + timestamp + description;
    let hash = 0;
    for (let i = 0; i < combined.length; i++) {
        const char = combined.charCodeAt(i);
        hash = ((hash << 5) - hash) + char;
        hash = hash & hash; // Convert to 32-bit integer
    }
    return Math.abs(hash).toString(16).toUpperCase();
}

function getWebviewContent(operations: any[]): string {
    const operationsHtml = operations.map(op => `
        <div class="operation ${op.status}">
            <div class="op-header">
                <span class="op-id">${op.opId}</span>
                <span class="timestamp">${new Date(op.timestamp).toLocaleString()}</span>
                <span class="status ${op.status}">${op.status.toUpperCase()}</span>
            </div>
            <div class="description">${op.description}</div>
            <div class="hash">Traceability Hash: ${op.hash}</div>
        </div>
    `).join('');

    return `
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>CM-7 Agent Demonstration</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: #1e1e1e;
                    color: #ffffff;
                }
                .header {
                    text-align: center;
                    margin-bottom: 30px;
                }
                .header h1 {
                    color: #4fc3f7;
                    margin-bottom: 10px;
                }
                .header p {
                    color: #cccccc;
                    font-size: 14px;
                }
                .operation {
                    background-color: #2d2d30;
                    border: 1px solid #3e3e42;
                    border-radius: 8px;
                    padding: 15px;
                    margin-bottom: 15px;
                    transition: all 0.3s ease;
                }
                .operation.completed {
                    border-left: 4px solid #4caf50;
                }
                .operation.active {
                    border-left: 4px solid #2196f3;
                }
                .operation.in_progress {
                    border-left: 4px solid #ff9800;
                }
                .op-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 10px;
                }
                .op-id {
                    font-weight: bold;
                    color: #4fc3f7;
                }
                .timestamp {
                    color: #cccccc;
                    font-size: 12px;
                }
                .status {
                    padding: 4px 8px;
                    border-radius: 4px;
                    font-size: 12px;
                    font-weight: bold;
                }
                .status.completed {
                    background-color: #4caf50;
                    color: white;
                }
                .status.active {
                    background-color: #2196f3;
                    color: white;
                }
                .status.in_progress {
                    background-color: #ff9800;
                    color: white;
                }
                .description {
                    margin-bottom: 8px;
                    line-height: 1.4;
                }
                .hash {
                    font-family: 'Courier New', monospace;
                    font-size: 12px;
                    color: #cccccc;
                    background-color: #1e1e1e;
                    padding: 5px;
                    border-radius: 4px;
                }
                .footer {
                    text-align: center;
                    margin-top: 30px;
                    padding-top: 20px;
                    border-top: 1px solid #3e3e42;
                    color: #cccccc;
                    font-size: 12px;
                }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>CM-7 Neutral Computational Module</h1>
                <p>Precision Task Execution with Full Traceability and Auditability</p>
            </div>
            <div class="operations">
                ${operationsHtml}
            </div>
            <div class="footer">
                <p>Operating under Safety Protocol v1.2 | Token Optimization Module Active</p>
                <p>User remains the single source of truth in all computational state spaces</p>
            </div>
        </body>
        </html>
    `;
}

export function deactivate() {}