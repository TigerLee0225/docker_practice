const express = require('express');
const cors = require('cors');  
const app = express();
const port = 3000;

app.use(cors({
  origin: 'http://localhost:5173',
}));
app.use(express.json());  

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.post('/api/data', (req, res) => {
  const { message } = req.body;
  console.log(`Received message: ${message}`);
  res.json({ response: `Received your message: ${message}` });
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Example app listening on port ${port}`);
});
