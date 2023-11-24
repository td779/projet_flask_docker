FROM node:latest
RUN mkdir -p home/app

#WORKDIR /usr/src/app
WORKDIR /home/app

COPY package*.json ./

RUN npm install --save dotenv

ENV TASKS=50

COPY . .

EXPOSE 3000

CMD ["node", "main.js"]
