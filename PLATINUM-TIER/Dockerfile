# Dockerfile for Platinum Tier Autonomous FTE
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create vault directory structure
RUN mkdir -p platinum_vault/Inbox \
    platinum_vault/Needs_Action \
    platinum_vault/Pending_Approval \
    platinum_vault/Done \
    platinum_vault/Agent_Logs \
    platinum_vault/Analytics \
    platinum_vault/Schedules \
    platinum_vault/API_Logs \
    platinum_vault/Watched_Data \
    platinum_vault/Processed_Data \
    platinum_vault/Posted_Content \
    platinum_vault/Error_Logs \
    platinum_vault/Reports \
    platinum_vault/Skills \
    platinum_vault/Dashboard \
    platinum_vault/Business_Integrations \
    platinum_vault/CRM_Data \
    platinum_vault/Stripe_Simulations \
    platinum_vault/WhatsApp_Data \
    platinum_vault/FileSystem_Monitor \
    platinum_vault/Emergency_Logs \
    platinum_vault/Self_Improvement \
    platinum_vault/Model_Training \
    platinum_vault/Production_Deployments

# Expose port for any web interfaces
EXPOSE 5001

# Run the application
CMD ["python", "platinum_tier_autonomous_fte.py"]