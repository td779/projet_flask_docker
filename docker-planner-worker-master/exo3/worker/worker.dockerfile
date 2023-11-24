FROM node:latest
RUN mkdir -p home/app

#WORKDIR /usr/src/app
WORKDIR /home/app

COPY package*.json ./

RUN npm install --save dotenv

ENV MULT=true ADD=true PORT=8080

COPY . .

EXPOSE 8080

CMD ["node", "main.js"]
