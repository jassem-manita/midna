FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy package files
COPY . .

# Install the package
RUN pip install --no-cache-dir .

# Create a test requirements file
RUN echo "requests>=2.25.0\nnumpy>=1.20.0\npandas>=1.3.0" > /tmp/test_requirements.txt

# Test the installation
RUN zap --version

# Test dry-run functionality
RUN zap --dry-run /tmp/test_requirements.txt

# Test help command
RUN zap --help

# Keep container running for manual testing (optional)
CMD ["bash"]
