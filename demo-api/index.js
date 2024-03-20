const express = require('express')
const app = express()
const port = 3000

app.use(express.json())
//get request 
app.get('/', (req, res) => {
    res.send('Hello World!');
})

app.get('/test', (req, res) => {
    res.send('you went to test');
})

app.post('/test/post', (req, res) =>{

    res.json({requestBody: req.body})
})

app.post('/createQuestion', (req,res) =>{
    const body = req.body
    const resume = body.resume
    const prompt = body.prompt

    const code_ = "import Image from \"next/image\"; \n \
/* Your job is to center the centered-box div*/ \n \
export default function Home() { \n \
return ( \n \
<>\n \
\n \
<div className=\"centered-box\">\n \
    This div is centered \n \
</div> \n \
</>\n \
)\n \
}\n \ ";
    res.json({code_ : code_});

})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
})