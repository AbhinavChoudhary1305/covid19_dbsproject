const express = require("express")
var mysql = require('mysql');
const cors = require('cors')

const app = express()
const port = 3000


app.use(cors());


app.get('/', (req,res)=>{
    const query = req.query.state
    console.log(query);
    var con = mysql.createConnection({
        host:"localhost",
        user:"root",
        password:"123",
        database:"covidProject"
    });
    
    con.connect();
    
    con.query(`Select Deaths, Cured,Date,Confirmed from mytable where StateName ='${query}'`, function(err, results, fields){
        res.send(results);
    })  
con.end();
});
app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
  })
  