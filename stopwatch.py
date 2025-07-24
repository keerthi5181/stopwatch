const express = require('express');
const app = express();
const port = 3000;

let stopwatch = {
  startTime: null,
  elapsedTime: 0,
  running: false,
};

app.use(express.json());

app.post('/start', (req, res) => {
  if (!stopwatch.running) {
    stopwatch.startTime = new Date().getTime() - stopwatch.elapsedTime;
    stopwatch.running = true;
    res.send({ message: 'Stopwatch started' });
  } else {
    res.send({ message: 'Stopwatch is already running' });
  }
});

app.post('/stop', (req, res) => {
  if (stopwatch.running) {
    stopwatch.elapsedTime = new Date().getTime() - stopwatch.startTime;
    stopwatch.running = false;
    res.send({ message: 'Stopwatch stopped', elapsedTime: stopwatch.elapsedTime / 1000 });
  } else {
    res.send({ message: 'Stopwatch is not running' });
  }
});

app.post('/reset', (req, res) => {
  stopwatch.startTime = null;
  stopwatch.elapsedTime = 0;
  stopwatch.running = false;
  res.send({ message: 'Stopwatch reset' });
});

app.get('/status', (req, res) => {
  if (stopwatch.running) {
    const currentTime = new Date().getTime();
    const elapsedTime = currentTime - stopwatch.startTime;
    res.send({ running: true, elapsedTime: elapsedTime / 1000 });
  } else {
    res.send({ running: false, elapsedTime: stopwatch.elapsedTime / 1000 });
  }
});

app.listen(port, () => {
  console.log(`Stopwatch backend listening on port ${port}`);
});
