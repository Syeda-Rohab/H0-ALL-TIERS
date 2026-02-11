#!/bin/bash
# Platinum Tier Deployment Script

set -e  # Exit on any error

echo "🚀 Deploying Platinum Tier Autonomous FTE..."

# Build the Docker image
echo "📦 Building Docker image..."
docker build -t platinum-tier-autonomous-fte .

# Check if build succeeded
if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully!"
else
    echo "❌ Docker build failed!"
    exit 1
fi

# Stop and remove any existing container
echo "🛑 Stopping existing container (if any)..."
docker stop platinum-fte || true
docker rm platinum-fte || true

# Run the new container
echo "🏃 Running Platinum Tier Autonomous FTE..."
docker run -d \
  --name platinum-fte \
  --restart unless-stopped \
  -p 5001:5001 \
  platinum-tier-autonomous-fte

# Check if container started successfully
if [ $? -eq 0 ]; then
    echo "✅ Platinum Tier Autonomous FTE deployed successfully!"
    echo "📊 Container is running in detached mode"
    echo "🔍 Monitor with: docker logs -f platinum-fte"
    echo "🐳 View containers: docker ps"
else
    echo "❌ Failed to start Platinum Tier Autonomous FTE container!"
    exit 1
fi

# Display container status
echo ""
echo "📋 Container Status:"
docker ps --filter name=platinum-fte

echo ""
echo "🎉 Platinum Tier Autonomous FTE is now running in production!"
echo "The system is fully autonomous and requires no human input except for emergencies."