# Use Node.js 22.15.0 as requested
FROM node:22.15.0-slim

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port 5174
EXPOSE 5174

# Run the app
# We use --host 0.0.0.0 to expose it outside the container
# We use --port 5174 to specifically bind to the requested port
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5174"]
