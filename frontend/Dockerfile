# Dockerfile
# Pull the base image
FROM node:20-alpine3.17

# Set the working directory
WORKDIR /app-two

# Install application dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY . .

# Install dependencies
RUN npm install


# Start the app
CMD ["npm", "run", "dev"]
