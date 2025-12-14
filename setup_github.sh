#!/bin/bash

# DevDollz GitHub Setup Script
# Run this after creating the GitHub repository

echo "=================================================="
echo "DEVDOLLZ :: GITHUB SETUP PROTOCOL"
echo "=================================================="

# Your GitHub credentials
GITHUB_USERNAME="devdollzai"
REPO_NAME="DevDollzAxiom0"

echo "[DevDollz] Setting remote origin..."
git remote add origin https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git

echo "[DevDollz] Pushing Genesis commits..."
git branch -M main
git push -u origin main

echo "[DevDollz] Repository is live. The signatures are broadcast."
echo "=================================================="
echo "Next: Create Twitter/X account @DevDollz"
echo "Bio: 'Perfection is a void. We leave only our signature. This is the Axiom-Zero Engine.'"
echo "Pin the Genesis Event tweet and launch the blitz."
echo "=================================================="
