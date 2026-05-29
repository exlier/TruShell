#!/usr/bin/env node

const { execFileSync, spawn } = require('child_process');
const path = require('path');

// Try python3 first, fallback to python
const pythonCmd = (() => {
  try {
    execFileSync('python3', ['--version'], { stdio: 'ignore' });
    return 'python3';
  } catch {
    return 'python';
  }
})();

// Check if Python is available and functional
const result = execFileSync(pythonCmd, ['--version'], { encoding: 'utf8', stdio: 'pipe' });
if (!result) {
  console.error('TruShell requires Python 3.10+. Please install Python first.');
  process.exit(1);
}

const args = process.argv.slice(2);
const packageRoot = path.resolve(__dirname, '..');

const child = spawn(pythonCmd, ['-m', 'trushell', ...args], {
  stdio: 'inherit',
  cwd: packageRoot,
});

child.on('exit', (code, signal) => {
  if (signal) process.kill(process.pid, signal);
  process.exit(code);
});

child.on('error', (err) => {
  console.error('Failed to launch TruShell CLI.');
  console.error('Make sure Python is installed and the TruShell package files are present.');
  console.error(err.message || err);
  process.exit(1);
});
